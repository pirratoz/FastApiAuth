from fastapi import HTTPException

from app.usecases.base_uc import BaseUseCase
from app.repositories.user_repo import UserRepository
from app.schemas.response.token_schema import TokenResponse
from app.schemas.request import UserLoginRequest
from app.utils import (
    cmp_password,
    encode_jwt,
)


class UserLoginUseCase(BaseUseCase):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def execute(self, user_data: UserLoginRequest) -> TokenResponse:
        user = await self.user_repo.get_user_by_email(user_data.email)

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Email or password incorrect"
            )
        
        if not cmp_password(user_data.password, user.password):
            raise HTTPException(
                status_code=401,
                detail="Email or password incorrect"
            )
        
        token = encode_jwt(
            {
                "id": user.id,
                "email": user.email
            }
        )

        return TokenResponse(
            access_token=token,
            token_type="Bearer"
        )
