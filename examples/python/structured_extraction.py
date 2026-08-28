"""Extract a support ticket with JSON Schema and semantic validation.

Requires OPENAI_API_KEY. API calls can incur cost.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

from openai import OpenAI


TICKET_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "category": {
            "type": "string",
            "enum": ["billing", "account", "bug", "feature_request", "other"],
        },
        "urgency": {"type": "string", "enum": ["low", "normal", "high"]},
        "customer_id": {"type": ["string", "null"]},
        "summary": {"type": "string", "minLength": 1, "maxLength": 240},
        "missing_information": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": [
        "category",
        "urgency",
        "customer_id",
        "summary",
        "missing_information",
    ],
    "additionalProperties": False,
}


def validate_semantics(ticket: dict[str, Any]) -> None:
    """Apply deterministic domain checks after schema-constrained generation."""
    customer_id = ticket["customer_id"]
    if customer_id is not None and not customer_id.startswith("C-"):
        raise ValueError("customer_id must start with 'C-' when present")

    if ticket["urgency"] == "high" and not ticket["summary"].strip():
        raise ValueError("high-urgency tickets require a non-empty summary")


def extract_ticket(message: str) -> dict[str, Any]:
    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-terra")

    response = client.responses.create(
        model=model,
        instructions=(
            "Extract only facts supported by the message. Set customer_id to null "
            "when absent. Put information needed for safe routing in missing_information."
        ),
        input=message,
        text={
            "format": {
                "type": "json_schema",
                "name": "support_ticket",
                "strict": True,
                "schema": TICKET_SCHEMA,
            }
        },
    )

    ticket: dict[str, Any] = json.loads(response.output_text)
    validate_semantics(ticket)
    return ticket


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python structured_extraction.py 'support message'")
    print(json.dumps(extract_ticket(sys.argv[1]), indent=2))


if __name__ == "__main__":
    main()
