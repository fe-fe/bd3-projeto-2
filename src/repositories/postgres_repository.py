from database import get_postgres_connection
from typing import Optional, Any
import json


class PostgresRepository:

    @staticmethod
    def _build_nested_path(field: str, value: Any) -> dict:
        keys = field.split(".")
        nested_dict = {keys[-1]: value}
        for key in reversed(keys[0:-1]):
            nested_dict = {key: nested_dict}
        return nested_dict


    @staticmethod
    def find_with_parameters(
        field: str = None, 
        value: Any = None, 
        limit: int = None
    ) -> Optional[list[dict]]:
        with get_postgres_connection() as con:
            with con.cursor() as cursor:
                query = "SELECT document FROM restaurants"
                parameters = []

                if isinstance(field, str):
                    if value is None:
                        query += "\nWHERE (document #>> %s) IS NULL"
                        parameters.append(field.split("."))
                    else:
                        query += "\nWHERE document @> %s::jsonb"
                        json_path = PostgresRepository._build_nested_path(field, value)
                        parameters.append(json.dumps(json_path))

                if isinstance(limit, int):
                    parameters.append(limit)
                    query += "\nLIMIT %s"

                cursor.execute(query, tuple(parameters))
                return cursor.fetchall()
