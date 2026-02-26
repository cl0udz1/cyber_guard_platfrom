# Week 6 To-Do List (Team A-F)

## Goal
Final stabilization, demo prep, and submission package completion.

| Person | To-Do | Main File Names |
|---|---|---|
| A | Final backend bug fixes and API polish for demo reliability. | `backend/app/api/v1/endpoints/auth.py`, `backend/app/api/v1/endpoints/scan.py`, `backend/app/api/v1/endpoints/ioc.py`, `backend/app/api/v1/endpoints/dashboard.py` |
| B | DB/migration readiness review and future migration notes. | `backend/alembic.ini`, `backend/app/models/user.py`, `backend/app/models/ioc.py`, `backend/app/models/scan_result.py` |
| C | Security/privacy final review against "Disconnect by Design" rule. | `backend/app/services/anonymizer.py`, `backend/app/schemas/ioc.py`, `README.md` |
| D | Frontend final demo flow polish and manual test walk-through. | `frontend/src/App.tsx`, `frontend/src/pages/GuestScanPage.tsx`, `frontend/src/pages/DashboardPage.tsx` |
| E | Final docs package and evidence map updates. | `docs/PROJECT_PLAN.md`, `docs/API_CONTRACT.md`, `docs/TEST_PLAN.md`, `docs/EVIDENCE_INDEX.md` |
| F | Execute final QA checklist and archive test evidence output. | `backend/tests/test_auth_endpoints.py`, `backend/tests/test_scan_endpoints.py`, `backend/tests/test_dashboard_endpoints.py`, `backend/tests/test_virustotal_client.py` |

## Team Checklist
- [ ] Demo script runs cleanly from start to finish.
- [ ] Final report references current file structure and contract.
- [ ] Evidence set is complete for grading/submission.
