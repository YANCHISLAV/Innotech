from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

from configs.auth_settings import AuthSettings
from configs.db_settings import DatabaseSettings


class Settings(BaseSettings):
    db_settings: DatabaseSettings
    auth_settings: AuthSettings
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_nested_delimiter="__",
    )

def get_settings() -> Settings:
    return Settings()