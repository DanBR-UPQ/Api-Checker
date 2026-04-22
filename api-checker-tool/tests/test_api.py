import json
import pytest

from utils.client import send_get
from utils.validators import validate_status_code, validate_keys, validate_response_time


with open("config/test_cases.json") as f:
    test_cases = json.load(f)



@pytest.mark.parametrize("case", test_cases, ids=[c["name"] for c in test_cases])
def test_api_cases(case):
    response = send_get(case["endpoint"])

    assert validate_status_code(response, case["expected_status"])

    if "expected_keys" in case:
        data = response.json()
        assert validate_keys(data, case["expected_keys"])
    
    if "max_response_time" in case:
        assert validate_response_time(response, case["max_response_time"])