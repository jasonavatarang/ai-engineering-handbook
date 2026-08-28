"""Minimal Responses API example.

Requires OPENAI_API_KEY. API calls can incur cost.
"""

from __future__ import annotations

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-terra")

    response = client.responses.create(
        model=model,
        instructions=(
            "Teach one concept at a time. State the mechanism, give one example, "
            "and end with one question that checks understanding."
        ),
        input="Explain why model output must be validated before software uses it.",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
