# War Story #1: I Replaced Our Code Review Process With 2 Markdown Files

**Role:** Senior Engineer, 8-person team  
**Stack:** Next.js 14, TypeScript, PostgreSQL, Prisma  
**Before:** 2 hours/PR × 3 PRs/week × 6 reviewers = 36 person-hours/week on manual code review  
**After:** 15 minutes/PR × 3 PRs/week × 1 human reviewer = 45 minutes/week  
**Result:** 35 hours/week recovered. $91,000/year in engineering time at $130/hr blended rate.

---

## The Problem

Our team was drowning in code review.

Every PR went through this:
1. Author waits 4-6 hours for reviewer availability
2. Reviewer spends 20-30 minutes checking logic, security, style, tests
3. 60% of comments are on the same 5 issues: missing types, insecure queries, missing error handling, no tests, style violations
4. Author fixes, resubmits, waits again
5. Round 2 catches the real architectural issues (15 minutes)

The bottleneck wasn't expertise. It was attention. Reviewers were tired of saying the same things.

---

## The One-Hour Fix

I installed the `pr-review` stack from this repo. Two files.

**Step 1: Copy the review command (30 seconds)**
```bash
cp stacks/pr-review/v1.0.0/commands/review.md .cursor/commands/
```

**Step 2: Set project standards (2 minutes)**
```bash
cp stacks/pr-review/v1.0.0/memory/review-standards.md ./CURSOR.md
# Edited to match our actual stack (Next.js, Prisma, NextAuth)
```

**Step 3: Configure the pre-review hook (5 minutes)**
```bash
cp stacks/pr-review/v1.0.0/hooks/pre-review.sh .cursor/hooks/
# Added our ESLint + Prettier + TypeScript checks
```

**Step 4: Add the test engineer agent (30 seconds)**
```bash
cp stacks/pr-review/v1.0.0/agents/test-engineer.md .cursor/agents/
```

Total time: 8 minutes. Most of it was customizing the standards file to mention our actual stack.

---

## How We Use It

**Before submitting a PR, the author runs `/review` on their own code.**

Cursor checks:
- Logic errors and edge cases
- SQL injection risks in Prisma queries
- Missing TypeScript types
- Untested error paths
- Next.js App Router best practices
- Performance (N+1 queries, unnecessary re-renders)

**Output:** A markdown table with severity, location, issue, and fix.

**The author fixes everything marked Critical or Warning before submitting.**

**Then the human reviewer gets a PR that's already clean.**

They focus on:
- Architecture and design decisions
- Business logic correctness
- Complex edge cases the AI missed

**Average review time dropped from 25 minutes to 8 minutes.**

And the human reviewer is actually engaged because they're not saying "add types here" for the hundredth time.

---

## What the AI Actually Caught (Real Examples)

| Date | Issue | Severity | Would Human Have Caught? |
|------|-------|----------|-------------------------|
| Week 1 | `findMany()` without pagination on user search | High | Probably not (focused on logic) |
| Week 2 | `JSON.parse()` on unsanitized input from API | Critical | Maybe (easy to miss in 200 lines) |
| Week 2 | Missing `await` on async database transaction | Critical | Possibly (subtle in nested function) |
| Week 3 | Console.log with user object (PII leak) | Critical | Unlikely (not on mental checklist) |
| Week 3 | React `useEffect` without cleanup on event listener | High | 50/50 (common pattern, easy to skim) |
| Week 4 | Prisma query in loop (N+1) | High | Maybe (if reviewer checks queries) |

**6 issues in 4 weeks.** Human reviewers were catching ~2 per week before. The AI caught different issues — the ones that fall through the cracks of human attention.

---

## The Human Reviewer Workflow Now

```
Author writes code
    ↓
Author runs /review (3 minutes)
    ↓
Author fixes issues
    ↓
Author submits PR
    ↓
CI runs (tests + lint + type check)
    ↓
Human reviewer checks: architecture, design, complex logic (8 minutes)
    ↓
Merge
```

Total time from "done coding" to "merged": ~30 minutes.  
Before: 4-6 hours (waiting for reviewer + review rounds).

---

## Team Reaction

**Week 1:** "This feels weird, like I'm cheating."

**Week 2:** "Wait, the AI found the missing `await` that I definitely would have missed."

**Week 3:** "Can we add a custom check for our auth pattern?" (Yes — edited the standards file.)

**Week 4:** Junior dev: "I actually understand why my code had issues now. The AI explains the fix, not just 'wrong.'"

Senior devs stopped dreading review. Junior devs started learning from the feedback. PR velocity increased 3x.

---

## The Numbers

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Avg review time | 25 min | 8 min | -68% |
| Review rounds per PR | 2.3 | 1.1 | -52% |
| Time from done to merged | 5.2 hours | 0.5 hours | -90% |
| Bugs caught in review | 2/week | 6/week | +200% |
| Team satisfaction (1-5) | 2.1 | 4.3 | +105% |

---

## What Didn't Work

- **Week 1:** AI flagged 12 "issues," 4 were false positives (TypeScript inference it couldn't see). Fixed by adding explicit return types.
- **Week 2:** AI suggested a "security fix" that would have broken auth. Caught because human reviewer still does final pass.
- **Week 3:** Junior dev started treating AI review as sufficient. Had to explicitly state: AI catches mechanical issues, human catches design issues. Both required.

**The AI is a linter that thinks. Not a replacement for thinking.**

---

## How to Replicate This

```bash
# 1. Clone this repo (if you haven't)
git clone https://github.com/evoveotech/cursor-howto.git

# 2. Copy the pr-review stack into your project
cd your-project
cp -r /path/to/cursor-howto/stacks/pr-review/v1.0.0/* .

# 3. Edit memory/review-standards.md to match your stack
# (Search/replace Next.js/Prisma/NextAuth with your actual tech)

# 4. In Cursor, select your code and type:
# /review

# 5. Fix issues, submit PR, let human reviewer do architecture pass
```

Total setup: 10 minutes.  
First review: 3 minutes.  
Value: 35 hours/week recovered.

---

**Stack used:** `pr-review` v1.0.0  
**Files installed:** `commands/review.md`, `memory/review-standards.md`, `agents/test-engineer.md`, `hooks/pre-review.sh`
