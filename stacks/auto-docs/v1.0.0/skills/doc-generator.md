SKILL.md — Auto Documentation Generator

---
name: doc-generator
version: 1.0.0
description: Automatically generate documentation when code is added or modified
auto_invoke: true
triggers:
  - file_created
  - file_modified
  - pattern: "*.ts"
  - pattern: "*.tsx"
  - pattern: "*.js"
  - pattern: "*.jsx"
  - pattern: "*.py"
---

## Invocation

When a new file is created or modified, automatically check if documentation exists and generate it if missing.

## Behavior

1. Check if file has JSDoc/TSDoc comments on exported functions/components
2. If missing: generate minimal but complete documentation
3. If API route: generate endpoint documentation in `docs/api/`
4. If React component: generate story/usage docs in `docs/components/`
5. Never overwrite existing documentation unless explicitly asked

## Documentation Style

Follow the project's existing docs. If no docs exist yet:
- API: OpenAPI-style path + request/response schemas
- Components: Props table + usage example
- Functions: Parameters + return type + example
- Modules: Overview + key exports + usage

## Output Location

| Code Type | Doc Location |
|-----------|-------------|
| API routes | `docs/api/{route-path}.md` |
| Components | `docs/components/{ComponentName}.md` |
| Utilities | Inline JSDoc + `docs/utils/README.md` index |
| Database | `docs/database/schema.md` |

## Rules

- Don't document private/internal functions unless they're complex
- Include at least one working code example
- Document error cases (what throws, what returns null)
- Keep docs in sync with code (regenerate on significant changes)
