from typing import List

from fastapi import FastAPI, APIRouter

from src.entrypoints import init_logging


from src.infrastructure.adapters.database.container import setup_db
from src.infrastructure.adapters.redis.container import setup_redis
from src.infrastructure.fastapi.main import create_app
from src.infrastructure.fastapi.base_endpoints import router as base_router


def setup() -> None:
    # pylint: disable=no-value-for-parameter,unnecessary-lambda

    setup_db()
    setup_redis()

    # Setup logging module
    init_logging()


def construct_api_app() -> FastAPI:
    setup()
    routers: List[APIRouter] = [base_router]
    app = create_app(routers)
    return app


app = construct_api_app()
