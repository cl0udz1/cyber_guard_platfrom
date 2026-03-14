import type { DashboardMetric } from "../../types/dashboard";
import { panelStyle, sectionTitleStyle } from "../../app/styles";

interface MetricsBoardProps {
  metrics: DashboardMetric[];
}

export default function MetricsBoard(props: MetricsBoardProps) {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "12px" }}>
      {props.metrics.map((metric) => (
        <section key={metric.label} style={panelStyle}>
          <p style={{ margin: 0, color: "#5e5a52", textTransform: "uppercase", fontSize: "12px", fontWeight: 700 }}>
            {metric.label}
          </p>
          <h3 style={{ ...sectionTitleStyle, margin: "10px 0 6px", fontSize: "32px" }}>{metric.value}</h3>
          <p style={{ margin: 0, color: "#5e5a52", lineHeight: 1.5 }}>{metric.note}</p>
        </section>
      ))}
    </div>
  );
}
