# 3. LLM foundations

## From text to output

A simplified language-model request works like this:

1. A tokenizer converts text into token IDs.
2. Embedding layers convert IDs into vectors.
3. Transformer blocks repeatedly mix contextual information using attention and feed-forward networks.
4. The model produces a probability distribution over the next token.
5. A decoding strategy selects a token.
6. The process repeats until a stop condition or output limit.

The model generates likely continuations; it does not query a perfect internal database of facts.

## Transformer concepts

### Attention

Each token produces query, key, and value representations. Similarity between queries and keys determines how value information is mixed. Multiple attention heads learn different relational patterns.

### Position

Because attention alone is order-agnostic, models encode token position. Long-context performance depends on model architecture and training, not only the advertised maximum window.

### Pretraining and post-training

- **Pretraining:** predicts text over large datasets and builds broad representations.
- **Instruction tuning:** teaches task-following formats and behavior.
- **Preference optimization:** shifts outputs toward desired human or model preferences.
- **Safety training:** reduces harmful or disallowed behavior.
- **Tool-use training:** teaches models to select and format calls.

## Tokens and context

Context is a scarce working-memory budget shared by:

- System/developer instructions
- User messages
- Retrieved documents
- Tool definitions and results
- Conversation history
- Model output and sometimes reasoning state

More context can reduce quality when it adds irrelevant, conflicting, stale, or adversarial information. Context engineering is selection, not accumulation.

## Embeddings

Embeddings map inputs to vectors where useful relationships can be measured. They support semantic search, clustering, classification features, deduplication, and recommendation.

Cosine similarity measures angular alignment, but relevance depends on the embedding model, corpus, chunking, query, and task. Always evaluate retrieval on your own data.

## Inference controls

Depending on the provider and model, you may control:

- Model family or snapshot
- Reasoning effort or execution mode
- Output-token limit and verbosity
- Sampling parameters
- Tool choice and tool budget
- Structured-output schema
- State persistence and caching

Treat defaults as configuration, not natural law. Pin important settings and measure changes.

## Fundamental limitations

### Hallucination

Fluent text can be unsupported or fabricated. Reduce impact using retrieval, tools, schemas, citations, verification, and abstention—not by asking the model to "never hallucinate."

### Nondeterminism

Identical-looking requests may vary due to sampling, infrastructure, model updates, or hidden state. Use evaluation distributions and operational tolerances rather than one golden transcript.

### Context sensitivity

Small changes in wording, order, examples, retrieved evidence, or tool descriptions can change behavior. Version the entire request assembly pipeline.

### Limited authority awareness

A model may propose or attempt actions beyond the user's intent unless authorization boundaries are explicit and enforced by tools.

## Model selection

Select by measured task requirements:

| Requirement | Likely direction |
|---|---|
| Complex planning or ambiguous reasoning | More capable model or higher reasoning effort |
| High-volume extraction/classification | Smaller model with strict schema |
| Low first-token latency | Fast model, streaming, shorter context |
| Sensitive local data | Approved hosted controls or self-hosted model |
| Large tool catalog | Tool filtering/search and strong tool descriptions |

Benchmark successful-task cost, not token price alone.

## Exercises

1. Tokenize the same paragraph with two tokenizers and compare token counts.
2. Embed 100 short documents and inspect nearest-neighbor successes and failures.
3. Run the same 20 prompts several times and categorize output variance.
4. Compare small/balanced/flagship models on quality, latency, and cost.
5. Explain a transformer to a product manager without using equations, then to an ML engineer with the relevant equations.

## Mastery check

You can explain:

- Why a context window is not a database
- Why embedding similarity is not guaranteed relevance
- Why higher reasoning effort is not automatically better
- How training, retrieval, tools, and prompting affect different parts of behavior
- Which limitations need software controls rather than prompt wording
