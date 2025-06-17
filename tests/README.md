# Testing the Python Fundamentals Documentation

This directory contains tests for the rendered HTML documentation in the `/docs` folder.

## Prerequisites

Before running the tests, make sure you have installed the required dependencies:

```bash
pip install -r requirements.txt
playwright install
```

## Running the Tests

To run all tests:

```bash
pytest
```

To run tests with detailed output:

```bash
pytest -v
```

To run a specific test file:

```bash
pytest tests/test_docs.py
```
