# 11. Model customization

Customization is a ladder. Climb only when the current level fails against a defined eval.

## The ladder

1. Improve the task definition and output schema.
2. Improve context selection and examples.
3. Add deterministic tools or retrieval.
4. Route to a better-suited model or reasoning configuration.
5. Fine-tune or distill for stable repeated behavior.
6. Self-host or train when control, economics, data, or research requirements justify it.

## Prompting versus retrieval versus fine-tuning

| Need | First approach |
|---|---|
| Current/private factual knowledge | Retrieval or tools |
| Strict machine-readable shape | Structured outputs and validation |
| Stable style or repeated decision boundary | Examples, then consider fine-tuning |
| Lower cost/latency at high volume | Distillation or fine-tuning a smaller model |
| New capability absent from the base model | Data/training work or a different model |
| Full infrastructure/data control | Evaluate self-hosting |

Fine-tuning is not a reliable database update mechanism.

## Data quality

Training data should be:

- Representative of deployment inputs
- Correct and consistently labeled
- Diverse across edge cases
- Free of unauthorized private content
- Deduplicated across train and eval sets
- Versioned with provenance and license information
- Reviewed for harmful shortcuts and subgroup bias

Ten thousand inconsistent examples can be worse than hundreds of carefully curated ones.

## Experiment design

Before training:

- Freeze an eval set and baseline.
- Define the desired behavior change.
- Define acceptable regressions.
- Estimate training and inference economics.
- Keep a rollback path.

After training:

- Compare against the unchanged baseline.
- Run capability, safety, and domain evals.
- Inspect memorization and privacy risks.
- Test unseen formats and distribution shifts.
- Monitor the deployed model separately by version.

## Parameter-efficient methods

Methods such as LoRA update a small set of learned adapters rather than every model weight. They can reduce training memory and storage, but do not remove the need for high-quality data, evaluation, or deployment controls.

## Distillation

A stronger teacher model can help create labels or demonstrations for a smaller student. Validate teacher errors, use human-reviewed anchors, and evaluate the student on held-out real tasks. The goal is not imitation for its own sake; it is a better quality/cost/latency frontier.

## Self-hosting considerations

Evaluate:

- Model license and acceptable use
- GPU availability, utilization, and memory
- Quantization and quality loss
- Serving framework and batching
- Autoscaling and cold starts
- Security patching and artifact provenance
- Monitoring and rollback
- Engineering on-call burden
- Total cost at realistic utilization

API price versus GPU price is not a complete total-cost comparison.

## Exercises

1. For three failing cases, decide whether the remedy is prompt, retrieval, tool, routing, or training.
2. Curate 100 high-quality examples and write labeling guidance.
3. Detect duplicate or near-duplicate examples across data splits.
4. Design a fine-tuning experiment with success and regression thresholds.
5. Write a total-cost comparison for hosted versus self-hosted inference.

## Mastery check

You can justify why training is necessary, prove it improved the target behavior, quantify regressions, and operate the resulting model version safely.
