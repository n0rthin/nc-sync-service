from dotenv import load_dotenv
load_dotenv()
from rq import Queue
from src.worker import conn
from src.sync_page import sync_page
from src.auth import token_required
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/import-page", methods=["POST"])
@token_required
def index():
  request_data = request.get_json()
  import_process_id, page_content, page_id, chat_id = request_data["import_process_id"], request_data["page_content"], request_data["page_id"], request_data["chat_id"]
  return f"Params: {import_process_id}, {page_content}, {page_id}, {chat_id}"

q = Queue(connection=conn)
