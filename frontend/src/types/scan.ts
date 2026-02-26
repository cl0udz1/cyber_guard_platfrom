/**
 * Purpose:
 *   Shared TypeScript types for scan request/response payloads.
 * Inputs:
 *   Data from backend scan endpoints.
 * Outputs:
 *   Type-safe objects used by pages/components.
 * Dependencies:
 *   None (type declarations only).
 * TODO Checklist:
 *   - [ ] Add richer report metadata (engine counts, risk categories).
 */

export type ScanStatus = "SAFE" | "SUSPICIOUS" | "MALICIOUS";

export interface ScanUrlRequest {
  url: string;
}

export interface ScanResponse {
  scan_id: string;
  status: ScanStatus;
  score: number;
  summary: string;
  reasons: string[];
  created_at: string;
}
