"""
Purpose:
    Small feature-flag helpers that document optional scaffold capabilities.
Inputs:
    Application settings.
Outputs:
    Readable flag checks for routes, docs, and tests.
Dependencies:
    `app.core.config.Settings`.
TODO Checklist:
    - [ ] Replace boolean flags with environment-based rollout strategy if needed.
    - [ ] Add frontend-consumable feature endpoint if the UI needs runtime flags.
"""

from app.core.config import Settings


def public_threats_api_enabled(settings: Settings) -> bool:
    """Return True when the planned public API should appear enabled."""
    return settings.public_threats_api_enabled


def api_ai_mode_available(settings: Settings) -> bool:
    """Return True when remote AI analysis is configured for demos."""
    return settings.api_ai_enabled and bool(settings.api_ai_provider_name)
