import requests
import access_key_vault, access_azure_storage
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = access_key_vault.get_secret()


BASE_URL = "https://v3.football.api-sports.io"

def get_data(api_key, endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    headers = {"x-apisports-key": api_key}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("API error:", response.text)
        return None

    return response.json()