# 10. Production systems

Production AI engineering optimizes a vector: quality, latency, cost, reliability, safety, and operability. Improvements count only when the whole product tradeoff gets better.

## Service-level objectives

Define targets such as:

- Successful task completion rate
- Availability
- Time to first useful output
- End-to-end p95 latency
- Maximum cost per successful task
- Maximum unsafe-action or cross-tenant error rate
- Recovery-time objective for provider failure

Use product-relevant success, not merely HTTP 200 responses.

## Latency budget

Break the request into:

```text
authentication + retrieval + model queue/inference + tools + validation + rendering
```

Optimize the largest measured component.

Techniques:

- Stream useful output when partial output is safe
- Parallelize independent reads
- Cache stable prefixes and reusable retrieval results
- Reduce irrelevant context and tool definitions
- Route simple tasks to faster models
- Move long tasks to background jobs
- Reuse connections and batch where appropriate
- Set deadlines and cancel abandoned work

## Cost model

Calculate cost per successful task:

```text
model input + model output + embeddings + reranking + tools + retries + infrastructure + human review
```

Cheap calls that frequently fail or require correction may cost more than a capable first attempt.

## Model routing

Start simple:

- Default balanced model
- Smaller model for proven low-complexity tasks
- Flagship or greater reasoning for difficult/high-value cases
- Safe fallback when the preferred provider is unavailable

Routing inputs may include task type, risk, context size, language, tool needs, latency tier, or a cheap complexity classifier. Evaluate routing errors and avoid silently sending sensitive data to an unapproved provider.

## Reliability patterns

- Timeout every network boundary
- Retry only safe/transient failures with jitter
- Use idempotency keys for writes
- Bound concurrency and queue depth
- Add circuit breakers and load shedding
- Persist resumable state for long tasks
- Design fallbacks for model, retrieval, and tool outages
- Distinguish partial success from full success
- Make deployments reversible

## Release process

Treat prompt/model/tool changes like code:

1. Version the complete configuration.
2. Run offline evals.
3. Review security and data-flow changes.
4. Deploy to shadow or canary traffic.
5. Compare quality, latency, cost, and safety.
6. Promote gradually.
7. Roll back automatically on defined thresholds.

## Capacity and rate limits

Model traffic is bursty. Plan for:

- Requests and tokens per minute
- Concurrent long-running requests
- Queue growth and user-visible status
- Provider and tenant quotas
- Retry storms
- Large-context outliers
- Tool dependencies with lower capacity than the model

Use per-tenant limits to prevent one user from exhausting shared capacity.

## Incident response

For each incident:

1. Protect users and stop unsafe actions.
2. Preserve traces and affected version IDs.
3. Reduce scope through rollback, tool disablement, or model fallback.
4. Identify the failing layer.
5. Communicate impact and current state.
6. Add regression tests, monitoring, and ownership.

## Exercises

1. Create and measure a latency budget for one project.
2. Calculate cost per successful task across two model configurations.
3. Simulate rate limiting and verify backoff plus bounded retries.
4. Canary a prompt change against recorded traffic.
5. Practice rolling back a model/tool configuration.

## Mastery check

You can defend operational targets, load-test the system, diagnose tail latency, estimate capacity, and recover from dependency failure.
