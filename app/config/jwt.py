from pathlib import Path

from pydantic_settings import SettingsConfigDict

from app.config.base_config import BaseConfig


class JWTConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="JWT_"
    )

    PUBLIC_KEY_PATH: Path
    PRIVATE_KEY_PATH: Path
    ACCESS_TOKEN_EXP_MINUTES: int
    ALGORITHM: str
