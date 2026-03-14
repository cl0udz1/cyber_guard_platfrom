import type { ReviewItem } from "../../types/publicThreat";
import { panelStyle, sectionTitleStyle } from "../../app/styles";

interface ReviewQueuePanelProps {
  items: ReviewItem[];
}

export default function ReviewQueuePanel(props: ReviewQueuePanelProps) {
  return (
    <section style={panelStyle}>
      <h3 style={sectionTitleStyle}>Moderation Queue</h3>
      <div style={{ display: "grid", gap: "10px" }}>
        {props.items.map((item) => (
          <article key={item.id} style={{ border: "1px solid #d5c5a7", borderRadius: "16px", padding: "12px" }}>
            <strong>{item.id}</strong>
            <p style={{ margin: "6px 0 0", color: "#5e5a52" }}>
              {item.type} • {item.status}
            </p>
            <p style={{ margin: "6px 0 0", color: "#5e5a52" }}>{item.note}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
