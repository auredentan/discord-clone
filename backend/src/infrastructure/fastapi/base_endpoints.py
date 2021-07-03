from fastapi import APIRouter  # type: ignore[attr-defined]
from fastapi import Depends  # type: ignore[attr-defined]

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

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
