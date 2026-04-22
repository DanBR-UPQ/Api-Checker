import requests
import logging

logging.basicConfig(
    filename="reports/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://jsonplaceholder.typicode.com"


def send_get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    logging.info(f"Sending GET request to {url}")
    
    response = requests.get(url)

    logging.info(f"Received status: {response.status_code}")
    return response