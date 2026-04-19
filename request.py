import requests

class FootballAPI:
    """
    Client simple pour l'API-Football.

    Ressources principales utilisées dans ce projet :

    1. /countries
       - Liste des pays disponibles dans l'API

    2. /fixtures
       - Liste des matchs (scores, équipes, dates)

    3. /standings
       - Classement des équipes par ligue

    4. /fixtures/statistics
       - Statistiques détaillées d’un match
         (possession, tirs, corners, etc.)

    Exemple d'utilisation :
        api.get("fixtures", {"league": 39, "season": 2023})
    """

    def __init__(self, api_key):
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {"x-apisports-key": api_key}

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

api = FootballAPI("ee7b766a90b97e3efa97394d20e78a52")
countries = api.get("countries")
print(countries["response"])