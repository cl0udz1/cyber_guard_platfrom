import { artifactOptions, pipelineStages } from "../../features/scan-jobs/scanJobMocks";
import { mutedTextStyle, panelStyle, sectionTitleStyle } from "../../app/styles";

export default function ArtifactSubmissionPanel() {
  return (
    <section style={panelStyle}>
      <h3 style={sectionTitleStyle}>Artifact Types</h3>
      <div style={{ display: "grid", gap: "10px" }}>
        {artifactOptions.map((option) => (
          <article key={option.type} style={{ padding: "12px", borderRadius: "16px", background: "#f4ead7" }}>
            <strong>{option.label}</strong>
            <p style={{ ...mutedTextStyle, marginTop: "6px" }}>{option.detail}</p>
          </article>
        ))}
      </div>
      <h4 style={{ margin: "18px 0 10px" }}>Pipeline Draft</h4>
      <ul style={{ margin: 0, paddingLeft: "18px", color: "#5e5a52", lineHeight: 1.7 }}>
        {pipelineStages.map((stage) => (
          <li key={stage.name}>
            <strong>{stage.name}:</strong> {stage.detail}
          </li>
        ))}
      </ul>
    </section>
  );
}
