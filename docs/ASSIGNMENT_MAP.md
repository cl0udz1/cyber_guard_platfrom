# ASSIGNMENT_MAP.md

## Purpose

This file maps repo areas to likely owners so team assignment is clear. Use the A-F labels as default role buckets, then replace them with actual names.

## Suggested Ownership Model

| Owner | Focus | Main Folders | Main Files |
|---|---|---|---|
| A | Backend API owner | `backend/app/api/`, `backend/app/schemas/` | `api/router.py`, `api/routes/*.py`, `schemas/auth.py`, `schemas/scan.py`, `schemas/report.py` |
| B | Backend services owner | `backend/app/services/` | `scan_orchestrator.py`, `normalization_service.py`, `ioc_extraction_service.py`, `report_service.py`, `dashboard_service.py` |
| C | DB/models + permissions owner | `backend/app/models/`, `backend/app/core/`, `backend/app/db/` | `models/*.py`, `core/permissions.py`, `db/base.py`, `db/session.py` |
| D | Frontend scan/report owner | `frontend/src/pages/scan/`, `frontend/src/pages/reports/`, `frontend/src/components/scan/`, `frontend/src/components/reports/` | `ScanWorkspacePage.tsx`, `ReportsPage.tsx`, `ArtifactSubmissionPanel.tsx`, `ReportSummaryCard.tsx` |
| E | Frontend dashboard/public-threats/admin owner | `frontend/src/pages/dashboard/`, `frontend/src/pages/public-threats/`, `frontend/src/pages/admin/` | `DashboardPage.tsx`, `PublicThreatsPage.tsx`, `AdminReviewPage.tsx`, related components |
| F | Docs/testing/integration owner | `docs/`, `backend/tests/`, `frontend/src/api/`, `frontend/src/features/` | `API_CONTRACT.md`, `TEST_PLAN.md`, weekly TODO files, `test_*`, `api/endpoints.ts` |

## Detailed Responsibility Notes

### A: Backend API Owner

Main job:

- keep route groups aligned with the contract
- keep request/response schemas stable
- keep access expectations obvious

Main files:

- `backend/app/api/router.py`
- `backend/app/api/routes/auth.py`
- `backend/app/api/routes/users.py`
- `backend/app/api/routes/orgs.py`
- `backend/app/api/routes/workspaces.py`
- `backend/app/api/routes/scan_jobs.py`
- `backend/app/api/routes/reports.py`
- `backend/app/api/routes/public_threats.py`
- `backend/app/api/routes/admin_reviews.py`
- `backend/app/api/routes/dashboard.py`
- `backend/app/api/routes/integrations.py`

### B: Backend Services Owner

Main job:

- build the actual implementation behind the route stubs
- keep orchestration readable and incremental

Main files:

- `backend/app/services/scan_orchestrator.py`
- `backend/app/services/artifact_service.py`
- `backend/app/services/normalization_service.py`
- `backend/app/services/ioc_extraction_service.py`
- `backend/app/services/caching_service.py`
- `backend/app/services/report_service.py`
- `backend/app/services/public_sharing_service.py`
- `backend/app/services/admin_review_service.py`
- `backend/app/services/dashboard_service.py`
- `backend/app/services/enrichment/*`
- `backend/app/services/ai/*`

### C: DB / Models / Permissions Owner

Main job:

- keep entities aligned with product reality
- protect private/public separation at the data-model level
- own RBAC helpers

Main files:

- `backend/app/models/user.py`
- `backend/app/models/organization.py`
- `backend/app/models/workspace.py`
- `backend/app/models/membership.py`
- `backend/app/models/artifact_submission.py`
- `backend/app/models/scan_job.py`
- `backend/app/models/enrichment_result.py`
- `backend/app/models/threat_report.py`
- `backend/app/models/public_report.py`
- `backend/app/models/admin_review.py`
- `backend/app/models/api_client_config.py`
- `backend/app/core/permissions.py`

### D: Frontend Scan / Report Owner

Main job:

- turn scan/report placeholders into working private user flows

Main files:

- `frontend/src/pages/scan/ScanWorkspacePage.tsx`
- `frontend/src/pages/reports/ReportsPage.tsx`
- `frontend/src/components/scan/ArtifactSubmissionPanel.tsx`
- `frontend/src/components/scan/QueueSnapshot.tsx`
- `frontend/src/components/reports/ReportSummaryCard.tsx`
- `frontend/src/types/scan.ts`
- `frontend/src/types/report.ts`

### E: Frontend Dashboard / Public / Admin Owner

Main job:

- implement the visibility and moderation side of the platform

Main files:

- `frontend/src/pages/dashboard/DashboardPage.tsx`
- `frontend/src/pages/public-threats/PublicThreatsPage.tsx`
- `frontend/src/pages/admin/AdminReviewPage.tsx`
- `frontend/src/pages/workspace/WorkspacePage.tsx`
- `frontend/src/components/dashboard/MetricsBoard.tsx`
- `frontend/src/components/public-threats/PublicThreatFeed.tsx`
- `frontend/src/components/admin-review/ReviewQueuePanel.tsx`

### F: Docs / Testing / Integration Owner

Main job:

- keep documentation, API planning, tests, and evidence aligned

Main files:

- `docs/API_CONTRACT.md`
- `docs/TEST_PLAN.md`
- `docs/ARCHITECTURE.md`
- `docs/DATA_FLOW.md`
- `docs/IMPLEMENTATION_STATUS.md`
- `docs/WEEK_1_TODO.md` to `docs/WEEK_6_TODO.md`
- `backend/tests/unit/*`
- `backend/tests/integration/*`
- `backend/tests/contract/*`
- `frontend/src/api/endpoints.ts`

## Handoff Rule

If one owner changes a contract file used by another owner, update:

1. the relevant schema or type
2. the weekly TODO file
3. the implementation status tracker
