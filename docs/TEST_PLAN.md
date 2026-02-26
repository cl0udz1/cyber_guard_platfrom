# TEST_PLAN.md - MVP Test Strategy and Traceability

## Header
- Purpose: Define what to test, why it matters, and where automated tests live.
- Inputs/Outputs: Test cases mapped to MVP requirements.
- Dependencies: pytest suite in `backend/tests`.
- TODO Checklist:
  - [ ] Add frontend test plan (component/unit/e2e).
  - [ ] Add performance and security test scenarios.
  - [ ] Add CI execution matrix and pass/fail thresholds.

## Test Levels
- Unit tests:
  - anonymizer rules
  - VT client behavior with mocked HTTP responses
  - helper logic (hashing/normalization in future expansion)
- API integration tests (local):
  - auth endpoints
  - scan endpoints
  - dashboard endpoint
- Manual UI smoke tests:
  - page navigation and API interaction from frontend

## Key Requirement Traceability

| Requirement ID | Requirement | Test Coverage |
|---|---|---|
| R1 | Guest URL scan returns SAFE/SUSPICIOUS/MALICIOUS report | `backend/tests/test_scan_endpoints.py` |
| R2 | Guest file scan does not execute files and returns report | `backend/tests/test_scan_endpoints.py` |
| R3 | URL/file caching reduces repeated external lookups | `backend/tests/test_scan_endpoints.py` cache hit tests |
| R4 | Login returns JWT bearer token | `backend/tests/test_auth_endpoints.py` |
| R5 | Authenticated `/auth/me` returns user info | `backend/tests/test_auth_endpoints.py` |
| R6 | IoC anonymization rejects identity-like fields | `backend/tests/test_anonymizer.py` |
| R7 | Dashboard summary returns counts and recent items | `backend/tests/test_dashboard_endpoints.py` |
| R8 | VirusTotal integration uses HTTP client + handles retry path | `backend/tests/test_virustotal_client.py` |

## Detailed Test Cases (Initial)

1. Auth login success
- Input: valid email + demo password
- Expected: 200 with `access_token`, `token_type="bearer"`

2. Auth me endpoint
- Input: valid bearer token
- Expected: 200 with `email`, `role`

3. URL scan cache miss then hit
- Input: same URL submitted twice
- Expected: first call triggers external lookup; second call reuses cached scan ID

4. File scan cache miss then hit
- Input: same file bytes submitted twice (different filename allowed)
- Expected: second call uses same cached scan result

5. Anonymizer reject identity field
- Input: IoC payload includes `user_id`
- Expected: reject with validation error

6. VT client mocked success
- Input: mocked HTTP 200 for VT URL endpoint
- Expected: parsed JSON returned correctly

7. VT client mocked 429 then 200
- Input: mocked sequence [429, 200]
- Expected: retry succeeds and returns second response

8. Dashboard summary shape
- Input: seeded IoC and scan rows + auth token
- Expected: `counts_by_type`, `recent_iocs`, `recent_scans` returned

## Manual Test Checklist (Frontend)

1. Start backend + frontend.
2. On Guest Scan page:
- Submit URL and verify safety report appears.
- Submit file and verify safety report appears.
- Click PDF download button and verify download starts.
3. On Login page:
- Login with demo password and verify no error.
4. On Submit IoC page:
- Submit valid IoC and verify success message.
5. On Dashboard page:
- Verify chart and recent lists render after login.
