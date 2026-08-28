from __future__ import annotations

import sys
import unittest
from pathlib import Path


EXAMPLE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXAMPLE_DIR))

from eval_harness import EvalCase, run_eval, score  # noqa: E402


class EvalHarnessTests(unittest.TestCase):
    def test_score_passes_required_and_absent_forbidden_text(self) -> None:
        case = EvalCase(
            case_id="one",
            input="hello",
            required_substrings=("answer",),
            forbidden_substrings=("secret",),
        )
        result = score(case, "The Answer is available.")
        self.assertTrue(result.passed)
        self.assertEqual(result.failures, ())

    def test_score_reports_all_failures(self) -> None:
        case = EvalCase(
            case_id="two",
            input="hello",
            required_substrings=("evidence",),
            forbidden_substrings=("guess",),
        )
        result = score(case, "I will guess.")
        self.assertFalse(result.passed)
        self.assertEqual(len(result.failures), 2)

    def test_run_eval_summarizes_cases(self) -> None:
        cases = [
            EvalCase(case_id="a", input="x", required_substrings=("ok",)),
            EvalCase(case_id="b", input="y", required_substrings=("missing",)),
        ]
        summary = run_eval(cases, lambda _: "ok")
        self.assertEqual(summary.passed, 1)
        self.assertEqual(summary.total, 2)
        self.assertEqual(summary.pass_rate, 0.5)


if __name__ == "__main__":
    unittest.main()
