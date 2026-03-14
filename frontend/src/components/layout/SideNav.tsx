import type { ViewKey } from "../../app/navigation";
import { navItems } from "../../app/navigation";
import { mutedTextStyle, panelStyle, theme } from "../../app/styles";

interface SideNavProps {
  activeView: ViewKey;
  onSelect: (view: ViewKey) => void;
}

export default function SideNav(props: SideNavProps) {
  return (
    <aside style={{ ...panelStyle, padding: "20px" }}>
      <p style={{ margin: 0, textTransform: "uppercase", letterSpacing: "0.12em", fontSize: "12px", fontWeight: 700 }}>
        Implementation Map
      </p>
      <p style={{ ...mutedTextStyle, marginTop: "12px" }}>
        Each section mirrors a folder in `frontend/src` so ownership is easy to assign.
      </p>
      <nav style={{ display: "grid", gap: "10px", marginTop: "18px" }}>
        {navItems.map((item) => {
          const active = item.key === props.activeView;
          return (
            <button
              key={item.key}
              onClick={() => props.onSelect(item.key)}
              style={{
                textAlign: "left",
                borderRadius: "18px",
                border: `1px solid ${active ? theme.accent : theme.border}`,
                background: active ? theme.accentSoft : theme.surface,
                color: theme.ink,
                padding: "12px 14px",
                cursor: "pointer",
              }}
            >
              <strong style={{ display: "block" }}>{item.label}</strong>
              <span style={{ color: theme.muted, fontSize: "13px" }}>{item.hint}</span>
            </button>
          );
        })}
      </nav>
    </aside>
  );
}
