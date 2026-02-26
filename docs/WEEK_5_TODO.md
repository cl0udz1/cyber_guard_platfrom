# Week 5 To-Do List (Team A-F)

## Goal
Integration hardening, developer workflow cleanup, and documentation quality.

| Person | To-Do | Main File Names |
|---|---|---|
| A | Improve backend app reliability (startup checks, logging TODOs, error handling notes). | `backend/app/main.py`, `backend/app/core/logging.py` |
| B | Tighten security and dependency checks for protected routes. | `backend/app/api/deps.py`, `backend/app/core/security.py` |
| C | Review and refine validation guards + input constraints. | `backend/app/utils/validators.py`, `backend/app/schemas/ioc.py`, `backend/app/schemas/scan.py` |
| D | Polish frontend UX messaging and validation clarity. | `frontend/src/utils/validators.ts`, `frontend/src/utils/formatters.ts`, `frontend/src/pages/LoginPage.tsx`, `frontend/src/pages/SubmitIocPage.tsx` |
| E | Finalize local setup docs and environment/run instructions. | `README.md`, `docker-compose.yml`, `.env.example`, `frontend/.env.example`, `backend/.env.example` |
| F | Full test run + report of failures/warnings and follow-up tasks. | `backend/tests/conftest.py`, `backend/tests/test_*.py`, `docs/TEST_PLAN.md` |

## Team Checklist
- [ ] Backend and frontend start with one command each.
- [ ] No contract mismatch between frontend and backend.
- [ ] Setup instructions are clear for a new teammate.
