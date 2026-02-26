# Week 3 To-Do List (Team A-F)

## Goal
Complete guest scan pipeline with caching and VirusTotal integration skeleton.

| Person | To-Do | Main File Names |
|---|---|---|
| A | Improve VirusTotal client request/retry behavior and errors. | `backend/app/services/virustotal_client.py`, `backend/app/utils/rate_limit.py` |
| B | Refine scan orchestration and report generation rules. | `backend/app/services/scan_service.py`, `backend/app/services/report_service.py` |
| C | Finalize scan endpoints and input normalization/hash utilities. | `backend/app/api/v1/endpoints/scan.py`, `backend/app/utils/validators.py`, `backend/app/utils/hashing.py`, `backend/app/models/scan_result.py` |
| D | Connect frontend guest scan page to URL/file scan endpoints. | `frontend/src/pages/GuestScanPage.tsx`, `frontend/src/components/UrlInput.tsx`, `frontend/src/components/FileUpload.tsx`, `frontend/src/api/endpoints.ts`, `frontend/src/types/scan.ts` |
| E | Document scan contract and caching notes. | `docs/API_CONTRACT.md`, `README.md`, `docs/PROJECT_PLAN.md` |
| F | Add/maintain scan and VT client test coverage. | `backend/tests/test_scan_endpoints.py`, `backend/tests/test_virustotal_client.py` |

## Team Checklist
- [ ] URL scan works and reuses cache.
- [ ] File scan works and reuses cache by SHA-256.
- [ ] Test suite covers cache hit vs miss behavior.
