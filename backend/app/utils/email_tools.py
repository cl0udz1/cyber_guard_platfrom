"""
Purpose:
    Lightweight helpers for pasted email indicator handling.
Inputs:
    Email addresses, subjects, or pasted email snippets from submissions.
Outputs:
    Normalized email-related values suitable for IOC extraction.
Dependencies:
    Standard library string helpers.
TODO Checklist:
    - [ ] Add MIME parsing if raw `.eml` upload support becomes part of the MVP.
    - [ ] Add domain extraction and sender/recipient field parsing.
"""


def normalize_email_signal(raw_value: str) -> str:
    """Normalize simple email indicator text for consistent processing."""
    return " ".join(raw_value.strip().split())
