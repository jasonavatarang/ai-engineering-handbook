# Project 1: structured support-ticket extractor

## Goal

Convert messy support messages into validated structured records that a normal application can route safely.

## Required fields

- `category`: billing, account, bug, feature_request, other
- `urgency`: low, normal, high
- `customer_id`: string or null
- `product`: string or null
- `summary`: concise factual text
- `requested_action`: string or null
- `missing_information`: array of strings
- `evidence`: input excerpts supporting important fields

## Requirements

- Strict schema and rejection of extra fields
- No guessing missing identifiers
- Semantic validation of category and urgency
- At least 30 labeled examples
- Fake provider for deterministic tests
- Live provider behind an interface
- Safe logging and configuration

## Evaluation

- Schema-valid rate
- Field-level accuracy
- Critical-field false-positive rate
- Missing-information recall
- p50/p95 latency
- Cost per valid extraction

## Failure cases

- Several requests in one message
- Conflicting urgency signals
- Prompt injection in quoted email content
- Missing customer identity
- Unsupported category
- Very long signature or thread history

## Stretch goals

- Human correction UI
- Active-learning queue for uncertain cases
- Small-versus-large model routing
- Multilingual inputs

## Deliverables

README, architecture, schema, code, tests, eval dataset, results table, failure analysis, and demo.
