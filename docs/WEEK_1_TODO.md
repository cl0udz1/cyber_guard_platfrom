# WEEK_1_TODO.md

## Goal

Lock scope and finish the repo refresh so the team is working from the same product definition.

## Deliverables

- updated README
- updated architecture and plan docs
- cleaned backend/frontend folder structure
- assignment map and implementation tracker in use

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Confirm route groups and schema ownership boundaries. | `backend/app/api/*`, `docs/API_CONTRACT.md` |
| B | Confirm service boundaries for scan orchestration, reporting, and sharing. | `backend/app/services/*`, `docs/ARCHITECTURE.md` |
| C | Confirm model list and privacy boundary at the data level. | `backend/app/models/*`, `docs/diagrams/ERD.md` |
| D | Confirm scan/report frontend page ownership and component grouping. | `frontend/src/pages/scan/*`, `frontend/src/pages/reports/*` |
| E | Confirm dashboard/public/admin page ownership and wording. | `frontend/src/pages/dashboard/*`, `frontend/src/pages/public-threats/*`, `frontend/src/pages/admin/*` |
| F | Update assignment docs, weekly plan, and implementation tracker. | `docs/ASSIGNMENT_MAP.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/WEEK_*.md` |

## Dependency Notes

- Do not start detailed implementation until the new concept is accepted by the whole team.
- Keep public/private data separation visible in every new plan or file.

## Done Criteria

- team agrees on updated product truth
- no major old-concept files remain in active folders
- ownership map is usable for assignment splitting
