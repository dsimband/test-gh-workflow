# test-gh-workflow

This repository demonstrates Codex workflow automation including automatic pull request generation.


## Agent Application

This repository now includes a minimal agent application implemented in Python.
The source code lives under `src/agent_app/` and can be run via:

```bash
python -m agent_app --name YOUR_NAME
```

Unit tests are located in the `tests/` directory and can be executed with:

```bash
pytest
```

## Sample Module

The `src/sample_module.py` file contains simple arithmetic functions used in the
test suite. It currently provides:

* `add(a, b)` – return the sum of two integers.
* `subtract(a, b)` – return the difference of two integers.
* `multiply(a, b)` – return the product of two integers.
* `divide(a, b)` – return the quotient of two integers, raising ``ValueError`` when dividing by zero.

## Continuous Integration

Automated tests run via GitHub Actions whenever commits are pushed or pull requests are opened against `main`. The workflow is defined in `.github/workflows/ci.yml` and installs dependencies, runs `pre-commit`, and executes the test suite.

