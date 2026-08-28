"""A tiny offline eval harness for deterministic response requirements."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable


@dataclass(frozen=True)
class EvalCase:
    case_id: str
    input: str
    required_substrings: tuple[str, ...] = ()
    forbidden_substrings: tuple[str, ...] = ()


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    passed: bool
    failures: tuple[str, ...]
    output: str


@dataclass(frozen=True)
class EvalSummary:
    passed: int
    total: int
    pass_rate: float
    results: tuple[CaseResult, ...]


def load_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            cases.append(
                EvalCase(
                    case_id=str(record["case_id"]),
                    input=str(record["input"]),
                    required_substrings=tuple(record.get("required_substrings", [])),
                    forbidden_substrings=tuple(record.get("forbidden_substrings", [])),
                )
            )
    if not cases:
        raise ValueError(f"No eval cases found in {path}")
    return cases


def score(case: EvalCase, output: str) -> CaseResult:
    normalized = output.casefold()
    failures: list[str] = []

    for required in case.required_substrings:
        if required.casefold() not in normalized:
            failures.append(f"missing required substring: {required}")

    for forbidden in case.forbidden_substrings:
        if forbidden.casefold() in normalized:
            failures.append(f"contained forbidden substring: {forbidden}")

    return CaseResult(
        case_id=case.case_id,
        passed=not failures,
        failures=tuple(failures),
        output=output,
    )


def run_eval(cases: Iterable[EvalCase], candidate: Callable[[str], str]) -> EvalSummary:
    results = tuple(score(case, candidate(case.input)) for case in cases)
    passed = sum(result.passed for result in results)
    total = len(results)
    if total == 0:
        raise ValueError("At least one eval case is required")
    return EvalSummary(
        passed=passed,
        total=total,
        pass_rate=passed / total,
        results=results,
    )


def demo_candidate(user_input: str) -> str:
    """Deterministic stand-in; replace with a recorded or live model adapter."""
    if "password" in user_input.casefold():
        return "Use the approved password-reset flow. Never share a password."
    return "I need more information before I can answer safely."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    args = parser.parse_args()
    summary = run_eval(load_cases(args.dataset), demo_candidate)
    print(json.dumps(asdict(summary), indent=2))
    raise SystemExit(0 if summary.pass_rate == 1.0 else 1)


if __name__ == "__main__":
    main()
