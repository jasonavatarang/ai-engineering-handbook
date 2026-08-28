# Repository guidance

## Purpose

Maintain a practical, vendor-neutral AI engineering curriculum. Optimize for technical accuracy, clear mental models, runnable examples, and evidence-driven practice.

## Writing

- Lead with the mechanism or decision.
- Distinguish stable principles from time-sensitive product details.
- Prefer primary sources for technical claims.
- Define unfamiliar terms or add them to `GLOSSARY.md`.
- Every module should include exercises and mastery checks.

## Code

- Examples must be typed, small, and readable without a framework.
- Treat model output and tool output as untrusted input.
- Keep credentials in environment variables and never log them.
- Run `python -m compileall examples/python` and the tests before committing.

## Definition of done

- Internal Markdown links resolve.
- Python examples compile.
- Deterministic tests pass.
- No secrets or generated caches are committed.
