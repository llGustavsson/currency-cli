from datetime import datetime, timedelta, timezone

import typer

from app.api import APIError, get_history, get_rates
from app.ui import display_history, display_rates

app = typer.Typer(name = "currency", help="CLI for getting exchange rates.")

PRESET_DAYS = {"7d": 7,
               "14d": 14,
               "1m": 30,
               "3m": 90,}

def calc_period(period: str):
    period_clean = period.lower().strip()
    today = datetime.now(timezone.utc).date()

    if period_clean in PRESET_DAYS:
        days = PRESET_DAYS[period_clean]
        start_date = today - timedelta(days=days)

        return start_date.isoformat(), today.isoformat()

@app.command(name="rates")
def rates(base: str = typer.Option("EUR", "--base", "-b"), 
          to: None | str = typer.Option(None, "--to", "-t")):

    targets = [target.strip() for target in to.split(",")] if to else None

    try:
        data = get_rates(base=base, targets=targets)
        display_rates(data)

    except APIError():
        raise typer.Exit()

@app.command(name="history")
def history(base: str = typer.Option("EUR", "--base", "-b"),
            to: None | str = typer.Option(None, "--to", "-t"),
            period: str = typer.Option("7d", "--period", "-p")):

    start_date, end_date = calc_period(period)

    try:
        data = get_history(start_date=start_date, end_date=end_date, base=base, target=to)

        display_history(data)

    except APIError:
        raise typer.Exit()

@app.command(name="currencies")
def currencies():
    pass