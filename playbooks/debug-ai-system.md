# Playbook: debug an AI system

## Preserve the failing run

Capture trace ID, application/prompt/model/tool/retrieval versions, safe inputs, retrieved IDs, tool calls, validation results, timing, and final output.

## Reproduce

- Replay the exact recorded configuration when possible.
- Separate deterministic replay from fresh model sampling.
- Run several times to estimate variability.

## Locate the failing layer

1. Input validation
2. Task instructions
3. Context assembly
4. Retrieval and ranking
5. Model reasoning/generation
6. Tool selection
7. Tool execution
8. Output validation
9. Authorization/business policy
10. User experience or infrastructure

Do not edit the prompt until evidence points to an instruction problem.

## Form a falsifiable hypothesis

Example: “The current-policy chunk is absent from the top five retrieval results because its version metadata was not indexed.”

## Change one layer

Implement the smallest fix, add a regression case, and rerun the broader eval suite for regressions.

## Close the loop

Document symptom, impact, root cause, contributing conditions, fix, verification, monitoring, and prevention owner.
