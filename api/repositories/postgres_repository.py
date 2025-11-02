from database import get_postgres_connection
from typing import Optional, Any


class PostgresRepository:

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
                        parameters.append(field)
                        query += "\nWHERE document->>%s IS NULL"
                    else:
                        parameters.extend([field, value])
                        query += "\nWHERE document->>%s = %s"

                if isinstance(limit, int):
                    parameters.append(limit)
                    query += "\nLIMIT %s"

                cursor.execute(query, tuple(parameters))
                return cursor.fetchall()
