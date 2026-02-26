/**
 * Purpose:
 *   Very simple chart-like view for dashboard counts by IoC type.
 * Inputs:
 *   `countsByType` key/value map.
 * Outputs:
 *   Lightweight horizontal bar visualization.
 * Dependencies:
 *   React rendering only (no chart library yet).
 * TODO Checklist:
 *   - [ ] Replace with real chart library (e.g., Recharts) if desired.
 *   - [ ] Add trend over time lines/areas from backend trend API.
 */

interface ChartsProps {
  countsByType: Record<string, number>;
}

export default function Charts({ countsByType }: ChartsProps) {
  const entries = Object.entries(countsByType);
  const maxValue = Math.max(1, ...entries.map(([, value]) => value));

  if (entries.length === 0) {
    return <p style={styles.empty}>No IoC data yet.</p>;
  }

  return (
    <div style={styles.container}>
      {entries.map(([type, value]) => {
        const widthPercent = Math.max(8, Math.round((value / maxValue) * 100));
        return (
          <div key={type} style={styles.row}>
            <span style={styles.label}>{type}</span>
            <div style={styles.barTrack}>
              <div style={{ ...styles.barFill, width: `${widthPercent}%` }} />
            </div>
            <strong style={styles.value}>{value}</strong>
          </div>
        );
      })}
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: "grid",
    gap: "8px",
  },
  row: {
    display: "grid",
    gridTemplateColumns: "120px 1fr 40px",
    gap: "10px",
    alignItems: "center",
  },
  label: {
    textTransform: "capitalize",
    color: "#1f3e5f",
  },
  barTrack: {
    borderRadius: "999px",
    background: "#e4edf7",
    height: "12px",
    overflow: "hidden",
  },
  barFill: {
    height: "100%",
    borderRadius: "999px",
    background: "linear-gradient(90deg, #2f7ac7, #55a7ff)",
  },
  value: {
    textAlign: "right",
  },
  empty: {
    margin: 0,
    color: "#456481",
  },
};




