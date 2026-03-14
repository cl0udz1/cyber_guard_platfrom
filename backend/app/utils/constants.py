"""
Purpose:
    Small shared constants that document scaffold defaults and route assumptions.
Inputs:
    Used by services, docs, and tests.
Outputs:
    Centralized constant values for demo records and planned integrations.
Dependencies:
    None.
TODO Checklist:
    - [ ] Move large mock datasets into fixtures if they become noisy here.
    - [ ] Keep these values aligned with frontend mock data and docs.
"""

DEFAULT_ORGANIZATION_ID = "demo-org"
DEFAULT_WORKSPACE_ID = "demo-workspace"
DEFAULT_PUBLIC_FEED_TITLE = "Cyber Guard Public Threats"

PLANNED_THREAT_SOURCES = [
    "virustotal",
    "source_a",
    "source_b",
    "source_c",
]

PLANNED_REPORT_SECTIONS = [
    "artifact_summary",
    "ioc_overview",
    "source_enrichment",
    "ai_analysis",
    "recommended_actions",
]
