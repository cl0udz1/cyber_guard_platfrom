import { mutedTextStyle, panelStyle, pillStyle, sectionTitleStyle } from "../../app/styles";

interface PlaceholderPanelProps {
  title: string;
  ownerHint: string;
  summary: string;
  todo: string[];
}

export default function PlaceholderPanel(props: PlaceholderPanelProps) {
  return (
    <section style={panelStyle}>
      <div style={pillStyle("warning")}>Scaffold Placeholder</div>
      <h3 style={{ ...sectionTitleStyle, marginTop: "14px" }}>{props.title}</h3>
      <p style={mutedTextStyle}>{props.summary}</p>
      <p style={{ ...mutedTextStyle, marginTop: "10px", fontWeight: 700 }}>Likely owner: {props.ownerHint}</p>
      <ul style={{ margin: "12px 0 0", paddingLeft: "20px", color: "#5e5a52", lineHeight: 1.7 }}>
        {props.todo.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
