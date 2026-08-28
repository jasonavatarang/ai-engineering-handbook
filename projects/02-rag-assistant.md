# Project 2: evidence-grounded document assistant

## Goal

Answer questions over a controlled document collection with verifiable citations and correct abstention.

## Requirements

- Reproducible ingestion with stable IDs and metadata
- Authorization filtering before retrieval
- Baseline keyword retrieval
- Dense or hybrid retrieval comparison
- Optional reranking experiment
- Citations pointing to exact source locations
- Abstention when evidence is insufficient
- Handling of stale and conflicting documents

## Dataset

Create at least:

- 40 answerable questions with supporting chunks
- 10 unanswerable questions
- 10 ambiguous/conflicting questions
- Several exact identifiers, paraphrases, and multi-hop questions

## Evaluation

### Retrieval

- Recall@1 and recall@5
- Mean reciprocal rank
- Permission-filter correctness

### Answers

- Correctness
- Citation support and completeness
- Abstention precision/recall
- Unsupported-claim rate

## Failure experiments

- Delete the supporting chunk from the index
- Insert a malicious instruction in a retrieved document
- Add an obsolete policy with similar wording
- Ask a question belonging to another tenant
- Return oversized retrieval context

## Deliverables

Architecture, ingestion report, retrieval comparison, eval results, threat model, cost/latency analysis, demo, and postmortem.
