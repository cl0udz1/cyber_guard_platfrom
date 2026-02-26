"""
Purpose:
    Entry point for Cyber Guard Platform backend API (FastAPI app instance).
Inputs:
    Runtime configuration from environment variables via `app.core.config`.
Outputs:
    Exposes HTTP routes for scan/auth/IoC/dashboard features under `/api/v1`.
Dependencies:
    FastAPI, API routers, logging config, settings.
TODO Checklist:
    - [ ] Add startup health checks for database and external APIs.
    - [ ] Add global exception handlers and structured error responses.
    - [ ] Add API versioning strategy beyond v1.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Keep startup/shutdown logic in one place.

    TODO:
        - Add DB connectivity checks.
        - Add warm-up job for cache/report templates if needed.
    """
    configure_logging()
    yield


def create_app() -> FastAPI:
    """Factory pattern helps tests import the same app object cleanly."""
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        version="0.1.0-skeleton",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/", tags=["system"])
    async def root() -> dict[str, str]:
        """Simple root endpoint to confirm API process is running."""
        return {"message": "Cyber Guard Platform API is running."}

    @app.get("/healthz", tags=["system"])
    async def healthz() -> dict[str, str]:
        """
        Lightweight health endpoint.

        TODO:
            - Include DB readiness in a richer health endpoint.
            - Add external dependency status checks.
        """
        return {"status": "ok"}

    return app


app = create_app()
