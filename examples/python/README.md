# Python examples

Small examples demonstrating model calls, structured outputs, tool loops, and offline evaluation without hiding the mechanics behind an agent framework.

## Setup

```bash
cd examples/python
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
export OPENAI_API_KEY="your-key"
```

Never commit `.env` or print an API key. API calls can incur cost. Confirm current models and parameters in the [official OpenAI documentation](https://developers.openai.com/api/docs/models).

## Run

```bash
python quickstart.py
python structured_extraction.py "Payment failed twice; customer C-1042 needs help."
python tool_loop.py
python eval_harness.py data/sample_eval.jsonl
python -m unittest discover -s tests
```

Set `OPENAI_MODEL` to a model available to your account. The examples default to `gpt-5.6-terra` as a balanced current model; availability can vary.

## Design lessons

- `quickstart.py`: smallest useful Responses API call
- `structured_extraction.py`: JSON Schema plus semantic validation
- `tool_loop.py`: the application executes and authorizes tools
- `eval_harness.py`: deterministic checks around variable model behavior
