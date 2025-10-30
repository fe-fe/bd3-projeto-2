from settings import PG_USER, PG_PW, PG_DB
from psycopg.types.json import Json
from datetime import datetime
import psycopg
import json


connection_string = f"postgresql://{PG_USER}:{PG_PW}@localhost:5433/{PG_DB}"

start_time = datetime.now()

document_count = 0

try:
    with psycopg.connect(connection_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS restaurants (
                    document JSONB
                )
            """)
            connection.commit()

            with open("restaurants.jsonl", "r", encoding="utf-8") as dataset:
                for document_str in dataset:
                    document = json.loads(document_str)
                    cursor.execute("""
                        INSERT INTO restaurants (document)
                        VALUES (%s)
                    """, (Json(document),))
                    document_count += 1
                connection.commit()
except Exception as e:
    print(f"failed to load documents to postgres: {e}")
    quit()

end_time = datetime.now()
total_time = end_time - start_time
print(f"finished loading postgres: loaded {document_count} in {total_time}")