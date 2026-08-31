---
name: review-ai-system-design
description: Review an AI or LLM system architecture for product fit, unnecessary agentic complexity, context and retrieval quality, tool safety, evaluation coverage, reliability, latency, and cost. Use when assessing a design document, architecture diagram, technical proposal, RAG pipeline, tool-using agent, multi-agent plan, or production-readiness decision.
---

# Review an AI System Design

Produce an evidence-based design review that identifies the smallest architecture able to meet the product requirement and the highest-value improvements.

## Workflow

1. Restate the user outcome, task boundary, success metric, and consequential actions. Label missing facts as assumptions.
2. Map the flow from request through context assembly, model calls, retrieval, tools, validation, persistence, and response.
3. Compare the proposal with the least nondeterministic adequate design: code, one model call, workflow, single agent, then multi-agent.
4. Read [references/review-checklist.md](references/review-checklist.md) and assess every applicable category. Mark inapplicable categories instead of inventing requirements.
5. Rank findings by user impact and likelihood. Separate observed facts, inferences, and unknowns.
6. Recommend controls at the correct layer: prompts for guidance, schemas and validators for correctness, permissions and hooks for enforcement, and evals for measured behavior.
7. Use [assets/review-report.md](assets/review-report.md) as the output structure. Adapt it to the scope rather than filling sections with low-value text.

## Decision Rules

- Prefer deterministic code for known rules and state transitions.
- Require a measurable reason to add retrieval, an agent loop, or multiple agents.
- Treat model output, retrieved text, webpages, and tool results as untrusted input.
- Separate tool selection from authorization. A model may propose a consequential action; trusted application code or a human must authorize it.
- Require idempotency, bounded retries, time and tool budgets, and explicit terminal states for agentic loops.
- Require task-specific eval cases before recommending prompt, model, or architecture optimization.
- Recommend current vendor features only after checking primary documentation; label time-sensitive details.

## Verification

Before finalizing:

- Trace at least three paths: normal success, dependency failure, and adversarial or malformed input.
- Confirm every high-priority recommendation has a validation method or acceptance criterion.
- Check that proposed hard guardrails are enforced outside model instructions.
- Check that quality, latency, and cost are measured per successful task rather than per model call alone.
- State what evidence could change the recommendation.

