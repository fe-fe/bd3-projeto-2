from dotenv import load_dotenv
import os

load_dotenv()

PG_USER = os.getenv("POSTGRES_USER")
PG_PW   = os.getenv("POSTGRES_PASSWORD")
PG_DB   = os.getenv("POSTGRES_DB")