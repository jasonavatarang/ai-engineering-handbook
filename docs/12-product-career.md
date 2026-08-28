# 12. Product judgment and career development

The best AI engineers do not begin with “where can I add an agent?” They begin with a costly user problem and decide which parts benefit from probabilistic judgment.

## Selecting a use case

Good early use cases have:

- High-frequency or high-value work
- Inputs and outcomes you can observe
- Tolerable and recoverable errors
- Accessible domain experts
- A path to representative evaluation data
- A clear fallback or human escalation

Be cautious when errors are irreversible, invisible, difficult to evaluate, or affect fundamental rights.

## Workflow decomposition

Map the current process:

1. Trigger
2. Inputs and sources of truth
3. Human judgments
4. Deterministic transformations
5. Decisions and approvals
6. External actions
7. Exceptions
8. Completion signal

Apply models to fuzzy interpretation or generation. Keep policy, authorization, calculations, and irreversible execution deterministic where possible.

## Product metrics

Connect technical metrics to outcomes:

| Technical metric | Possible product consequence |
|---|---|
| Retrieval recall | Whether the answer had access to the needed evidence |
| Tool argument accuracy | Failed or incorrect operations |
| Abstention rate | Work deferred to humans |
| p95 latency | User abandonment or interrupted workflow |
| Cost per success | Unit economics |
| Correction rate | Trust and hidden labor |

Measure whether the system saves time or improves decisions after including review and correction effort.

## UX for uncertainty

Design:

- Evidence and source visibility
- Editable drafts rather than immediate actions
- Clear previews for consequential changes
- Useful error recovery
- Explicit partial completion
- Easy escalation to a human
- Feedback tied to the exact run

Avoid fake confidence scores without calibration or a clear user decision attached.

## Architecture communication

A strong design document includes:

- User problem and non-goals
- Success, safety, latency, and cost requirements
- Data-flow and trust-boundary diagram
- Alternatives considered
- Evaluation plan
- Failure modes and mitigations
- Rollout, rollback, and monitoring
- Open decisions and owners

## Portfolio evidence

For each project publish:

- A concise demo
- Architecture diagram
- Representative eval dataset description
- Baseline and improved results
- Failure analysis
- Threat model
- Latency/cost report
- Tradeoff decisions
- Operational or incident scenario

Hiring teams need evidence of judgment, not a list of frameworks.

## Interview preparation

Practice explaining:

- RAG architecture and retrieval evaluation
- Workflow versus agent tradeoffs
- Tool authorization and idempotency
- Prompt injection and data isolation
- Model routing and cost control
- Online/offline eval design
- A production failure you diagnosed
- A feature you chose not to build with AI

## Continuing development

Build a durable learning loop:

- Read primary documentation and papers
- Reproduce small mechanisms from scratch
- Maintain a failure journal
- Review model/provider changes against your eval suite
- Teach concepts publicly or internally
- Contribute fixes and evaluation cases to real projects

## Exercises

1. Interview three users about a repeated knowledge-work task.
2. Draw the existing workflow and identify deterministic versus probabilistic steps.
3. Write a one-page product and evaluation brief.
4. Present an architecture decision with two rejected alternatives.
5. Publish a project postmortem centered on what failed and changed.

## Mastery check

You can connect system metrics to user value, explain uncertainty honestly, and show artifacts proving that your decisions improved a real workflow.
