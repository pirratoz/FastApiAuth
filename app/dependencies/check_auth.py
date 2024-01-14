from typing import Any
from abc import ABC

from fastapi import (
    HTTPException,
    Depends,
)
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from jwt.exceptions import (
    InvalidTokenError,
    ExpiredSignatureError,
)

from app.dependencies.db_session import SessionReadOnly
from app.repositories.user_repo import UserRepository
from app.utils import decode_jwt


class Auth(ABC):
    security = HTTPBearer()

    # for openapi docs
    def __init__(self,
        credentials: HTTPAuthorizationCredentials = Depends(security) 
    ) -> None:
        ...

    async def auth(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        session: SessionReadOnly = Depends()
    ) -> dict[str, Any]:
        payload: dict[str, Any]

        try:
            payload = decode_jwt(access_token=credentials.credentials)
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Expired signature"
            )
        except InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail="Token is invalid"
            )

        id = payload.get("id")
        
        user_repo = UserRepository(session)

        if await user_repo.get_user_by_id(id) is None:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )

        return payload
