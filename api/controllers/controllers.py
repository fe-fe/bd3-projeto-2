from datetime import datetime
from fastapi import APIRouter, Query
from typing import Any, Optional
from repositories.postgres_repository import PostgresRepository
from repositories.mongo_repository import MongoRepository

router = APIRouter(
    prefix="/api",
    tags=["PostgreSQL", "MongoDB"]
)


@router.get("/restaurants")
async def get_restaurants(
    origin:     Optional[str] = Query("mongo", description="Database para pesquisar [mongo/postgres]"),
    field:      Optional[str] = Query(None, description="Atributo/coluna para filtrar"), 
    value:      Optional[Any] = Query(None, description="Valor do atributo/coluna"), 
    limit:      Optional[int] = Query(None, description="Máximo de resultados"),
    show_data:  Optional[bool] = Query(False, description="Enviar ou não os dados buscados")
) -> dict:
    start_time = datetime.now()
    response = {}

    if origin == "postgres":
        repo = PostgresRepository
        format_data = lambda results: [r[0] for r in results] # postgres envia tuplas que contém o json no primeiro índice
    else:
        repo = MongoRepository
        format_data = lambda results: results # mongo já envia em dicionario/json, não precisa formatar
    
    try: 
        results = repo.find_with_parameters(field, value, limit)
        response["elapsed_time"] = (datetime.now() - start_time).total_seconds()
        response["status"] = "success"
        response["count"] = len(results)
        if show_data:
            response["data"] = format_data(results)
    except Exception as e:
        response["elapsed_time"] = (datetime.now() - start_time).total_seconds()
        response["status"] = "error"
        response["count"] = 0
        response["message"] = str(e) 
    return response