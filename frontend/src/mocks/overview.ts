import type { DashboardMetric } from "../types/dashboard";
import type { PublicThreatCard, ReviewItem } from "../types/publicThreat";
import type { QueueItem } from "../types/scan";
import type { ReportCard } from "../types/report";

export const dashboardMetrics: DashboardMetric[] = [
  { label: "Queued Jobs", value: "3", note: "Artifacts waiting for enrichment or report generation." },
  { label: "Private Reports", value: "8", note: "Generated reports visible inside the workspace only." },
  { label: "Public Posts", value: "2", note: "Sanitized public reports already approved." },
];

export const scanQueue: QueueItem[] = [
  { id: "job-101", artifactType: "url", state: "completed", aiMode: "local" },
  { id: "job-102", artifactType: "file", state: "enriching", aiMode: "api" },
  { id: "job-103", artifactType: "email_signal", state: "queued", aiMode: "off" },
];

export const reportCards: ReportCard[] = [
  {
    id: "report-201",
    title: "Phishing URL infrastructure correlation",
    severity: "high",
    sections: ["Artifact summary", "IOC overview", "Source comparison", "Publishing decision"],
    publicationState: "private",
  },
  {
    id: "report-202",
    title: "Malicious attachment hash lookup",
    severity: "medium",
    sections: ["Artifact summary", "Source enrichment", "AI note", "Recommended actions"],
    publicationState: "pending_review",
  },
];

export const publicThreatCards: PublicThreatCard[] = [
  {
    title: "Credential phishing infrastructure indicators",
    severity: "medium",
    source: "workspace_publish",
    summary: "An anonymized report with indicators extracted from a private workspace analysis.",
  },
  {
    title: "External campaign report awaiting API publication",
    severity: "high",
    source: "external_report_upload",
    summary: "Admin-reviewed public-safe summary prepared for the threats page and future API.",
  },
];

export const reviewQueue: ReviewItem[] = [
  { id: "review-301", type: "external_report_upload", status: "pending_review", note: "Check redactions." },
  { id: "review-302", type: "report_publish_request", status: "approved", note: "Ready for public feed." },
];
