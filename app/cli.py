from datetime import UTC, datetime, timedelta

import typer

from app.api import APIError, get_currencies, get_history, get_rates
from app.ui import (
    display_all_currencies,
    display_conversion,
    display_history,
    display_rates,
)

app = typer.Typer(name = "currency", help="CLI for getting exchange rates.")


# DAYS PRESET AND PERIOD CALCULATION
PRESET_DAYS = {"7d": 7,
               "14d": 14,
               "1m": 30,
               "3m": 90,}

def calc_period(period: str):
    period_clean = period.lower().strip()
    today = datetime.now(UTC).date()

    if period_clean in PRESET_DAYS:
        days = PRESET_DAYS[period_clean]
        start_date = today - timedelta(days=days)

        return start_date.isoformat(), today.isoformat()


# CLI COMMAND FOR RATES
@app.command(name="rates")
def rates(base: str = typer.Option("EUR", "--base", "-b"), 
          target: None | str = typer.Option(None, "--to", "-t")):

    targets = [target.strip() for target in target.split(",")] if target else None

    try:
        data = get_rates(base=base, targets=targets)
        display_rates(data)

    except APIError:
        raise typer.Exit(code=1)


#CLI COMMAND FOR HISTORY
@app.command(name="history")
def history(base: str = typer.Option("EUR", "--base", "-b"),
            target: None | str = typer.Option(None, "--to", "-t"),
            period: str = typer.Option("7d", "--period", "-p")):

    start_date, end_date = calc_period(period)

    try:
        data = get_history(start_date=start_date, end_date=end_date, base=base, target=target)

        display_history(data)

    except APIError:
        raise typer.Exit(code=1)


# CLI COMMANDO FOR CURRENCIES
@app.command(name="currencies")
def currencies():
    data = get_currencies()

    try:
        display_all_currencies(data)

    except APIError:
        raise typer.Exit(code=1)

# CLI COMMAND FOR CONVERSION
@app.command(name="convert")
def convert(amount: float = typer.Argument(),
            base: str = typer.Option("EUR", "--base", "-b"), 
            target: None | str = typer.Option("USD", "--to", "-t")):

    targets = [target.strip() for target in target.split(",")] if target else None
    
    try:
        data = get_rates(base=base, targets=targets)

        data["conversions"] = {currency: (rate * amount) for currency, rate in data["rates"].items()}

        data["amount"] = amount

        display_conversion(data)

    except APIError:
        raise typer.Exit(code=1)
