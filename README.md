# CAD to OpenUSD

## Configuration

### uv
This repository uses [uv](https://docs.astral.sh/uv/) for dependency management. If you're new to uv, you don't need to know much more than the commands we use in the [build instructions](#How-to-Build). We recommend [installing uv](https://docs.astral.sh/uv/getting-started/installation/).


## Run the Converter

1. In the `./kit/`, run `./repo.bat build`
2. `uv run cad2usd`

This will convert the `nova_carter_full.step` at the root of the rop and output a USD file in the same location.

## Build Docs
1. `uv run sphinx-build -M html docs/ docs/_build/`
1. `uv run python -m http.server 8000 -d docs/_build/html/`
1. In a web browser, open `http://localhost:8000`