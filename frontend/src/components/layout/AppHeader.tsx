import { shellStyles } from "../../app/styles";

interface AppHeaderProps {
  activeLabel: string;
  subtitle: string;
}

export default function AppHeader(props: AppHeaderProps) {
  return (
    <header style={shellStyles.hero}>
      <p style={shellStyles.eyebrow}>Senior Project II Scaffold</p>
      <h1 style={shellStyles.heroTitle}>Cyber Guard Platform</h1>
      <p style={shellStyles.heroCopy}>{props.subtitle}</p>
      <p style={{ ...shellStyles.heroCopy, marginTop: "14px", fontWeight: 700 }}>
        Current focus: {props.activeLabel}
      </p>
    </header>
  );
}
