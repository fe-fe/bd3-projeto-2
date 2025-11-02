from fastapi import FastAPI
from api.controllers import postgres_controller, mongo_controller

app = FastAPI()

app.include_router(postgres_controller.router, prefix="/postgres", tags=["PostgreSQL"])
# app.include_router(mongo_controller.router, prefix="/mongo", tags=["MongoDB"])

