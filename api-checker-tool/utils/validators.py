

def validate_status_code(response, expected_code):
    return response.status_code == expected_code

def validate_keys(response_json, expected_keys):
    return all(key in response_json for key in expected_keys)

def validate_response_time(response, max_ms):
    return response.elapsed.total_seconds() * 1000 < max_ms