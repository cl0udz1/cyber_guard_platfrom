# PROJECT_PLAN.md

## Purpose

This plan is for implementing the refreshed Cyber Guard scaffold in a realistic student sequence. It separates MVP commitments from later expansion so the team can deliver something coherent instead of overpromising.

## MVP Scope

The MVP target for this repo should include:

- user and organization account flow scaffold
- organization workspaces and role-based access placeholders
- artifact submission for file/hash/url/email signal
- asynchronous scan job contract
- multi-source enrichment adapter structure
- optional AI mode selection structure
- private threat report generation flow
- workspace dashboard overview
- anonymized public threats publishing flow
- admin review path for external public uploads
- documented Disconnect by Design separation

## Phase 2 Scope

Only enter Phase 2 if MVP is stable:

- public threats API for third-party use
- richer dashboard analytics and filters
- real background worker queue
- real external threat-intel integrations
- real local AI and remote AI provider execution
- export/download workflows beyond simple placeholders

## Delivery Strategy

### Phase 1: Scope Lock + Restructure

- align the repo to the new Cyber Guard concept
- clean outdated VirusTotal-only and guest-only assumptions
- finalize folder ownership and docs structure

### Phase 2: Models + Contracts

- finalize ORM entities and schemas
- freeze scaffold-level API routes
- make role boundaries and public/private separation explicit

### Phase 3: Scan Engine Skeleton

- build artifact normalization, IOC extraction, cache, enrichment adapter, and AI mode skeletons
- keep execution lightweight and synchronous-in-code while exposing async job concepts

### Phase 4: Reports + Sharing

- define threat report structure
- define sanitization/publication workflow
- add admin review queue shape

### Phase 5: Frontend Ownership Map

- create page groups for auth, workspace, scan, reports, dashboard, public threats, and admin review
- wire a navigable shell with clear placeholder responsibilities

### Phase 6: Validation + Handover

- align tests to the new route surface
- update diagrams, TODO files, and implementation tracker
- prepare the repo for team assignment and incremental implementation

## Feasibility Notes

- keep one backend app and one frontend app
- avoid microservices
- avoid full production infrastructure unless required by the course
- use stubs and placeholders aggressively where the implementation is not yet assigned
- prioritize clarity of ownership over feature count

## Suggested Milestone Gates

### Gate 1

- repo tree matches updated concept
- README and assignment docs are current

### Gate 2

- backend route groups, schemas, and models exist
- frontend page groups exist

### Gate 3

- scan job flow, report flow, and public sharing flow are represented end-to-end at scaffold level

### Gate 4

- weekly TODO system is actionable
- implementation status tracker is in use
- tests and docs pass basic validation
