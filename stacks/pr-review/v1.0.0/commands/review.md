---
description: 'AI-powered code review: bugs, security, performance, style'
---

Review the selected code (or entire file if nothing selected) as if you're a senior engineer doing a final pass before merge.

Execute this workflow:

1. **Bug Hunt** — Logic errors, off-by-one, null derefs, race conditions, async mishandling
2. **Security Scan** — Injection risks, auth flaws, secrets exposure, XSS, CSRF, insecure dependencies
3. **Performance** — N+1 queries, unnecessary re-renders, memory leaks, blocking I/O, algorithmic inefficiency
4. **Style & Maintainability** — Naming consistency, function length, dead code, missing types, error handling gaps
5. **Test Coverage** — Untested paths, missing edge cases, brittle assertions

For each issue found, provide:

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Critical / Warning / Suggestion | `src/api.ts:42` | Brief description | Corrected code snippet |

If no issues: "Clean pass. Ship it."

If issues found: Summarize top 3 by impact, then full table.
