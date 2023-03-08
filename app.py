from dotenv import load_dotenv
load_dotenv()
from rq import Queue
from worker import conn
from src.sync_page import sync_page
from src.auth import token_required
from flask import Flask, request

app = Flask(__name__)
q = Queue(connection=conn)

@app.route("/api/import-page", methods=["POST"])
@token_required
def index():
  request_data = request.get_json()
  sync_page_args = (request_data["import_process_id"], request_data["page_content"], request_data["page_id"], request_data["chat_id"])
  q.enqueue_call(
    sync_page, sync_page_args
  )
  return "Page import scheduled"

