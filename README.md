# currency-cli

Terminal application for querying live exchange rates, performing multi-currency conversions, and analyzing historical trends. Using the Frankfurter API and built with Typer and Rich.

---

## Installation & Global Setup

### Prerequisites
* Python 3.14 or higher
* Git

### 1. Local Package Setup

Clone the repository and install the project in editable mode within a virtual environment:

```bash
# 1. Clone repository
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

### 2. Access currency Globally (Without Activating .venv)
```bash
# Go to repository folder
cd currency-cli

# For Zsh users (default on macOS):
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.zshrc
source ~/.zshrc

# For Bash users:
echo "export PATH=\"$(pwd)/.venv/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

# For Powershell users:
$env:Path += ";$PWD\.venv\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)

