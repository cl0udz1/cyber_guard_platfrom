import ReportSummaryCard from "../../components/reports/ReportSummaryCard";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";
import { reportSections } from "../../features/reports/reportPlan";
import { reportCards } from "../../mocks/overview";

export default function ReportsPage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "16px" }}>
        {reportCards.map((report) => (
          <ReportSummaryCard key={report.id} report={report} />
        ))}
      </div>
      <PlaceholderPanel
        title="Threat Report Shape"
        ownerHint="Backend report owner + frontend report owner"
        summary="Reports should stay implementation-friendly: one clear artifact story, source summaries, optional AI notes, and publication status."
        todo={reportSections}
      />
    </div>
  );
}
