from pydantic import EmailStr

from app.dto.base_dto import BaseModelDto


class UserDto(BaseModelDto):
    id: int
    email: EmailStr
    password: bytes
