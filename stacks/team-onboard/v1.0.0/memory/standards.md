# Coding Standards

## Style Rules

- Max 50 lines per function
- Max 3 parameters per function (use config object)
- Early returns preferred over nested ifs
- Async/await only, no .then() chains
- Destructure in function parameters when possible

## Component Rules

- Server Components by default
- 'use client' only when using: useState, useEffect, browser APIs, event handlers
- Props interface named `[ComponentName]Props`
- Default export for page components, named exports for everything else

## Database Rules

- All queries in `lib/db/` directory
- Prisma transactions for multi-step operations
- Soft deletes (deletedAt timestamp), never hard delete
- Pagination on all list queries (cursor-based)

## Testing Rules

- Unit tests: `*.test.ts` alongside source
- E2E tests: `tests/e2e/*.spec.ts`
- One assertion per test (use parameterized tests for multiples)
- Mock external APIs, test against real database (test container)

## Security Rules

- Rate limit all mutations (60/min per user)
- Validate all inputs with Zod (both API and Server Actions)
- Auth check on every route except `/login`, `/register`, `/api/public/*`
- No secrets in code. Use `process.env`. Check with `grep -r "sk-" .`

## Performance Rules

- Page load < 2s (Lighthouse)
- API response < 200ms (p95)
- Use React Suspense for async boundaries
- Images: Next.js Image component with priority for above-fold
- Database: index on query columns, review query plans for slow queries
