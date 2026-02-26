/**
 * Purpose:
 *   Present scan result in beginner-friendly SAFE/SUSPICIOUS/MALICIOUS format.
 * Inputs:
 *   `ScanResponse` object (or null before first scan).
 * Outputs:
 *   Readable report card with score, summary, reasons, and advice.
 * Dependencies:
 *   Scan type definitions and formatter helpers.
 * TODO Checklist:
 *   - [ ] Replace static advice with context-aware recommendations.
 *   - [ ] Add collapsible section for raw VT metadata.
 */

import type * as React from "react";
import type { ScanResponse } from "../types/scan";
import { formatIsoDate, getStatusColor } from "../utils/formatters";

interface SafetyReportProps {
  report: ScanResponse | null;
}

function getAdvice(status: ScanResponse["status"]): string {
  if (status === "MALICIOUS") {
    return "Advice: Block this indicator immediately and alert your team.";
  }
  if (status === "SUSPICIOUS") {
    return "Advice: Treat with caution, verify with additional tools, and monitor activity.";
  }
  return "Advice: No immediate red flags, but keep monitoring and re-scan if context changes.";
}

export default function SafetyReport({ report }: SafetyReportProps) {
  if (!report) {
    return (
      <section style={styles.empty}>
        <h3 style={styles.heading}>Safety Report</h3>
        <p style={styles.emptyText}>Run a scan to see SAFE/SUSPICIOUS/MALICIOUS results here.</p>
      </section>
    );
  }

  return (
    <section style={styles.card}>
      <h3 style={styles.heading}>Safety Report</h3>
      <p style={{ ...styles.status, color: getStatusColor(report.status) }}>{report.status}</p>
      <p style={styles.meta}>Score: {report.score}/100</p>
      <p style={styles.meta}>Scan ID: {report.scan_id}</p>
      <p style={styles.meta}>Created: {formatIsoDate(report.created_at)}</p>
      <p style={styles.summary}>{report.summary}</p>

      <div>
        <strong>Reasons</strong>
        <ul style={styles.reasonList}>
          {report.reasons.map((reason) => (
            <li key={reason}>{reason}</li>
          ))}
        </ul>
      </div>

      <p style={styles.advice}>{getAdvice(report.status)}</p>
    </section>
  );
}

const styles: Record<string, React.CSSProperties> = {
  card: {
    border: "1px solid #d4dfec",
    borderRadius: "12px",
    padding: "16px",
    background: "#ffffff",
  },
  empty: {
    border: "1px dashed #a8bfd7",
    borderRadius: "12px",
    padding: "16px",
    background: "#f8fbff",
  },
  heading: {
    margin: "0 0 8px 0",
  },
  status: {
    fontSize: "24px",
    fontWeight: 700,
    margin: "0 0 6px 0",
  },
  meta: {
    margin: "2px 0",
    color: "#39526b",
    fontSize: "14px",
  },
  summary: {
    marginTop: "12px",
    fontWeight: 500,
  },
  reasonList: {
    marginTop: "6px",
  },
  advice: {
    marginTop: "12px",
    padding: "10px",
    borderRadius: "8px",
    background: "#eef5fd",
    color: "#123252",
  },
  emptyText: {
    margin: 0,
    color: "#35506b",
  },
};




