# Curriculum map

## The competency model

A strong AI engineer combines six disciplines:

| Discipline | You should be able to... |
|---|---|
| Software engineering | Design APIs, data models, tests, queues, deployments, and failure handling |
| Machine learning | Reason about data quality, distributions, metrics, overfitting, and experimentation |
| Model interaction | Control prompts, context, structured outputs, tools, and multimodal inputs |
| System design | Build retrieval, workflow, agent, caching, and model-routing architectures |
| Quality and safety | Create evals, observability, security boundaries, and human escalation paths |
| Product judgment | Choose valuable problems, manage uncertainty, and communicate tradeoffs |

AI engineering is strongest at the intersections. Prompting without testing is fragile. ML knowledge without production engineering stays in notebooks. Infrastructure without product judgment makes expensive systems nobody needs.

## Learning order

### Phase 1: deterministic foundations

Study modules 1–3. Build normal software and learn enough ML/LLM mechanics to predict common failures.

Exit test: you can explain a model request from HTTP input through tokenization, inference, response parsing, logging, and user-visible output.

### Phase 2: model interfaces

Study modules 4–6. Learn prompts, context, schemas, tool calling, embeddings, and retrieval.

Exit test: you can build a document assistant that cites its evidence, abstains when evidence is insufficient, and passes a small retrieval-and-answer eval set.

### Phase 3: agentic systems

Study modules 7–9. Package reusable procedures as skills, then add dynamic decisions, tools, tracing, evals, and security controls.

Exit test: your agent chooses the correct tool, supplies valid arguments, respects approval boundaries, and exposes enough trace data to debug failures.

### Phase 4: production and professional practice

Study modules 10–12. Optimize deployment, reliability, cost, customization, product selection, and communication.

Exit test: you can defend an architecture using measured quality, latency, cost, safety, and operational tradeoffs.

## Depth guide

You do not need equal depth everywhere.

### Required for every AI engineer

- Python or TypeScript proficiency
- HTTP, JSON, databases, queues, containers, CI/CD, and cloud basics
- LLM limitations and context behavior
- Structured outputs and tool calling
- Agent Skill design and evaluation
- Retrieval fundamentals
- Task-specific evaluation
- Observability and incident debugging
- Prompt-injection and data-security defenses
- Cost and latency analysis

### Required for model-heavy roles

- Linear algebra, probability, optimization, PyTorch
- Training loops, data pipelines, fine-tuning, quantization
- GPU memory and distributed inference concepts
- Experiment tracking and dataset curation

### Required for product-heavy roles

- User research and workflow decomposition
- Human-in-the-loop interaction design
- Trust, transparency, and failure recovery
- Business metrics and adoption analysis

## What to postpone

Postpone these until a real project demands them:

- Multi-agent systems
- Fine-tuning
- Custom vector databases
- Training a transformer from scratch at scale
- Kubernetes
- Elaborate prompt-management platforms
- A new framework for every prototype

Learn the concepts early; add the infrastructure only when simpler approaches fail against measured requirements.

## The proof-of-skill standard

For every topic, produce four artifacts:

1. **Explanation:** describe the mechanism and tradeoffs in plain language.
2. **Implementation:** build the smallest useful version.
3. **Evaluation:** define cases and metrics before optimizing.
4. **Postmortem:** document one failure and the guardrail that prevents recurrence.

Use [SCORECARD.md](SCORECARD.md) to track your evidence.
