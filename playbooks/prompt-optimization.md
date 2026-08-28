# Playbook: optimize a prompt

## Inputs

- Versioned baseline prompt
- Fixed representative eval set
- Model and settings
- Context-builder version
- Tool definitions
- Quality, latency, and cost metrics

## Procedure

1. Run and record the baseline.
2. Cluster failures by cause.
3. Remove repeated, obsolete, or non-behavioral instructions.
4. Clarify goal, success criteria, evidence, boundaries, output, and stop rules.
5. Move machine-readable format requirements into a schema.
6. Move tool-specific guidance into tool descriptions.
7. Add examples only for measured decision-boundary failures.
8. Change one coherent instruction group.
9. Rerun all evals and inspect both gains and regressions.
10. Keep the change only if the overall tradeoff improves.

## Report

```text
Baseline version:
Candidate version:
Changed:
Hypothesis:
Dataset:
Quality delta:
Latency delta:
Cost delta:
Regressions:
Decision:
```
