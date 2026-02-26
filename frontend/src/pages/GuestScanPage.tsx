/**
 * Purpose:
 *   Guest scanning workflow page (no login required).
 * Inputs:
 *   URL text or file input from user.
 * Outputs:
 *   Displays scan report and allows PDF download.
 * Dependencies:
 *   API endpoint helpers and scan UI components.
 * TODO Checklist:
 *   - [ ] Add loading skeletons and richer empty-state guidance.
 *   - [ ] Add "scan by previous scan_id" form for retrieval.
 */

import type * as React from "react";
import { useState } from "react";

import { postScanFile, postScanUrl } from "../api/endpoints";
import FileUpload from "../components/FileUpload";
import PdfDownloadButton from "../components/PdfDownloadButton";
import SafetyReport from "../components/SafetyReport";
import UrlInput from "../components/UrlInput";
import type { ScanResponse } from "../types/scan";

export default function GuestScanPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [report, setReport] = useState<ScanResponse | null>(null);

  async function handleUrlSubmit(url: string) {
    setError("");
    setLoading(true);
    try {
      const result = await postScanUrl({ url });
      setReport(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to scan URL.");
    } finally {
      setLoading(false);
    }
  }

  async function handleFileSubmit(file: File) {
    setError("");
    setLoading(true);
    try {
      const result = await postScanFile(file);
      setReport(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to scan file.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section style={styles.page}>
      <h2 style={styles.heading}>Guest Scan</h2>
      <p style={styles.description}>
        Scan suspicious URLs or files with a simple SAFE/SUSPICIOUS/MALICIOUS report.
      </p>

      <div style={styles.grid}>
        <UrlInput loading={loading} onSubmit={handleUrlSubmit} />
        <FileUpload loading={loading} onSubmit={handleFileSubmit} />
      </div>

      {error ? <p style={styles.error}>Error: {error}</p> : null}

      <div style={styles.reportBlock}>
        <SafetyReport report={report} />
        <PdfDownloadButton report={report} />
      </div>
    </section>
  );
}

const styles: Record<string, React.CSSProperties> = {
  page: {
    display: "grid",
    gap: "14px",
  },
  heading: {
    margin: 0,
  },
  description: {
    margin: "0 0 6px 0",
    color: "#3b5875",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
    gap: "12px",
  },
  error: {
    margin: 0,
    color: "#b12828",
    fontWeight: 600,
  },
  reportBlock: {
    display: "grid",
    gap: "10px",
  },
};




