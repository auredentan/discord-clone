from typing import Optional

from pydantic import BaseSettings
from pydantic import Field


class EnvBaseSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DBConfiguration(EnvBaseSettings):
    database_host: str
    database_name: str
    database_user: str
    database_password: str
    database_verbose: Optional[bool] = Field(default=False)
    database_pool_size: Optional[int] = Field(default=20)
    database_pool_max_overflow: Optional[int] = Field(default=10)


class RedisConfiguration(EnvBaseSettings):
    redis_host: str
    redis_port: int


class BroadcastConfiguration(EnvBaseSettings):
    redis_config: RedisConfiguration = Field(default_factory=RedisConfiguration)
