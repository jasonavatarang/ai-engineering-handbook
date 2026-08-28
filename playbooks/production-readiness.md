# Playbook: production readiness review

## Product

- [ ] Named user and measurable outcome
- [ ] Non-AI or simpler baseline compared
- [ ] Failure and fallback experience designed
- [ ] Human review burden included in value calculation

## Quality

- [ ] Representative offline eval set
- [ ] Typical, edge, adversarial, and unanswerable cases
- [ ] Automated graders calibrated with humans
- [ ] Acceptance and regression thresholds
- [ ] Versioned prompts, models, tools, retrieval, and data

## Safety and security

- [ ] Data-flow diagram and threat model
- [ ] Authentication and tenant isolation tested
- [ ] Model/tool outputs treated as untrusted
- [ ] Least-privilege tools and network access
- [ ] Consequential actions require authorization/approval
- [ ] Secrets absent from prompts and logs
- [ ] Retention, deletion, and incident policies documented

## Reliability

- [ ] Timeouts, bounded retries, and backoff
- [ ] Idempotency for retried writes
- [ ] Rate limiting and backpressure
- [ ] Provider/tool outage fallback
- [ ] Durable state for long tasks
- [ ] Canary, rollback, and kill switch

## Operations

- [ ] Task-success, latency, cost, and error dashboards
- [ ] Trace IDs across model and tool calls
- [ ] Alerts tied to user impact
- [ ] On-call owner and incident playbook
- [ ] Capacity and quota plan

## Release evidence

- [ ] Eval report
- [ ] Security review
- [ ] Load test
- [ ] Cost estimate
- [ ] Rollout and rollback plan
- [ ] Known limitations communicated to users
