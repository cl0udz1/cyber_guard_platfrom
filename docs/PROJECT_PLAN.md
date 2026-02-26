# PROJECT_PLAN.md - Week-by-Week Roadmap

## Header
- Purpose: Provide a student-friendly implementation timeline for Senior Project II.
- Inputs/Outputs: Weekly objectives, deliverables, and checkpoints.
- Dependencies: API contract, test plan, project rubric.
- TODO Checklist:
  - [ ] Align dates with your university calendar.
  - [ ] Add owner names for each task.
  - [ ] Track risks and mitigation per week.

## Week 1 - Problem Framing and Scope Lock
- Confirm MVP scope and non-functional constraints.
- Define "Disconnect by Design" privacy rules.
- Finalize architecture decision (FastAPI + React + PostgreSQL).
- Deliverable: approved scope document and architecture sketch.

## Week 2 - Backend Skeleton
- Setup FastAPI structure and dependencies.
- Add config, logging, DB session, model skeletons.
- Add core endpoint routes (scan/auth/ioc/dashboard) with stubs.
- Deliverable: backend app boots with `uvicorn app.main:app --reload`.

## Week 3 - Database and Models
- Finalize SQLAlchemy models for `users`, `scan_results`, `iocs`.
- Ensure IoC table has no identity-link fields.
- Prepare Alembic migration workflow skeleton.
- Deliverable: schema created locally and model-level tests passing.

## Week 4 - Scan Service MVP
- Implement URL normalization and file SHA-256 hashing.
- Add VirusTotal client wrapper with timeout/retry notes.
- Add cache behavior by normalized URL and SHA-256.
- Deliverable: scan endpoints return deterministic reports.

## Week 5 - Auth + Privacy Enforcement
- Add login endpoint and JWT helper flow.
- Add `/auth/me` protected endpoint.
- Implement anonymizer service to reject identity-like fields.
- Deliverable: IoC submission enforces anonymity constraints.

## Week 6 - Dashboard MVP
- Add dashboard summary endpoint with:
  - counts by IoC type
  - recent IoCs
  - recent scans
- Deliverable: JSON summary consumed by frontend.

## Week 7 - Frontend Skeleton
- Build Vite React TypeScript app scaffolding.
- Create pages/components for guest scan, login, submit IoC, dashboard.
- Add API client wrappers and base UI wiring.
- Deliverable: `npm run dev` starts and page navigation works.

## Week 8 - Frontend Integration
- Connect forms to backend endpoints.
- Render safety report with status and reasons.
- Add placeholder PDF download button workflow.
- Deliverable: end-to-end manual flow for guest scan and login flow.

## Week 9 - Testing Expansion
- Add pytest endpoint tests and service tests.
- Add VT httpx mocking tests.
- Add anonymizer and cache hit/miss coverage.
- Deliverable: repeatable test run with clear pass/fail report.

## Week 10 - Documentation and Evidence
- Complete API contract and test traceability.
- Capture screenshots, logs, and demo scripts.
- Deliverable: updated docs and evidence index.

## Week 11 - Hardening and Refinement
- Improve error handling for rate limits/timeouts.
- Improve UI clarity and accessibility basics.
- Deliverable: polished MVP demo candidate.

## Week 12 - Final Demo and Handover
- Run full walkthrough demo.
- Present privacy design and security decisions.
- Hand over code, docs, and known limitations.
- Deliverable: final report + demo package.
