from fastapi import FastAPI
from controllers import controllers

app = FastAPI()

app.include_router(controllers.router)


