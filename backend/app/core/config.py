"""
Purpose:
    Centralized runtime configuration using environment variables.
Inputs:
    Values from OS environment and optional `.env` file in backend root.
Outputs:
    `Settings` object shared across backend modules.
Dependencies:
    pydantic-settings for typed config loading.
TODO Checklist:
    - [ ] Split config into local/stage/prod profiles.
    - [ ] Add strict validation for CORS URLs and secrets.
    - [ ] Move secrets to vault/secret manager for production.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application settings for consistent config access."""

    app_name: str = Field(default="Cyber Guard Platform API")
    app_env: str = Field(default="dev")
    app_debug: bool = Field(default=True)
    api_v1_prefix: str = Field(default="/api/v1")

    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/cyber_guard"
    )

    jwt_secret_key: str = Field(default="CHANGE_ME_LOCAL_DEV_SECRET")
    jwt_algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=60)

    virustotal_api_key: str = Field(default="")
    virustotal_base_url: str = Field(default="https://www.virustotal.com/api/v3")
    http_timeout_seconds: int = Field(default=20)

    max_upload_size_mb: int = Field(default=10)
    cors_origins_csv: str = Field(default="http://localhost:5173", alias="CORS_ORIGINS")
    demo_org_user_password: str = Field(default="changeme123!")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    @property
    def cors_origins(self) -> list[str]:
        """
        Parse comma-separated CORS origins from env.

        TODO:
            - Harden this parser with URL validation for production.
        """
        return [origin.strip() for origin in self.cors_origins_csv.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    """Use cache so settings are loaded once per process."""
    return Settings()
