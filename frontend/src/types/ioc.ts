/**
 * Purpose:
 *   Shared TypeScript types for anonymous IoC submission and dashboard data.
 * Inputs:
 *   Data from `/api/v1/ioc/submit` and `/api/v1/dashboard/summary`.
 * Outputs:
 *   Type-safe IoC objects used across frontend pages.
 * Dependencies:
 *   None (type declarations only).
 * TODO Checklist:
 *   - [ ] Add stricter per-type value metadata.
 *   - [ ] Add trend series type for chart component upgrades.
 */

export type IocType = "ip" | "domain" | "url" | "hash" | "email" | "file_name" | "other";

export interface IocSubmitRequest {
  type: IocType;
  value: string;
  confidence: number;
  tags: string[];
  first_seen?: string;
}

export interface IocSubmitResponse {
  ioc_id: string;
  stored: boolean;
}

export interface IocPublicRecord {
  ioc_id: string;
  type: IocType;
  value: string;
  confidence: number;
  tags: string[];
  first_seen: string | null;
  created_at: string;
}

export interface DashboardRecentScan {
  scan_id: string;
  status: "SAFE" | "SUSPICIOUS" | "MALICIOUS";
  score: number;
  summary: string;
  created_at: string;
}

export interface DashboardSummaryResponse {
  counts_by_type: Record<string, number>;
  recent_iocs: IocPublicRecord[];
  recent_scans: DashboardRecentScan[];
}
