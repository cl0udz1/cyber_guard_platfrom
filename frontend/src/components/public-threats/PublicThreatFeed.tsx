import type { PublicThreatCard } from "../../types/publicThreat";
import { mutedTextStyle, panelStyle, sectionTitleStyle } from "../../app/styles";

interface PublicThreatFeedProps {
  items: PublicThreatCard[];
}

export default function PublicThreatFeed(props: PublicThreatFeedProps) {
  return (
    <section style={panelStyle}>
      <h3 style={sectionTitleStyle}>Public Feed Draft</h3>
      <div style={{ display: "grid", gap: "12px" }}>
        {props.items.map((item) => (
          <article key={item.title} style={{ borderBottom: "1px solid #eadcc3", paddingBottom: "12px" }}>
            <strong>{item.title}</strong>
            <p style={{ ...mutedTextStyle, marginTop: "6px" }}>{item.summary}</p>
            <p style={{ ...mutedTextStyle, marginTop: "6px", fontWeight: 700 }}>
              {item.severity} severity • {item.source}
            </p>
          </article>
        ))}
      </div>
    </section>
  );
}
