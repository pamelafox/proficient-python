# Testing the course

This directory contains tests for the rendered HTML course content in the `build` folder.

## Prerequisites

Before running the tests, make sure you have installed the required dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Then build the course content:

```bash
./build.sh
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