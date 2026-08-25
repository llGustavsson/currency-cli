from unittest.mock import patch

from typer.testing import CliRunner

from app.cli import app

runner = CliRunner()


# TESTS FOR RATES COMMAND
@patch("app.cli.get_rates")
def test_rates_command(mock_get_rates):
    mock_get_rates.return_value = {"base": "USD",
                                   "date": "2026-08-24",
                                   "rates": {"EUR": 0.88}}

result = runner.invoke(app, ["rates", "--base", "USD"])
assert result.exit_code == 0

def test_rates_command_fail():
    result = runner.invoke(app, ["rates", "--flag-invalid", "USD"])

    assert result.exit_code == 2


# TESTS FOR HISTORY COMMAND
@patch("app.cli.get_history")
def test_history_command(mock_get_history):
    mock_get_history.return_value = {"base": "USD",
                                     "rates": {"2026-08-17": {"EUR": 0.88}}}

    result = runner.invoke(app, ["history", "--base", "USD", "--to", "EUR", "--period", "7d"])

    assert result.exit_code == 0


# TESTS FOR CONVERT COMMAND
@patch("app.cli.get_rates")
def test_converter_command(mock_get_rates):
    mock_get_rates.return_value = {"amount": 1.0,
                                   "base": "EUR",
                                   "date": "2026-08-25",
                                   "rates": {"USD": 1.17, "BRL": 6.06}}

    result = runner.invoke(app, ["convert", "100", "--base", "EUR", "--to", "USD,BRL"])

    assert result.exit_code == 0