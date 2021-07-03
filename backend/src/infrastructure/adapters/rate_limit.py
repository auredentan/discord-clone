from typing import Any
from typing import Tuple

from fastapi import FastAPI  # type: ignore[attr-defined]

from ratelimit import RateLimitMiddleware
from ratelimit import Rule
from ratelimit.backends.redis import RedisBackend


async def AUTH_FUNCTION(scope: Any) -> Tuple[str, str]:
    """
    Resolve the user's unique identifier and the user's group from ASGI SCOPE.

    If there is no user information, it should raise `EmptyInformation`.
    If there is no group information, it should return "default".
    """
    # FIXME
    # You must write the logic of this function yourself,
    # or use the function in the following document directly.
    return "-1", "default"


def setup_rate_limit(app: FastAPI) -> None:

    app.add_middleware(
        RateLimitMiddleware,
        authenticate=AUTH_FUNCTION,
        backend=RedisBackend(),
        config={
            r"^/towns": [Rule(minute=200, second=10)],
        },
    )
