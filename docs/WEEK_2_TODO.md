# WEEK_2_TODO.md

## Goal

Finish backend model/schema/contract alignment so implementation can start without route confusion.

## Deliverables

- stable schema files
- stable route surface
- stable model list
- initial RBAC and privacy helpers

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Refine request/response models for auth, orgs, workspaces, scan jobs, and reports. | `backend/app/schemas/*`, `backend/app/api/routes/*` |
| B | Confirm service input/output shapes match route payloads. | `backend/app/services/*` |
| C | Finalize entity fields and FK intentions without overbuilding. | `backend/app/models/*` |
| D | Mirror important backend contract types in frontend planning files. | `frontend/src/types/*`, `frontend/src/api/endpoints.ts` |
| E | Review public-threats/admin route shapes for frontend needs. | `frontend/src/pages/public-threats/*`, `frontend/src/pages/admin/*` |
| F | Update API contract and test plan to match exact route names. | `docs/API_CONTRACT.md`, `docs/TEST_PLAN.md` |

## Dependency Notes

- route shapes should stabilize before deep frontend wiring begins
- avoid adding endpoints that have no clear assignment owner

## Done Criteria

- route groups are frozen at scaffold level
- schema names and file ownership are clear
- team can start implementation without guessing field names
