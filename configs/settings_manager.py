from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from configs.db_settings import DatabaseSettings


class Settings(BaseSettings):
    db_settings: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
    )

def get_settings() -> Settings:
    return Settings()