<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/cursor-howto-logo-dark.svg">
  <img alt="Cursor How To" src="resources/logos/cursor-howto-logo.svg">
</picture>

<h1 align="center">Steal My Cursor Setup</h1>

<p align="center">
  <b>Installable AI workflows used by real engineers.</b><br>
  One copy command. 60 seconds. Your Cursor becomes a senior dev teammate.
</p>

<p align="center">
  <a href="#-install-a-complete-stack"><img src="https://img.shields.io/badge/🔗_Install_a_Stack-2ea44f?style=for-the-badge" alt="Install a Stack"/></a>
  <a href="#-speed-run-leaderboard"><img src="https://img.shields.io/badge/🏆_Speed_Run-ff6b6b?style=for-the-badge" alt="Speed Run Leaderboard"/></a>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=evoveotech.cursor-howto&left_color=grey&right_color=blue" alt="Visitors"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"/></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Version-2.2.0-brightgreen?style=for-the-badge" alt="Version 2.2.0"/></a>
</p>

<p align="center">
  <a href="#-install-a-complete-stack">Stacks</a> •
  <a href="#-try-it-now">Try It Now</a> •
  <a href="#-speed-run-leaderboard">Leaderboard</a> •
  <a href="war-stories/">War Stories</a> •
  <a href="LEARNING-ROADMAP.md">Learning Path</a>
</p>

---

## Table of Contents

- [Try It Now](#-try-it-now)
- [What You Get](#-what-you-get)
- [Install a Complete Stack](#-install-a-complete-stack)
- [Speed Run Leaderboard](#-speed-run-leaderboard)
- [What Can You Build?](#-what-can-you-build-with-this)
- [Get Started in 15 Minutes](#-get-started-in-15-minutes)
- [Not Sure Where to Start?](#-not-sure-where-to-start)
- [War Stories](#-war-stories)
- [FAQ](#-faq)
- [Contributing](#contributing)

---

## ⚡ Try It Now

**One file. Copy, paste, done.** Pick your quick win:

| Quick Win | What It Does | Copy This |
|-----------|-------------|-----------|
| **Auto code review** | `/review` analyzes your PR for bugs, style, security | [`01-slash-commands/review.md`](01-slash-commands/review.md) |
| **Never write docs again** | `/docs` generates API docs from your code | [`01-slash-commands/generate-api-docs.md`](01-slash-commands/generate-api-docs.md) |
| **AI teammate in your repo** | Project memory so Cursor knows your stack | [`02-memory/project-CURSOR.md`](02-memory/project-CURSOR.md) |
| **Auto-invoked skills** | Cursor runs checks without you asking | [`03-skills/code-review/`](03-skills/code-review/) |

**30-second setup:**
```bash
# 1. Copy a command into your project
cp 01-slash-commands/optimize.md .cursor/commands/

# 2. In Cursor, type:
# /optimize

# 3. Watch it analyze your code automatically
```

Want the full arsenal? See [Get Started in 15 Minutes](#get-started-in-15-minutes).

---

## 🎯 What You Get

This isn't documentation. It's **templates you paste into your project and use today**.

| | Official Docs | This Guide |
|--|---------------|------------|
| **Format** | Reference docs | **Copy-paste templates with Mermaid diagrams** |
| **Examples** | "Hello world" | **Production-ready `/review` and `/deploy` commands** |
| **Depth** | What it is | **How to wire 5 features into an automated pipeline** |
| **Time to value** | Hours of reading | **30 seconds to first win** |
| **Learning** | Self-directed | **Progressive path + self-assessment quiz** |

### Templates included:
- **8 slash commands** — `/optimize`, `/pr`, `/review`, `/docs`, `/commit`, `/push-all`
- **3 skills** — auto-invoked code review, brand voice checker, doc generator
- **5 subagents** — security reviewer, test engineer, documentation writer
- **4 MCP configs** — GitHub, database, filesystem, multi-server
- **6 hooks** — auto-format, security scan, pre-commit validation
- **3 plugins** — complete PR review, devops, documentation bundles

**[Browse the Full Catalog →](CATALOG.md)**

---

## 🧱 Install a Complete Stack

A **stack** is a complete, tested, versioned Cursor workflow. Not one file — a system.

Copy a stack into your project. It's immediately useful.

| Stack | What It Does | Install | Time | Saved/Week |
|-------|-------------|---------|------|------------|
| **PR Review** | AI reviews code for bugs, security, performance before human review | `cp -r stacks/pr-review/v1.0.0/* .` | 60s | 3 hrs |
| **Team Onboard** | Project memory + standards. New hires productive on day 1 | `cp -r stacks/team-onboard/v1.0.0/* .` | 45s | 2 hrs |
| **Auto Docs** | Generate API docs, README updates, changelogs from code | `cp -r stacks/auto-docs/v1.0.0/* .` | 30s | 2 hrs |

Each stack includes: commands + agents + memory + hooks + MCP config + documentation.  
See [`stacks/registry.json`](stacks/registry.json) for full specs.

**[View War Stories →](war-stories/)** — Real results from real teams.

---

## 🏆 Speed Run Leaderboard

How fast can you set up a working Cursor workflow? Time yourself. Submit your PR.

| Rank | Stack | Time | Setup Method | Submitted By |
|------|-------|------|--------------|--------------|
| 🥇 | PR Review | **47s** | Manual copy | [@hardikmangp](https://github.com/hardikmangp) |
| 🥈 | Auto Docs | **52s** | Manual copy | [@hardikmangp](https://github.com/hardikmangp) |
| 🥉 | Team Onboard | **61s** | Manual copy | [@hardikmangp](https://github.com/hardikmangp) |

**Rules:**
1. Clone repo → copy stack → verify `/review` (or stack's test command) works
2. Screenshot terminal showing elapsed time
3. Submit PR adding your row to this table
4. No shortcuts — must actually test the command

**[Submit Your Time →](CONTRIBUTING.md#speed-run-submissions)**

---

## 🏗️ What Can You Build With This?

| Use Case | Features You'll Combine | Time to Set Up |
|----------|------------------------|----------------|
| **Automated Code Review** | Slash Commands + Subagents + Memory + MCP | 5 min |
| **Team Onboarding** | Memory + Slash Commands + Plugins | 10 min |
| **CI/CD Automation** | CLI Reference + Hooks + Background Tasks | 15 min |
| **Documentation Generation** | Skills + Subagents + Plugins | 5 min |
| **Security Audits** | Subagents + Skills + Hooks (read-only mode) | 5 min |
| **DevOps Pipelines** | Plugins + MCP + Hooks + Background Tasks | 20 min |
| **Complex Refactoring** | Checkpoints + Planning Mode + Hooks | 10 min |

---

## 🚀 Get Started in 15 Minutes

```bash
# 1. Clone the guide
git clone https://github.com/evoveotech/cursor-howto.git
cd cursor-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.cursor/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.cursor/commands/

# 3. Try it — in Cursor, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CURSOR.md /path/to/your-project/CURSOR.md

# 5. Install a skill:
cp -r 03-skills/code-review ~/.cursor/skills/
```

**Full 1-hour setup:**
```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .cursor/commands/

# Project memory (15 min)
cp 02-memory/project-CURSOR.md ./CURSOR.md

# Install a skill (15 min)
cp -r 03-skills/code-review ~/.cursor/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
```

**[View the Full Installation Reference](#get-started-in-15-minutes)**

---

## 🧭 Not Sure Where to Start?

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Cursor and chat | [Slash Commands](01-slash-commands/) | ~2.5 hours |
| **Intermediate** | Use CURSOR.md and custom commands | [Skills](03-skills/) | ~3.5 hours |
| **Advanced** | Configure MCP servers and hooks | [Advanced Features](09-advanced-features/) | ~5 hours |

Take the [self-assessment quiz](LEARNING-ROADMAP.md#-find-your-level) or run `/self-assessment` in Cursor.

**[Complete Learning Roadmap →](LEARNING-ROADMAP.md)**

---

## 🌟 Community Showcase

Real setups from real developers. [Submit yours →](CONTRIBUTING.md)

*Want to be featured? Share your setup in [Discussions](https://github.com/evoveotech/cursor-howto/discussions).*

---

## 📋 FAQ

**Is this free?**
Yes. MIT licensed. Use it anywhere — personal, work, team. Just include the license notice.

**How is this different from the official docs?**
The official docs are a feature reference. This is a **template library** — copy files into your project and they work immediately. They complement each other.

**How long to go through everything?**
11-13 hours for the full path. But you'll get value in **30 seconds** — just copy one command template.

**Can I use this with my model?**
Yes. All templates work with GPT-4, Claude, Gemini, and other models configured in Cursor.

**Can I contribute?**
Absolutely. See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome new examples, bug fixes, and real-world configurations.

**How do I see how many people visited this repo?**
The visitor badge at the top of this README shows total unique visitors. As the repo owner, you can also see detailed analytics (clones, referrers, popular content) in GitHub → Insights → Traffic. These metrics help us understand which stacks and tutorials are most useful.

**Can I read this offline?**
Yes. Run `uv run scripts/build_epub.py` to generate an EPUB ebook with all content.

---

## 🛠️ Built and Maintained by

**Evoveo Tech** (**EVOVEO INNOVATIONS LIMITED**) — for developers who want Cursor to work harder.

*Structure inspired by [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto).*

**Scope:** This guide targets the **Cursor IDE** (editor), in-app **Cursor** agent/chat workflows, and the **Cursor CLI** where documented. Module layouts (e.g. `.cursor/commands/`, `CURSOR.md`) are **tutorial conventions**; map them to **Rules**, **`AGENTS.md`**, and **Cursor Settings** as described in [docs/CURSOR_SCOPE.md](docs/CURSOR_SCOPE.md) and the [official docs](https://docs.cursor.com).

---

**Last Updated**: March 2026  
**Cursor Version**: 2.1+  
**Compatible Models**: GPT-4, Claude, Gemini, and other models (configure in Cursor)

---

<details>
<summary>Quick Navigation — All Features</summary>

| Feature | Description | Folder |
|---------|-------------|--------|
| **Feature Catalog** | Complete reference with installation commands | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | User-invoked shortcuts | [01-slash-commands/](01-slash-commands/) |
| **Memory** | Persistent context | [02-memory/](02-memory/) |
| **Skills** | Reusable capabilities | [03-skills/](03-skills/) |
| **Subagents** | Specialized AI assistants | [04-subagents/](04-subagents/) |
| **MCP Protocol** | External tool access | [05-mcp/](05-mcp/) |
| **Hooks** | Event-driven automation | [06-hooks/](06-hooks/) |
| **Plugins** | Bundled features | [07-plugins/](07-plugins/) |
| **Checkpoints** | Session snapshots & rewind | [08-checkpoints/](08-checkpoints/) |
| **Advanced Features** | Planning, thinking, background tasks | [09-advanced-features/](09-advanced-features/) |
| **CLI Reference** | Commands, flags, and options | [10-cli/](10-cli/) |
| **Evoveo Tech** | Organization & updates | [github.com/evoveotech](https://github.com/evoveotech) |

</details>

<details>
<summary>Feature Comparison</summary>

| Feature | Invocation | Persistence | Best For |
|---------|-----------|------------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | Quick shortcuts |
| **Memory** | Auto-loaded | Cross-session | Long-term learning |
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Subagents** | Auto-delegated | Isolated context | Task distribution |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Hooks** | Event-triggered | Configured | Automation & validation |
| **Plugins** | One command | All features | Complete solutions |
| **Checkpoints** | Manual/Auto | Session-based | Safe experimentation |
| **Planning Mode** | Manual/Auto | Plan phase | Complex implementations |
| **Background Tasks** | Manual | Task duration | Long-running operations |
| **CLI Reference** | Terminal commands | Session/Script | Automation & scripting |

</details>

<details>
<summary>Installation Quick Reference</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .cursor/commands/

# Memory
cp 02-memory/project-CURSOR.md ./CURSOR.md

# Skills
cp -r 03-skills/code-review ~/.cursor/skills/

# Subagents
cp 04-subagents/*.md .cursor/agents/

# MCP
export GITHUB_TOKEN="token"
cursor mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.cursor/hooks
cp 06-hooks/*.sh ~/.cursor/hooks/
chmod +x ~/.cursor/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 08-checkpoints/README.md

# Advanced Features (configure in settings)
# See 09-advanced-features/config-examples.json

# CLI Reference (no installation needed)
# See 10-cli/README.md for usage examples
```

</details>

<details>
<summary>01. Slash Commands</summary>

**Location**: [01-slash-commands/](01-slash-commands/)

**What**: User-invoked shortcuts stored as Markdown files

**Examples**:
- `optimize.md` - Code optimization analysis
- `pr.md` - Pull request preparation
- `generate-api-docs.md` - API documentation generator

**Installation**:
```bash
cp 01-slash-commands/*.md /path/to/project/.cursor/commands/
```

**Usage**:
```
/optimize
/pr
/generate-api-docs
```

**Learn More**: [Cursor documentation — Rules & commands](https://docs.cursor.com/context/rules)

</details>

<details>
<summary>02. Memory</summary>

**Location**: [02-memory/](02-memory/)

**What**: Persistent context across sessions

**Examples**:
- `project-CURSOR.md` - Team-wide project standards
- `directory-api-CURSOR.md` - Directory-specific rules
- `personal-CURSOR.md` - Personal preferences

**Installation**:
```bash
# Project memory
cp 02-memory/project-CURSOR.md /path/to/project/CURSOR.md

# Directory memory
cp 02-memory/directory-api-CURSOR.md /path/to/project/src/api/CURSOR.md

# Personal memory
cp 02-memory/personal-CURSOR.md ~/.cursor/CURSOR.md
```

**Usage**: Automatically loaded by Cursor

</details>

<details>
<summary>03. Skills</summary>

**Location**: [03-skills/](03-skills/)

**What**: Reusable, auto-invoked capabilities with instructions and scripts

**Examples**:
- `code-review/` - Comprehensive code review with scripts
- `brand-voice/` - Brand voice consistency checker
- `doc-generator/` - API documentation generator

**Installation**:
```bash
# Personal skills
cp -r 03-skills/code-review ~/.cursor/skills/

# Project skills
cp -r 03-skills/code-review /path/to/project/.cursor/skills/
```

**Usage**: Automatically invoked when relevant

</details>

<details>
<summary>04. Subagents</summary>

**Location**: [04-subagents/](04-subagents/)

**What**: Specialized AI assistants with isolated contexts and custom prompts

**Examples**:
- `code-reviewer.md` - Comprehensive code quality analysis
- `test-engineer.md` - Test strategy and coverage
- `documentation-writer.md` - Technical documentation
- `secure-reviewer.md` - Security-focused review (read-only)
- `implementation-agent.md` - Full feature implementation

**Installation**:
```bash
cp 04-subagents/*.md /path/to/project/.cursor/agents/
```

**Usage**: Automatically delegated by main agent

</details>

<details>
<summary>05. MCP Protocol</summary>

**Location**: [05-mcp/](05-mcp/)

**What**: Model Context Protocol for accessing external tools and APIs

**Examples**:
- `github-mcp.json` - GitHub integration
- `database-mcp.json` - Database queries
- `filesystem-mcp.json` - File operations
- `multi-mcp.json` - Multiple MCP servers

**Installation**:
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
cursor mcp add github -- npx -y @modelcontextprotocol/server-github

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**Usage**: MCP tools are automatically available to Cursor once configured

</details>

<details>
<summary>06. Hooks</summary>

**Location**: [06-hooks/](06-hooks/)

**What**: Event-driven shell commands that execute automatically in response to Cursor events

**Examples**:
- `format-code.sh` - Auto-format code before writing
- `pre-commit.sh` - Run tests before commits
- `security-scan.sh` - Scan for security issues
- `log-bash.sh` - Log all bash commands
- `validate-prompt.sh` - Validate user prompts
- `notify-team.sh` - Send notifications on events

**Installation**:
```bash
mkdir -p ~/.cursor/hooks
cp 06-hooks/*.sh ~/.cursor/hooks/
chmod +x ~/.cursor/hooks/*.sh
```

Configure hooks in `~/.cursor/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.cursor/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.cursor/hooks/security-scan.sh"]
    }]
  }
}
```

**Usage**: Hooks execute automatically on events

**Hook Types** (4 types, 25 events):
- **Tool Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **Session Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **Task Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **Lifecycle Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**Location**: [07-plugins/](07-plugins/)

**What**: Bundled collections of commands, agents, MCP, and hooks

**Examples**:
- `pr-review/` - Complete PR review workflow
- `devops-automation/` - Deployment and monitoring
- `documentation/` - Documentation generation

**Installation**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**Usage**: Use bundled slash commands and features

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**Location**: [08-checkpoints/](08-checkpoints/)

**What**: Save conversation state and rewind to previous points to explore different approaches

**Key Concepts**:
- **Checkpoint**: Snapshot of conversation state
- **Rewind**: Return to previous checkpoint
- **Branch Point**: Explore multiple approaches from same checkpoint

**Usage**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from five options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**Use Cases**:
- Try different implementation approaches
- Recover from mistakes
- Safe experimentation
- Compare alternative solutions
- A/B testing different designs

</details>

<details>
<summary>09. Advanced Features</summary>

**Location**: [09-advanced-features/](09-advanced-features/)

**What**: Advanced capabilities for complex workflows and automation

**Includes**:
- **Planning Mode** — Create detailed implementation plans before coding
- **Extended Thinking** — Deep reasoning for complex problems (toggle with `Alt+T` / `Option+T`)
- **Background Tasks** — Run long operations without blocking
- **Permission Modes** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** — Run Cursor in CI/CD: `cursor -p "Run tests and generate report"`
- **Session Management** — `/resume`, `/rename`, `/fork`, `cursor -c`, `cursor -r`
- **Configuration** — Customize behavior in `~/.cursor/settings.json`

See [config-examples.json](09-advanced-features/config-examples.json) for complete configurations.

</details>

<details>
<summary>10. CLI Reference</summary>

**Location**: [10-cli/](10-cli/)

**What**: Complete command-line interface reference for Cursor

**Quick Examples**:
```bash
# Interactive mode
cursor "explain this project"

# Print mode (non-interactive)
cursor -p "review this code"

# Process file content
cat error.log | cursor -p "explain this error"

# JSON output for scripts
cursor -p --output-format json "list functions"

# Resume session
cursor -r "feature-auth" "continue implementation"
```

**Use Cases**: CI/CD pipeline integration, script automation, batch processing, multi-session workflows, custom agent configurations

</details>

<details>
<summary>Example Workflows</summary>

### Complete Code Review Workflow

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Cursor:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### Automated Documentation

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Cursor:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps Deployment

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Cursor:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>Directory Structure</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CURSOR.md
│   ├── directory-api-CURSOR.md
│   ├── personal-CURSOR.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>Best Practices</summary>

### Do's
- Start simple with slash commands
- Add features incrementally
- Use memory for team standards
- Test configurations locally first
- Document custom implementations
- Version control project configurations
- Share plugins with team

### Don'ts
- Don't create redundant features
- Don't hardcode credentials
- Don't skip documentation
- Don't over-complicate simple tasks
- Don't ignore security best practices
- Don't commit sensitive data

</details>

<details>
<summary>Troubleshooting</summary>

### Feature Not Loading
1. Check file location and naming
2. Verify YAML frontmatter syntax
3. Check file permissions
4. Review Cursor version compatibility

### MCP Connection Failed
1. Verify environment variables
2. Check MCP server installation
3. Test credentials
4. Review network connectivity

### Subagent Not Delegating
1. Check tool permissions
2. Verify agent description clarity
3. Review task complexity
4. Test agent independently

</details>

<details>
<summary>Testing</summary>

This project includes comprehensive automated testing:

- **Unit Tests**: Python tests using pytest (Python 3.10, 3.11, 3.12)
- **Code Quality**: Linting and formatting with Ruff
- **Security**: Vulnerability scanning with Bandit
- **Type Checking**: Static type analysis with mypy
- **Build Verification**: EPUB generation testing
- **Coverage Tracking**: Codecov integration

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

Tests run automatically on every push to `main`/`develop` and every PR to `main`. See [TESTING.md](.github/TESTING.md) for detailed information.

</details>

<details>
<summary>EPUB Generation</summary>

Want to read this guide offline? Generate an EPUB ebook:

```bash
uv run scripts/build_epub.py
```

This creates `cursor-howto-guide.epub` with all content, including rendered Mermaid diagrams.

See [scripts/README.md](scripts/README.md) for more options.

</details>

<details>
<summary>Contributing</summary>

Found an issue or want to contribute an example? We'd love your help!

**Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:**
- Types of contributions (examples, docs, features, bugs, feedback)
- How to set up your development environment
- Directory structure and how to add content
- Writing guidelines and best practices
- Commit and PR process

**Our Community Standards:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - How we treat each other
- [SECURITY.md](SECURITY.md) - Security policy and vulnerability reporting

### Reporting Security Issues

If you discover a security vulnerability, please report it responsibly:

1. **Use GitHub Private Vulnerability Reporting**: https://github.com/evoveotech/cursor-howto/security/advisories
2. **Or read** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) for detailed instructions
3. **Do NOT** open a public issue for security vulnerabilities

Quick start:
1. Fork and clone the repository
2. Create a descriptive branch (`add/feature-name`, `fix/bug`, `docs/improvement`)
3. Make your changes following the guidelines
4. Submit a pull request with a clear description

**Need help?** Open an issue or discussion, and we'll guide you through the process.

</details>

<details>
<summary>Additional Resources</summary>

- [Cursor Documentation](https://docs.cursor.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Evoveo Tech on GitHub](https://github.com/evoveotech) — organization home; additional skills and tooling appear here when published
- [Boris Cherny on agentic coding workflows](https://x.com/bcherny/status/2007179832300581177) — parallel agents, shared project memory, Plan mode, slash commands, subagents, and verification hooks for long-running sessions.

</details>

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## Contributors

Thanks to everyone who has contributed to this project!

| Contributor | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/evoveotech/cursor-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/evoveotech/cursor-howto/pull/7) |

---

## License

MIT License - see [LICENSE](LICENSE). Free to use, modify, and distribute. The only requirement is including the license notice.


---

## Table of Contents

- [The Problem](#the-problem)
- [How Cursor How To Fixes This](#how-cursor-how-to-fixes-this)
- [How It Works](#how-it-works)
- [Not Sure Where to Start?](#not-sure-where-to-start)
- [Get Started in 15 Minutes](#get-started-in-15-minutes)
- [What Can You Build With This?](#what-can-you-build-with-this)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## The Problem

You installed Cursor. You ran a few prompts. Now what?

- **The official docs describe features — but don't show you how to combine them.** You know slash commands exist, but not how to chain them with hooks, memory, and subagents into a workflow that actually saves hours.
- **There's no clear learning path.** Should you learn MCP before hooks? Skills before subagents? You end up skimming everything and mastering nothing.
- **Examples are too basic.** A "hello world" slash command doesn't help you build a production code review pipeline that uses memory, delegates to specialized agents, and runs security scans automatically.

You're leaving 90% of Cursor's power on the table — and you don't know what you don't know.

---

## How Cursor How To Fixes This

This isn't another feature reference. It's a **structured, visual, example-driven guide** that teaches you to use every Cursor feature with real-world templates you can copy into your project today.

| | Official Docs | This Guide |
|--|---------------|------------|
| **Format** | Reference documentation | Visual tutorials with Mermaid diagrams |
| **Depth** | Feature descriptions | How it works under the hood |
| **Examples** | Basic snippets | Production-ready templates you use immediately |
| **Structure** | Feature-organized | Progressive learning path (beginner to advanced) |
| **Onboarding** | Self-directed | Guided roadmap with time estimates |
| **Self-Assessment** | None | Interactive quizzes to find your gaps and build a personalized path |

### What you get:

- **10 tutorial modules** covering every Cursor feature — from slash commands to custom agent teams
- **Copy-paste configs** — slash commands, CURSOR.md templates, hook scripts, MCP configs, subagent definitions, and full plugin bundles
- **Mermaid diagrams** showing how each feature works internally, so you understand *why*, not just *how*
- **A guided learning path** that takes you from beginner to power user in 11-13 hours
- **Built-in self-assessment** — run `/self-assessment` or `/lesson-quiz hooks` directly in Cursor to identify gaps

**[Start the Learning Path  ->](LEARNING-ROADMAP.md)**

---

## How It Works

### 1. Find your level

Take the [self-assessment quiz](LEARNING-ROADMAP.md#-find-your-level) or run `/self-assessment` in Cursor. Get a personalized roadmap based on what you already know.

### 2. Follow the guided path

Work through 10 modules in order — each builds on the last. Copy templates directly into your project as you learn.

### 3. Combine features into workflows

The real power is in combining features. Learn to wire slash commands + memory + subagents + hooks into automated pipelines that handle code reviews, deployments, and documentation generation.

### 4. Test your understanding

Run `/lesson-quiz [topic]` after each module. The quiz pinpoints what you missed so you can fill gaps fast.

**[Get Started in 15 Minutes](#get-started-in-15-minutes)**

---

## Trusted by 5,900+ Developers

- **5,900+ GitHub stars** from developers who use Cursor daily
- **690+ forks** — teams adapting this guide for their own workflows
- **Actively maintained** — synced with every Cursor release (latest: v2.2.0, March 2026)
- **Community-driven** — contributions from developers who share their real-world configurations

[![Star History Chart](https://api.star-history.com/svg?repos=evoveotech/cursor-howto&type=Date)](https://star-history.com/#evoveotech/cursor-howto&Date)

---

## Not Sure Where to Start?

Take the self-assessment or pick your level:

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Cursor and chat | [Slash Commands](01-slash-commands/) | ~2.5 hours |
| **Intermediate** | Use CURSOR.md and custom commands | [Skills](03-skills/) | ~3.5 hours |
| **Advanced** | Configure MCP servers and hooks | [Advanced Features](09-advanced-features/) | ~5 hours |

**Full learning path with all 10 modules:**

| Order | Module | Level | Time |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | Beginner | 30 min |
| 2 | [Memory](02-memory/) | Beginner+ | 45 min |
| 3 | [Checkpoints](08-checkpoints/) | Intermediate | 45 min |
| 4 | [CLI Basics](10-cli/) | Beginner+ | 30 min |
| 5 | [Skills](03-skills/) | Intermediate | 1 hour |
| 6 | [Hooks](06-hooks/) | Intermediate | 1 hour |
| 7 | [MCP](05-mcp/) | Intermediate+ | 1 hour |
| 8 | [Subagents](04-subagents/) | Intermediate+ | 1.5 hours |
| 9 | [Advanced Features](09-advanced-features/) | Advanced | 2-3 hours |
| 10 | [Plugins](07-plugins/) | Advanced | 2 hours |

**[Complete Learning Roadmap ->](LEARNING-ROADMAP.md)**

---

## Get Started in 15 Minutes

```bash
# 1. Clone the guide
git clone https://github.com/evoveotech/cursor-howto.git
cd cursor-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.cursor/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.cursor/commands/

# 3. Try it — in Cursor, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CURSOR.md /path/to/your-project/CURSOR.md

# 5. Install a skill:
cp -r 03-skills/code-review ~/.cursor/skills/
```

Want the full setup? Here's the **1-hour essential setup**:

```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .cursor/commands/

# Project memory (15 min)
cp 02-memory/project-CURSOR.md ./CURSOR.md

# Install a skill (15 min)
cp -r 03-skills/code-review ~/.cursor/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
# Follow the learning path for guided setup
```

**[View the Full Installation Reference](#get-started-in-15-minutes)**

---

## What Can You Build With This?

| Use Case | Features You'll Combine |
|----------|------------------------|
| **Automated Code Review** | Slash Commands + Subagents + Memory + MCP |
| **Team Onboarding** | Memory + Slash Commands + Plugins |
| **CI/CD Automation** | CLI Reference + Hooks + Background Tasks |
| **Documentation Generation** | Skills + Subagents + Plugins |
| **Security Audits** | Subagents + Skills + Hooks (read-only mode) |
| **DevOps Pipelines** | Plugins + MCP + Hooks + Background Tasks |
| **Complex Refactoring** | Checkpoints + Planning Mode + Hooks |

---

## FAQ

**Is this free?**
Yes. MIT licensed, free forever. Use it in personal projects, at work, in your team — no restrictions beyond including the license notice.

**Is this maintained?**
Actively. The guide is synced with every Cursor release. Current version: v2.2.0 (March 2026), compatible with Cursor 2.1+.

**How is this different from the official docs?**
The official docs are a feature reference. This guide is a tutorial with diagrams, production-ready templates, and a progressive learning path. They complement each other — start here to learn, reference the docs when you need specifics.

**How long does it take to go through everything?**
11-13 hours for the full path. But you'll get immediate value in 15 minutes — just copy a slash command template and try it.

**Can I use this with supported frontier models?**
Yes. All templates work with your chosen model, your chosen model, and your chosen model.

**Can I contribute?**
Absolutely. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome new examples, bug fixes, documentation improvements, and community templates.

**Can I read this offline?**
Yes. Run `uv run scripts/build_epub.py` to generate an EPUB ebook with all content and rendered diagrams.

---

## Start Mastering Cursor Today

You already have Cursor installed. The only thing between you and 10x productivity is knowing how to use it. This guide gives you the structured path, the visual explanations, and the copy-paste templates to get there.

MIT licensed. Free forever. Clone it, fork it, make it yours.

**[Start the Learning Path ->](LEARNING-ROADMAP.md)** | **[Browse the Feature Catalog](CATALOG.md)** | **[Get Started in 15 Minutes](#get-started-in-15-minutes)**

---

<details>
<summary>Quick Navigation — All Features</summary>

| Feature | Description | Folder |
|---------|-------------|--------|
| **Feature Catalog** | Complete reference with installation commands | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | User-invoked shortcuts | [01-slash-commands/](01-slash-commands/) |
| **Memory** | Persistent context | [02-memory/](02-memory/) |
| **Skills** | Reusable capabilities | [03-skills/](03-skills/) |
| **Subagents** | Specialized AI assistants | [04-subagents/](04-subagents/) |
| **MCP Protocol** | External tool access | [05-mcp/](05-mcp/) |
| **Hooks** | Event-driven automation | [06-hooks/](06-hooks/) |
| **Plugins** | Bundled features | [07-plugins/](07-plugins/) |
| **Checkpoints** | Session snapshots & rewind | [08-checkpoints/](08-checkpoints/) |
| **Advanced Features** | Planning, thinking, background tasks | [09-advanced-features/](09-advanced-features/) |
| **CLI Reference** | Commands, flags, and options | [10-cli/](10-cli/) |
| **Evoveo Tech** | Organization & updates | [github.com/evoveotech](https://github.com/evoveotech) |

</details>

<details>
<summary>Feature Comparison</summary>

| Feature | Invocation | Persistence | Best For |
|---------|-----------|------------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | Quick shortcuts |
| **Memory** | Auto-loaded | Cross-session | Long-term learning |
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Subagents** | Auto-delegated | Isolated context | Task distribution |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Hooks** | Event-triggered | Configured | Automation & validation |
| **Plugins** | One command | All features | Complete solutions |
| **Checkpoints** | Manual/Auto | Session-based | Safe experimentation |
| **Planning Mode** | Manual/Auto | Plan phase | Complex implementations |
| **Background Tasks** | Manual | Task duration | Long-running operations |
| **CLI Reference** | Terminal commands | Session/Script | Automation & scripting |

</details>

<details>
<summary>Installation Quick Reference</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .cursor/commands/

# Memory
cp 02-memory/project-CURSOR.md ./CURSOR.md

# Skills
cp -r 03-skills/code-review ~/.cursor/skills/

# Subagents
cp 04-subagents/*.md .cursor/agents/

# MCP
export GITHUB_TOKEN="token"
cursor mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.cursor/hooks
cp 06-hooks/*.sh ~/.cursor/hooks/
chmod +x ~/.cursor/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 08-checkpoints/README.md

# Advanced Features (configure in settings)
# See 09-advanced-features/config-examples.json

# CLI Reference (no installation needed)
# See 10-cli/README.md for usage examples
```

</details>

<details>
<summary>01. Slash Commands</summary>

**Location**: [01-slash-commands/](01-slash-commands/)

**What**: User-invoked shortcuts stored as Markdown files

**Examples**:
- `optimize.md` - Code optimization analysis
- `pr.md` - Pull request preparation
- `generate-api-docs.md` - API documentation generator

**Installation**:
```bash
cp 01-slash-commands/*.md /path/to/project/.cursor/commands/
```

**Usage**:
```
/optimize
/pr
/generate-api-docs
```

**Learn More**: [Cursor documentation — Rules & commands](https://docs.cursor.com/context/rules)

</details>

<details>
<summary>02. Memory</summary>

**Location**: [02-memory/](02-memory/)

**What**: Persistent context across sessions

**Examples**:
- `project-CURSOR.md` - Team-wide project standards
- `directory-api-CURSOR.md` - Directory-specific rules
- `personal-CURSOR.md` - Personal preferences

**Installation**:
```bash
# Project memory
cp 02-memory/project-CURSOR.md /path/to/project/CURSOR.md

# Directory memory
cp 02-memory/directory-api-CURSOR.md /path/to/project/src/api/CURSOR.md

# Personal memory
cp 02-memory/personal-CURSOR.md ~/.cursor/CURSOR.md
```

**Usage**: Automatically loaded by Cursor

</details>

<details>
<summary>03. Skills</summary>

**Location**: [03-skills/](03-skills/)

**What**: Reusable, auto-invoked capabilities with instructions and scripts

**Examples**:
- `code-review/` - Comprehensive code review with scripts
- `brand-voice/` - Brand voice consistency checker
- `doc-generator/` - API documentation generator

**Installation**:
```bash
# Personal skills
cp -r 03-skills/code-review ~/.cursor/skills/

# Project skills
cp -r 03-skills/code-review /path/to/project/.cursor/skills/
```

**Usage**: Automatically invoked when relevant

</details>

<details>
<summary>04. Subagents</summary>

**Location**: [04-subagents/](04-subagents/)

**What**: Specialized AI assistants with isolated contexts and custom prompts

**Examples**:
- `code-reviewer.md` - Comprehensive code quality analysis
- `test-engineer.md` - Test strategy and coverage
- `documentation-writer.md` - Technical documentation
- `secure-reviewer.md` - Security-focused review (read-only)
- `implementation-agent.md` - Full feature implementation

**Installation**:
```bash
cp 04-subagents/*.md /path/to/project/.cursor/agents/
```

**Usage**: Automatically delegated by main agent

</details>

<details>
<summary>05. MCP Protocol</summary>

**Location**: [05-mcp/](05-mcp/)

**What**: Model Context Protocol for accessing external tools and APIs

**Examples**:
- `github-mcp.json` - GitHub integration
- `database-mcp.json` - Database queries
- `filesystem-mcp.json` - File operations
- `multi-mcp.json` - Multiple MCP servers

**Installation**:
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
cursor mcp add github -- npx -y @modelcontextprotocol/server-github

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**Usage**: MCP tools are automatically available to Cursor once configured

</details>

<details>
<summary>06. Hooks</summary>

**Location**: [06-hooks/](06-hooks/)

**What**: Event-driven shell commands that execute automatically in response to Cursor events

**Examples**:
- `format-code.sh` - Auto-format code before writing
- `pre-commit.sh` - Run tests before commits
- `security-scan.sh` - Scan for security issues
- `log-bash.sh` - Log all bash commands
- `validate-prompt.sh` - Validate user prompts
- `notify-team.sh` - Send notifications on events

**Installation**:
```bash
mkdir -p ~/.cursor/hooks
cp 06-hooks/*.sh ~/.cursor/hooks/
chmod +x ~/.cursor/hooks/*.sh
```

Configure hooks in `~/.cursor/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.cursor/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.cursor/hooks/security-scan.sh"]
    }]
  }
}
```

**Usage**: Hooks execute automatically on events

**Hook Types** (4 types, 25 events):
- **Tool Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **Session Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **Task Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **Lifecycle Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**Location**: [07-plugins/](07-plugins/)

**What**: Bundled collections of commands, agents, MCP, and hooks

**Examples**:
- `pr-review/` - Complete PR review workflow
- `devops-automation/` - Deployment and monitoring
- `documentation/` - Documentation generation

**Installation**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**Usage**: Use bundled slash commands and features

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**Location**: [08-checkpoints/](08-checkpoints/)

**What**: Save conversation state and rewind to previous points to explore different approaches

**Key Concepts**:
- **Checkpoint**: Snapshot of conversation state
- **Rewind**: Return to previous checkpoint
- **Branch Point**: Explore multiple approaches from same checkpoint

**Usage**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from five options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**Use Cases**:
- Try different implementation approaches
- Recover from mistakes
- Safe experimentation
- Compare alternative solutions
- A/B testing different designs

</details>

<details>
<summary>09. Advanced Features</summary>

**Location**: [09-advanced-features/](09-advanced-features/)

**What**: Advanced capabilities for complex workflows and automation

**Includes**:
- **Planning Mode** — Create detailed implementation plans before coding
- **Extended Thinking** — Deep reasoning for complex problems (toggle with `Alt+T` / `Option+T`)
- **Background Tasks** — Run long operations without blocking
- **Permission Modes** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** — Run Cursor in CI/CD: `cursor -p "Run tests and generate report"`
- **Session Management** — `/resume`, `/rename`, `/fork`, `cursor -c`, `cursor -r`
- **Configuration** — Customize behavior in `~/.cursor/settings.json`

See [config-examples.json](09-advanced-features/config-examples.json) for complete configurations.

</details>

<details>
<summary>10. CLI Reference</summary>

**Location**: [10-cli/](10-cli/)

**What**: Complete command-line interface reference for Cursor

**Quick Examples**:
```bash
# Interactive mode
cursor "explain this project"

# Print mode (non-interactive)
cursor -p "review this code"

# Process file content
cat error.log | cursor -p "explain this error"

# JSON output for scripts
cursor -p --output-format json "list functions"

# Resume session
cursor -r "feature-auth" "continue implementation"
```

**Use Cases**: CI/CD pipeline integration, script automation, batch processing, multi-session workflows, custom agent configurations

</details>

<details>
<summary>Example Workflows</summary>

### Complete Code Review Workflow

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Cursor:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### Automated Documentation

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Cursor:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps Deployment

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Cursor:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>Directory Structure</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CURSOR.md
│   ├── directory-api-CURSOR.md
│   ├── personal-CURSOR.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>Best Practices</summary>

### Do's
- Start simple with slash commands
- Add features incrementally
- Use memory for team standards
- Test configurations locally first
- Document custom implementations
- Version control project configurations
- Share plugins with team

### Don'ts
- Don't create redundant features
- Don't hardcode credentials
- Don't skip documentation
- Don't over-complicate simple tasks
- Don't ignore security best practices
- Don't commit sensitive data

</details>

<details>
<summary>Troubleshooting</summary>

### Feature Not Loading
1. Check file location and naming
2. Verify YAML frontmatter syntax
3. Check file permissions
4. Review Cursor version compatibility

### MCP Connection Failed
1. Verify environment variables
2. Check MCP server installation
3. Test credentials
4. Review network connectivity

### Subagent Not Delegating
1. Check tool permissions
2. Verify agent description clarity
3. Review task complexity
4. Test agent independently

</details>

<details>
<summary>Testing</summary>

This project includes comprehensive automated testing:

- **Unit Tests**: Python tests using pytest (Python 3.10, 3.11, 3.12)
- **Code Quality**: Linting and formatting with Ruff
- **Security**: Vulnerability scanning with Bandit
- **Type Checking**: Static type analysis with mypy
- **Build Verification**: EPUB generation testing
- **Coverage Tracking**: Codecov integration

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

Tests run automatically on every push to `main`/`develop` and every PR to `main`. See [TESTING.md](.github/TESTING.md) for detailed information.

</details>

<details>
<summary>EPUB Generation</summary>

Want to read this guide offline? Generate an EPUB ebook:

```bash
uv run scripts/build_epub.py
```

This creates `cursor-howto-guide.epub` with all content, including rendered Mermaid diagrams.

See [scripts/README.md](scripts/README.md) for more options.

</details>

<details>
<summary>Contributing</summary>

Found an issue or want to contribute an example? We'd love your help!

**Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:**
- Types of contributions (examples, docs, features, bugs, feedback)
- How to set up your development environment
- Directory structure and how to add content
- Writing guidelines and best practices
- Commit and PR process

**Our Community Standards:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - How we treat each other
- [SECURITY.md](SECURITY.md) - Security policy and vulnerability reporting

### Reporting Security Issues

If you discover a security vulnerability, please report it responsibly:

1. **Use GitHub Private Vulnerability Reporting**: https://github.com/evoveotech/cursor-howto/security/advisories
2. **Or read** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) for detailed instructions
3. **Do NOT** open a public issue for security vulnerabilities

Quick start:
1. Fork and clone the repository
2. Create a descriptive branch (`add/feature-name`, `fix/bug`, `docs/improvement`)
3. Make your changes following the guidelines
4. Submit a pull request with a clear description

**Need help?** Open an issue or discussion, and we'll guide you through the process.

</details>

<details>
<summary>Additional Resources</summary>

- [Cursor Documentation](https://docs.cursor.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Evoveo Tech on GitHub](https://github.com/evoveotech) — organization home; additional skills and tooling appear here when published
- [Boris Cherny on agentic coding workflows](https://x.com/bcherny/status/2007179832300581177) — parallel agents, shared project memory, Plan mode, slash commands, subagents, and verification hooks for long-running sessions.

</details>

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## Contributors

Thanks to everyone who has contributed to this project!

| Contributor | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/evoveotech/cursor-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/evoveotech/cursor-howto/pull/7) |

---

## License

MIT License - see [LICENSE](LICENSE). Free to use, modify, and distribute. The only requirement is including the license notice.

---

**Design & curation:** **Evoveo Tech** (**EVOVEO INNOVATIONS LIMITED**) — for teams and developers using the Cursor IDE and Cursor CLI.

**Last Updated**: March 2026  
**Cursor Version**: 2.1+  
**Compatible Models**: GPT-4, Cursor, Gemini, and other models (configure in Cursor)
