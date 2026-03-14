# WEEK_6_TODO.md

## Goal

Finish validation, docs, diagrams, and handoff readiness for implementation.

## Deliverables

- passing backend tests
- passing frontend build
- current diagrams
- current implementation tracker
- ready-to-assign repo for the full team

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Review route consistency and remove stale contract drift. | `backend/app/api/*`, `docs/API_CONTRACT.md` |
| B | Review service TODOs and mark realistic next steps. | `backend/app/services/*`, `docs/ARCHITECTURE.md` |
| C | Review model comments, privacy separation, and RBAC notes. | `backend/app/models/*`, `docs/diagrams/DATA_SEPARATION.md`, `docs/diagrams/ERD.md` |
| D | Review scan/report UI ownership and placeholder quality. | `frontend/src/pages/scan/*`, `frontend/src/pages/reports/*` |
| E | Review dashboard/public/admin pages for assignment clarity. | `frontend/src/pages/dashboard/*`, `frontend/src/pages/public-threats/*`, `frontend/src/pages/admin/*` |
| F | Run tests/build, update status tracker, and capture evidence checklist. | `backend/tests/*`, `frontend/src/*`, `docs/IMPLEMENTATION_STATUS.md`, `docs/EVIDENCE_INDEX.md` |

## Dependency Notes

- this week is about stabilization, not new feature sprawl
- any scope increase must be labeled as Phase 2

## Done Criteria

- `pytest -q` passes
- `npm run build` passes
- docs and diagrams match the current tree
- a new teammate can open the repo and know where to start
