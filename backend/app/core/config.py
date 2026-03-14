"""
Purpose:
    Centralized runtime configuration for the refreshed Cyber Guard scaffold.
Inputs:
    Environment variables from backend `.env` and deployment runtime.
Outputs:
    Cached `Settings` object shared by routes, services, and tests.
Dependencies:
    pydantic-settings for typed config loading.
TODO Checklist:
    - [ ] Split settings into local/demo/review profiles if the team needs them.
    - [ ] Validate external API URLs and secrets more strictly before production.
    - [ ] Add per-workspace storage settings if file handling becomes persistent.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application settings for the current scaffold phase."""

    app_name: str = Field(default="Cyber Guard Platform API")
    app_env: str = Field(default="dev")
    app_debug: bool = Field(default=True)
    api_v1_prefix: str = Field(default="/api/v1")

    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/cyber_guard"
    )

    jwt_secret_key: str = Field(default="CHANGE_ME_LOCAL_DEV_SECRET")
    jwt_algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=120)

    max_upload_size_mb: int = Field(default=20)
    http_timeout_seconds: int = Field(default=20)
    scan_job_poll_seconds: int = Field(default=5)
    cors_origins_csv: str = Field(default="http://localhost:5173", alias="CORS_ORIGINS")

    demo_org_admin_password: str = Field(default="org-admin-demo")
    demo_platform_admin_password: str = Field(default="platform-admin-demo")

    default_ai_mode: str = Field(default="local")
    local_ai_enabled: bool = Field(default=True)
    api_ai_enabled: bool = Field(default=True)
    api_ai_provider_name: str = Field(default="openai-compatible")
    api_ai_base_url: str = Field(default="")
    api_ai_key: str = Field(default="")

    virustotal_enabled: bool = Field(default=True)
    virustotal_api_key: str = Field(default="")
    virustotal_base_url: str = Field(default="https://www.virustotal.com/api/v3")

    source_a_enabled: bool = Field(default=True)
    source_b_enabled: bool = Field(default=True)
    source_c_enabled: bool = Field(default=False)

    public_threats_api_enabled: bool = Field(default=False)
    admin_review_required_for_external_reports: bool = Field(default=True)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    @property
    def cors_origins(self) -> list[str]:
        """Parse comma-separated CORS origins for local development."""
        return [origin.strip() for origin in self.cors_origins_csv.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    """Load settings once per process for predictable dependency injection."""
    return Settings()
