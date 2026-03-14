# WEEK_3_TODO.md

## Goal

Build the scan orchestration skeleton: normalization, IOC extraction, adapters, caching, and AI mode selection.

## Deliverables

- working scaffold `POST /scan-jobs`
- multi-source enrichment slots
- local/API AI mode placeholders
- duplicate submission cache behavior

## Per-Owner Tasks

| Owner | Tasks | Main Files |
|---|---|---|
| A | Keep scan job route behavior and responses consistent. | `backend/app/api/routes/scan_jobs.py`, `backend/app/schemas/scan.py` |
| B | Implement orchestration flow and adapter interfaces. | `backend/app/services/scan_orchestrator.py`, `backend/app/services/enrichment/*`, `backend/app/services/ai/*` |
| C | Validate model alignment for artifact submissions, scan jobs, and enrichment results. | `backend/app/models/artifact_submission.py`, `backend/app/models/scan_job.py`, `backend/app/models/enrichment_result.py` |
| D | Build scan page forms and queue view wiring plan. | `frontend/src/pages/scan/*`, `frontend/src/components/scan/*` |
| E | Keep dashboard placeholders ready for scan-state metrics. | `frontend/src/pages/dashboard/*`, `frontend/src/components/dashboard/*` |
| F | Add tests for duplicate submissions, adapter shape, and AI mode decisions. | `backend/tests/unit/*`, `backend/tests/integration/test_scan_jobs_routes.py` |

## Dependency Notes

- do not hard-code the app around a single source
- keep AI optional and swappable

## Done Criteria

- scan job route works end-to-end at scaffold level
- repeated identical submission reuses cached result
- at least two enrichment adapters are visible in the flow
