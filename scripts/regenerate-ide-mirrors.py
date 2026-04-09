#!/usr/bin/env python3
"""
Regenerate .github, .cursor, and .claude mirrors from .steering (agents, skills, templates).

This is the same logic as the "Regenerate IDE mirrors" step in
.github/workflows/verify-steering-sync.yml — run locally after editing .steering
or to match CI before pushing.
"""

import re
import sys
from pathlib import Path

EMBED = re.compile(r"!\[\[([^\]#]+)(?:#([^|\]]+))?\]\]")
GITHUB_COPILOT_EMBED = re.compile(
    r"!\[\[github-copilot/[^\]#]+(?:#[^|\]]+)?\]\]\s*"
)
GITHUB_EMBED_POINTER = (
    "> **Copilot Agent Skills (steering):** see `.steering/github-copilot/Skills.md` "
    "in this repository.\n\n"
)


def strip_copilot_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return content
    end = content.find("\n---\n", 4)
    if end == -1:
        return content
    fm = content[4:end]
    body = content[end + 5 :]
    lines = fm.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("tools:"):
            i += 1
            while i < len(lines):
                L = lines[i]
                if L.strip() == "" or L.startswith(" ") or L.startswith("\t"):
                    i += 1
                    continue
                break
            continue
        if line.startswith("mcp-servers:"):
            i += 1
            while i < len(lines):
                L = lines[i]
                if L.strip() == "" or L.startswith(" ") or L.startswith("\t"):
                    i += 1
                    continue
                break
            continue
        out.append(line)
        i += 1
    new_fm = "\n".join(out).strip("\n")
    return "---\n" + new_fm + "\n---\n" + body


def extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    target = "## " + heading.strip()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == target:
            start = i
            break
    if start is None:
        return "<!-- missing section: " + heading.strip() + " -->\n"
    out = []
    for line in lines[start + 1 :]:
        st = line.strip()
        if st == "---":
            break
        if line.startswith("## "):
            break
        if line.startswith("# ") and not line.startswith("##"):
            break
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def strip_first_yaml_block(s: str) -> str:
    if not s.startswith("---"):
        return s
    end = s.find("\n---\n", 4)
    if end == -1:
        return s
    return s[end + 5 :].lstrip("\n")


def normalize_embed_path(p: str) -> str:
    p = p.strip().rstrip("/")
    while p.startswith("./"):
        p = p[2:]
    return p


def path_allowed(pn: str, prefixes: tuple[str, ...]) -> bool:
    for pref in prefixes:
        if pref == "templates":
            if pn == "templates" or pn.startswith("templates/"):
                return True
        elif pref == "github-copilot":
            if pn == "github-copilot" or pn.startswith("github-copilot/"):
                return True
    return False


def resolve_one_embed(root: Path, path_part: str, section: str | None) -> str:
    p = normalize_embed_path(path_part)
    if not p or Path(p).name == "":
        return "<!-- invalid embed path -->\n"
    rel = Path(p)
    if rel.is_absolute() or ".." in rel.parts:
        return "<!-- invalid embed path -->\n"
    if rel.suffix != ".md":
        rel = rel.with_suffix(".md")
    tpl = (root / ".steering" / rel).resolve()
    steering_root = (root / ".steering").resolve()
    if not tpl.is_relative_to(steering_root):
        return "<!-- invalid embed path -->\n"
    if not tpl.is_file():
        return "<!-- missing: .steering/" + rel.as_posix() + " -->\n"
    raw = tpl.read_text(encoding="utf-8")
    if section:
        return extract_section(raw, section)
    return strip_first_yaml_block(raw).rstrip() + "\n"


def expand_obsidian_embeds(root: Path, body: str, prefixes: tuple[str, ...]) -> str:
    for _ in range(16):
        if not EMBED.search(body):
            break

        def repl(m):
            p = m.group(1).strip()
            sec = m.group(2).strip() if m.group(2) else None
            pn = normalize_embed_path(p)
            if not path_allowed(pn, prefixes):
                return m.group(0)
            return resolve_one_embed(root, pn, sec)

        body = EMBED.sub(repl, body)
    return body


def process_markdown_doc(root: Path, text: str, prefixes: tuple[str, ...]) -> str:
    if not text.startswith("---"):
        return expand_obsidian_embeds(root, text, prefixes)
    end = text.find("\n---\n", 4)
    if end == -1:
        return expand_obsidian_embeds(root, text, prefixes)
    fm = text[: end + 5]
    body = text[end + 5 :]
    return fm + expand_obsidian_embeds(root, body, prefixes)


def replace_github_copilot_embeds(text: str) -> str:
    return GITHUB_COPILOT_EMBED.sub(GITHUB_EMBED_POINTER, text)


def strip_github_copilot_embeds_doc(text: str) -> str:
    if not text.startswith("---"):
        return replace_github_copilot_embeds(text)
    end = text.find("\n---\n", 4)
    if end == -1:
        return replace_github_copilot_embeds(text)
    fm = text[: end + 5]
    body = text[end + 5 :]
    return fm + replace_github_copilot_embeds(body)


def assert_cursor_claude_agent_no_copilot_keys(agents_root: Path) -> None:
    for name in (".cursor", ".claude"):
        ad = agents_root / name / "agents"
        if not ad.is_dir():
            continue
        for f in sorted(ad.iterdir()):
            if not f.is_file() or not f.name.endswith(".md"):
                continue
            t = f.read_text(encoding="utf-8")
            if not t.startswith("---"):
                continue
            e = t.find("\n---\n", 4)
            if e == -1:
                continue
            fm = t[4:e]
            for line in fm.splitlines():
                s = line.strip()
                if s.startswith("tools:") or s.startswith("mcp-servers:"):
                    print(
                        f"::error::Mirror {f} must not contain Copilot-only YAML: {s}",
                        file=sys.stderr,
                    )
                    sys.exit(1)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    agents_dir = root / ".steering" / "agents"
    (root / ".github" / "agents").mkdir(parents=True, exist_ok=True)
    (root / ".cursor" / "agents").mkdir(parents=True, exist_ok=True)
    (root / ".claude" / "agents").mkdir(parents=True, exist_ok=True)

    expected_agent_files: set[str] = set()
    for f in sorted(agents_dir.iterdir()):
        if not f.is_file() or f.name == "README.md":
            continue
        expected_agent_files.add(f.name)
        raw = f.read_text(encoding="utf-8")
        if f.name == "research-skill.agent.md":
            built_gh_claude = strip_github_copilot_embeds_doc(
                process_markdown_doc(root, raw, ("templates",))
            )
            built_cursor = strip_copilot_frontmatter(
                process_markdown_doc(
                    root, raw, ("templates", "github-copilot")
                )
            )
            (root / ".github" / "agents" / f.name).write_text(
                built_gh_claude, encoding="utf-8"
            )
            (root / ".claude" / "agents" / f.name).write_text(
                strip_copilot_frontmatter(built_gh_claude), encoding="utf-8"
            )
            (root / ".cursor" / "agents" / f.name).write_text(
                built_cursor, encoding="utf-8"
            )
        else:
            built = process_markdown_doc(root, raw, ("templates",))
            (root / ".github" / "agents" / f.name).write_text(built, encoding="utf-8")
            stripped = strip_copilot_frontmatter(built)
            (root / ".cursor" / "agents" / f.name).write_text(stripped, encoding="utf-8")
            (root / ".claude" / "agents" / f.name).write_text(stripped, encoding="utf-8")

    # Prune stale agent mirrors
    for folder in (".github", ".cursor", ".claude"):
        ad = root / folder / "agents"
        if ad.is_dir():
            for stale in sorted(ad.iterdir()):
                if stale.is_file() and stale.name.endswith(".md") and stale.name not in expected_agent_files:
                    stale.unlink()

    skills_root = root / ".steering" / "skills"
    expected_skill_names: set[str] = set()
    for skill_dir in sorted(skills_root.iterdir()):
        if not skill_dir.is_dir():
            continue
        sk = skill_dir / "SKILL.md"
        if not sk.is_file():
            continue
        name = skill_dir.name
        expected_skill_names.add(name)
        raw_skill = sk.read_text(encoding="utf-8")
        for folder in ("cursor", "claude", "github"):
            dest = root / f".{folder}" / "skills" / name
            dest.mkdir(parents=True, exist_ok=True)
            if name == "skill-research":
                if folder == "cursor":
                    out = process_markdown_doc(
                        root, raw_skill, ("templates", "github-copilot")
                    )
                else:
                    out = strip_github_copilot_embeds_doc(
                        process_markdown_doc(root, raw_skill, ("templates",))
                    )
            else:
                out = process_markdown_doc(root, raw_skill, ("templates",))
            (dest / "SKILL.md").write_text(out, encoding="utf-8")

    # Prune stale skill mirrors (but keep special non-steering directories)
    special_skill_dirs = {"skill-research", "skill-template", "agentic-programming"}
    for folder in ("cursor", "claude", "github"):
        sd = root / f".{folder}" / "skills"
        if sd.is_dir():
            for stale_dir in sorted(sd.iterdir()):
                if stale_dir.is_dir() and stale_dir.name not in expected_skill_names and stale_dir.name not in special_skill_dirs:
                    skill_md = stale_dir / "SKILL.md"
                    if skill_md.is_file():
                        skill_md.unlink()
                    if not any(stale_dir.iterdir()):
                        stale_dir.rmdir()

    for sub in (
        root / ".github" / "skills" / "skill-research",
        root / ".claude" / "skills" / "skill-template",
        root / ".cursor" / "skills" / "skill-template",
    ):
        sub.mkdir(parents=True, exist_ok=True)
    tpl = (root / ".steering" / "templates" / "skill.md").read_text(encoding="utf-8")
    (root / ".github" / "skills" / "skill-research" / "skill-template.md").write_text(
        tpl, encoding="utf-8"
    )
    (root / ".claude" / "skills" / "skill-template" / "SKILL.md").write_text(
        tpl, encoding="utf-8"
    )
    (root / ".cursor" / "skills" / "skill-template" / "SKILL.md").write_text(
        tpl, encoding="utf-8"
    )

    assert_cursor_claude_agent_no_copilot_keys(root)


if __name__ == "__main__":
    main()
