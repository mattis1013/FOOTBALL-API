from datetime import datetime
from access_azure_storage import upload_blob_from_memory

def ingest(api_func, api_key, account_url, credential, container_name,
           endpoint, params=None, filename=None):

    data = api_func(api_key, endpoint, params)

    if not data:
        return None

    if not filename:
        filename = f"{endpoint}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    upload_blob_from_memory(
        account_url,
        credential,
        container_name,
        data,
        filename
    )

    return filename