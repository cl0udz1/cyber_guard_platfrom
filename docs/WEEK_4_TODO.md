# WEEK_4_TODO.md

## Goal

Build report generation, anonymized sharing, and admin review structure.

## Deliverables

- private report retrieval flow
- publish request flow
- external report upload path
- admin review queue and decision skeleton

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Stabilize report, public-threat, and admin-review routes. | `backend/app/api/routes/reports.py`, `public_threats.py`, `admin_reviews.py` |
| B | Implement report building, sanitization, and publication services. | `backend/app/services/report_service.py`, `public_sharing_service.py`, `sanitization_service.py`, `admin_review_service.py` |
| C | Verify public/private entity separation in models. | `backend/app/models/threat_report.py`, `public_report.py`, `admin_review.py` |
| D | Build private report UI placeholders and publication state display. | `frontend/src/pages/reports/*`, `frontend/src/components/reports/*` |
| E | Build public threats and admin review page placeholders. | `frontend/src/pages/public-threats/*`, `frontend/src/pages/admin/*` |
| F | Add tests and docs for publish requests and admin review. | `backend/tests/integration/test_public_threats_routes.py`, `docs/DATA_FLOW.md`, `docs/TEST_PLAN.md` |

## Dependency Notes

- public reports must not directly expose private IDs
- external upload flow must always route through review

## Done Criteria

- report retrieval works after scan creation
- publish request returns sanitized preview-oriented data
- admin review queue exists and is protected by RBAC
