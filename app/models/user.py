from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from sqlalchemy.dialects.postgresql import BYTEA

from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[bytes] = mapped_column(BYTEA, nullable=False)
