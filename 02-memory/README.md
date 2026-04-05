<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/cursor-howto-logo-dark.svg">
  <img alt="Cursor How To" src="../resources/logos/cursor-howto-logo.svg">
</picture>

# Memory Guide

Memory enables Cursor to retain context across sessions and conversations. It exists in two forms: automatic synthesis in cursor.com, and filesystem-based CURSOR.md in Cursor.

## Overview

Memory in Cursor provides persistent context that carries across multiple sessions and conversations. Unlike temporary context windows, memory files allow you to:

- Share project standards across your team
- Store personal development preferences
- Maintain directory-specific rules and configurations
- Import external documentation
- Version control memory as part of your project

The memory system operates at multiple levels, from global personal preferences down to specific subdirectories, allowing for fine-grained control over what Cursor remembers and how it applies that knowledge.

## Memory Commands Quick Reference

| Command | Purpose | Usage | When to Use |
|---------|---------|-------|-------------|
| `/init` | Initialize project memory | `/init` | Starting new project, first-time CURSOR.md setup |
| `/memory` | Edit memory files in editor | `/memory` | Extensive updates, reorganization, reviewing content |
| `#` prefix | Quick single-line memory add | `# Your rule here` | Adding quick rules during conversation |
| `# new rule into memory` | Explicit memory addition | `# new rule into memory<br/>Your detailed rule` | Adding complex multi-line rules |
| `# remember this` | Natural language memory | `# remember this<br/>Your instruction` | Conversational memory updates |
| `@path/to/file` | Import external content | `@README.md` or `@docs/api.md` | Referencing existing documentation in CURSOR.md |

## Quick Start: Initializing Memory

### The `/init` Command

The `/init` command is the fastest way to set up project memory in Cursor. It initializes a CURSOR.md file with foundational project documentation.

**Usage:**

```bash
/init
```

**What it does:**

- Creates a new CURSOR.md file in your project (typically at `./CURSOR.md` or `./.cursor/CURSOR.md`)
- Establishes project conventions and guidelines
- Sets up the foundation for context persistence across sessions
- Provides a template structure for documenting your project standards

**Enhanced interactive mode:** Set `CURSOR_NEW_INIT=true` to enable a multi-phase interactive flow that walks you through project setup step by step:

```bash
CURSOR_NEW_INIT=true cursor
/init
```

**When to use `/init`:**

- Starting a new project with Cursor
- Establishing team coding standards and conventions
- Creating documentation about your codebase structure
- Setting up memory hierarchy for collaborative development

**Example workflow:**

```markdown
# In your project directory
/init

# Cursor creates CURSOR.md with structure like:
# Project Configuration
## Project Overview
- Name: Your Project
- Tech Stack: [Your technologies]
- Team Size: [Number of developers]

## Development Standards
- Code style preferences
- Testing requirements
- Git workflow conventions
```

### Quick Memory Updates with `#`

You can quickly add information to memory during any conversation by starting your message with `#`:

**Syntax:**

```markdown
# Your memory rule or instruction here
```

**Examples:**

```markdown
# Always use TypeScript strict mode in this project

# Prefer async/await over promise chains

# Run npm test before every commit

# Use kebab-case for file names
```

**How it works:**

1. Start your message with `#` followed by your rule
2. Cursor recognizes this as a memory update request
3. Cursor asks which memory file to update (project or personal)
4. The rule is added to the appropriate CURSOR.md file
5. Future sessions automatically load this context

**Alternative patterns:**

```markdown
# new rule into memory
Always validate user input with Zod schemas

# remember this
Use semantic versioning for all releases

# add to memory
Database migrations must be reversible
```

### The `/memory` Command

The `/memory` command provides direct access to edit your CURSOR.md memory files within Cursor sessions. It opens your memory files in your system editor for comprehensive editing.

**Usage:**

```bash
/memory
```

**What it does:**

- Opens your memory files in your system's default editor
- Allows you to make extensive additions, modifications, and reorganizations
- Provides direct access to all memory files in the hierarchy
- Enables you to manage persistent context across sessions

**When to use `/memory`:**

- Reviewing existing memory content
- Making extensive updates to project standards
- Reorganizing memory structure
- Adding detailed documentation or guidelines
- Maintaining and updating memory as your project evolves

**Comparison: `/memory` vs `/init`**

| Aspect | `/memory` | `/init` |
|--------|-----------|---------|
| **Purpose** | Edit existing memory files | Initialize new CURSOR.md |
| **When to use** | Update/modify project context | Begin new projects |
| **Action** | Opens editor for changes | Generates starter template |
| **Workflow** | Ongoing maintenance | One-time setup |

**Example workflow:**

```markdown
# Open memory for editing
/memory

# Cursor presents options:
# 1. Managed Policy Memory
# 2. Project Memory (./CURSOR.md)
# 3. User Memory (~/.cursor/CURSOR.md)
# 4. Local Project Memory

# Choose option 2 (Project Memory)
# Your default editor opens with ./CURSOR.md content

# Make changes, save, and close editor
# Cursor automatically reloads the updated memory
```

**Using Memory Imports:**

CURSOR.md files support the `@path/to/file` syntax to include external content:

```markdown
# Project Documentation
See @README.md for project overview
See @package.json for available npm commands
See @docs/architecture.md for system design

# Import from home directory using absolute path
@~/.cursor/my-project-instructions.md
```

**Import features:**

- Both relative and absolute paths are supported (e.g., `@docs/api.md` or `@~/.cursor/my-project-instructions.md`)
- Recursive imports are supported with a maximum depth of 5
- First-time imports from external locations trigger an approval dialog for security
- Import directives are not evaluated inside markdown code spans or code blocks (so documenting them in examples is safe)
- Helps avoid duplication by referencing existing documentation
- Automatically includes referenced content in Cursor's context

## Memory Architecture

Memory in Cursor follows a hierarchical system where different scopes serve different purposes:

```mermaid
graph TB
    A["Cursor Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

## Memory Hierarchy in Cursor

Cursor uses a multi-tier hierarchical memory system. Memory files are automatically loaded when Cursor launches, with higher-level files taking precedence.

**Complete Memory Hierarchy (in order of precedence):**

1. **Managed Policy** - Organization-wide instructions
   - macOS: `/Library/Application Support/Cursor/CURSOR.md`
   - Linux/WSL: `/etc/cursor-code/CURSOR.md`
   - Windows: `%LOCALAPPDATA%\Programs\Cursor\CURSOR.md`

2. **Managed Drop-ins** - Alphabetically merged policy files (v2.1.83+)
   - `managed-settings.d/` directory alongside the managed policy CURSOR.md
   - Files are merged in alphabetical order for modular policy management

3. **Project Memory** - Team-shared context (version controlled)
   - `./.cursor/CURSOR.md` or `./CURSOR.md` (in repository root)

4. **Project Rules** - Modular, topic-specific project instructions
   - `./.cursor/rules/*.md`

5. **User Memory** - Personal preferences (all projects)
   - `~/.cursor/CURSOR.md`

6. **User-Level Rules** - Personal rules (all projects)
   - `~/.cursor/rules/*.md`

7. **Local Project Memory** - Personal project-specific preferences
   - `./CURSOR.local.md`

> **Note**: `CURSOR.local.md` is not mentioned in the [official documentation](https://docs.cursor.com/docs/en/memory) as of March 2026. It may still work as a legacy feature. For new projects, consider using `~/.cursor/CURSOR.md` (user-level) or `.cursor/rules/` (project-level, path-scoped) instead.

8. **Auto Memory** - Cursor's automatic notes and learnings
   - `~/.cursor/projects/<project>/memory/`

**Memory Discovery Behavior:**

Cursor searches for memory files in this order, with earlier locations taking precedence:

```mermaid
graph TD
    A["Managed Policy<br/>/Library/.../Cursor/CURSOR.md"] -->|highest priority| A2["Managed Drop-ins<br/>managed-settings.d/"]
    A2 --> B["Project Memory<br/>./CURSOR.md"]
    B --> C["Project Rules<br/>./.cursor/rules/*.md"]
    C --> D["User Memory<br/>~/.cursor/CURSOR.md"]
    D --> E["User Rules<br/>~/.cursor/rules/*.md"]
    E --> F["Local Project Memory<br/>./CURSOR.local.md"]
    F --> G["Auto Memory<br/>~/.cursor/projects/.../memory/"]

    B -->|imports| H["@docs/architecture.md"]
    H -->|imports| I["@docs/api-standards.md"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style A2 fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
    style H fill:#e1f5fe,stroke:#333,color:#333
    style I fill:#e1f5fe,stroke:#333,color:#333
```

## Excluding CURSOR.md Files with `cursorMdExcludes`

In large monorepos, some CURSOR.md files may be irrelevant to your current work. The `cursorMdExcludes` setting lets you skip specific CURSOR.md files so they are not loaded into context:

```jsonc
// In ~/.cursor/settings.json or .cursor/settings.json
{
  "cursorMdExcludes": [
    "packages/legacy-app/CURSOR.md",
    "vendors/**/CURSOR.md"
  ]
}
```

Patterns are matched against paths relative to the project root. This is particularly useful for:

- Monorepos with many sub-projects, where only some are relevant
- Repositories that contain vendored or third-party CURSOR.md files
- Reducing noise in Cursor's context window by excluding stale or unrelated instructions

## Settings File Hierarchy

Cursor settings (including `autoMemoryDirectory`, `cursorMdExcludes`, and other configuration) are resolved from a five-level hierarchy, with higher levels taking precedence:

| Level | Location | Scope |
|-------|----------|-------|
| 1 (Highest) | Managed policy (system-level) | Organization-wide enforcement |
| 2 | `managed-settings.d/` (v2.1.83+) | Modular policy drop-ins, merged alphabetically |
| 3 | `~/.cursor/settings.json` | User preferences |
| 4 | `.cursor/settings.json` | Project-level (committed to git) |
| 5 (Lowest) | `.cursor/settings.local.json` | Local overrides (git-ignored) |

**Platform-specific configuration (v2.1.51+):**

Settings can also be configured via:
- **macOS**: Property list (plist) files
- **Windows**: Windows Registry

These platform-native mechanisms are read alongside JSON settings files and follow the same precedence rules.

## Modular Rules System

Create organized, path-specific rules using the `.cursor/rules/` directory structure. Rules can be defined at both the project level and user level:

```
your-project/
├── .cursor/
│   ├── CURSOR.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       ├── security.md
│       └── api/                  # Subdirectories supported
│           ├── conventions.md
│           └── validation.md

~/.cursor/
├── CURSOR.md
└── rules/                        # User-level rules (all projects)
    ├── personal-style.md
    └── preferred-patterns.md
```

Rules are discovered recursively within the `rules/` directory, including any subdirectories. User-level rules at `~/.cursor/rules/` are loaded before project-level rules, allowing personal defaults that projects can override.

### Path-Specific Rules with YAML Frontmatter

Define rules that apply only to specific file paths:

```markdown
---
paths: src/api/**/*.ts
---

# API Development Rules

- All API endpoints must include input validation
- Use Zod for schema validation
- Document all parameters and response types
- Include error handling for all operations
```

**Glob Pattern Examples:**

- `**/*.ts` - All TypeScript files
- `src/**/*` - All files under src/
- `src/**/*.{ts,tsx}` - Multiple extensions
- `{src,lib}/**/*.ts, tests/**/*.test.ts` - Multiple patterns

### Subdirectories and Symlinks

Rules in `.cursor/rules/` support two organizational features:

- **Subdirectories**: Rules are discovered recursively, so you can organize them into topic-based folders (e.g., `rules/api/`, `rules/testing/`, `rules/security/`)
- **Symlinks**: Symlinks are supported for sharing rules across multiple projects. For example, you can symlink a shared rule file from a central location into each project's `.cursor/rules/` directory

## Memory Locations Table

| Location | Scope | Priority | Shared | Access | Best For |
|----------|-------|----------|--------|--------|----------|
| `/Library/Application Support/Cursor/CURSOR.md` (macOS) | Managed Policy | 1 (Highest) | Organization | System | Company-wide policies |
| `/etc/cursor-code/CURSOR.md` (Linux/WSL) | Managed Policy | 1 (Highest) | Organization | System | Organization standards |
| `%LOCALAPPDATA%\Programs\Cursor\CURSOR.md` (Windows) | Managed Policy | 1 (Highest) | Organization | System | Corporate guidelines |
| `managed-settings.d/*.md` (alongside policy) | Managed Drop-ins | 1.5 | Organization | System | Modular policy files (v2.1.83+) |
| `./CURSOR.md` or `./.cursor/CURSOR.md` | Project Memory | 2 | Team | Git | Team standards, shared architecture |
| `./.cursor/rules/*.md` | Project Rules | 3 | Team | Git | Path-specific, modular rules |
| `~/.cursor/CURSOR.md` | User Memory | 4 | Individual | Filesystem | Personal preferences (all projects) |
| `~/.cursor/rules/*.md` | User Rules | 5 | Individual | Filesystem | Personal rules (all projects) |
| `./CURSOR.local.md` | Project Local | 6 | Individual | Git (ignored) | Personal project-specific preferences |
| `~/.cursor/projects/<project>/memory/` | Auto Memory | 7 (Lowest) | Individual | Filesystem | Cursor's automatic notes and learnings |

## Memory Update Lifecycle

Here's how memory updates flow through your Cursor sessions:

```mermaid
sequenceDiagram
    participant User
    participant Cursor as Cursor
    participant Editor as File System
    participant Memory as CURSOR.md

    User->>Cursor: "Remember: use async/await"
    Cursor->>User: "Which memory file?"
    User->>Cursor: "Project memory"
    Cursor->>Editor: Open ~/.cursor/settings.json
    Cursor->>Memory: Write to ./CURSOR.md
    Memory-->>Cursor: File saved
    Cursor->>Cursor: Load updated memory
    Cursor-->>User: "Memory saved!"
```

## Auto Memory

Auto memory is a persistent directory where Cursor automatically records learnings, patterns, and insights as it works with your project. Unlike CURSOR.md files which you write and maintain manually, auto memory is written by Cursor itself during sessions.

### How Auto Memory Works

- **Location**: `~/.cursor/projects/<project>/memory/`
- **Entrypoint**: `MEMORY.md` serves as the main file in the auto memory directory
- **Topic files**: Optional additional files for specific subjects (e.g., `debugging.md`, `api-conventions.md`)
- **Loading behavior**: The first 200 lines of `MEMORY.md` are loaded into the system prompt at session start. Topic files are loaded on demand, not at startup.
- **Read/write**: Cursor reads and writes memory files during sessions as it discovers patterns and project-specific knowledge

### Auto Memory Architecture

```mermaid
graph TD
    A["Cursor Session Starts"] --> B["Load MEMORY.md<br/>(first 200 lines)"]
    B --> C["Session Active"]
    C --> D["Cursor discovers<br/>patterns & insights"]
    D --> E{"Write to<br/>auto memory"}
    E -->|General notes| F["MEMORY.md"]
    E -->|Topic-specific| G["debugging.md"]
    E -->|Topic-specific| H["api-conventions.md"]
    C --> I["On-demand load<br/>topic files"]
    I --> C

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#fff3e0,stroke:#333,color:#333
    style F fill:#fce4ec,stroke:#333,color:#333
    style G fill:#fce4ec,stroke:#333,color:#333
    style H fill:#fce4ec,stroke:#333,color:#333
    style I fill:#f3e5f5,stroke:#333,color:#333
```

### Auto Memory Directory Structure

```
~/.cursor/projects/<project>/memory/
├── MEMORY.md              # Entrypoint (first 200 lines loaded at startup)
├── debugging.md           # Topic file (loaded on demand)
├── api-conventions.md     # Topic file (loaded on demand)
└── testing-patterns.md    # Topic file (loaded on demand)
```

### Version Requirement

Auto memory requires **Cursor v2.1.59 or later**. If you are on an older version, upgrade first:

```bash
# Install Cursor from https://cursor.com (or your OS package manager)
```

### Custom Auto Memory Directory

By default, auto memory is stored in `~/.cursor/projects/<project>/memory/`. You can change this location using the `autoMemoryDirectory` setting (available since **v2.1.74**):

```jsonc
// In ~/.cursor/settings.json or .cursor/settings.local.json (user/local settings only)
{
  "autoMemoryDirectory": "/path/to/custom/memory/directory"
}
```

> **Note**: `autoMemoryDirectory` can only be set in user-level (`~/.cursor/settings.json`) or local settings (`.cursor/settings.local.json`), not in project or managed policy settings.

This is useful when you want to:

- Store auto memory in a shared or synced location
- Separate auto memory from the default Cursor configuration directory
- Use a project-specific path outside the default hierarchy

### Worktree and Repository Sharing

All worktrees and subdirectories within the same git repository share a single auto memory directory. This means switching between worktrees or working in different subdirectories of the same repo will read and write to the same memory files.

### Subagent Memory

Subagents (spawned via tools like Task or parallel execution) can have their own memory context. Use the `memory` frontmatter field in the subagent definition to specify which memory scopes to load:

```yaml
memory: user      # Load user-level memory only
memory: project   # Load project-level memory only
memory: local     # Load local memory only
```

This allows subagents to operate with focused context rather than inheriting the full memory hierarchy.

### Controlling Auto Memory

Auto memory can be controlled via the `CURSOR_DISABLE_AUTO_MEMORY` environment variable:

| Value | Behavior |
|-------|----------|
| `0` | Force auto memory **on** |
| `1` | Force auto memory **off** |
| *(unset)* | Default behavior (auto memory enabled) |

```bash
# Disable auto memory for a session
CURSOR_DISABLE_AUTO_MEMORY=1 cursor

# Force auto memory on explicitly
CURSOR_DISABLE_AUTO_MEMORY=0 cursor
```

## Additional Directories with `--add-dir`

The `--add-dir` flag allows Cursor to load CURSOR.md files from additional directories beyond the current working directory. This is useful for monorepos or multi-project setups where context from other directories is relevant.

To enable this feature, set the environment variable:

```bash
CURSOR_ADDITIONAL_DIRECTORIES_CURSOR_MD=1
```

Then launch Cursor with the flag:

```bash
cursor --add-dir /path/to/other/project
```

Cursor will load CURSOR.md from the specified additional directory alongside the memory files from your current working directory.

## Practical Examples

### Example 1: Project Memory Structure

**File:** `./CURSOR.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

### Example 2: Directory-Specific Memory

**File:** `./src/api/CURSOR.md`

```markdown
# API Module Standards

This file overrides root CURSOR.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
```

### Example 3: Personal Memory

**File:** `~/.cursor/CURSOR.md`

```markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:

   project/
   ├── src/
   │   ├── api/
   │   ├── services/
   │   ├── models/
   │   └── utils/
   ├── tests/
   ├── docs/
   └── docker/

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
```

_My Test_
Ask Cursor to save a new rule

![Ask Cursor to save a new rule](memory-ask-cursor.png)
Cursor has not save the rule because I did not have any `Cursor.md` file anywhere. Then asked Cursor to confirm the location.

![Ask Cursor to save a new rule](memory-saved.png)

### Example 4: Memory Update During Session

You can add new rules to memory during an active Cursor session. There are two ways to do this:

#### Method 1: Direct Request

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Cursor: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CURSOR.md)
        2. Personal memory (~/.cursor/CURSOR.md)

User: Project memory

Cursor: ✅ Memory saved!

Added to ./CURSOR.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

#### Method 2: Using "# new rule into memory" Pattern

You can also use the explicit pattern "# new rule into memory" to trigger memory updates:

```markdown
User: # new rule into memory
      Always validate user input with Zod schemas before processing.

Cursor: I'm saving this rule to memory. Which memory file should I use?
        1. Project memory (./CURSOR.md)
        2. Personal memory (~/.cursor/CURSOR.md)

User: Project memory

Cursor: ✅ Memory saved!

Added to ./CURSOR.md:
---

### Input Validation
- Always validate user input with Zod schemas before processing
- Define schemas at the top of each API handler file
- Return 400 status with validation errors
```

#### Tips for Adding Memory

- Be specific and actionable in your rules
- Group related rules together under a section header
- Update existing sections instead of duplicating content
- Choose the appropriate memory scope (project vs. personal)

## Memory Features Comparison

| Feature | Cursor Web/Desktop | Cursor (CURSOR.md) |
|---------|-------------------|------------------------|
| Auto-synthesis | ✅ Every 24h | ❌ Manual |
| Cross-project | ✅ Shared | ❌ Project-specific |
| Team access | ✅ Shared projects | ✅ Git-tracked |
| Searchable | ✅ Built-in | ✅ Through `/memory` |
| Editable | ✅ In-chat | ✅ Direct file edit |
| Import/Export | ✅ Yes | ✅ Copy/paste |
| Persistent | ✅ 24h+ | ✅ Indefinite |

### Memory in Cursor Web/Desktop

#### Memory Synthesis Timeline

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**Example Memory Summary:**

```markdown
## Cursor's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

## Best Practices

### Do's - What To Include

- **Be specific and detailed**: Use clear, detailed instructions rather than vague guidance
  - ✅ Good: "Use 2-space indentation for all JavaScript files"
  - ❌ Avoid: "Follow best practices"

- **Keep organized**: Structure memory files with clear markdown sections and headings

- **Use appropriate hierarchy levels**:
  - **Managed policy**: Company-wide policies, security standards, compliance requirements
  - **Project memory**: Team standards, architecture, coding conventions (commit to git)
  - **User memory**: Personal preferences, communication style, tooling choices
  - **Directory memory**: Module-specific rules and overrides

- **Leverage imports**: Use `@path/to/file` syntax to reference existing documentation
  - Supports up to 5 levels of recursive nesting
  - Avoids duplication across memory files
  - Example: `See @README.md for project overview`

- **Document frequent commands**: Include commands you use repeatedly to save time

- **Version control project memory**: Commit project-level CURSOR.md files to git for team benefit

- **Review periodically**: Update memory regularly as projects evolve and requirements change

- **Provide concrete examples**: Include code snippets and specific scenarios

### Don'ts - What To Avoid

- **Don't store secrets**: Never include API keys, passwords, tokens, or credentials

- **Don't include sensitive data**: No PII, private information, or proprietary secrets

- **Don't duplicate content**: Use imports (`@path`) to reference existing documentation instead

- **Don't be vague**: Avoid generic statements like "follow best practices" or "write good code"

- **Don't make it too long**: Keep individual memory files focused and under 500 lines

- **Don't over-organize**: Use hierarchy strategically; don't create excessive subdirectory overrides

- **Don't forget to update**: Stale memory can cause confusion and outdated practices

- **Don't exceed nesting limits**: Memory imports support up to 5 levels of nesting

### Memory Management Tips

**Choose the right memory level:**

| Use Case | Memory Level | Rationale |
|----------|-------------|-----------|
| Company security policy | Managed Policy | Applies to all projects organization-wide |
| Team code style guide | Project | Shared with team via git |
| Your preferred editor shortcuts | User | Personal preference, not shared |
| API module standards | Directory | Specific to that module only |

**Quick update workflow:**

1. For single rules: Use `#` prefix in conversation
2. For multiple changes: Use `/memory` to open editor
3. For initial setup: Use `/init` to create template

**Import best practices:**

```markdown
# Good: Reference existing docs
@README.md
@docs/architecture.md
@package.json

# Avoid: Copying content that exists elsewhere
# Instead of copying README content into CURSOR.md, just import it
```

## Installation Instructions

### Setup Project Memory

#### Method 1: Using `/init` Command (Recommended)

The fastest way to set up project memory:

1. **Navigate to your project directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the init command in Cursor:**
   ```bash
   /init
   ```

3. **Cursor will create and populate CURSOR.md** with a template structure

4. **Customize the generated file** to match your project needs

5. **Commit to git:**
   ```bash
   git add CURSOR.md
   git commit -m "Initialize project memory with /init"
   ```

#### Method 2: Manual Creation

If you prefer manual setup:

1. **Create a CURSOR.md in your project root:**
   ```bash
   cd /path/to/your/project
   touch CURSOR.md
   ```

2. **Add project standards:**
   ```bash
   cat > CURSOR.md << 'EOF'
   # Project Configuration

   ## Project Overview
   - **Name**: Your Project Name
   - **Tech Stack**: List your technologies
   - **Team Size**: Number of developers

   ## Development Standards
   - Your coding standards
   - Naming conventions
   - Testing requirements
   EOF
   ```

3. **Commit to git:**
   ```bash
   git add CURSOR.md
   git commit -m "Add project memory configuration"
   ```

#### Method 3: Quick Updates with `#`

Once CURSOR.md exists, add rules quickly during conversations:

```markdown
# Use semantic versioning for all releases

# Always run tests before committing

# Prefer composition over inheritance
```

Cursor will prompt you to choose which memory file to update.

### Setup Personal Memory

1. **Create ~/.cursor directory:**
   ```bash
   mkdir -p ~/.cursor
   ```

2. **Create personal CURSOR.md:**
   ```bash
   touch ~/.cursor/CURSOR.md
   ```

3. **Add your preferences:**
   ```bash
   cat > ~/.cursor/CURSOR.md << 'EOF'
   # My Development Preferences

   ## About Me
   - Experience Level: [Your level]
   - Preferred Languages: [Your languages]
   - Communication Style: [Your style]

   ## Code Preferences
   - [Your preferences]
   EOF
   ```

### Setup Directory-Specific Memory

1. **Create memory for specific directories:**
   ```bash
   mkdir -p /path/to/directory/.cursor
   touch /path/to/directory/CURSOR.md
   ```

2. **Add directory-specific rules:**
   ```bash
   cat > /path/to/directory/CURSOR.md << 'EOF'
   # [Directory Name] Standards

   This file overrides root CURSOR.md for this directory.

   ## [Specific Standards]
   EOF
   ```

3. **Commit to version control:**
   ```bash
   git add /path/to/directory/CURSOR.md
   git commit -m "Add [directory] memory configuration"
   ```

### Verify Setup

1. **Check memory locations:**
   ```bash
   # Project root memory
   ls -la ./CURSOR.md

   # Personal memory
   ls -la ~/.cursor/CURSOR.md
   ```

2. **Cursor will automatically load** these files when starting a session

3. **Test with Cursor** by starting a new session in your project

## Official Documentation

For the most up-to-date information, refer to the official Cursor documentation:

- **[Memory Documentation](https://docs.cursor.com/docs/en/memory)** - Complete memory system reference
- **[Slash Commands Reference](https://docs.cursor.com/docs/en/interactive-mode)** - All built-in commands including `/init` and `/memory`
- **[CLI Reference](https://docs.cursor.com/docs/en/cli-reference)** - Command-line interface documentation

### Key Technical Details from Official Docs

**Memory Loading:**

- All memory files are automatically loaded when Cursor launches
- Cursor traverses upward from the current working directory to discover CURSOR.md files
- Subtree files are discovered and loaded contextually when accessing those directories

**Import Syntax:**

- Use `@path/to/file` to include external content (e.g., `@~/.cursor/my-project-instructions.md`)
- Supports both relative and absolute paths
- Recursive imports supported with a maximum depth of 5
- First-time external imports trigger an approval dialog
- Not evaluated inside markdown code spans or code blocks
- Automatically includes referenced content in Cursor's context

**Memory Hierarchy Precedence:**

1. Managed Policy (highest precedence)
2. Managed Drop-ins (`managed-settings.d/`, v2.1.83+)
3. Project Memory
4. Project Rules (`.cursor/rules/`)
5. User Memory
6. User-Level Rules (`~/.cursor/rules/`)
7. Local Project Memory
8. Auto Memory (lowest precedence)

## Related Concepts Links

### Integration Points
- [MCP Protocol](../05-mcp/) - Live data access alongside memory
- [Slash Commands](../01-slash-commands/) - Session-specific shortcuts
- [Skills](../03-skills/) - Automated workflows with memory context

### Related Cursor Features
- [Cursor Web Memory](https://cursor.com) - Automatic synthesis
- [Official Memory Docs](https://docs.cursor.com/docs/en/memory) - Cursor documentation
