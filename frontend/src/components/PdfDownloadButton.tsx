/**
 * Purpose:
 *   Allow users to download a simple scan report file from frontend.
 * Inputs:
 *   Current `ScanResponse` data.
 * Outputs:
 *   Triggers browser download (`.pdf` placeholder text file for now).
 * Dependencies:
 *   Browser Blob and URL APIs.
 * TODO Checklist:
 *   - [ ] Replace client-generated placeholder with backend PDF endpoint.
 *   - [ ] Add real PDF binary response handling (`application/pdf`).
 */

import type * as React from "react";
import type { ScanResponse } from "../types/scan";

interface PdfDownloadButtonProps {
  report: ScanResponse | null;
}

export default function PdfDownloadButton({ report }: PdfDownloadButtonProps) {
  if (!report) return null;
  const currentReport = report;

  function handleDownload() {
    // TODO: Replace this placeholder with backend-generated report bytes.
    const content = [
      "cyber_guard_platform - Safety Report",
      `Scan ID: ${currentReport.scan_id}`,
      `Status: ${currentReport.status}`,
      `Score: ${currentReport.score}`,
      `Created At: ${currentReport.created_at}`,
      `Summary: ${currentReport.summary}`,
      "Reasons:",
      ...currentReport.reasons.map((reason) => `- ${reason}`),
    ].join("\n");

    const blob = new Blob([content], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = `safety-report-${currentReport.scan_id}.pdf`;
    anchor.click();
    URL.revokeObjectURL(url);
  }

  return (
    <button onClick={handleDownload} style={styles.button}>
      Download Safety Report (PDF)
    </button>
  );
}

const styles: Record<string, React.CSSProperties> = {
  button: {
    border: "1px solid #385878",
    borderRadius: "8px",
    background: "#eff6ff",
    padding: "8px 12px",
    cursor: "pointer",
    width: "fit-content",
  },
};




