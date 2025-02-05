import requests
import pytest

EXPECTED_JSON_SCHEMA = {
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

@pytest.mark.regression_tests
def test_get_companies():

    url = "https://fake-json-api.mock.beeceptor.com/companies"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        assert response.status_code == 200
    except requests.exceptions.Timeout:
        pytest.fail("Request timed out after 5 seconds")
    except requests.exceptions.TooManyRedirects:
        pytest.fail("Too many redirects, check the URL")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request error: {e}")

    try:
        response_json = response.json()
    except ValueError:
        pytest.fail("Invalid JSON response")

    assert isinstance(response_json, list), "Response is not a list"

    for company in response_json:
        for key, expected_type in EXPECTED_JSON_SCHEMA.items():
           
            assert key in company, f"Missing key '{key}' in company {company.get('name', 'unknown')}"         
            assert isinstance(company[key], expected_type), (
                f"Expected '{key}' to be of type {expected_type}, but got {type(company[key])}"
            )