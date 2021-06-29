from typing import List

from fastapi import FastAPI
from fastapi import APIRouter

from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

from src.entrypoints import init_logging

from src.infrastructure.adapters.database.container import setup_db
from src.infrastructure.adapters.redis.container import setup_redis
from src.infrastructure.adapters.broadcast.container import setup_broadcast

from src.infrastructure.adapters.tracing import setup_tracing

from src.infrastructure.adapters.rate_limit import setup_rate_limit

from src.infrastructure.adapters.cors import setup_cors

from src.infrastructure.fastapi.main import create_app

from src.infrastructure.fastapi import base_endpoints
from src.infrastructure.fastapi import channel_endpoints
from src.infrastructure.fastapi import user_endpoints

from src.use_cases import user as user_use_case


def setup_containers(app: FastAPI) -> None:
    # pylint: disable=no-value-for-parameter,unnecessary-lambda
    injectable_modules = [base_endpoints, channel_endpoints, user_use_case]

    app.db_container = setup_db(injectable_modules)
    app.redis_container = setup_redis(injectable_modules)
    app.broadcast_container = setup_broadcast(injectable_modules)


def construct_api_app() -> FastAPI:
    routers: List[APIRouter] = [
        base_endpoints.router,
        channel_endpoints.router,
        user_endpoints.router,
    ]
    app = create_app(routers)

    # Tracing
    setup_tracing(app)

    # Cors
    setup_cors(app)

    # Rate limit
    setup_rate_limit(app)

    # Https redirect
    app.add_middleware(HTTPSRedirectMiddleware)

    # Dependency injection
    setup_containers(app)

    # Setup logging module
    init_logging()

    return app


app = construct_api_app()
