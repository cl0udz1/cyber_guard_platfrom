"""
Purpose:
    FastAPI application entry point for the Cyber Guard scaffold refresh.
Inputs:
    Runtime configuration, logging setup, and API router.
Outputs:
    Runnable API with scaffold routes under `/api/v1`.
Dependencies:
    FastAPI, CORS middleware, settings, and route registration.
TODO Checklist:
    - [ ] Add startup checks for DB and configured enrichment adapters.
    - [ ] Add exception handlers with a consistent error envelope.
    - [ ] Add worker/process notes once async jobs move beyond placeholder orchestration.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Keep startup and shutdown hooks in one obvious place."""
    configure_logging()
    yield


def create_app() -> FastAPI:
    """Create the FastAPI app used by the server and tests."""
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        version="0.2.0-scaffold",
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
        """Simple root endpoint to confirm the scaffold boots."""
        return {"message": "Cyber Guard Platform API scaffold is running."}

    @app.get("/healthz", tags=["system"])
    async def healthz() -> dict[str, object]:
        """Return a lightweight local health signal."""
        return {
            "status": "ok",
            "mode": "scaffold",
            "features": {
                "async_scan_jobs": True,
                "public_threats": True,
                "disconnect_by_design": True,
            },
        }

    return app


app = create_app()
