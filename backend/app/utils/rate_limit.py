"""
Purpose:
    Small retry/backoff helper utilities for external API calls.
Inputs:
    Retry attempt number and optional tuning parameters.
Outputs:
    Wait duration in seconds.
Dependencies:
    Standard library math.
TODO Checklist:
    - [ ] Add jitter strategy to avoid synchronized retry storms.
    - [ ] Respect server-provided retry headers when available.
"""


def get_backoff_seconds(attempt: int, base: float = 1.0, cap: float = 8.0) -> float:
    """
    Exponential backoff calculation.

    attempt=1 -> base
    attempt=2 -> base*2
    attempt=3 -> base*4 ... capped at `cap`
    """
    if attempt < 1:
        attempt = 1
    seconds = base * (2 ** (attempt - 1))
    return min(seconds, cap)
