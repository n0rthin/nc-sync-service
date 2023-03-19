import requests
import os

api_url = os.environ["MAIN_SERVICE_API_URL"]
api_token = os.environ["MAIN_SERVICE_API_TOKEN"]

def update_import_progress(sync_process_id, page_id):
  headers = {
    "x-access-token": api_token,
  }
  pload = {"syncProcessId": sync_process_id, "pageId": page_id}
  requests.post(f"{api_url}/api/sync/progress", data=pload, headers=headers)
