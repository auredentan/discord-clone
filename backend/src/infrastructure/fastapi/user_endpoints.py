from fastapi import APIRouter
from fastapi import HTTPException

from src.entities.user import PydanticUser

from src.use_cases.user import get_user as get_user_use_case
from src.use_cases.user import create_user as create_user_use_case

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(
    user_id: str,
) -> PydanticUser:

    user = await get_user_use_case(user_id)

    if not user:
        raise HTTPException(status=404, detail="User not found")

    return user


@router.put("/users/")
async def create_user() -> PydanticUser:

    created_user = await create_user_use_case()

    return created_user
