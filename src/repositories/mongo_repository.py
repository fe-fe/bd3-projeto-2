from database import get_mongo_connection
from typing import Optional, Any


class MongoRepository:

    @staticmethod
    def find_with_parameters(
        field: str = None, 
        value: Any = None, 
        limit: int = None
    ) -> Optional[list[dict]]:
        db = get_mongo_connection()
        collection = db.restaurants
        
        query_filter = {}
        if isinstance(field, str):
            query_filter[field] = value
        
        cursor = collection.find(query_filter)
        
        if isinstance(limit, int):
            cursor = cursor.limit(limit)
        
        return list(cursor)