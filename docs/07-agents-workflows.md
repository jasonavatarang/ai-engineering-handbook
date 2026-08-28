# 7. Agents and workflows

Use the least nondeterministic architecture that solves the problem.

## Architecture ladder

1. **Deterministic code:** use when rules are known.
2. **Single model call:** use for one bounded transformation or judgment.
3. **Workflow:** use when the steps and transitions are mostly known.
4. **Single agent:** use when tool choice or investigation path must remain flexible.
5. **Multi-agent system:** use only when specialized contexts or parallel work measurably improve results.

Every step upward adds more failure modes, latency, cost, and debugging difficulty.

## Workflow versus agent

Use a workflow when you can draw the state machine in advance:

```text
receive -> classify -> retrieve -> draft -> validate -> respond
```

Use an agent when the next useful action depends on information discovered during execution:

```text
inspect -> form hypothesis -> choose tool -> observe -> revise -> verify
```

Many reliable products use a workflow containing one or two bounded agentic stages.

## Agent contract

Define:

- Goal and success criteria
- Allowed data and tools
- Action and approval boundaries
- Evidence requirements
- Tool-call, token, time, and retry budgets
- Completion, partial-success, blocked, and failure states
- State that must survive retries or compaction

Persistence is not the same as unlimited autonomy.

## State

Track durable structured state outside prose history:

- Task ID and status
- User-approved scope
- Completed actions and idempotency keys
- Retrieved evidence IDs
- Current plan or hypotheses
- Tool results and errors
- Remaining budget
- Blockers and requested input

The conversation can explain state; it should not be the only state store.

## Multi-agent decision

Multi-agent systems help when work decomposes into genuinely independent or specialized contexts, such as parallel repository audits or research lanes. They are a poor default when agents share most context, perform the same tools, or need frequent coordination.

Evaluate:

- Routing/handoff accuracy
- Duplicate or contradictory work
- Context lost at handoffs
- Total tokens and latency
- Final result versus a strong single-agent baseline

OpenAI's evaluation guidance recommends letting eval results drive a move to multi-agent architecture rather than starting there: [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Failure handling

Classify errors:

- Transient dependency failure → bounded retry
- Invalid tool arguments → repair once using validation feedback
- Permission denial → stop or request approval
- Missing evidence → retrieve or abstain
- Conflicting evidence → surface conflict or escalate
- Budget exhausted → return partial state and blocker
- Repeated identical failure → stop, do not loop

## Human-in-the-loop design

Ask for approval at the decision boundary, with:

- Proposed action
- Target and scope
- Evidence and rationale
- Expected effect
- Reversibility
- Exact alternatives

Do not ask humans to approve vague intentions such as “continue working.”

## Exercises

1. Implement the same support workflow as deterministic code and as an agent; compare results.
2. Add hard budgets and show the agent terminating cleanly.
3. Persist state, interrupt a run, and resume without repeating a write.
4. Test topic changes and handoffs in a two-agent design.
5. Design an approval screen for an external write.

## Mastery check

You can justify why each nondeterministic decision must be model-driven and explain how the system stops, recovers, and avoids duplicate side effects.
