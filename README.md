# currency-cli

Terminal application for querying live exchange rates, multi-currency conversions, and analyzing historical trends. Using the Frankfurter API and built with Typer and Rich.



## Installation & Global Setup

### Prerequisites
* Python 3.14 or higher
* Git

### 1. Local Package Setup

Clone the repository and install the project in editable mode within a virtual environment:

#### Clone repository
```bash
git clone https://github.com/llGustavsson/currency-cli.git
cd currency-cli
```

#### Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### Install in editable mode
```bash
pip install -e .
```

### 2. Access currency Globally

#### Go to repository folder
```bash
cd currency-cli
```

#### For Zsh users
```bash
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.zshrc
source ~/.zshrc
```

#### For Bash users
```bash
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc
```

#### Powershell
```bash
$env:Path += ";$PWD\.venv\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)
```

### 3. Commands & Usage Examples

#### 1. View Live Exchange Rates (rates)

Fetch live exchange rates relative to a base currency (defaults to EUR if omitted).

```bash
# View all available exchange rates relative to USD
currency rates --base USD

# Query specific target currencies
currency rates --base USD --to EUR,BRL,GBP

# Short Flags:
currency rates -b USD -t EUR,BRL
```

#### 2. Convert Currencies (convert)

Convert a specified monetary amount from a base currency into one or more target currencies.

```bash
# Convert 100 USD into all available targets
currency convert 100 --base USD

# Convert 250 EUR into specific currencies
currency convert 250 --base EUR --to USD,BRL,GBP

# Short Flags:
currency convert 250 -b EUR -t USD,BRL
```

#### 3. Historical Trends (history)

View rate fluctuations over predefined time intervals (7d, 14d, 1m, 3m).

```bash
# Track USD to EUR changes over the last 7 days
currency history --base USD --to EUR --period 7d

# Track EUR across multiple targets over 1 month
currency history --base EUR --to USD,BRL --period 1m

# Short Flags:
currency history -b USD -t EUR,BRL -p 14d
```

#### 4. Currencies available (currencies)

List all currencies available with ISO code and name.

```bash
# List all currencies
currency currencies
```