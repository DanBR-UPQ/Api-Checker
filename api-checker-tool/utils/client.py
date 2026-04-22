import requests
import logging
import os

BASE_URL = "https://jsonplaceholder.typicode.com"


os.makedirs("reports", exist_ok=True)
logger = logging.getLogger("api_test_logger")
logger.setLevel(logging.INFO)


if not logger.handlers:
    file_handler = logging.FileHandler("reports/test.log")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def send_get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    logger.info(f"Received status: {response.status_code}")
    return response