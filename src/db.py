import psycopg2
import os

conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')
cursor = conn.cursor()