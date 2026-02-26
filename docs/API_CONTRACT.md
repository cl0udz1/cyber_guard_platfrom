# API Contract - Cyber Guard Platform (MVP Skeleton)

## Header
- Purpose: Define required endpoint contract for backend/frontend alignment.
- Inputs/Outputs: Request/response schemas for scan/auth/ioc/dashboard routes.
- Dependencies: FastAPI schemas in `backend/app/schemas/*`.
- TODO Checklist:
  - [ ] Add error response standard (problem+json style).
  - [ ] Add pagination/query parameters for history endpoints.
  - [ ] Add endpoint examples with curl/Postman collection.

Base prefix: `/api/v1`

---

## 1) Scan

### POST `/api/v1/scan/url`
Request body:
```json
{
  "url": "https://example.org"
}
```

Response:
```json
{
  "scan_id": "string-uuid",
  "status": "SAFE",
  "score": 10,
  "summary": "No immediate malicious indicators were detected.",
  "reasons": ["..."],
  "created_at": "2026-02-26T15:02:00Z"
}
```

### POST `/api/v1/scan/file`
Request: `multipart/form-data` with file field:
- key: `file`
- value: uploaded file bytes (never executed)

Response: same shape as scan URL response.

### GET `/api/v1/scan/{scan_id}` (optional/recommended, implemented)
Response: same shape as scan URL response.

---

## 2) Auth

### POST `/api/v1/auth/login`
Request body:
```json
{
  "email": "analyst@example.edu",
  "password": "string"
}
```

Response:
```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

### GET `/api/v1/auth/me`
Auth: `Authorization: Bearer <token>`

Response:
```json
{
  "email": "analyst@example.edu",
  "role": "org_user"
}
```

---

## 3) IoC (Anonymized)

### POST `/api/v1/ioc/submit`
Auth: `Authorization: Bearer <token>`

Request body:
```json
{
  "type": "domain",
  "value": "bad.example",
  "confidence": 75,
  "tags": ["phishing", "credential-theft"],
  "first_seen": "2026-02-26T09:30:00Z"
}
```

Allowed `type` enum:
- `ip`
- `domain`
- `url`
- `hash`
- `email`
- `file_name`
- `other`

Response:
```json
{
  "ioc_id": "string-uuid",
  "stored": true
}
```

Important privacy validation:
- Identity-like fields must be rejected (for example: `user_id`, `org_id`, `ip`, `email`, `username`).
- Unknown extra fields are rejected.

---

## 4) Dashboard

### GET `/api/v1/dashboard/summary`
Auth: `Authorization: Bearer <token>`

Response:
```json
{
  "counts_by_type": {
    "domain": 12,
    "ip": 3
  },
  "recent_iocs": [
    {
      "ioc_id": "string-uuid",
      "type": "domain",
      "value": "bad.example",
      "confidence": 75,
      "tags": ["phishing"],
      "first_seen": null,
      "created_at": "2026-02-26T10:00:00Z"
    }
  ],
  "recent_scans": [
    {
      "scan_id": "string-uuid",
      "status": "SUSPICIOUS",
      "score": 55,
      "summary": "At least one indicator appears suspicious.",
      "created_at": "2026-02-26T10:05:00Z"
    }
  ]
}
```

---

## Status Enum
- `SAFE`
- `SUSPICIOUS`
- `MALICIOUS`

## Authentication Notes
- Current scaffold uses JWT with demo-password login logic.
- TODO: Replace with DB-backed authentication and secure password lifecycle.
