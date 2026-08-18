import typer

from app.api import APIError, get_rates

app = typer.Typer(name = "currency", help="CLI for getting exchange rates.")

@app.command(name="rates")
def rates(base: str = typer.Option("EUR", "--base", "-b"), to: None | str = typer.Option(None, "--to", "-t")):
    targets = [target.strip() for target in to.split(",")] if to else None

    try:
        print(get_rates(base=base, targets=targets))

    except APIError():
        raise typer.exit()