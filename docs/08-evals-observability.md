# 8. Evals and observability

Evals tell you whether behavior is good. Observability tells you why a particular run behaved the way it did. You need both.

## Eval-driven development

1. Define the user outcome.
2. Collect representative cases before optimizing.
3. Define objective checks and judgment rubrics.
4. Record the baseline configuration.
5. Make one coherent change.
6. Compare quality, latency, cost, and regressions.
7. Add production failures continuously.

OpenAI's official guidance recommends task-specific evals, early and continuous evaluation, production-derived cases, automated scoring where appropriate, and human calibration: [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Dataset design

Include:

- Common happy paths
- Boundary and ambiguous cases
- Rare high-impact cases
- Adversarial or malicious inputs
- Missing, stale, and conflicting evidence
- Tool timeouts and malformed results
- Different user groups, formats, and languages relevant to production

Maintain a held-out set for final comparisons and a growing regression set for known failures.

## Grader hierarchy

Prefer the most objective grader available:

1. Code execution or deterministic business check
2. Schema or exact-match validation
3. Reference-guided comparison
4. Pairwise model judgment with a rubric
5. Single-answer model score
6. Human expert review

Use multiple graders when one score hides important tradeoffs.

### Calibrating model graders

- Write a specific rubric with pass/fail anchors.
- Collect human labels on a representative sample.
- Measure agreement and inspect disagreements.
- Control for ordering and verbosity bias.
- Recalibrate when the task or output distribution changes.

## What to evaluate in an agent

- Final task success
- Instruction following
- Tool selection
- Argument accuracy
- Evidence use
- Authorization and approval behavior
- Handoff accuracy
- Stop-condition compliance
- Recovery from injected failures
- Total calls, tokens, latency, and cost

Do not declare victory because an intermediate tool result was correct if the final answer omitted it.

## Trace design

For each run, record safe, structured fields:

- Trace, request, user/tenant pseudonymous IDs
- Prompt, model, tool, retrieval, and application versions
- Start/end timestamps and latency by stage
- Token and cost data
- Tool names, argument hashes or safely redacted arguments, results, and errors
- Retrieved document IDs and scores
- Validation outcomes
- User feedback and final task status

Avoid raw secrets and unnecessary personal data. Access to traces should follow the same tenant and role boundaries as application data.

## Operational dashboards

Track distributions, not only averages:

- Task-success rate
- Schema and tool error rate
- Abstention and escalation rate
- p50/p95/p99 latency
- Tokens and cost per successful task
- Tool-call counts and retry rates
- Retrieval recall on labeled shadow traffic
- User corrections and negative feedback
- Safety-policy interventions

## Failure taxonomy

Tag failures consistently:

```text
input | instruction | context | retrieval | model | tool-selection |
tool-execution | validation | authorization | UX | infrastructure
```

This prevents every incident from becoming an unstructured “prompt problem.”

## Exercises

1. Build a JSONL eval set with 30 typical, edge, and adversarial cases.
2. Implement exact, schema, and rubric graders.
3. Compare two configurations using confidence intervals or repeated runs.
4. Create a trace for a tool-using request and diagnose an injected failure.
5. Convert one real failure into a regression test and a monitoring alert.

## Mastery check

You can show measured improvement, explain grader reliability, reproduce a failed run, and locate the failing system layer.
