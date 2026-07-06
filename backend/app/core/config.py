from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Configuration
    Loaded automatically from .env file
    """

    # ----------------------------------------------------
    # Project Information
    # ----------------------------------------------------
    PROJECT_NAME: str = "Farm Credit Platform"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # ----------------------------------------------------
    # Security
    # ----------------------------------------------------
    SECRET_KEY: str = "CHANGE_ME_IN_PRODUCTION"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ----------------------------------------------------
    # Database
    # ----------------------------------------------------
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "farm_credit_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"

    # ----------------------------------------------------
    # Google Earth Engine
    # ----------------------------------------------------
    GEE_PROJECT_ID: str = ""
    GEE_SERVICE_ACCOUNT: str = ""
    GEE_PRIVATE_KEY_PATH: str = ""

    # ----------------------------------------------------
    # AWS / S3
    # ----------------------------------------------------
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "ap-south-1"
    S3_BUCKET_NAME: str = ""

    # ----------------------------------------------------
    # Email
    # ----------------------------------------------------
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    # ----------------------------------------------------
    # Redis
    # ----------------------------------------------------
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # ----------------------------------------------------
    # Logging
    # ----------------------------------------------------
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """
    return Settings()


settings = get_settings()
