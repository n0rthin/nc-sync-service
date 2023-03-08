from dotenv import load_dotenv
load_dotenv()
from rq import Queue
from src.worker import conn
from src.sync_page import sync_page
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

q = Queue(connection=conn)
