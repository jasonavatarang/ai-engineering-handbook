# 9. Safety, security, and governance

AI security is normal application security plus new trust-boundary failures created by model-generated actions and untrusted context.

## Threat-model assets

Protect:

- User and tenant data
- Credentials and signing keys
- System/developer instructions
- Proprietary prompts, datasets, and model artifacts
- Tool permissions and external accounts
- Production infrastructure
- Logs and traces
- User trust and business reputation

## Primary threats

### Prompt injection

Untrusted text attempts to alter instructions, reveal data, or cause tool use. It may arrive directly from a user or indirectly through webpages, emails, documents, tickets, or tool output.

Controls:

- Treat retrieved/tool content as data, never policy
- Keep instructions and untrusted content structurally separated
- Minimize tools and permissions
- Require authorization outside the model
- Validate destinations and arguments
- Add human approval for consequential actions
- Test realistic attacks continuously

There is no universal “ignore prompt injection” sentence that solves this.

### Excessive agency

The agent can take more actions than the use case requires.

Controls:

- Read-only by default
- Narrow task-level tools
- Time, call, token, and monetary budgets
- Sandbox and network allowlists
- Approval gates and previews
- Idempotency and undo paths

### Data leakage

Private information reaches another tenant, an unauthorized tool, logs, training data, or the response.

Controls:

- Tenant filters before retrieval
- Field-level authorization
- Data minimization and redaction
- Retention and deletion policies
- Encryption and secret management
- DLP checks where justified
- Access-controlled traces

### Insecure output handling

Generated code, HTML, SQL, URLs, commands, or Markdown is executed without validation.

Controls:

- Treat output as untrusted input
- Use parameterized queries and safe renderers
- Validate URLs and destinations
- Sandbox code execution
- Escape output for its destination context
- Use schemas/grammars and allowlists

### Supply-chain risk

Models, datasets, packages, MCP servers, plugins, and containers may be compromised or unexpectedly updated.

Controls:

- Pin and verify dependencies
- Review permissions and provenance
- Scan artifacts
- Restrict egress
- Maintain an inventory and rollback path

## Guardrail stack

Use multiple independent layers:

1. Product policy and UX boundaries
2. Prompt-level behavior guidance
3. Input classification or moderation where appropriate
4. Authentication and authorization
5. Tool allowlists and schemas
6. Sandbox, network, filesystem, and secret isolation
7. Output validation and domain checks
8. Approval for consequential actions
9. Monitoring, rate limits, abuse detection, and incident response

Prompt instructions are the softest layer; enforced permissions are stronger.

## Privacy questions

Before shipping, document:

- What data enters each provider or tool?
- Where is it processed and stored?
- How long is it retained?
- Is it used for training?
- Who can inspect traces?
- How are deletion requests handled?
- Which regions or regulations apply?
- Can the feature work with less data?

Verify contractual and provider-specific answers with current documentation.

## Governance artifacts

Maintain:

- Use-case and risk classification
- Data-flow diagram
- Threat model
- Model/system card
- Eval report and known limitations
- Approval matrix
- Dependency/provider inventory
- Incident playbook and owners
- Change log for prompts, models, tools, and datasets

## Exercises

1. Complete [the threat-model template](../templates/threat-model.md) for a RAG assistant.
2. Create direct and indirect prompt-injection tests.
3. Demonstrate that a cross-tenant document cannot be retrieved.
4. Add approval and idempotency to a consequential tool.
5. Run an incident tabletop for leaked credentials and malicious tool output.

## Mastery check

You can identify trust boundaries, enforce least privilege outside the model, prove tenant isolation, and explain residual risk honestly.
