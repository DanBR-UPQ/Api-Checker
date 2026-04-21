import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

    
def send_get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    return response