# 2. Machine-learning foundations

You do not need to become a research scientist, but you must reason correctly about data, uncertainty, and measurement.

## The supervised-learning frame

Given inputs `x`, labels `y`, a parameterized model `f`, and loss function `L`, training seeks parameters that minimize expected loss on the target distribution—not merely the training examples.

That distinction creates most of the important engineering questions:

- Does the dataset represent production traffic?
- Is the label actually connected to user value?
- Is information leaking from the future or test set?
- Are rare but costly cases represented?
- Does average performance hide subgroup failures?

## Data splits

- **Training set:** used to update parameters.
- **Validation set:** used to select models, prompts, thresholds, and hyperparameters.
- **Test set:** held back for a final unbiased estimate.
- **Production shadow set:** recent real traffic labeled after deployment.

Repeatedly optimizing against the test set turns it into another validation set.

## Metrics

### Classification

- Accuracy is useful only when classes and error costs are reasonably balanced.
- Precision asks: when the system predicts positive, how often is it correct?
- Recall asks: among true positives, how many did it find?
- F1 balances precision and recall but hides their individual business costs.
- Calibration asks whether predicted confidence matches observed frequency.

Always inspect a confusion matrix and slice metrics by meaningful cohorts.

### Ranking and retrieval

- Recall@k: did the relevant item appear in the top `k`?
- Precision@k: how much of the top `k` was relevant?
- Mean reciprocal rank: how early did the first relevant item appear?
- NDCG: did the ranking place highly relevant items near the top?

### Generation

Open-ended generation rarely has one correct string. Use combinations of:

- Exact or schema checks for objective requirements
- Reference-guided scoring
- Pairwise preference judgments
- Factuality or citation checks
- Task-completion tests
- Human review calibrated against automated graders

## Baselines

Before using an LLM, compare against:

- A constant or majority-class prediction
- Keyword/rule-based logic
- Logistic regression or a small tree model
- Full-text or BM25 search
- A human-operated workflow

A baseline reveals whether the AI component creates enough value to justify its complexity.

## Common failure modes

### Leakage

The input contains information unavailable at decision time, duplicates from another split, or labels encoded indirectly in metadata.

### Distribution shift

Production inputs differ by time, geography, user population, product changes, or adversarial behavior.

### Class imbalance

Rare cases disappear inside an attractive average metric. Choose thresholds and sampling strategies based on actual error costs.

### Goodhart's law

When a proxy metric becomes the target, teams can improve the score while harming the real objective. Pair automatic metrics with product outcomes and human review.

## Minimum mathematics

Understand conceptually and calculate small examples involving:

- Vectors, matrices, dot products, cosine similarity
- Probability, conditional probability, expectation, variance
- Distributions and sampling
- Derivatives, gradients, learning rates
- Cross-entropy and softmax
- Bias–variance tradeoffs

The goal is not symbolic virtuosity. It is the ability to diagnose experiments and read technical material without magical thinking.

## Exercises

1. Train a simple text classifier and compare it with a keyword baseline.
2. Create a deliberately leaked feature, observe the inflated score, and remove it.
3. Plot precision and recall across thresholds; select one using explicit error costs.
4. Build a 50-query search dataset and calculate recall@1, recall@5, and MRR.
5. Write a one-page model report describing data, metrics, limitations, and monitoring.

## Mastery check

You can:

- Select metrics from the product's error costs
- Detect obvious leakage and distribution mismatch
- Separate model, dataset, threshold, and product failures
- Explain why a benchmark score does not predict your application's quality
- Design a representative held-out evaluation set
