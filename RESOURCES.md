# Primary learning resources

Use this as a reference shelf, not a sequential reading assignment. Build projects while consulting the relevant source.

## Software engineering

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [Docker getting started](https://docs.docker.com/get-started/)
- [Git documentation](https://git-scm.com/doc)

## Mathematics and machine learning

- [MIT OpenCourseWare Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [PyTorch tutorials](https://docs.pytorch.org/tutorials/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)

## Language models

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

## Retrieval and agents

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Agent Skills overview](https://agentskills.io/home)
- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Build skills in Codex](https://learn.chatgpt.com/docs/build-skills)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)

## Customization and serving

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/index)
- [vLLM documentation](https://docs.vllm.ai/)

## Evaluation, security, and governance

- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [MITRE ATLAS](https://atlas.mitre.org/)

## OpenAI implementation references

- [Model catalog](https://developers.openai.com/api/docs/models)
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices)

Model names, capabilities, prices, rate limits, and API fields change. Verify them in current official documentation before making production decisions.

## Reading papers effectively

For each paper:

1. State the problem and prior baseline.
2. Draw the method from memory.
3. Identify the training/evaluation data.
4. Read the ablations and failure cases.
5. Reproduce one small claim or mechanism.
6. Write what would have to be true for the result to matter in your product.

Do not confuse reproducing a benchmark result with operating a reliable product.
