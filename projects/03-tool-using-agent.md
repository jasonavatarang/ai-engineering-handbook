# Project 3: tool-using operations agent

## Goal

Build an agent that investigates an operational request using read-only tools and prepares a proposed action requiring approval.

## Example domain

Use a simulated order, incident, or account-management system. Do not connect consequential tools to production.

## Tools

- Search records
- Fetch one record
- Read policy
- Create a draft action
- Execute the approved action using an idempotency key

## Requirements

- Explicit goal, action boundaries, budgets, and stop states
- Narrow typed tool schemas
- Authorization outside the model
- Tool timeouts and bounded retries
- Durable state and trace IDs
- Preview plus approval for the final write
- Idempotent execution
- Malicious tool-output handling

## Evaluation

- Tool-choice accuracy
- Tool-argument accuracy
- Policy/evidence compliance
- Approval-boundary compliance
- Duplicate-action rate
- Recovery from dependency failures
- Final task success
- Calls, latency, and cost per success

## Failure experiments

- Tool timeout
- Malformed record
- Policy conflict
- Prompt injection in a record note
- User changes scope mid-run
- Same approval submitted twice
- Budget exhausted before completion

## Deliverables

State diagram, code, tests, traces, eval report, approval UX, threat model, incident exercise, and demo.
