from typing import Any

from rich.console import Console
from rich.table import Table

console = Console()

def display_rates(data: dict[str, Any]):
    base = data.get("base", "N/A")
    date = data.get("date", "N/A")
    rates = data.get("rates", "N/A")

    table = Table(title=f"Exchange Rates for 1 {base} {date}",
                  show_header=True,
                  header_style="bold magenta")

    table.add_column("Currency", style="cyan", justify="left")
    table.add_column("Exchange Rate", style="green", justify="right")

    for symbol, rate in sorted(rates.items()):
        table.add_row(symbol, f"{rate:.4f}")

    console.print(table)

def display_history():
    pass