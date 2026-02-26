# Database ERD - cyber_guard_platform

## Purpose
- Document current SQLAlchemy table layout used by the MVP skeleton.
- Highlight the intentional anonymity rule for IoC submissions.

```mermaid
erDiagram
    USERS {
        string id PK
        string email UNIQUE
        string password_hash
        string role
        boolean is_active
        datetime created_at
    }

    IOCS {
        string id PK
        string type
        text value
        int confidence
        json tags
        datetime first_seen
        datetime created_at
    }

    SCAN_RESULTS {
        string id PK
        string scan_type
        string scan_key UNIQUE
        text original_input
        string status
        int score
        text summary
        json reasons
        json raw_vt_json
        datetime created_at
    }
```

Notes:
- `iocs` has no `user_id` or `org_id` foreign key by design.
- `scan_results.scan_key` is unique and used for cache lookups.
