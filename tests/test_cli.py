from unittest.mock import patch

from typer.testing import CliRunner

from app.cli import app

runner = CliRunner()

@patch("app.cli.get_rates")
def test_rates_flag(mock_get_rates):
    mock_get_rates.return_value = {"base": "USD",
                                   "date": "2026-08-24",
                                   "rates": {"EUR": 0.88}}

result = runner.invoke(app, ["rates", "--base", "USD"])
assert result.exit_code == 0

def test_rates_command_fail():
    result = runner.invoke(app, ["rates", "--flag-invalid", "USD"])

    assert result.exit_code == 2


