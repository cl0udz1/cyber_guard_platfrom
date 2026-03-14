import type { ReportCard } from "../../types/report";
import { mutedTextStyle, panelStyle, pillStyle, sectionTitleStyle } from "../../app/styles";

interface ReportSummaryCardProps {
  report: ReportCard;
}

export default function ReportSummaryCard(props: ReportSummaryCardProps) {
  return (
    <section style={panelStyle}>
      <div style={pillStyle(props.report.publicationState.includes("pending") ? "warning" : "accent")}>
        {props.report.publicationState}
      </div>
      <h3 style={{ ...sectionTitleStyle, marginTop: "14px" }}>{props.report.title}</h3>
      <p style={{ ...mutedTextStyle, marginBottom: "10px" }}>Severity: {props.report.severity}</p>
      <ul style={{ margin: 0, paddingLeft: "18px", color: "#5e5a52", lineHeight: 1.7 }}>
        {props.report.sections.map((section) => (
          <li key={section}>{section}</li>
        ))}
      </ul>
    </section>
  );
}
