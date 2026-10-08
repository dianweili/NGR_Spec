import json

import pytest

from ngr.extract.backend import CliResult
from ngr.extract.budget import Budget, BudgetExhausted


def test_check_passes_under_limit():
    budget = Budget(max_calls=2)
    budget.check()
    budget.spend(CliResult("x", {"output_tokens": 5}, 0.01))
    budget.check()


def test_check_raises_when_exhausted():
    budget = Budget(max_calls=1)
    budget.check()
    budget.spend(CliResult("x", {}, 0.01))
    with pytest.raises(BudgetExhausted):
        budget.check()


def test_totals_accumulate():
    budget = Budget(max_calls=5)
    budget.spend(CliResult("x", {"output_tokens": 5}, 0.01))
    budget.spend(CliResult("y", {"output_tokens": 7}, 0.02))
    assert budget.calls == 2
    assert round(budget.cost_usd, 4) == 0.03


def test_log_appends_jsonl(tmp_path):
    budget = Budget(max_calls=5)
    budget.spend(CliResult("x", {"output_tokens": 5}, 0.01), task="summary")
    path = tmp_path / "usage.jsonl"
    budget.log(path)
    budget.spend(CliResult("y", {}, 0.02), task="summary")
    budget.log(path)
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["task"] == "summary"
