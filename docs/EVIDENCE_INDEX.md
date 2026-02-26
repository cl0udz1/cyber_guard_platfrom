# EVIDENCE_INDEX.md - Demo and Verification Artifacts

## Header
- Purpose: Track where evidence files/screenshots/logs for grading are stored.
- Inputs/Outputs: List of artifact names, location, and what requirement they prove.
- Dependencies: Demo recordings, screenshots, test output files.
- TODO Checklist:
  - [ ] Attach actual screenshot/video/log paths.
  - [ ] Add timestamps and owner initials for each artifact.
  - [ ] Keep evidence synchronized with latest commit hash.

## Suggested Evidence Entries

| Evidence ID | Description | Suggested File Path | Requirement(s) |
|---|---|---|---|
| E1 | Backend startup screenshot (`uvicorn app.main:app --reload`) | `docs/evidence/backend-startup.png` | R1-R8 baseline |
| E2 | Frontend startup screenshot (`npm run dev`) | `docs/evidence/frontend-startup.png` | UI readiness |
| E3 | Guest URL scan successful response | `docs/evidence/guest-url-scan.png` | R1 |
| E4 | Guest file scan successful response | `docs/evidence/guest-file-scan.png` | R2 |
| E5 | Login + `/auth/me` proof | `docs/evidence/auth-flow.png` | R4, R5 |
| E6 | IoC anonymizer rejection proof | `docs/evidence/anonymizer-reject.png` | R6 |
| E7 | Dashboard summary render | `docs/evidence/dashboard-summary.png` | R7 |
| E8 | Pytest run output | `docs/evidence/pytest-output.txt` | R1-R8 |

## Notes
- Keep raw test logs and screenshots unedited.
- Include commit hash in final report for reproducibility.
