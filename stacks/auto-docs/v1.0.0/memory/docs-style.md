# Documentation Standards

This file tells Cursor how to write documentation for this project.

## Tone

- Professional but approachable
- Direct and concise — no filler
- Assume reader is competent but unfamiliar with THIS codebase
- Code examples must compile and run

## Format

- All docs in Markdown
- API docs: path → auth → request → response → errors
- Component docs: props table → usage example → notes
- Architecture docs: text diagram → data flow → decisions

## Rules

- Every public function must have JSDoc/TSDoc
- Every API endpoint must have request/response examples
- Every component must have a usage example
- Every database table must have schema docs
- Changelog follows Keep a Changelog format
- README is updated when architecture changes

## Anti-Patterns (Don't Do This)

- Don't write "simple" or "just" — if it were simple, we wouldn't need docs
- Don't document what the code does (we can read code) — document WHY and WHEN
- Don't leave TODOs in docs — either document it or don't
- Don't write generic advice — be specific to this project
