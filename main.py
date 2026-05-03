import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

from api import get_data
from ingestion import ingest
from access_key_vault import get_secret

load_dotenv()

API_KEY = get_secret()

client_id = os.getenv("AZURE_CLIENT_ID")
tenant_id = os.getenv("AZURE_TENANT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
account_url = os.getenv("AZURE_STORAGE_URL")

container_name = "storagecommoncontainer"

credential = ClientSecretCredential(
    client_id=client_id,
    tenant_id=tenant_id,
    client_secret=client_secret
)

def run_pipeline():

    ingest(get_data, API_KEY, account_url, credential, container_name,
           "countries", filename="countries.json")

    ingest(get_data, API_KEY, account_url, credential, container_name,
           "fixtures", {"league": 39, "season": 2023}, "fixtures.json")

    ingest(get_data, API_KEY, account_url, credential, container_name,
           "standings", {"league": 39, "season": 2023}, "standings.json")

    ingest(get_data, API_KEY, account_url, credential, container_name,
           "fixtures/statistics", {"fixture": 1035037}, "stats.json")

    print("DONE and CLEAN ! Files uploaded")