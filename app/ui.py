from typing import Any

from rich.console import Console
from rich.table import Table

console = Console()


# UI FOR RATES
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


# UI FOR HISTORY
def display_history(data: dict[str, Any]):
    base = data.get("base", "N/A")
    rates_by_date = data.get("rates", {})

    sorted_dates = sorted(rates_by_date.keys())
    first_entry = rates_by_date[sorted_dates[0]]
    targets = sorted(first_entry.keys())

    table = Table(title=f"Historical Rates for 1 {base} ({sorted_dates[0]} 🠆 {sorted_dates[-1]})\n",
                  show_header=True,
                  header_style="bold magenta")

    table.add_column("Date", style="dim", justify="left")

    for target in targets:
        table.add_column(f"1 {base} 🠆 {target}", justify="right")

    prev_rates: dict[str, float] = {}
    symbol_series: dict[str, list[float]] = {t: [] for t in targets}

    for date_str in sorted_dates:
        row_cells = [date_str]
        current_rates = rates_by_date[date_str]

        for target in targets:
            rate = current_rates.get(target)
            symbol_series[target].append(rate)

            if target in prev_rates:
                prev = prev_rates[target]

                if prev > 0:
                    pct_change = ((rate - prev) / prev) * 100

                else:
                    pct_change = 0.0

                if rate > prev:
                    cell_text = f"[bold green]🠵 {rate:.4f} (+{pct_change:.2f}%)[/bold green]"

                elif rate < prev:
                    cell_text = f"[bold red]🠷 {rate:.4f} (+{pct_change:.2f}%)[/bold red]"

            else:
                cell_text = f"{rate:.4f}"

            prev_rates[target] = rate
            row_cells.append(cell_text)

        table.add_row(*row_cells)

    table.add_section()

    summary_cells = ["[bold magenta]Summary[/bold magenta]"]
    for target in targets:
        series = symbol_series[target]

        low = min(series)
        high = max(series)
        first_rate = series[0]
        last_rate = series[-1]

        if first_rate > 0:
            total_return = ((last_rate - first_rate) / first_rate) * 100

        else:
            total_return = 0.0

        if total_return > 0:
            return_str = f"[bold green]+{total_return:.2f}%[/bold green]"

        elif total_return < 0:
            return_str = f"[bold red]+{total_return:.2f}%[/bold red]"

        else:
            return_str = "[dim]0.00%[/dim]"

        summary_text = (f"[dim] Low:[/dim] {low:.4f}\n"
                        f"[dim] High:[/dim] {high:.4f}\n"
                        f"[dim] Total Return:[/dim] {return_str}\n")

        summary_cells.append(summary_text)

    table.add_row(*summary_cells)

    console.print(table)


# UI FOR CURRENCIES LIST
def display_all_currencies(data: dict[str, str ]):

    table = Table(title="All Currencies Available",
                  show_header=True,
                  header_style="bold magenta")

    table.add_column("ISO code", style="cyan", justify="left")
    table.add_column("Currency Name", style="cyan", justify="right")

    for key, value in data.items():
        table.add_row(key, value)

    console.print(table)
        

# UI FOR CONVERT
def display_conversion(data: dict[str, Any ]):
    base = data.get("base", "N/A")
    date = data.get("date", "N/A")
    amount = data.get("amount", "N/A")

    table = Table(title=f"Conversion for {amount} {base} {date}",
                  show_header=True,
                  header_style="bold magenta")

    table.add_column("Target", style="cyan", justify="left")
    table.add_column("Converted Amount", style="green", justify="right")

    for currency, converted_value in data["conversions"].items():
        table.add_row(currency, f"{converted_value:.2f}")

    console.print(table)