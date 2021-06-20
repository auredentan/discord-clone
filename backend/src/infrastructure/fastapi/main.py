from typing import List

from fastapi import FastAPI
from fastapi import APIRouter


def create_app(routers: List[APIRouter]) -> FastAPI:
    app = FastAPI()

    for router in routers:
        app.include_router(router)
    return app
