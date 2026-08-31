# AI system design review checklist

Use the applicable sections. Do not require every component for every system.

## 1. Product and task contract

- Is the user outcome concrete and valuable?
- Are success, refusal, partial success, and failure observable?
- Is uncertainty communicated appropriately?
- Which actions are consequential, external, costly, or irreversible?

## 2. Architecture choice

- Could deterministic code or a state machine replace model judgment?
- Could one bounded model call replace a workflow or agent?
- Does retrieval solve a demonstrated knowledge or evidence problem?
- Does each additional agent provide specialization, isolation, or parallelism that beats a single-agent baseline?

## 3. Prompt and context

- Are instructions, user data, retrieved data, and tool output clearly separated?
- Is context relevant, fresh, deduplicated, and within budget?
- Are examples representative of difficult cases?
- Are prompt changes versioned and evaluated?

## 4. Retrieval

- Are parsing, chunking, metadata, access control, ranking, and freshness intentional?
- Are retrieval metrics separated from answer metrics?
- Can the system cite evidence and abstain when evidence is missing?
- Is tenant filtering enforced before retrieval results reach the model?

## 5. Models and outputs

- Is model choice justified by measured quality, latency, and cost?
- Are outputs schema-constrained and semantically validated?
- Are fallbacks designed for specific failure classes?
- Are provider limits and capabilities checked against current primary documentation?

## 6. Tools and agent control

- Are tools minimal, typed, least-privileged, and safe against malformed arguments?
- Are writes idempotent and protected by authorization or approval?
- Are retries bounded and classified by error type?
- Are state, budgets, completion criteria, and recovery behavior explicit?

## 7. Security and privacy

- Is untrusted content prevented from granting authority or exposing secrets?
- Are authentication, authorization, tenant isolation, and data retention enforced outside the model?
- Are logs redacted and tool outputs treated as untrusted?
- Are dependencies, plugins, MCP servers, skills, and model changes part of the supply-chain threat model?

## 8. Evals and observability

- Does the eval set represent normal, difficult, adversarial, and regression cases?
- Are graders calibrated against human judgment?
- Can traces connect the user request, model calls, retrieval, tools, validation, and final result?
- Does feedback become reviewed eval data instead of silently becoming ground truth?

## 9. Operations and economics

- Are p50 and p95 latency, availability, error rate, and cost per successful task measured?
- Are caching, concurrency, rate limits, circuit breakers, and degradation modes intentional?
- Can releases be canaried, compared, and rolled back?
- Is there an owner and playbook for incidents and data-quality failures?

