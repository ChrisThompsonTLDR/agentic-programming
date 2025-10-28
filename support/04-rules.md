# Rule Loader

Before executing any command, load the shared rule set:

1. Enumerate every rule file under `.cursor/rules/epics/*.mdc`.
2. Read each file completely so the active session inherits its constraints.
3. Re-read this loader whenever new rule files are introduced during the workflow.
