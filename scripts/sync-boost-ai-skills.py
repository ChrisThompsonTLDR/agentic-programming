#!/usr/bin/env python3
"""
Pull selected Laravel Boost .ai guidelines into .steering/skills as portable SKILL.md files.

Upstream: https://github.com/laravel/boost/tree/main/.ai

Boost ships Blade templates ({{ $assist->... }}, @boostsnippet). This script emits static
Markdown with conventional command placeholders so skills work outside Boost installs.

Usage:
  python3 scripts/sync-boost-ai-skills.py
  BOOST_REPO_ROOT=/path/to/boost/checkout python3 scripts/sync-boost-ai-skills.py
  BOOST_REV=v1.2.3 python3 scripts/sync-boost-ai-skills.py   # pin tag or commit when cloning

After updating .steering/skills, regenerate IDE mirrors (same as CI):
  python3 scripts/regenerate-ide-mirrors.py
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[1]
STEERING_SKILLS = REPO_ROOT / ".steering" / "skills"
DEFAULT_REMOTE = "https://github.com/laravel/boost.git"

# Major versions for versioned .ai subtrees (bump when Boost adds newer paths).
LIVEWIRE_MAJOR = "4"
PEST_MAJOR = "4"
TAILWIND_MAJOR = "4"


def clone_boost(dest: Path, rev: str | None) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    cmd = ["git", "clone", "--depth", "1", DEFAULT_REMOTE, str(dest)]
    subprocess.run(cmd, check=True)
    if rev:
        subprocess.run(
            ["git", "-C", str(dest), "fetch", "--depth", "1", "origin", rev],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(dest), "checkout", "FETCH_HEAD"],
            check=True,
        )


def git_head_sha(repo: Path) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return p.stdout.strip()


def strip_blade_php_blocks(text: str) -> str:
    return re.sub(r"@php\s*.*?\s*@endphp\s*", "", text, flags=re.DOTALL)


def convert_boostsnippets(text: str) -> str:
    pat = re.compile(
        r'@boostsnippet\("([^"]+)",\s*"([^"]+)"\)\s*\n(.*?)\n@endboostsnippet',
        re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        title, lang, body = m.group(1), m.group(2), m.group(3).strip("\n")
        return f"<!-- {title} -->\n```{lang}\n{body}\n```\n"

    return pat.sub(repl, text)


def replace_artisan(text: str, prefix: str) -> str:
    """prefix is '' for php artisan or ./vendor/bin/sail artisan (no backticks — caller context supplies fences)."""

    def one(cmd: str) -> str:
        inner = cmd.replace("{name}", "<name>")
        if prefix:
            return f"{prefix} {inner}"
        return f"php artisan {inner}"

    def sub_single(m: re.Match[str]) -> str:
        return one(m.group(1))

    text = re.sub(
        r"\{\{\s*\$assist->artisanCommand\('([^']*)'\)\s*\}\}",
        sub_single,
        text,
    )
    return re.sub(
        r'\{\{\s*\$assist->artisanCommand\("([^"]*)"\)\s*\}\}',
        sub_single,
        text,
    )


def replace_app_path(text: str) -> str:
    def sub(m: re.Match[str]) -> str:
        p = m.group(1)
        return f"`app/{p}`"

    return re.sub(r"\{\{\s*\$assist->appPath\('([^']*)'\)\s*\}\}", sub, text)


def replace_sail_path(text: str) -> str:
    return text.replace("{{ $assist->sailBinaryPath() }}", "./vendor/bin/sail")


def replace_composer_sail(text: str) -> str:
    return re.sub(
        r"\{\{\s*\$assist->composerCommand\('([^']*)'\)\s*\}\}",
        r"./vendor/bin/sail composer \1",
        text,
    )


def replace_npm_sail(text: str) -> str:
    return re.sub(
        r"\{\{\s*\$assist->nodePackageManagerCommand\('([^']*)'\)\s*\}\}",
        r"./vendor/bin/sail npm \1",
        text,
    )


def transform_blade_skill_body(body: str, *, sail_artisan: bool) -> str:
    body = strip_blade_php_blocks(body)
    body = convert_boostsnippets(body)
    prefix = "./vendor/bin/sail artisan" if sail_artisan else ""
    body = replace_artisan(body, prefix)
    body = replace_app_path(body)
    if sail_artisan:
        body = replace_sail_path(body)
        body = replace_composer_sail(body)
        body = replace_npm_sail(body)
    note = (
        "\n\n---\n\n**Command prefix:** These examples use `php artisan` and `composer` / `npm` "
        "as if you run PHP on the host. If the app uses **Laravel Sail**, prefix with "
        "`./vendor/bin/sail` (for example `./vendor/bin/sail artisan test --compact`).\n"
    )
    if not sail_artisan:
        body = body.rstrip() + note
    return body.strip() + "\n"


def patch_yaml_name(fm: str, new_name: str) -> str:
    return re.sub(
        r"(?m)^name:\s*\S+.*$",
        f"name: {new_name}",
        fm,
        count=1,
    )


def write_flux_like(
    boost_root: Path,
    dest_dir: Path,
    rel_source: str,
    commit: str,
    sail_artisan: bool,
    *,
    canonical_name: str | None = None,
) -> None:
    raw = (boost_root / rel_source).read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise SystemExit(f"Expected YAML frontmatter in {rel_source}")
    end_fm = raw.find("\n---\n", 4)
    if end_fm == -1:
        raise SystemExit(f"Invalid frontmatter in {rel_source}")
    fm = raw[: end_fm + 5]
    if canonical_name:
        fm = patch_yaml_name(fm, canonical_name)
    body = raw[end_fm + 5 :]
    body = transform_blade_skill_body(body, sail_artisan=sail_artisan)
    banner = (
        f"> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `{commit}` "
        f"— `{rel_source}`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.\n\n"
    )
    out = fm + banner + body
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "SKILL.md").write_text(out, encoding="utf-8")


def write_tailwind_md(
    boost_root: Path, dest_dir: Path, rel_source: str, commit: str
) -> None:
    raw = (boost_root / rel_source).read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise SystemExit(f"Expected YAML frontmatter in {rel_source}")
    end_fm = raw.find("\n---\n", 4)
    if end_fm == -1:
        raise SystemExit(f"Invalid frontmatter in {rel_source}")
    fm = raw[: end_fm + 5]
    body = raw[end_fm + 5 :].lstrip("\n")
    banner = (
        f"> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `{commit}` "
        f"— `{rel_source}`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.\n\n"
    )
    out = fm + banner + body
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "SKILL.md").write_text(out, encoding="utf-8")


def write_sail_core(boost_root: Path, dest_dir: Path, rel_source: str, commit: str) -> None:
    raw = (boost_root / rel_source).read_text(encoding="utf-8")
    body = strip_blade_php_blocks(raw)
    body = replace_sail_path(body)
    body = replace_artisan(body, prefix="./vendor/bin/sail artisan")
    body = replace_composer_sail(body)
    body = replace_npm_sail(body)
    body = re.sub(
        r"\{\{\s*\$assist->sailBinaryPath\(\)\s*\}\}\s+php",
        "./vendor/bin/sail php",
        body,
    )
    fm = """---
name: laravel-sail
description: "Use when the Laravel project runs under Laravel Sail. Trigger for Docker/Sail workflows, running artisan, composer, npm, or PHP only inside containers. Covers: ./vendor/bin/sail up/down, sail artisan, sail composer, sail npm, and never running host PHP/Composer against a Sail-only app by mistake."
license: MIT
metadata:
  author: laravel
---

"""
    banner = (
        f"> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `{commit}` "
        f"— `{rel_source}`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.\n\n"
    )
    out = fm + banner + body.strip() + "\n"
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "SKILL.md").write_text(out, encoding="utf-8")


def write_pint_core(boost_root: Path, dest_dir: Path, rel_source: str, commit: str) -> None:
    _ = (boost_root / rel_source).read_text(encoding="utf-8")  # ensure path exists
    fm = """---
name: laravel-pint
description: "Use when formatting PHP in Laravel projects that use Laravel Pint. Trigger after editing PHP files, before finalizing a change, or when the user mentions Pint or project PHP style. Covers: running pint on dirty files, --format agent when supported, and not using pint --test for autofix workflows."
license: MIT
metadata:
  author: laravel
---

"""
    banner = (
        f"> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `{commit}` "
        f"— `{rel_source}` (Blade branches merged). Regenerate: `python3 scripts/sync-boost-ai-skills.py`.\n\n"
    )
    body = """# Laravel Pint Code Formatter

- If you have modified any PHP files, run `./vendor/bin/pint --dirty` before finalizing changes so code matches the project's expected style.
- When your tooling supports Pint's agent formatter, prefer `./vendor/bin/pint --dirty --format agent`.
- Do not rely on `./vendor/bin/pint --test` to fix style; run `./vendor/bin/pint` (with or without `--format agent`) to apply fixes.
- With **Laravel Sail**, prefix: `./vendor/bin/sail bin pint --dirty` (and add `--format agent` when appropriate).
"""
    out = fm + banner + body
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "SKILL.md").write_text(out, encoding="utf-8")


def write_phpunit_core(boost_root: Path, dest_dir: Path, rel_source: str, commit: str) -> None:
    raw = (boost_root / rel_source).read_text(encoding="utf-8")
    body = strip_blade_php_blocks(raw)
    body = replace_artisan(body, prefix="")
    fm = """---
name: phpunit-laravel
description: "Use when writing or running PHPUnit tests in a Laravel app that uses PHPUnit (not Pest). Trigger for test classes, assertions, make:test --phpunit, or running the test suite. Covers: creating tests, running filtered tests, and treating tests as core code that must not be removed without approval."
license: MIT
metadata:
  author: laravel
---

"""
    banner = (
        f"> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `{commit}` "
        f"— `{rel_source}`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.\n\n"
    )
    note = (
        "\n**Command prefix:** Use `php artisan` on the host or `./vendor/bin/sail artisan` "
        "when using Sail.\n"
    )
    out = fm + banner + body.strip() + note + "\n"
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "SKILL.md").write_text(out, encoding="utf-8")


def write_livewire_with_reference(
    boost_root: Path, dest_dir: Path, rel_skill: str, rel_ref: str, commit: str
) -> None:
    write_flux_like(
        boost_root,
        dest_dir,
        rel_skill,
        commit,
        sail_artisan=False,
        canonical_name="livewire-development",
    )
    path = dest_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    ref_raw = (boost_root / rel_ref).read_text(encoding="utf-8").strip()
    ref_lines = ref_raw.splitlines()
    if ref_lines and ref_lines[0].startswith("# "):
        ref_lines = ref_lines[1:]
    ref = "\n".join(ref_lines).strip() + "\n"
    needle = "For interceptors and hooks, see [reference/javascript-hooks.md](reference/javascript-hooks.md)."
    if needle not in text:
        raise SystemExit("Livewire skill: expected reference link not found")
    text = text.replace(
        needle,
        "## JavaScript integration\n\n"
        + ref
        + "\n",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    env_root = os.environ.get("BOOST_REPO_ROOT")
    rev = os.environ.get("BOOST_REV")

    if env_root:
        boost_root = Path(env_root).resolve()
        if not (boost_root / ".git").is_dir():
            print("BOOST_REPO_ROOT must be a git checkout of laravel/boost", file=sys.stderr)
            sys.exit(1)
        commit = git_head_sha(boost_root)
    else:
        tmp = Path(tempfile.mkdtemp(prefix="boost-ai-sync-"))
        try:
            clone_boost(tmp, rev)
            commit = git_head_sha(tmp)
            boost_root = tmp
        except subprocess.CalledProcessError:
            shutil.rmtree(tmp, ignore_errors=True)
            raise

    try:
        STEERING_SKILLS.mkdir(parents=True, exist_ok=True)

        write_flux_like(
            boost_root,
            STEERING_SKILLS / "fluxui-free-development",
            ".ai/fluxui-free/skill/fluxui-development/SKILL.blade.php",
            commit,
            sail_artisan=False,
            canonical_name="fluxui-free-development",
        )
        write_flux_like(
            boost_root,
            STEERING_SKILLS / "fluxui-pro-development",
            ".ai/fluxui-pro/skill/fluxui-development/SKILL.blade.php",
            commit,
            sail_artisan=False,
            canonical_name="fluxui-pro-development",
        )
        write_flux_like(
            boost_root,
            STEERING_SKILLS / "pest-testing",
            f".ai/pest/{PEST_MAJOR}/skill/pest-testing/SKILL.blade.php",
            commit,
            sail_artisan=False,
        )
        write_sail_core(
            boost_root,
            STEERING_SKILLS / "laravel-sail",
            ".ai/sail/core.blade.php",
            commit,
        )
        write_livewire_with_reference(
            boost_root,
            STEERING_SKILLS / "livewire-development",
            f".ai/livewire/{LIVEWIRE_MAJOR}/skill/livewire-development/SKILL.blade.php",
            f".ai/livewire/{LIVEWIRE_MAJOR}/skill/livewire-development/reference/javascript-hooks.md",
            commit,
        )
        write_tailwind_md(
            boost_root,
            STEERING_SKILLS / "tailwindcss-development",
            f".ai/tailwindcss/{TAILWIND_MAJOR}/skill/tailwindcss-development/SKILL.md",
            commit,
        )
        write_phpunit_core(
            boost_root,
            STEERING_SKILLS / "phpunit-laravel",
            ".ai/phpunit/core.blade.php",
            commit,
        )
        write_pint_core(
            boost_root,
            STEERING_SKILLS / "laravel-pint",
            ".ai/pint/core.blade.php",
            commit,
        )

        manifest = STEERING_SKILLS / ".boost-ai-sync.json"
        manifest.write_text(
            '{\n  "repo": "laravel/boost",\n  "commit": "%s"\n}\n' % commit,
            encoding="utf-8",
        )
        print(f"Wrote Boost-derived skills from laravel/boost @ {commit}")
    finally:
        if not env_root:
            shutil.rmtree(boost_root, ignore_errors=True)


if __name__ == "__main__":
    main()
