# 1. Engineering foundations

AI applications are distributed systems with an unusually nondeterministic dependency. Strong software engineering is therefore the first prerequisite, not an optional layer added later.

## Core capabilities

### Programming

Be fluent in one production language—usually Python or TypeScript—and comfortable reading the other.

You should understand:

- Types, interfaces, modules, packaging, and dependency management
- Exceptions, retries, timeouts, cancellation, and cleanup
- Async I/O and bounded concurrency
- Unit, integration, contract, and end-to-end tests
- Profiling, logging, and debugging
- Serialization and schema validation

### APIs and distributed systems

Know what happens when a dependency is slow, unavailable, duplicated, or returns malformed data.

Practice:

- HTTP semantics and status codes
- Idempotency keys for retried writes
- Exponential backoff with jitter
- Deadlines rather than unbounded waits
- Rate limits and backpressure
- Queues for long-running work
- Circuit breakers and graceful degradation

### Data systems

Learn relational databases before specialized vector infrastructure.

Be able to:

- Model entities and relationships
- Write joins, aggregations, transactions, and migrations
- Select indexes based on query patterns
- Explain consistency and isolation tradeoffs
- Separate operational data from analytics and traces
- Enforce tenant boundaries in queries and storage

### Delivery

Every project should have:

- Reproducible local setup
- Environment-based configuration
- Secret management
- Automated tests in CI
- Container or equivalent deployable artifact
- Health/readiness checks
- Rollback strategy
- Basic monitoring

## The AI request lifecycle

Trace every application through these stages:

1. Authenticate and authorize the caller.
2. Validate and normalize input.
3. Load application and tenant context.
4. Construct the model request.
5. Call the model with timeout and retry policy.
6. Execute any approved tools.
7. Parse and validate the result.
8. Apply domain rules.
9. Persist or return the result.
10. Record safe telemetry and feedback hooks.

A failure at each step should have an intentional behavior.

## Configuration hierarchy

Separate:

- **Code:** stable logic under version control
- **Configuration:** environment-specific non-secret values
- **Secrets:** credentials with restricted access and rotation
- **Prompts:** versioned behavioral artifacts
- **Policy:** rules enforced independently of model output

Do not hide business policy inside a paragraph that only the model interprets.

## Testing pyramid for AI products

| Layer | Examples |
|---|---|
| Deterministic unit tests | Parsers, permissions, chunking, routing, cost calculations |
| Contract tests | Tool schemas, provider adapters, database boundaries |
| Recorded integration tests | Model/tool response fixtures without live cost |
| Offline AI evals | Representative tasks scored for quality and behavior |
| End-to-end smoke tests | Small live suite in a controlled environment |
| Production monitoring | Drift, incidents, latency, cost, feedback |

Push as much behavior as possible into the cheaper deterministic layers.

## Exercises

1. Build a typed `/classify` API with validation, persistence, tests, and a fake model adapter.
2. Add a timeout and bounded retry policy. Demonstrate a simulated timeout.
3. Add an idempotent write endpoint and prove duplicate requests do not duplicate side effects.
4. Emit structured logs with a correlation ID while redacting secrets and user content.
5. Containerize the service and run its tests from a clean checkout.

## Mastery check

You are ready to continue when you can explain and demonstrate:

- The difference between retry-safe reads and unsafe repeated writes
- Why validation must occur after model generation
- How a request is traced across model and tool calls
- How you would roll back a broken prompt or model configuration
- Which data should never appear in logs
