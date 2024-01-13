from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Body,
)

from app.repositories import UserRepository
from app.usecases import (
    GetAllUsersUseCase,
    UserCreateUseCase,
    UserLoginUseCase,
)
from app.dependencies import (
    Session,
    SessionReadOnly,
    IsAuth,
)
from app.schemas.response.user_schema import (
    UserManyResponse,
    UserResponse,
)
from app.schemas.request import (
    UserCreateRequest,
    UserLoginRequest,
)
from app.schemas.response import (
    TokenResponse
)

users = APIRouter()


@users.get("/", response_model=UserManyResponse, dependencies=[Depends(IsAuth.auth)])
async def get_users(
    session: SessionReadOnly = Depends()
) -> UserManyResponse:
    users = await GetAllUsersUseCase(
        UserRepository(session)
    ).execute()
    return users


@users.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreateRequest,
    session: Session = Depends()
) -> UserResponse:
    user = await UserCreateUseCase(
        UserRepository(session)
    ).execute(user_data)
    return user


@users.post("/login", response_model=TokenResponse)
async def user_login(
    user_data: Annotated[UserLoginRequest, Body],
    session: SessionReadOnly = Depends()
) -> TokenResponse:
    token = await UserLoginUseCase(
        UserRepository(session)
    ).execute(user_data)
    return token
