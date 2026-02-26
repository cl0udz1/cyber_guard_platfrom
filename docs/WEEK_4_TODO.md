# Week 4 To-Do List (Team A-F)

## Goal
Deliver dashboard summary flow and PDF report path (skeleton level).

| Person | To-Do | Main File Names |
|---|---|---|
| A | Improve dashboard backend aggregation and response quality. | `backend/app/api/v1/endpoints/dashboard.py`, `backend/app/schemas/dashboard.py` |
| B | Validate DB model fields and query ordering for dashboard data. | `backend/app/models/ioc.py`, `backend/app/models/scan_result.py` |
| C | Wire and test backend PDF generation utility behavior. | `backend/app/services/pdf_service.py`, `backend/app/services/report_service.py` |
| D | Build dashboard UI and chart/recent list rendering. | `frontend/src/pages/DashboardPage.tsx`, `frontend/src/components/Charts.tsx`, `frontend/src/components/SafetyReport.tsx`, `frontend/src/components/PdfDownloadButton.tsx` |
| E | Update testing and evidence planning docs for dashboard/PDF demo. | `docs/TEST_PLAN.md`, `docs/EVIDENCE_INDEX.md` |
| F | Expand dashboard endpoint tests and regression checks. | `backend/tests/test_dashboard_endpoints.py`, `backend/tests/test_scan_endpoints.py` |

## Team Checklist
- [ ] `/api/v1/dashboard/summary` shows valid counts + recent data.
- [ ] Frontend dashboard page renders backend summary.
- [ ] PDF path is documented and demonstrable (skeleton or endpoint).
