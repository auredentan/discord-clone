import logging

from fastapi import APIRouter, Depends

from dependency_injector.wiring import inject, Provide

from src.infrastructure.adapters.redis.container import RedisContainer
from src.infrastructure.adapters.redis.service import RedisService

router = APIRouter()


@router.get("/ping")
def ping() -> str:
    return "pong"


@router.get("/redis")
@inject
async def redis(
    redis_service: RedisService = Depends(Provide[RedisContainer.service]),
) -> str:
    return await redis_service.process()
