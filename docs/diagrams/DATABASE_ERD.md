# Database ERD - cyber_guard_platform

## Purpose
- Document current SQLAlchemy table layout used by the MVP skeleton.
- Highlight the intentional anonymity rule for IoC submissions.

```mermaid
erDiagram
    USERS {
        string id PK
        string email UK
        string password_hash
        string role
        boolean is_active
        string created_at
    }

    IOCS {
        string id PK
        string type
        string value
        int confidence
        string tags_json
        string first_seen
        string created_at
    }

    SCAN_RESULTS {
        string id PK
        string scan_type
        string scan_key UK
        string original_input
        string status
        int score
        string summary
        string reasons_json
        string raw_vt_json
        string created_at
    }
```

Notes:
- `iocs` has no `user_id` or `org_id` foreign key by design.
- `scan_results.scan_key` is unique and used for cache lookups.
