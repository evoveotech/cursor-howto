# Changelog

This project is **built and maintained by [Evoveo Tech](https://github.com/evoveotech)** (**EVOVEO INNOVATIONS LIMITED**). It documents the **Cursor IDE** (editor), **Cursor** in-editor agent workflows, and the **Cursor CLI** where applicable—see [Cursor documentation](https://docs.cursor.com).

---

## v2.2.0 — 2026-03-26

### Documentation

- Sync all tutorials and references with Cursor v2.1.84 (f78c094) @evoveotech
  - Update slash commands to 55+ built-in + 5 bundled skills, mark 3 deprecated
  - Expand hook events from 18 to 25, add `agent` hook type (now 4 types)
  - Add Auto Mode, Channels, Voice Dictation to advanced features
  - Add `effort`, `shell` skill frontmatter fields; `initialPrompt`, `disallowedTools` agent fields
  - Add WebSocket MCP transport, elicitation, 2KB tool cap
  - Add plugin LSP support, `userConfig`, `${CURSOR_PLUGIN_DATA}`
  - Update all reference docs (CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX)
- Rewrite README as landing-page-structured guide (32a0776) @evoveotech

### Bug Fixes

- Add missing cSpell words and README sections for CI compliance (93f9d51) @evoveotech
- Add `Sandboxing` to cSpell dictionary (b80ce6f) @evoveotech

**Full Changelog**: https://github.com/evoveotech/cursor-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug Fixes

- Remove dead marketplace link failing CI link checks (3fdf0d6) @evoveotech
- Add `sandboxed` and `pycache` to cSpell dictionary (dc64618) @evoveotech

**Full Changelog**: https://github.com/evoveotech/cursor-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Features

- Add adaptive learning path with self-assessment and lesson quiz skills (1ef46cd) @evoveotech
  - `/self-assessment` — interactive proficiency quiz across 10 feature areas with personalized learning path
  - `/lesson-quiz [lesson]` — per-lesson knowledge check with 8-10 targeted questions

### Bug Fixes

- Update broken URLs, deprecations, and outdated references (8fe4520) @evoveotech
- Fix broken links in resources and self-assessment skill (7a05863) @evoveotech
- Use tilde fences for nested code blocks in concepts guide (5f82719) @VikalpP
- Add missing words to cSpell dictionary (8df7572) @evoveotech

### Documentation

- Phase 5 QA — fix consistency, URLs, and terminology across docs (00bbe4c) @evoveotech
- Complete Phases 3-4 — new feature coverage and reference doc updates (132de29) @evoveotech
- Add MCPorter runtime to MCP context bloat section (ef52705) @evoveotech
- Add missing commands, features, and settings across 6 guides (4bc8f15) @evoveotech
- Add style guide based on existing repo conventions (84141d0) @evoveotech
- Add self-assessment row to guide comparison table (8fe0c96) @evoveotech
- Add VikalpP to contributors list for PR #7 (d5b4350) @evoveotech
- Add self-assessment and lesson-quiz skill references to README and roadmap (d5a6106) @evoveotech

### New Contributors

- @VikalpP made their first contribution in #7

**Full Changelog**: https://github.com/evoveotech/cursor-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Features

- Sync all documentation with Cursor February 2026 features (487c96d)
  - Update 26 files across all 10 tutorial directories and 7 reference documents
  - Add documentation for **Auto Memory** — persistent learnings per project
  - Add documentation for **Remote Control**, **Web Sessions**, and **Desktop App**
  - Add documentation for **Agent Teams** (experimental multi-agent collaboration)
  - Add documentation for **MCP OAuth 2.0**, **Tool Search**, and **Cursor connectors**
  - Add documentation for **Persistent Memory** and **Worktree Isolation** for subagents
  - Add documentation for **Background Subagents**, **Task List**, **Prompt Suggestions**
  - Add documentation for **Sandboxing** and **Managed Settings** (Enterprise)
  - Add documentation for **HTTP Hooks** and 7 new hook events
  - Add documentation for **Plugin Settings**, **LSP Servers**, and Marketplace updates
  - Add documentation for **Summarize from Checkpoint** rewind option
  - Document 17 new slash commands (`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast`, etc.)
  - Document new CLI flags (`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode`, etc.)
  - Document new environment variables for auto memory, effort levels, agent teams, and more

### Design

- Redesign logo to compass-bracket mark with minimal palette (20779db)

### Bug Fixes / Corrections

- Update model names: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- Fix permission mode names: replace fictional "Unrestricted/Confirm/Read-only" with actual `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- Fix hook events: remove fictional `PreCommit`/`PostCommit`/`PrePush`, add real events (`SubagentStart`, `WorktreeCreate`, `ConfigChange`, etc.)
- Fix CLI syntax: replace `cursor-code --headless` with `cursor -p` (print mode)
- Fix checkpoint commands: replace fictional `/checkpoint save/list/rewind/diff` with actual `Esc+Esc` / `/rewind` interface
- Fix session management: replace fictional `/session list/new/switch/save` with real `/resume`/`/rename`/`/fork`
- Fix plugin manifest format: migrate `plugin.yaml` → `.cursor-plugin/plugin.json`
- Fix MCP config paths: `~/.cursor/mcp.json` → `.mcp.json` (project) / `~/.cursor/mcp.json` (user)
- Fix documentation URLs to use [docs.cursor.com](https://docs.cursor.com); remove fictional `plugins.*` hostnames
- Remove fictional configuration fields across multiple files
- Update all "Last Updated" dates to February 2026

**Full Changelog**: https://github.com/evoveotech/cursor-howto/compare/20779db...v2.0.0
