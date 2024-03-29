from typing import Any
from datetime import (
    datetime,
    timedelta,
)

from jwt import (
    encode,
    decode,
)

from app.config import JWTConfig


def encode_jwt(
    payload: dict[str, Any],
    key: str = JWTConfig().PRIVATE_KEY_PATH.read_text(),
    algorithm: str = JWTConfig().ALGORITHM,
    exp: timedelta = timedelta(minutes=JWTConfig().ACCESS_TOKEN_EXP_MINUTES)
) -> str:
    current_time = datetime.utcnow()
    payload = payload | {
        "iat": current_time,
        "exp": current_time + exp
    }
    return encode(
        payload=payload,
        key=key,
        algorithm=algorithm
    )


def decode_jwt(
    access_token: str, 
    key: str = JWTConfig().PUBLIC_KEY_PATH.read_text(),
    algorithm: str = JWTConfig().ALGORITHM
) -> Any:
    return decode(
        jwt=access_token,
        key=key,
        algorithms=[algorithm]
    )
