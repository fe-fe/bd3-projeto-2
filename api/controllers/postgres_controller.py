import time
from fastapi import APIRouter, Body
import docker
from load_postgres import load_postgres

from psycopg import connect
from psycopg.types.json import Json

from settings import PG_USER, PG_PW, PG_DB

import subprocess

router = APIRouter()
client = docker.from_env()

@router.post("/init/db")
def init_db():
    try:
        postgres = client.containers.get("postgres")
        if postgres.status != "running":
            postgres.start()

    except docker.errors.NotFound:
        subprocess.run(["docker-compose", "up", "postgres", "-d"], check=True)

@router.post("/load/db")
def load_db():
    try:
        load_postgres()
        return {"status": "success", "message": "Container pronto e PostgreSQL carregado"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.post("/off/db")
def off_db():
    try:
        subprocess.run(["docker-compose", "down", "-v"], check=True)
        return {"status": "success", "message": "docker compose down -v true"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/query/db/limit-5")
def query_db_limit_5():
    try:
        with connect(
            host="localhost",
            port=5433,
            dbname=PG_DB,
            user=PG_USER,
            password=PG_PW
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT document FROM restaurants LIMIT 5;")
                rows = cur.fetchall() 

                results = [row[0] for row in rows]

        return {"status": "success", "data": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.get("/query/db/limit-1000")
def query_db_limit_1000():
    try:
        with connect(
            host="localhost",
            port=5433,
            dbname=PG_DB,
            user=PG_USER,
            password=PG_PW
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT document FROM restaurants LIMIT 1000;")
                rows = cur.fetchall() 

                results = [row[0] for row in rows]

        return {"status": "success", "data": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.get("/query/db/limit/")
def query_db_limit(total: int):
    try:
        start_time = time.time() 
        with connect(
            host="localhost",
            port=5433,
            dbname=PG_DB,
            user=PG_USER,
            password=PG_PW
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT document FROM restaurants LIMIT %s;", (total,))
                rows = cur.fetchall() 

                results = [row[0] for row in rows]
                qtd = len(results)

        end_time = time.time() 
        elapsed_ms = (end_time - start_time) * 1000

        return {
            "status": "success",
            "quantidade": qtd,
            "tempo_ms": round(elapsed_ms, 2),
            "data": results
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
