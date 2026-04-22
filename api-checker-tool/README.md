# ApiCheck - API Test Automation Framework

Lightweight API testing tool built with Python and pytest to validate endpoints using configurable test cases

Designed to demonstrate modular test architecture, configurable test execution, and CI-compatible reporting


## Features

- Config-driven test cases (JSON)
- Status code validation
- Response structure validation
- Response time validation
- Logging of requests and responses
- JUnit XML reporting (CI-compatible)

## How to Run

```
pip install -r requirements.txt
python run_tests.py
```

## Architecture

```
├── api-checker-tool
│   ├── config
│   │   └── test_cases.json
│   ├── reports
│   │   └── results.xml
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_api.py
│   ├── utils
│   │   ├── client.py
│   │   └── validators.py
│   ├── README.md
│   └── run_tests.py
├── venv
└── requirements.txt
```

## Example Test Case

```
{
  "endpoint": "/posts/1",
  "expected_status": 200,
  "expected_keys": ["userId", "id"],
  "max_response_time": 500
}
```


## Output

```
pytest -k "Post_valido_1" -v 
```

The framework generates:

- Console test results (pass/fail summary)
- JUnit XML report (`reports/results.xml`)
- Execution logs (`reports/test.log`) with request/response tracing


```
===================================================================== test session starts =====================================================================
platform win32 -- Python 3.13.3, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\danie\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: D:\Projects\Api-Checker\api-checker-tool
collected 5 items / 4 deselected / 1 selected                                                                                                                  

tests/test_api.py::test_api_cases[Post_valido_1] PASSED                                                                                                  [100%]

=============================================================== 1 passed, 4 deselected in 0.86s ===============================================================
```

## Failure Example

If an endpoint returns an unexpected status code or exceeds the response time threshold, the test will fail with a descriptive assertion error