import { scanQueue } from "../../mocks/overview";
import { panelStyle, sectionTitleStyle } from "../../app/styles";

export default function QueueSnapshot() {
  return (
    <section style={panelStyle}>
      <h3 style={sectionTitleStyle}>Queue Snapshot</h3>
      <div style={{ display: "grid", gap: "10px" }}>
        {scanQueue.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid #d5c5a7",
              borderRadius: "16px",
              padding: "12px",
              background: "#fffdf8",
            }}
          >
            <strong>{item.id}</strong>
            <p style={{ margin: "6px 0 0", color: "#5e5a52" }}>
              {item.artifactType} • {item.aiMode} AI • {item.state}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
