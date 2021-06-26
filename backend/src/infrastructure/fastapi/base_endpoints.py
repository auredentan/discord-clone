from fastapi import APIRouter
from fastapi import Depends

from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide

from src.infrastructure.adapters.redis.container import RedisContainer
from src.infrastructure.adapters.redis.service import RedisService

router = APIRouter()


@router.get("/healthz")
def healthz() -> str:
    return "healthy"


@router.get("/redis")
@inject
async def redis(
    redis_service: RedisService = Depends(Provide[RedisContainer.service]),
) -> str:
    return await redis_service.process()
