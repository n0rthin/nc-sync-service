import requests
import os

api_url = os.environ["MAIN_SERVICE_API_URL"]
api_token = os.environ["MAIN_SERVICE_API_TOKEN"]

def update_import_progress(import_process_id, page_id):
  headers = {
    "x-access-token": api_token,
  }
  pload = {"import_process_id": import_process_id, "page_id": page_id}
  requests.patch(f"{api_url}/api/import/progress", data=pload, headers=headers)
