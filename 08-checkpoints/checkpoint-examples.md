# Checkpoint Examples

Real-world examples of using checkpoints effectively in Cursor.

Note: Checkpoints are created automatically with every user prompt. You do not need to manually save them. To rewind, press `Esc` twice (`Esc+Esc`) or use `/rewind` to open the checkpoint browser.

## Example 1: Database Migration

### Scenario
You need to migrate from MySQL to PostgreSQL but want to explore both a direct migration and a gradual dual-write approach.

### Workflow

```
User: Let's implement a direct migration from MySQL to PostgreSQL
      [Checkpoint A created automatically]

Cursor: I'll implement the direct migration...
[Changes database driver, updates queries, modifies schema]

User: Run the tests
      [Checkpoint B created automatically]

Cursor: Running tests...
❌ 15 tests failing - connection pool issues

User: This approach has issues. Let's try the dual-write pattern instead.
[User presses Esc+Esc, selects Checkpoint A, chooses "Restore code and conversation"]

User: Now implement a dual-write pattern where we write to both databases

Cursor: I'll implement dual-write migration...
[Implements dual-write layer, gradual migration strategy]

User: Run the tests

Cursor: Running tests...
✅ All tests passing

User: The dual-write approach is clearly safer. Let's commit this.
```

## Example 2: Performance Optimization

### Scenario
Multiple performance optimization strategies to try.

### Workflow

```
User: Let's optimize the API response time. Current: 450ms
      [Checkpoint "Baseline" created automatically]

Cursor: I'll add database query caching...
[Implements Redis caching]

User: Run performance tests

Cursor: Results: 280ms average response time (38% improvement)

User: Let me try a different approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try database query optimization instead

Cursor: I'll optimize database queries...
[Adds indexes, optimizes N+1 queries]

User: Run performance tests

Cursor: Results: 180ms average response time (60% improvement)

User: Let me also try a third approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try response compression and CDN

Cursor: I'll add compression and CDN...
[Implements gzip, sets up CDN]

User: Run performance tests

Cursor: Results: 320ms average response time (29% improvement)

User: Query optimization was the best. Let me go back and combine it with caching.
[User presses Esc+Esc, selects the checkpoint after query optimization, chooses "Restore code and conversation"]

User: Now add Redis caching on top of these optimized queries

Cursor: [Adds Redis caching on top of optimized queries]

User: Run performance tests

Cursor: Results: 95ms average response time (79% improvement) 🎉

User: Perfect! This is the winner. Let's commit this.
```

## Example 3: UI/UX Iteration

### Scenario
Trying different layouts for a dashboard.

### Workflow

```
User: Let's redesign the dashboard with a sidebar layout
      [Checkpoint "Start" created automatically]

Cursor: [Implements sidebar layout]

User: Show me a screenshot

Cursor: [Shows screenshot]

User: The sidebar feels cramped. Let's try a top navigation instead.
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a top navigation layout

Cursor: [Implements top navigation]

User: Show me a screenshot

Cursor: [Shows screenshot]

User: Better, but let's try a card-based grid layout
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a card-based grid layout

Cursor: [Implements card grid]

User: Show me a screenshot

Cursor: [Shows screenshot]

User: This is great! But can we combine the top nav with the card grid?
[User presses Esc+Esc, selects the checkpoint after the card grid, chooses "Restore code and conversation"]

User: Add top navigation to the card grid layout

Cursor: [Adds top navigation to card grid]

User: Perfect! This is the final design.
```

## Example 4: Debugging Session

### Scenario
Hunting down a tricky bug with multiple hypotheses.

### Workflow

```
User: There's a memory leak in the application
      [Checkpoint "Before debugging" created automatically]

Cursor: Let me investigate...
[Analyzes code]

User: I think it's in the event listeners. Let's fix those.

Cursor: [Fixes event listener cleanup]

User: Run memory profiler

Cursor: Still leaking memory - event listeners weren't the issue

User: Let me go back and try a different hypothesis.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Maybe it's the database connections?

Cursor: [Implements connection pooling fixes]

User: Run memory profiler

Cursor: Still leaking - not the connections either

User: Let me go back and try another angle.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Let's check for circular references

Cursor: [Finds and fixes circular references in cache]

User: Run memory profiler

Cursor: ✅ Memory leak fixed! The circular references in the caching layer were the culprit.

User: Excellent! Let's commit this fix.
```

## Example 5: API Design Evolution

### Scenario
Designing a REST API with multiple iterations.

### Workflow

```
User: Create a REST API for our blog platform
      [Checkpoint "Before API design" created automatically]

Cursor: [Creates basic CRUD API]

User: This is too simple. Let's add pagination and filtering

Cursor: [Adds pagination and filtering]

User: We need better resource relationships

Cursor: [Implements HATEOAS links]

User: Actually, let's try GraphQL instead of REST
[User presses Esc+Esc, selects "Before API design" checkpoint, chooses "Restore code and conversation"]

User: Implement a GraphQL API for our blog platform instead

Cursor: [Implements GraphQL API]

User: I think REST is better for our use case.
[User presses Esc+Esc, selects the checkpoint after HATEOAS, chooses "Restore code and conversation"]

User: Let's finalize the REST approach.
```

## Example 6: Configuration Management

### Scenario
Testing different configuration approaches.

### Workflow

```
User: Move configuration to environment variables
      [Checkpoint "Original config" created automatically]

Cursor: [Implements env var configuration]

User: Test in development

Cursor: Works locally but deployment issues in production

User: Let me try a different approach.
[User presses Esc+Esc, selects "Original config" checkpoint, chooses "Restore code and conversation"]

User: Try a config file approach with validation

Cursor: [Implements YAML config with JSON schema validation]

User: Test in development

Cursor: ✅ Works well, good validation errors

User: Can we also support env vars for sensitive values?

Cursor: [Adds env var override for secrets]

User: Test deployment

Cursor: ✅ All environments working correctly

User: Perfect! This is production-ready.
```

## Example 7: Test Strategy

### Scenario
Implementing comprehensive testing.

### Workflow

```
User: Add unit tests for the auth module
      [Checkpoint created automatically]

Cursor: [Adds Jest unit tests]

User: Run tests

Cursor: 45 tests passing, 78% coverage

User: Add integration tests too

Cursor: [Adds integration tests]

User: Run tests

Cursor: 89 tests passing, 92% coverage, but tests are slow (3 minutes)

User: The tests are too slow. Let's optimize.

Cursor: [Optimizes test setup, adds parallel execution]

User: Run tests

Cursor: 89 tests passing, 92% coverage, 35 seconds ✅

User: Great! Now add E2E tests for critical paths

Cursor: [Adds Playwright E2E tests]

User: Run all tests

Cursor: 112 tests passing, 94% coverage, 2 minutes

User: Perfect balance of coverage and speed!
```

## Example 8: Using Summarize from Checkpoint

### Scenario
After a long debugging session, you want to condense the conversation while preserving context.

### Workflow

```
User: [After 20+ messages of debugging and exploration]

[User presses Esc+Esc, selects an early checkpoint, chooses "Summarize from here"]
[Optionally provides instructions: "Focus on what we tried and what worked"]

Cursor: [Generates a summary of the conversation from that point forward]
[Original messages are preserved in the transcript]
[The summary replaces the visible conversation, reducing context window usage]

User: Now let's continue with the approach that worked.
```

## Key Takeaways

1. **Checkpoints are automatic**: Every user prompt creates a checkpoint -- no manual saving needed
2. **Use Esc+Esc or /rewind**: These are the two ways to access the checkpoint browser
3. **Choose the right restore option**: Restore code, conversation, both, or summarize depending on your needs
4. **Don't fear experimentation**: Checkpoints make it safe to try radical changes
5. **Combine with git**: Use checkpoints for exploration, git for finalized work
6. **Summarize long sessions**: Use "Summarize from here" to keep conversations manageable
