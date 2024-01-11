from fastapi import (
    APIRouter,
    Depends
)

from app.repositories import UserRepository
from app.usecases import (
    GetAllUsersUseCase,
    UserCreateUseCase,
)
from app.dependencies import (
    Session,
    SessionReadOnly
)
from app.schemas.response.user_schema import (
    UserManyResponse,
    UserResponse
)
from app.schemas.request.user_create import UserCreateRequest

users = APIRouter()


@users.get("/")
async def get_users(session: SessionReadOnly = Depends()) -> UserManyResponse:
    users = await GetAllUsersUseCase(
        UserRepository(session)
    ).execute()
    return users


@users.post("/")
async def create_user(user_data: UserCreateRequest, session: Session = Depends()) -> UserResponse:
    user = await UserCreateUseCase(
        UserRepository(session)
    ).execute(user_data)
    return user
