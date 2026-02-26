/**
 * Purpose:
 *   Auth-protected dashboard showing IoC counts and recent activity.
 * Inputs:
 *   Auth token from parent app.
 * Outputs:
 *   Summary cards/lists from dashboard endpoint.
 * Dependencies:
 *   Dashboard endpoint helper and chart component.
 * TODO Checklist:
 *   - [ ] Add auto-refresh polling or manual refresh control.
 *   - [ ] Add trend time-series chart once backend provides buckets.
 */

import type * as React from "react";
import { useEffect, useState } from "react";

import { getDashboardSummary } from "../api/endpoints";
import Charts from "../components/Charts";
import type { DashboardSummaryResponse } from "../types/ioc";
import { formatIsoDate } from "../utils/formatters";

interface DashboardPageProps {
  token: string;
}

export default function DashboardPage({ token }: DashboardPageProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [summary, setSummary] = useState<DashboardSummaryResponse | null>(null);

  useEffect(() => {
    async function load() {
      if (!token) {
        setSummary(null);
        return;
      }
      setLoading(true);
      setError("");
      try {
        const response = await getDashboardSummary(token);
        setSummary(response);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Failed to load dashboard.");
      } finally {
        setLoading(false);
      }
    }
    void load();
  }, [token]);

  if (!token) {
    return (
      <section style={styles.page}>
        <h2 style={styles.heading}>Dashboard</h2>
        <p style={styles.info}>Login is required to view organization dashboard data.</p>
      </section>
    );
  }

  return (
    <section style={styles.page}>
      <h2 style={styles.heading}>Threat Feed Dashboard</h2>
      {loading ? <p style={styles.info}>Loading dashboard...</p> : null}
      {error ? <p style={styles.error}>{error}</p> : null}

      {summary ? (
        <>
          <div style={styles.card}>
            <h3 style={styles.subheading}>Counts by IoC Type</h3>
            <Charts countsByType={summary.counts_by_type} />
          </div>

          <div style={styles.grid}>
            <section style={styles.card}>
              <h3 style={styles.subheading}>Recent IoCs</h3>
              {summary.recent_iocs.length === 0 ? (
                <p style={styles.info}>No IoCs yet.</p>
              ) : (
                <ul style={styles.list}>
                  {summary.recent_iocs.map((ioc) => (
                    <li key={ioc.ioc_id}>
                      <strong>{ioc.type}</strong>: {ioc.value} (confidence {ioc.confidence}){" "}
                      <span style={styles.timestamp}>[{formatIsoDate(ioc.created_at)}]</span>
                    </li>
                  ))}
                </ul>
              )}
            </section>

            <section style={styles.card}>
              <h3 style={styles.subheading}>Recent Scans</h3>
              {summary.recent_scans.length === 0 ? (
                <p style={styles.info}>No scans yet.</p>
              ) : (
                <ul style={styles.list}>
                  {summary.recent_scans.map((scan) => (
                    <li key={scan.scan_id}>
                      <strong>{scan.status}</strong> - {scan.summary}{" "}
                      <span style={styles.timestamp}>[{formatIsoDate(scan.created_at)}]</span>
                    </li>
                  ))}
                </ul>
              )}
            </section>
          </div>
        </>
      ) : null}
    </section>
  );
}

const styles: Record<string, React.CSSProperties> = {
  page: {
    display: "grid",
    gap: "12px",
  },
  heading: {
    margin: 0,
  },
  subheading: {
    margin: "0 0 10px 0",
  },
  info: {
    margin: 0,
    color: "#3c5b78",
  },
  error: {
    margin: 0,
    color: "#b12828",
    fontWeight: 600,
  },
  card: {
    border: "1px solid #d4dfec",
    borderRadius: "12px",
    padding: "14px",
    background: "#ffffff",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
    gap: "12px",
  },
  list: {
    margin: 0,
    paddingLeft: "18px",
    display: "grid",
    gap: "8px",
  },
  timestamp: {
    color: "#4f6985",
    fontSize: "13px",
  },
};




