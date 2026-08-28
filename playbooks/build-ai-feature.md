# Playbook: build an AI feature

## 1. Frame the problem

- Name the user, trigger, current workflow, and painful step.
- Define the user-visible outcome.
- Define non-goals.
- Decide what happens when the model is wrong or unavailable.

## 2. Define acceptance

- Product success metric
- Offline quality metrics
- Safety invariants
- Latency and cost ceilings
- Human escalation and approval points

Create at least 20 representative examples before optimizing.

## 3. Establish the simplest baseline

Try deterministic rules, search, templates, or one model call. Record quality, latency, cost, and failure categories.

## 4. Design the system

- Keep policy and authorization outside the model.
- Retrieve only required context.
- Prefer schemas over text parsing.
- Expose only necessary tools.
- Bound calls, time, tokens, and retries.
- Record versions and trace IDs.

## 5. Implement vertically

Build one end-to-end slice with fake adapters, then a small live integration. Add deterministic tests before scaling the eval suite.

## 6. Evaluate and red-team

Test typical, edge, adversarial, missing-context, conflicting-evidence, dependency-failure, and permission cases.

## 7. Release safely

Shadow → internal users → small canary → gradual rollout. Define rollback thresholds before deployment.

## 8. Operate

Review failures, corrections, latency, cost, and safety signals. Convert meaningful failures into regression cases.
