# Cyber Guard Platform

This repository is a Senior Project II implementation scaffold, not a finished application. Its job is to act as an implementation map for a 6-person student team: the folder structure, placeholders, API stubs, diagrams, weekly TODO files, and ownership notes are the product here.

## What Cyber Guard Is

Cyber Guard is a web platform where users and organizations can:

- create accounts
- join organizations with workspace roles
- submit artifacts for analysis by file upload, hash, URL, or pasted email signal
- run asynchronous scan jobs
- normalize artifacts, extract IOCs, enrich from multiple threat-intel sources, and optionally use AI analysis
- generate private threat reports and dashboard views
- publish anonymized reports to a public threats page
- upload external reports for anonymous public sharing through admin review
- optionally expose a future Public Threats API

Critical rule: public threat data must remain disconnected from private identity and workspace data.

## What This Repo Is For

- showing the updated product scope clearly
- showing where each backend/frontend concern belongs
- keeping assignment ownership visible
- giving the team a realistic next-step checklist without pretending the whole app is already built

The backend and frontend both run, but many files are intentionally placeholders with rich headers and TODO blocks.

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```

### Validation

```bash
cd backend
pytest -q

cd ../frontend
npm run build
```

Demo passwords in the scaffold:

- org routes: `org-admin-demo`
- admin review routes: `platform-admin-demo`

## Architecture Tree

```text
cyber-guard-platform/
|-- backend/
|   |-- app/
|   |   |-- api/
|   |   |   |-- routes/
|   |   |-- core/
|   |   |-- db/
|   |   |   |-- models/
|   |   |-- models/
|   |   |-- schemas/
|   |   |-- services/
|   |   |   |-- enrichment/
|   |   |   |-- ai/
|   |   |-- utils/
|   |-- tests/
|   |   |-- unit/
|   |   |-- integration/
|   |   |-- contract/
|-- frontend/
|   |-- src/
|   |   |-- api/
|   |   |-- app/
|   |   |-- pages/
|   |   |   |-- auth/
|   |   |   |-- dashboard/
|   |   |   |-- scan/
|   |   |   |-- reports/
|   |   |   |-- public-threats/
|   |   |   |-- admin/
|   |   |   |-- workspace/
|   |   |-- components/
|   |   |-- features/
|   |   |-- types/
|   |   |-- utils/
|   |   |-- mocks/
|-- docs/
|   |-- PROJECT_PLAN.md
|   |-- API_CONTRACT.md
|   |-- TEST_PLAN.md
|   |-- ARCHITECTURE.md
|   |-- DATA_FLOW.md
|   |-- ASSIGNMENT_MAP.md
|   |-- IMPLEMENTATION_STATUS.md
|   |-- WEEK_1_TODO.md ... WEEK_6_TODO.md
|   |-- diagrams/
```

## Implementation Phases

### MVP

1. auth, orgs, workspaces, and RBAC scaffold
2. models, schemas, and API contract alignment
3. async scan orchestration skeleton with multi-source adapters
4. private reports, public sharing, and admin review structure
5. frontend page/component ownership map
6. tests, docs, and implementation tracking

### Later / Phase 2

- public threats API
- richer trend analytics
- real background workers
- real adapter integrations
- real AI provider/local model implementations

## How The Team Should Use This Repo

1. Read [`docs/ASSIGNMENT_MAP.md`](docs/ASSIGNMENT_MAP.md) before splitting work.
2. Use [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md) as the live tracker.
3. Work from the current weekly file in `docs/WEEK_*_TODO.md`.
4. Keep placeholders and TODOs meaningful when adding new files.
5. Preserve the privacy boundary: public threat records must not expose identity/workspace linkage.

## Key Docs

- [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md)
- [`docs/API_CONTRACT.md`](docs/API_CONTRACT.md)
- [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/DATA_FLOW.md`](docs/DATA_FLOW.md)
- [`docs/ASSIGNMENT_MAP.md`](docs/ASSIGNMENT_MAP.md)
- [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md)
- [`docs/diagrams/SYSTEM_OVERVIEW.md`](docs/diagrams/SYSTEM_OVERVIEW.md)
- [`docs/diagrams/DATA_SEPARATION.md`](docs/diagrams/DATA_SEPARATION.md)
- [`docs/diagrams/SCAN_PIPELINE.md`](docs/diagrams/SCAN_PIPELINE.md)
- [`docs/diagrams/SHARING_REVIEW_FLOW.md`](docs/diagrams/SHARING_REVIEW_FLOW.md)
- [`docs/diagrams/ERD.md`](docs/diagrams/ERD.md)
