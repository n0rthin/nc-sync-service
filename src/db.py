import psycopg2
import os

conn = psycopg2.connect(os.environ["HEROKU_POSTGRESQL_COPPER_URL"], sslmode='require')
cursor = conn.cursor()