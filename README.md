# Project Title
API Testing with Pytest

* Python 3.12.3
* pytest 8.3.4
* requests 2.32.3



## Description
This project demonstrates how to use pytest and requests to test an API. The test validates the response from an API endpoint to ensure it meets an expected format.

Prerequisites
Ensure you have Python 3.12.3 and the required dependencies:

## Installation
| `pip install -r requirements.txt` |

### Features
Code Explanation

test_api.py
API Request: The test sends a GET request to https://fake-json-api.mock.beeceptor.com/companies.
Validation: It checks:


Status code: 200.
The response is a list.
Each company contains the expected fields with correct data types.
Expected JSON Schema
The API should return a list of companies with fields like:

{
    "id": int,
    "name": str,
    "address": str,
    "zip": str,
    "country": str,
    "employeeCount": int,
    "industry": str,
    "marketCap": int,
    "domain": str,
    "logo": str,
    "ceoName": str
}


Run the test:
| `pytest test_api.py -v` |