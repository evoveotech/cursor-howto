# Project Context

This file is loaded automatically by Cursor. It ensures every AI response is tailored to our actual stack and conventions.

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS + shadcn/ui components
- **State**: Zustand for client, Server Actions for server
- **Database**: PostgreSQL via Prisma ORM
- **Auth**: NextAuth.js v5 (OAuth + email)
- **Testing**: Vitest (unit), Playwright (E2E)
- **API**: tRPC for internal, REST for external
- **Hosting**: Vercel (frontend), Railway (database)

## Architecture

```
User → Next.js (App Router) → tRPC → Prisma → PostgreSQL
                ↓
           NextAuth (JWT)
                ↓
           Zustand (client state)
```

## Project Structure

```
app/              # Next.js App Router pages
├── api/          # API routes (REST external)
├── _trpc/        # tRPC routers
components/       # React components (PascalCase)
├── ui/           # shadcn/ui components
lib/              # Utilities, hooks, types
├── db/           # Prisma client, queries
├── auth/         # NextAuth config
├── trpc/         # tRPC setup
prisma/           # Schema + migrations
public/           # Static assets
tests/            # Vitest + Playwright
```

## Key Conventions

- **File naming**: Components = PascalCase, utilities = camelCase, constants = UPPER_SNAKE
- **Imports**: Absolute paths via `@/` alias, group: React → lib → components → types
- **Error handling**: Never swallow errors. Always log + show user-friendly message.
- **Database**: All queries go through `lib/db/` functions. No raw SQL in components.
- **Types**: Strict TypeScript. No `any`. Unknown types must be validated with Zod.

## Business Context

This is a SaaS platform for [YOUR_BUSINESS]. Key entities:
- User (auth, subscription, team membership)
- Team (billing, members, permissions)
- Project (the core unit of work)

Before suggesting changes, consider: does this affect billing? Does this change permissions?
