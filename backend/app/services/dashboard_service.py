"""
Purpose:
    Build workspace dashboard overview responses from scan/report activity.
Inputs:
    Workspace scope plus future DB aggregates.
Outputs:
    Typed dashboard summary payloads for the frontend.
Dependencies:
    Dashboard schemas.
TODO Checklist:
    - [ ] Replace placeholder metrics with DB aggregates.
    - [ ] Add time-range filtering and charts once the frontend needs real series data.
"""

from app.schemas.dashboard import DashboardMetric, DashboardOverviewResponse
from app.utils.constants import DEFAULT_WORKSPACE_ID


class DashboardService:
    """Return high-level workspace metrics suitable for scaffold demos."""

    def build_overview(self, workspace_id: str = DEFAULT_WORKSPACE_ID) -> DashboardOverviewResponse:
        """Return a small fixed-shape dashboard response."""
        return DashboardOverviewResponse(
            workspace_id=workspace_id,
            metrics=[
                DashboardMetric(label="Queued Jobs", value="3", note="Async analysis waiting or running."),
                DashboardMetric(label="Reports Ready", value="8", note="Private reports available to analysts."),
                DashboardMetric(label="Public Posts", value="2", note="Approved anonymized reports in public feed."),
            ],
            recent_scan_statuses={"completed": 8, "enriching": 2, "queued": 1},
            publish_queue_count=1,
            top_sources=["virustotal", "source_a", "source_b"],
        )
