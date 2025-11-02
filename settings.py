from dotenv import load_dotenv
import os

load_dotenv()

PG_USER = os.getenv("POSTGRES_USER")
PG_PW   = os.getenv("POSTGRES_PASSWORD")
PG_DB   = os.getenv("POSTGRES_DB")


MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PW = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB")