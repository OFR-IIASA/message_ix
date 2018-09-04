# Overview

This folder is used for generating a database of testable scenario
instances. You must have the following envrionment variables set to execute all
aspects:

- `MESSAGE_IX_CI_USER`
- `MESSAGE_IX_CI_PW`

# Generate the Database

To generate and upload the database execute the follow files in order:

1. `fetch_scenarios.py`
2. `make_scenario_db.py`
3. `upload_scenario_db.sh`

# Tests running on CI

These tests are designed to run on CI. To do so, one must download the test
database, generate the test file, and run `pytest`.

Downloading the database is done with `download_scenario_db.py`.

Generating the test file is done with `generate_test_file.py`.

You can then run the test with

```
pytest test_scenarios.py
```
