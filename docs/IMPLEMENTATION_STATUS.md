# IMPLEMENTATION_STATUS.md

Use this as the live tracker during implementation. Replace owner labels with names as soon as assignments are locked.

| Area | Status | Owner | Main Files | Blockers | Notes |
|---|---|---|---|---|---|
| Repo restructure | Scaffold refreshed | A / F | `README.md`, `backend/app/*`, `frontend/src/*` | None | New concept reflected across backend, frontend, docs |
| Auth + RBAC | Scaffold ready | A / C | `api/routes/auth.py`, `schemas/auth.py`, `core/permissions.py` | Real DB auth not implemented | Demo passwords and JWT scaffolding only |
| Orgs + workspaces | Scaffold ready | A / C | `api/routes/orgs.py`, `api/routes/workspaces.py`, `models/organization.py`, `models/workspace.py` | DB persistence not wired | Good assignment surface |
| Scan orchestration | Scaffold ready | B | `services/scan_orchestrator.py`, `services/enrichment/*`, `services/ai/*` | Real async worker not implemented | Contract and service boundaries are in place |
| Reports | Scaffold ready | B / D | `services/report_service.py`, `api/routes/reports.py`, `pages/reports/*` | Real persistence/export missing | Private report flow is represented |
| Public sharing | Scaffold ready | B / E | `services/public_sharing_service.py`, `schemas/public_threats.py`, `pages/public-threats/*` | Final sanitizer policy not written | Keep identity separation strict |
| Admin review | Scaffold ready | A / E | `api/routes/admin_reviews.py`, `services/admin_review_service.py`, `pages/admin/*` | Queue persistence missing | External uploads route exists |
| Dashboard | Scaffold ready | B / E | `api/routes/dashboard.py`, `services/dashboard_service.py`, `pages/dashboard/*` | Real aggregates missing | Current metrics are placeholders |
| Tests | Basic suite passing | F | `backend/tests/*` | Need more coverage for org/workspace flows | `pytest -q` passes |
| Frontend shell | Build passing | D / E | `frontend/src/app/*`, `frontend/src/pages/*`, `frontend/src/components/*` | No live API wiring yet | `npm run build` passes |
| Docs + diagrams | In progress | F | `docs/*`, `docs/diagrams/*` | Keep synced with future changes | Use weekly TODO files and assignment map |
