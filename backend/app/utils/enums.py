"""
Purpose:
    Common enums reused across schemas, routes, and service placeholders.
Inputs:
    Domain values for artifact types, roles, scan states, and report states.
Outputs:
    Readable enums that keep the scaffold contract consistent.
Dependencies:
    Standard library `enum`.
TODO Checklist:
    - [ ] Replace loose string roles with policy-driven permissions if the project grows.
    - [ ] Keep public-share enums separate if governance rules become more complex.
"""

from enum import Enum


class ArtifactType(str, Enum):
    FILE = "file"
    HASH = "hash"
    URL = "url"
    EMAIL_SIGNAL = "email_signal"


class AiMode(str, Enum):
    OFF = "off"
    LOCAL = "local"
    API = "api"


class ScanJobStatus(str, Enum):
    QUEUED = "queued"
    NORMALIZING = "normalizing"
    ENRICHING = "enriching"
    REPORTING = "reporting"
    COMPLETED = "completed"
    FAILED = "failed"


class WorkspaceRole(str, Enum):
    ORG_OWNER = "org_owner"
    ORG_ADMIN = "org_admin"
    ANALYST = "analyst"
    VIEWER = "viewer"
    PLATFORM_ADMIN = "platform_admin"
    SECURITY_REVIEWER = "security_reviewer"


class ThreatSeverity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class PublicShareStatus(str, Enum):
    PRIVATE = "private"
    PENDING_REVIEW = "pending_review"
    PUBLISHED = "published"
    REJECTED = "rejected"
