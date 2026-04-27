# Project Review Standards

This file is loaded automatically by Cursor. It tells the AI our team's review standards so every /review command uses our actual conventions.

## Code Quality Bar

- **No functions over 50 lines** without explicit justification
- **All public functions must have JSDoc/TSDoc comments**
- **All API endpoints must have input validation**
- **All database queries must use parameterized statements**
- **No console.log in production code** — use structured logging

## Security Requirements

- Auth checks on every route that isn't public
- Rate limiting on all mutation endpoints
- Input sanitization before storage
- No secrets in code (use env vars, check with /security-scan)

## Testing Requirements

- Minimum 80% coverage for business logic
- Every bug fix must include a regression test
- Integration tests for every API endpoint
- E2E tests for critical user journeys

## Performance Standards

- Page load < 2s (Lighthouse)
- API response < 200ms (p95)
- Database queries must have explain plan reviewed
- No N+1 queries

## Tech Stack (for context)

- Backend: Node.js / Express / TypeScript
- Frontend: React / Next.js / Tailwind
- Database: PostgreSQL via Prisma
- Testing: Vitest + Playwright
- Auth: NextAuth.js
