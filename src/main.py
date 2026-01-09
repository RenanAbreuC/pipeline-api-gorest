import requests 
import os 
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
URL = "https://gorest.co.in/public/v2"
PARAMS = {
    "page": 1}

response = requests.get(f"{URL}/users", headers=HEADERS, params=PARAMS)
print(f"Status Code: {response.status_code}")

all_data = response.json()
total_pages = int(response.headers["x-pagination-pages"])

for page in range(2, total_pages + 1):
    PARAMS["page"] = page
    response = requests.get(f"{URL}/users", headers=HEADERS, params=PARAMS)
    data = response.json()
    all_data.extend(data)

all_data = pd.DataFrame.from_dict(all_data, orient="columns")
print(all_data)

