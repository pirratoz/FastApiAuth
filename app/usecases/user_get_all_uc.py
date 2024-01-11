from app.usecases.base_uc import BaseUseCase
from app.repositories.user_repo import UserRepository
from app.schemas.response.user_schema import (
    UserManyResponse,
    UserResponse
)


class GetAllUsersUseCase(BaseUseCase):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def execute(self) -> UserManyResponse:
        users = await self.user_repo.get_all_users()
        return UserManyResponse(users=[
            UserResponse.model_validate(user.model_dump())
            for user in users
        ])
