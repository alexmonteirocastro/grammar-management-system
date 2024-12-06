from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # database settings
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Grammar Management System API"
    PROJECT_DESCRIPTION: str = (
        "Grammar Management System API helps you manage your grammar rules."
    )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    class Config:
        env_file = Path(__file__).parent.parent.parent / ".env"
        case_sensitive = True


# create a cached instance of the settings
@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore


# export settings instance
settings = get_settings()
