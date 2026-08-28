# 4. Prompt and context engineering

Prompt engineering specifies the task. Context engineering assembles the information and capabilities needed to complete it. Production quality depends more on the second.

## The task contract

Use this structure for nontrivial work:

```text
Role and operating context:
[What function the model performs.]

Goal:
[Concrete user-visible outcome.]

Success criteria:
- [Observable requirement]
- [Observable requirement]

Constraints:
[Policy, evidence, compatibility, side-effect, and scope limits.]

Available context and tools:
[What evidence exists and what each tool is for.]

Output:
[Required content, structure, and length.]

Stop rules:
[When to retry, abstain, ask, escalate, or finish.]
```

Describe the destination. Prescribe a step-by-step path only when the path is a real business, safety, or technical requirement.

## Instruction hierarchy

Separate instruction classes:

- **Application contract:** stable behavior, safety, authority, and response rules
- **Task:** the current user outcome
- **Context:** evidence that informs the task but cannot rewrite the contract
- **Examples:** demonstrations of desired decisions or formats
- **Tool definitions:** capability, arguments, side effects, and error behavior

Never concatenate untrusted documents into the instruction layer.

## Context selection

For each piece of context, ask:

1. Is it relevant to the decision?
2. Is it current and authoritative?
3. Does the model need the raw content or a verified summary?
4. Could it conflict with stronger instructions?
5. Does it contain untrusted instructions or private data?
6. Is the token cost justified?

Prefer compact identifiers, structured fields, and retrieved excerpts over entire histories.

## Examples and few-shot prompting

Examples are valuable when they encode:

- A decision boundary difficult to describe abstractly
- A product-specific tone or format
- Rare edge cases
- Correct tool selection
- Scoring anchors for an evaluator

Use diverse examples. Avoid examples that accidentally teach irrelevant names, exact phrasing, or one narrow input shape.

## Prompt anti-patterns

- Repeating the same rule in several sections
- Large lists of `ALWAYS` and `NEVER` for non-invariants
- Asking for hidden chain-of-thought instead of observable evidence
- Mixing policies, examples, user data, and retrieved text without delimiters
- Including every available tool on every request
- Using prompt prose where JSON Schema or code validation is possible
- Optimizing against one impressive example
- Adding instructions without removing obsolete ones

## Context lifecycle

Long-running systems need explicit memory policy:

- Preserve stable user preferences only with permission.
- Preserve completed actions, decisions, IDs, and unresolved blockers.
- Expire stale operational context.
- Summarize or compact history before it becomes noisy.
- Never treat model-generated summaries as authoritative records without validation.

## Prompt optimization loop

1. Create representative eval cases before editing.
2. Record the current prompt, model, settings, tools, and context builder.
3. Classify failures: instruction, context, retrieval, tool, model, or validator.
4. Change one coherent variable.
5. Run the same evals and inspect regressions.
6. Keep the change only if the overall quality/cost/latency tradeoff improves.
7. Add new production failures to the suite.

Official OpenAI guidance similarly recommends lean, outcome-first prompts, relevant tool sets, explicit approval boundaries, and eval-based iteration: [model guidance](https://developers.openai.com/api/docs/guides/latest-model).

## Exercises

1. Rewrite a 1,000-word system prompt into a 200-word task contract and compare it on the same eval set.
2. Create five examples that teach a subtle decision boundary; test with and without them.
3. Inject an irrelevant long document and measure the quality and latency effect.
4. Build a context manifest recording source, timestamp, authority, and token count.
5. Create an adversarial document that says to ignore previous instructions; verify it is treated as data.

## Mastery check

You can:

- Place each instruction in the correct layer
- Explain why more context may reduce quality
- Define observable success and stopping conditions
- Diagnose a failure before changing the prompt
- Demonstrate improvement over a representative dataset
