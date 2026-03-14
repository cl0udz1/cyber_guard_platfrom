# WEEK_5_TODO.md

## Goal

Upgrade the frontend from placeholder shell to assignment-ready implementation skeleton.

## Deliverables

- navigable frontend shell
- page groups mapped to backend route groups
- typed mocks and components by domain
- clear ownership hints in the UI scaffold

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Confirm frontend/backend naming stays aligned. | `docs/API_CONTRACT.md`, `frontend/src/api/endpoints.ts` |
| B | Expose any missing backend fields needed by pages. | `backend/app/schemas/*`, `backend/app/api/routes/*` |
| C | Review RBAC and workspace context needs from the UI. | `backend/app/core/permissions.py`, `backend/app/models/membership.py` |
| D | Implement scan and reports page wiring first. | `frontend/src/pages/scan/*`, `frontend/src/pages/reports/*`, `frontend/src/components/scan/*`, `frontend/src/components/reports/*` |
| E | Implement dashboard, public threats, admin, and workspace pages. | `frontend/src/pages/dashboard/*`, `frontend/src/pages/public-threats/*`, `frontend/src/pages/admin/*`, `frontend/src/pages/workspace/*` |
| F | Keep feature notes, types, and docs synchronized. | `frontend/src/features/*`, `frontend/src/types/*`, `docs/IMPLEMENTATION_STATUS.md` |

## Dependency Notes

- do not overbuild visuals before data contracts settle
- prioritize clear ownership and file placement over polish

## Done Criteria

- frontend shell reflects the updated product concept
- every main page has a clear owner and component boundary
- build passes cleanly
