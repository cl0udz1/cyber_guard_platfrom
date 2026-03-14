"""
Purpose:
    Shared logging setup for API routes, scan orchestration, and review workflows.
Inputs:
    Python logging configuration invoked during app startup.
Outputs:
    Consistent console logging format for local development and demos.
Dependencies:
    Standard library `logging`.
TODO Checklist:
    - [ ] Add structured audit logs for publish/review decisions.
    - [ ] Split request logs from enrichment adapter diagnostics.
    - [ ] Add correlation IDs once async workers are introduced for real.
"""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure a lightweight readable logging format for the scaffold."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
