# currency-cli

Terminal application for querying live exchange rates, multi-currency conversions, and analyzing historical trends. Using the Frankfurter API and built with Typer and Rich.



## Installation & Global Setup

### Prerequisites
* Python 3.14 or higher
* Git

### 1. Local Package Setup

Clone the repository and install the project in editable mode within a virtual environment:

#### 1. Clone repository
```bash
git clone https://github.com/llGustavsson/currency-cli.git
cd currency-cli
```
```bash
# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
```bash
# 3. Install in editable mode
pip install -e .
```

### 2. Access currency Globally
```bash
# Go to repository folder
cd currency-cli
```
```bash
# For Zsh users (default on macOS):
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.zshrc
source ~/.zshrc
```
```bash
# For Bash users:
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc
```

#### Powershell
```bash
# For Powershell users:
$env:Path += ";$PWD\.venv\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)
```

### Features & Usage Examples
1. View Live Exchange Rates (rates)

Fetch live exchange rates relative to a base currency (defaults to EUR if omitted).
Bash

# View all available exchange rates relative to USD
currency rates --base USD

# Query specific target currencies
currency rates --base USD --to EUR,BRL,GBP

Short Flags:
Bash

currency rates -b USD -t EUR,BRL

2. Convert Currencies (convert)

Convert a specified monetary amount from a base currency into one or more target currencies.
Bash

# Convert 100 USD into all available targets
currency convert 100 --base USD

# Convert 250 EUR into specific currencies
currency convert 250 --base EUR --to USD,BRL,GBP

Short Flags:
Bash

currency convert 250 -b EUR -t USD,BRL

3. Historical Trends (history)

View rate fluctuations over predefined time intervals (7d, 14d, 1m, 3m).
Bash

# Track USD to EUR changes over the last 7 days
currency history --base USD --to EUR --period 7d

# Track EUR across multiple targets over 1 month
currency history --base EUR --to USD,BRL --period 1m

Short Flags:
Bash

currency history -b USD -t EUR,BRL -p 14d