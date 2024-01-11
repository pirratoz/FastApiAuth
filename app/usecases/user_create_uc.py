from fastapi import HTTPException

from app.usecases.base_uc import BaseUseCase
from app.repositories.user_repo import UserRepository
from app.schemas.request.user_create import UserCreateRequest
from app.schemas.response.user_schema import UserResponse


class UserCreateUseCase(BaseUseCase):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def execute(self, user_data: UserCreateRequest) -> UserResponse:
        user = await self.user_repo.get_user_by_email(user_data.email)

        if user is None:
            user = await self.user_repo.create(user_data)
            return UserResponse.model_validate(user.model_dump())

        raise HTTPException(
            status_code=409,
            detail="User Already exists"
        )
