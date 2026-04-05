# Cursor IDE: what this guide assumes

*Built by **Evoveo Tech** (**EVOVEO INNOVATIONS LIMITED**).*

This repository teaches the **Cursor IDE** and **Cursor CLI** (see [Cursor documentation](https://docs.cursor.com)) from [Anysphere](https://cursor.com). It is not documentation for other agent CLIs. Use it together with the **[official Cursor documentation](https://docs.cursor.com)**.

## Cursor-native building blocks

| Idea in this repo | What to use in Cursor |
|-------------------|------------------------|
| **Project instructions** (`CURSOR.md` in tutorials) | Prefer **`AGENTS.md`** at the repo root and/or **`.cursor/rules/`** (`.mdc` rules with globs). See [Rules](https://docs.cursor.com/context/rules). |
| **“Slash commands”** (markdown files under `01-slash-commands/`) | Treat them as **reusable prompts**: paste into Chat/Agent, or fold into **Rules**, **Notepads**, or team snippets. Cursor does not ship a separate “commands folder” identical to other tools. |
| **Skills** (`03-skills/`) | Map to **Cursor Rules**, **Notepads**, or documented workflows—patterns you apply consistently, not a different runtime. |
| **MCP** (`05-mcp/`) | Configure in **Cursor Settings → MCP** and/or project MCP config as described in [Cursor MCP docs](https://docs.cursor.com/context/mcp). |
| **Subagents** (`04-subagents/`) | Use Cursor’s **multi-step Agent** / focused tasks; store prompts and checklists as markdown the same way. |
| **Hooks / plugins** (`06-hooks/`, `07-plugins/`) | Cursor does **not** mirror other products’ shell-hook or plugin manifests 1:1. Prefer **git hooks**, **CI**, **formatters**, and **MCP tools** for automation. |

## Version and docs

- Feature names and shortcuts change. **Trust [docs.cursor.com](https://docs.cursor.com)** over any version number in this repo.
- Badges and “compatible with Cursor X.Y” lines are **approximate**; verify in your installed app (**Help → About** or equivalent).

## Repository health checks

From the repo root (with Python 3.10+):

```bash
python scripts/check_cross_references.py
python scripts/check_links.py
```

Optional: install `@mermaid-js/mermaid-cli` and run `python scripts/check_mermaid.py` to validate diagrams.

GitHub URLs under `github.com/evoveotech/cursor-howto` may 404 until the repository is public; the link checker skips them on purpose.
