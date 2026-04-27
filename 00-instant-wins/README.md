# ⚡ Instant Wins — 30-Second Setup

No reading. No theory. Copy one file. Paste it. Done.

Each template below is **self-contained** and gives you immediate value.

---

## 1. Auto Code Reviewer (`/review`)

**What it does:** Cursor automatically reviews your code for bugs, style issues, and security problems every time you ask.

**Copy this → paste into `.cursor/commands/review.md`:**

```markdown
---
description: 'Auto code review: bugs, style, security, performance'
---

Review the selected code (or entire file if nothing selected) for:
1. Bugs and logic errors
2. Security vulnerabilities (SQL injection, XSS, auth issues)
3. Performance bottlenecks
4. Code style consistency
5. Missing error handling

For each issue found, provide:
- Severity: Critical / Warning / Suggestion
- Location: line number
- Explanation: why it's a problem
- Fix: corrected code snippet

Format output as a markdown table.
```

**Use it:** Select any code → type `/review`

---

## 2. Explain Like I'm 5 (`/explain`)

**What it does:** Any complex code becomes a simple explanation with visual metaphors.

**Copy this → paste into `.cursor/commands/explain.md`:**

```markdown
---
description: 'Explain code in plain English with analogies'
---

Explain the selected code as if I'm a junior developer seeing it for the first time.

Structure:
1. **One-sentence summary** — what this code does at a high level
2. **Step-by-step walkthrough** — what each section does
3. **Real-world analogy** — compare to something non-technical (cooking, driving, organizing a closet)
4. **Key concepts** — define any patterns or libraries used
5. **Common pitfalls** — mistakes people make with this pattern

Keep it under 200 words. No jargon without explanation.
```

**Use it:** Select confusing code → type `/explain`

---

## 3. Smart Commit Message (`/commit`)

**What it does:** Generate perfect commit messages from your diff, following conventional commits.

**Copy this → paste into `.cursor/commands/commit.md`:**

```markdown
---
description: 'Generate conventional commit message from diff'
---

Analyze the current git diff and write a commit message following the Conventional Commits specification.

Format:
```
type(scope): description

[optional body]

[optional footer(s)]
```

Rules:
- Type: feat, fix, docs, style, refactor, test, chore
- Scope: the main component changed (e.g., auth, api, ui)
- Description: imperative mood, lowercase, no period, max 50 chars
- Body: explain what changed and why (not how)

If the diff is large, summarize the main change. Suggest splitting if appropriate.

Output ONLY the commit message. No markdown code fences. No explanations.
```

**Use it:** Stage your changes → type `/commit` → paste into `git commit -m "..."`

---

## Next Steps

- Want more commands? → [`01-slash-commands/`](../01-slash-commands/)
- Want project-wide memory? → [`02-memory/project-CURSOR.md`](../02-memory/project-CURSOR.md)
- Want auto-invoked skills? → [`03-skills/`](../03-skills/)
