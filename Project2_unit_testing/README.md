# GSpread and Weather API Integration - Pytest Test Suite

This repository contains a pytest test suite for testing the upload of a json file from weatherAPI to a Google Sheet using the gspread library.

## Prerequisites

Before running the tests, ensure you have the following prerequisites installed:

- Python 3.11
- `pip` package manager
- Google Sheets API credentials JSON file (`Project_key`)
- Weather API key (set in your environment as `API_key`)
- Required Python libraries (dotenv, pytest, os , logging, requests )

## Test Structure

- `test_successful_worksheet_creation.py`: Tests related to successful worksheet creation.
- `test_connection_with_API.py`: Tests for the connection with the Weather API.
- `test_column_names.py`: Tests to check if the expected column names are present.
- `test_column_datatypes.py`: Tests to check the data types of columns.
- `test_error_handling.py`: Tests for error handling when invalid API data is provided.
- `test_data_validation.py`: Tests to check if data in certain columns falls within valid ranges.


## Running the Tests

You can run the tests using the following command in the file directory:

```bash
pytest
```
