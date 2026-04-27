---
description: 'Generate changelog entry from git diff or PR description'
---

Write a changelog entry for the current changes (diff or PR).

Format (Keep a Changelog):

```markdown
## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Now removed features

### Fixed
- Bug fixes

### Security
- Vulnerability fixes
```

Rules:
- Start each entry with a verb (Added, Fixed, Changed, etc.)
- Reference issue/PR numbers when available
- Group related changes
- Keep user-facing language (not implementation details)
- One bullet per logical change

If this is a version bump, suggest the semver bump:
- PATCH: bug fixes only
- MINOR: new features, backwards compatible
- MAJOR: breaking changes
