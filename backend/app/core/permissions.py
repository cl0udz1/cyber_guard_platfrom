"""
Purpose:
    Centralize role and scope checks for organization and admin endpoints.
Inputs:
    Authenticated principal context from JWT dependencies.
Outputs:
    Small helper functions used by routes and tests.
Dependencies:
    Route-level principal dictionaries and role constants.
TODO Checklist:
    - [ ] Replace simple string checks with DB-backed membership permissions.
    - [ ] Add per-workspace scoped roles once workspace selection is real.
    - [ ] Add publish/review policy helpers when governance rules are finalized.
"""

from collections.abc import Iterable


ORG_ROLES = {"org_owner", "org_admin", "analyst", "viewer"}
ADMIN_ROLES = {"platform_admin", "security_reviewer"}


def has_any_role(role: str, allowed_roles: Iterable[str]) -> bool:
    """Return True when the current role is in the allowed set."""
    return role in set(allowed_roles)


def can_manage_workspace(role: str) -> bool:
    """Owners and admins can create/update workspace resources."""
    return role in {"org_owner", "org_admin"}


def can_review_public_content(role: str) -> bool:
    """Platform admins and reviewers can operate the moderation queue."""
    return role in ADMIN_ROLES
