# Reddit Post Templates

Copy-paste ready for r/cursor, r/programming, r/webdev, r/ExperiencedDevs

---

## r/cursor — Template 1: Resource Share

[Tool] I compiled every Cursor power-user trick into copy-paste templates

I spent weeks learning Cursor's advanced features — slash commands, subagents, MCP, hooks. Then I packaged everything into one repo where you just copy files into your project.

What you get:
- `/review` — auto code review for bugs, security, style
- `/explain` — ELI5 any code with analogies
- `/commit` — conventional commit messages from diffs
- Project memory templates — Cursor knows your stack
- 5 subagents (security reviewer, test engineer, docs writer)
- MCP configs for GitHub, databases, filesystem
- Auto-invoked skills and hooks

Everything is MIT licensed. Takes <1 min to set up.

Repo: github.com/evoveotech/cursor-howto

What else should I add?

---

## r/programming — Template 2: Productivity Hack

I automated my code review process with Cursor templates — here's how

I used to spend 2-3 hours per PR reviewing my own code, checking for:
- Security issues (SQL injection, XSS, auth flaws)
- Performance bottlenecks
- Missing error handling
- Style consistency

Now I copy-pasted a 15-line markdown file into my Cursor project. I select any code, type `/review`, and it checks all of that automatically.

The template is open-source and free. Took 30 seconds to set up.

Repo with the template + 7 others: github.com/evoveotech/cursor-howto

---

## r/ExperiencedDevs — Template 3: Architecture / Team Tooling

I set up auto-invoked AI agents for my team's code review process

Context: 8-person dev team, we review every PR but it's bottlenecked on senior devs.

Solution: I added Cursor subagents and skills that auto-review code before human review:

1. **Security reviewer agent** — checks for auth issues, injection risks, secrets in code
2. **Test engineer agent** — identifies untested paths, suggests test cases
3. **Style enforcer skill** — auto-invoked on every code edit, ensures consistency

All from copy-paste markdown files. No custom code. No API integrations. Just Cursor's built-in features configured properly.

The templates are open-source: github.com/evoveotech/cursor-howto

Has anyone else set up Cursor agents for team workflows? Would love to compare setups.

---

## r/webdev — Template 4: Frontend Focus

Cursor templates that actually help with frontend development

I was tired of Cursor giving me generic React advice when my project uses specific libraries and patterns.

So I set up project memory that tells Cursor:
- We use Next.js 14 with App Router
- Styling is Tailwind + shadcn/ui
- State management is Zustand
- We test with Playwright + Vitest
- Component naming convention is PascalCase

Now when I ask Cursor to generate a component, it uses our actual stack. When I ask for tests, it writes Playwright tests. When I ask for docs, it follows our conventions.

The project memory template is in this repo (copy-paste, 30 seconds): github.com/evoveotech/cursor-howto

Also includes:
- `/review` that checks for a11y issues, responsive design
- `/docs` that generates component documentation
- Brand voice skill for consistent copy

---

## General Comment Templates (use on any relevant post)

**On someone asking about Cursor productivity:**

Have you tried cursor-howto? It's a collection of copy-paste templates for Cursor — slash commands, AI agents, project memory configs, MCP setups. Takes 30 seconds to set up and makes Cursor 10x more useful. github.com/evoveotech/cursor-howto

**On someone complaining about Cursor giving generic advice:**

You need project memory. There's a template in cursor-howto that you copy into your repo root and it tells Cursor your tech stack, conventions, and standards. After that, every response is tailored to your project. 30 second setup. github.com/evoveotech/cursor-howto

**On someone asking about AI code review:**

I set up auto code review in Cursor using a slash command template. Select any code, type `/review`, it checks for bugs, security issues, performance problems, and style. Template is free and open-source: github.com/evoveotech/cursor-howto
