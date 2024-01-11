from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str


class UserManyResponse(BaseModel):
    users: list[UserResponse]
