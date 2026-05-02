import requests
import access_key_vault
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = access_key_vault.get_secret()

class FootballAPI:

    def __init__(self, api_key):
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {"x-apisports-key": api_key}

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code != 200:
            print(f"❌ Erreur {endpoint} :", response.text)
            return None

        return response.json()


def save_to_file(data, filename):
    os.makedirs("input", exist_ok=True)  # crée le dossier si pas existant

    filepath = os.path.join("input", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Sauvegardé : {filepath}")


def main():
    api = FootballAPI(API_KEY)

    # 🔹 1. Countries
    countries = api.get("countries")
    if countries:
        save_to_file(countries, "countries.json")

    # 🔹 2. Fixtures (ex: Premier League 2023)
    fixtures = api.get("fixtures", {"league": 39, "season": 2023})
    if fixtures:
        save_to_file(fixtures, "fixtures.json")

    # 🔹 3. Standings
    standings = api.get("standings", {"league": 39, "season": 2023})
    if standings:
        save_to_file(standings, "standings.json")

    # 🔹 4. Statistics (ex: match ID)
    stats = api.get("fixtures/statistics", {"fixture": 1035037})
    if stats:
        save_to_file(stats, "statistics.json")


if __name__ == "__main__":
    main()