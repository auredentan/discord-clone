from typing import List

from fastapi import APIRouter  # type: ignore[attr-defined]
from fastapi import FastAPI  # type: ignore[attr-defined]


def create_app(routers: List[APIRouter]) -> FastAPI:
    app = FastAPI()

    for router in routers:
        app.include_router(router)
    return app
