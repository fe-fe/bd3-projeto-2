from psycopg import connect, Connection
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

PG_USER = os.getenv("POSTGRES_USER")
PG_PW   = os.getenv("POSTGRES_PASSWORD")
PG_DB   = os.getenv("POSTGRES_DB")

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PW = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB")


def get_postgres_connection() -> Connection:
    return connect(
        host="localhost",
        port=5433,
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PW
    )


def get_mongo_connection():
    client = MongoClient(
        host="localhost",
        port=27018,
        username=MONGO_USER,
        password=MONGO_PW
    )
    return client[MONGO_DB]