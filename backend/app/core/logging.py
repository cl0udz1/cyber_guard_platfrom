"""
Purpose:
    Minimal logging configuration for backend observability.
Inputs:
    Python `logging` module settings.
Outputs:
    Configured log format and level for console output.
Dependencies:
    Standard library `logging`.
TODO Checklist:
    - [ ] Add request ID correlation middleware.
    - [ ] Ship logs as JSON in production.
    - [ ] Add separate handlers for access/error logs.
"""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """
    Configure root logger once.

    NOTE:
        This skeleton keeps logging intentionally simple for student readability.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
