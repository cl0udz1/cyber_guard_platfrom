# Week 2 To-Do List (Team A-F)

## Goal
Complete authentication and anonymous IoC submission foundation.

| Person | To-Do | Main File Names |
|---|---|---|
| A | Strengthen login flow and token claims handling. | `backend/app/api/v1/endpoints/auth.py`, `backend/app/core/security.py` |
| B | Improve dependency wiring for auth-protected routes. | `backend/app/api/deps.py`, `backend/app/api/v1/router.py` |
| C | Enforce anonymization and identity-field rejection logic. | `backend/app/services/anonymizer.py`, `backend/app/schemas/ioc.py`, `backend/app/models/ioc.py` |
| D | Implement frontend login and IoC submit form behavior. | `frontend/src/pages/LoginPage.tsx`, `frontend/src/pages/SubmitIocPage.tsx`, `frontend/src/types/user.ts`, `frontend/src/types/ioc.ts` |
| E | Update privacy design notes and endpoint examples in docs. | `docs/API_CONTRACT.md`, `README.md` |
| F | Expand tests for auth and anonymizer edge cases. | `backend/tests/test_auth_endpoints.py`, `backend/tests/test_anonymizer.py` |

## Team Checklist
- [ ] `/api/v1/auth/login` works end-to-end.
- [ ] `/api/v1/ioc/submit` rejects identity-like fields.
- [ ] Docs reflect the final Week 2 auth/privacy behavior.
