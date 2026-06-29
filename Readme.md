## Installation

```bash
# Clone the repository
git clone https://github.com/doriath17/LineCounter.git
cd line-counter

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

## Example of using the line counter

```bash
# Run the line counter script
python line_counter.py -p '/path/to/directory' -ext '.py,.js' -e 'build,node_modules'
```

Or using the extended version:

```bash
python line_counter_extended.py --path '/path/to/directory' --extensions '.py,.js' --exclude-dirs 'build,node_modules'
```

You can also run the script with the `--help` flag to see all available options:

```bash
python line_counter.py --help
```
