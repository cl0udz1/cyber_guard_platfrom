"""
Purpose:
    Dashboard overview schemas for workspace and organization analytics.
Inputs:
    Dashboard service outputs.
Outputs:
    Typed summary responses for the frontend dashboard page.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add time-range filters and trend buckets when chart work begins.
    - [ ] Add public/private comparison metrics only if they improve the demo.
"""

from pydantic import BaseModel


class DashboardMetric(BaseModel):
    """Single dashboard KPI card."""

    label: str
    value: str
    note: str


class DashboardOverviewResponse(BaseModel):
    """High-level dashboard response."""

    workspace_id: str
    metrics: list[DashboardMetric]
    recent_scan_statuses: dict[str, int]
    publish_queue_count: int
    top_sources: list[str]
