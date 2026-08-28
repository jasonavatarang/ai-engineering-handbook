# 16-week roadmap

Assumption: 8–12 focused hours each week. Compress or expand the schedule, but preserve the build-and-evaluate loop.

## Weeks 1–2: software systems for AI

Learn:

- Python typing, packaging, testing, async I/O, HTTP clients
- REST APIs, JSON Schema, SQL, caching, queues
- Git, containers, CI, configuration, secret handling

Build:

- A typed API that validates input, persists records, exposes health checks, and has unit/integration tests

Evidence:

- CI passes from a clean checkout
- Invalid input produces intentional errors
- Logs include request and correlation IDs without secrets

## Weeks 3–4: ML and LLM foundations

Learn:

- Train/validation/test splits, leakage, baselines, precision/recall
- Tokens, embeddings, attention, transformers, pretraining, post-training
- Context windows, hallucination, calibration, inference cost

Build:

- A small classifier and a semantic-search notebook or script

Evidence:

- Compare against a simple baseline
- Explain the largest error categories
- Show how threshold selection changes precision and recall

## Weeks 5–6: prompting and structured outputs

Learn:

- Outcome-first task contracts
- Context selection and prompt injection boundaries
- JSON Schema, validation, retries, refusals, and partial failure
- Model and reasoning-effort routing

Build:

- [Project 1: structured extractor](projects/01-structured-extractor.md)

Evidence:

- At least 30 labeled examples
- Schema-valid output rate and field-level accuracy
- A comparison of two prompt/model configurations

## Weeks 7–8: retrieval-augmented generation

Learn:

- Parsing, chunking, embeddings, sparse/dense/hybrid retrieval
- Metadata filters, reranking, evidence packing, citations
- Retrieval metrics versus answer metrics

Build:

- [Project 2: document assistant](projects/02-rag-assistant.md)

Evidence:

- Retrieval recall@k
- Citation correctness
- Explicit abstention on unanswerable questions

## Weeks 9–10: tools and agents

Learn:

- Function tools, idempotency, permissions, state machines
- Workflow versus single-agent versus multi-agent decisions
- Stop conditions, retries, budgets, and human approval

Build:

- [Project 3: operations agent](projects/03-tool-using-agent.md)

Evidence:

- Tool-choice and argument-accuracy evals
- Tests for duplicate actions and malicious tool output
- A trace showing one recovered failure

## Weeks 11–12: evals, observability, and security

Learn:

- Golden datasets, graders, pairwise evaluation, human calibration
- Tracing, token/cost telemetry, feedback capture
- Prompt injection, least privilege, tenant isolation, data retention

Build:

- An offline eval runner and a production-style trace schema

Evidence:

- Every important failure becomes a regression case
- Automated graders agree acceptably with human labels
- A threat model documents assets, threats, controls, and residual risk

## Weeks 13–14: production optimization

Learn:

- Streaming, caching, batching, concurrency, rate-limit handling
- Model routing, fallbacks, circuit breakers, SLOs
- Canary releases, rollback, data migrations, incident response

Build:

- Add operational hardening to one earlier project

Evidence:

- Load-test report with p50/p95 latency and error rate
- Cost per successful task
- Failure-mode and rollback demonstration

## Weeks 15–16: capstone and career package

Build:

- [Project 4: production capstone](projects/04-production-capstone.md)

Publish:

- Architecture diagram and decision record
- Two-minute demo
- Eval report
- Threat model
- Cost/latency report
- Incident postmortem
- README explaining what you personally designed and learned

## Weekly operating rhythm

| Day | Activity |
|---|---|
| 1 | Read concepts and write your own explanation |
| 2 | Design the smallest experiment and its evaluation |
| 3–4 | Implement and instrument |
| 5 | Run evals, classify failures, and improve one variable |
| 6 | Write a short engineering note or postmortem |
| 7 | Rest or review spaced-repetition notes |
