import logging
from fastapi import FastAPI

from src.routes.planet import router

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(router)
