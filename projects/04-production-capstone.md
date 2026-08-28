# Project 4: production AI feature capstone

## Goal

Solve a real user workflow end to end and demonstrate professional engineering judgment.

## Choose a problem

The workflow must have:

- A named user and measurable pain
- Accessible data or realistic synthetic data
- A clear success signal
- At least one meaningful failure/edge case
- A safe fallback

Examples: contract intake, support resolution drafting, incident triage, research synthesis, meeting-to-action workflow, or domain-specific document review.

## Required architecture

Use only the complexity the evals justify. The project must include:

- Typed service boundary
- Versioned prompt/model/tool configuration
- Structured output or bounded tool use
- Offline eval runner
- Trace and operational metrics
- Security controls and threat model
- Deployment and rollback path

Retrieval or an agent is optional; do not add either decoratively.

## Acceptance bar

- At least 75 representative eval cases
- A deterministic or simpler AI baseline
- Measured improvement over baseline
- No critical safety or tenant-isolation failures in the test set
- Load test with p50/p95 latency
- Cost per successful task
- Canary and rollback design
- Three documented failure investigations

## Final package

1. Two-minute demo
2. User and system requirements
3. Architecture and data-flow diagram
4. Decision records and rejected alternatives
5. Eval dataset methodology and results
6. Threat model and approval matrix
7. Load/cost report
8. Operations dashboard screenshot or mock
9. Incident postmortem
10. Reflection: what you would change with another month

## Review questions

- Which parts are deterministic and why?
- What evidence shows the model adds value?
- Where can untrusted input change behavior?
- How does the system prevent unauthorized actions?
- Which metric would trigger rollback?
- What is the largest remaining risk?
