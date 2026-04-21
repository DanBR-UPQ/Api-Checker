

def validate_status_code(response, expected_code):
    return response.status_code == expected_code

def validate_keys(response_json, expected_keys):
    return all(key in response_json for key in expected_keys)