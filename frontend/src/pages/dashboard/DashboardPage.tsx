import MetricsBoard from "../../components/dashboard/MetricsBoard";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";
import { dashboardMetrics } from "../../mocks/overview";

export default function DashboardPage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <MetricsBoard metrics={dashboardMetrics} />
      <PlaceholderPanel
        title="Dashboard Ownership Notes"
        ownerHint="Frontend dashboard owner + backend dashboard owner"
        summary="Dashboard work should stay lightweight at first: KPI cards, recent scan states, publish queue visibility, and source usage overview."
        todo={[
          "Wire `/dashboard/overview` before building extra charts.",
          "Keep dashboard private to the active workspace context.",
          "Avoid mixing public feed metrics with identity-linked private metrics.",
        ]}
      />
    </div>
  );
}
