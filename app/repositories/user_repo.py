from sqlalchemy import (
    select,
    insert
)
from pydantic import EmailStr

from app.repositories.base_repo import BaseRepository
from app.models.user import User
from app.dto.user_dto import UserDto
from app.schemas.request import UserCreateRequest
from app.utils import hash_password


class UserRepository(BaseRepository):
    async def get_user_by_id(self, user_id: int) -> UserDto | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return UserDto.one_from_orm(user)
    
    async def get_user_by_email(self, email: EmailStr) -> UserDto | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return UserDto.one_from_orm(user)
    
    async def get_all_users(self) -> list[UserDto]:
        stmt = select(User)
        result = await self.session.execute(stmt)
        users = result.scalars().all()
        return UserDto.many_from_orm(users)
    
    async def create(self, user: UserCreateRequest) -> UserDto | None:
        data = user.model_dump()
        data["password"] = hash_password(data["password"])
        stmt = insert(User).values(data)
        await self.session.execute(stmt)
        return await self.get_user_by_email(user.email)
