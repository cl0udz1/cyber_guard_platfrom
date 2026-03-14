/**
 * Purpose:
 *   Shared theme tokens and layout styles for the scaffold UI.
 * Inputs:
 *   Imported by pages and components.
 * Outputs:
 *   Readable style objects that keep placeholders visually consistent.
 * Dependencies:
 *   React CSSProperties typing only.
 */

import type { CSSProperties } from "react";

export const theme = {
  ink: "#1c1b18",
  muted: "#5e5a52",
  border: "#d5c5a7",
  surface: "#fff9ef",
  surfaceAlt: "#f4ead7",
  accent: "#0f766e",
  accentSoft: "#d4f4ed",
  warning: "#a14d0d",
  warningSoft: "#fde9d7",
  danger: "#9f2d20",
  shadow: "0 18px 40px rgba(28, 27, 24, 0.10)",
  pageBackground:
    "radial-gradient(circle at top left, rgba(253, 241, 221, 0.95), rgba(246, 236, 218, 0.85) 35%, rgba(232, 245, 241, 0.9) 100%)",
  fontFamily: "'IBM Plex Sans', 'Trebuchet MS', sans-serif",
};

export const shellStyles: Record<string, CSSProperties> = {
  page: {
    minHeight: "100vh",
    background: theme.pageBackground,
    color: theme.ink,
    fontFamily: theme.fontFamily,
    padding: "24px",
  },
  frame: {
    maxWidth: "1280px",
    margin: "0 auto",
    display: "grid",
    gridTemplateColumns: "280px minmax(0, 1fr)",
    gap: "20px",
  },
  sidebar: {
    background: "rgba(255, 249, 239, 0.9)",
    border: `1px solid ${theme.border}`,
    borderRadius: "24px",
    padding: "20px",
    boxShadow: theme.shadow,
    alignSelf: "start",
    position: "sticky",
    top: "20px",
  },
  main: {
    display: "grid",
    gap: "20px",
  },
  hero: {
    background: "linear-gradient(135deg, rgba(255, 248, 235, 0.96), rgba(233, 246, 242, 0.96))",
    border: `1px solid ${theme.border}`,
    borderRadius: "28px",
    padding: "28px",
    boxShadow: theme.shadow,
  },
  eyebrow: {
    margin: 0,
    textTransform: "uppercase",
    letterSpacing: "0.12em",
    fontSize: "12px",
    color: theme.warning,
    fontWeight: 700,
  },
  heroTitle: {
    margin: "10px 0 10px",
    fontSize: "40px",
    lineHeight: 1,
    fontWeight: 800,
  },
  heroCopy: {
    margin: 0,
    maxWidth: "820px",
    color: theme.muted,
    lineHeight: 1.6,
    fontSize: "16px",
  },
  cardGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
    gap: "16px",
  },
};

export const panelStyle: CSSProperties = {
  background: theme.surface,
  border: `1px solid ${theme.border}`,
  borderRadius: "20px",
  padding: "18px",
  boxShadow: "0 10px 24px rgba(28, 27, 24, 0.06)",
};

export const sectionTitleStyle: CSSProperties = {
  margin: "0 0 10px",
  fontSize: "22px",
  fontWeight: 800,
};

export const mutedTextStyle: CSSProperties = {
  margin: 0,
  color: theme.muted,
  lineHeight: 1.6,
};

export function pillStyle(kind: "accent" | "warning" | "neutral"): CSSProperties {
  const lookup = {
    accent: { background: theme.accentSoft, color: theme.accent },
    warning: { background: theme.warningSoft, color: theme.warning },
    neutral: { background: theme.surfaceAlt, color: theme.ink },
  };
  return {
    display: "inline-flex",
    alignItems: "center",
    gap: "6px",
    borderRadius: "999px",
    padding: "6px 10px",
    fontSize: "12px",
    fontWeight: 700,
    ...lookup[kind],
  };
}
