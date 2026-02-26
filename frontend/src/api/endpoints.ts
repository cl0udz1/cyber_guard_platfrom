/**
 * Purpose:
 *   Endpoint-specific API helpers that map to backend contract routes.
 * Inputs:
 *   Typed request payloads from pages/components.
 * Outputs:
 *   Typed backend responses.
 * Dependencies:
 *   `apiRequest` wrapper and frontend types.
 * TODO Checklist:
 *   - [ ] Add pagination query parameters for dashboard history endpoints.
 *   - [ ] Add PDF endpoint integration once backend route is added.
 */

import { apiRequest } from "./client";
import type {
  DashboardSummaryResponse,
  IocSubmitRequest,
  IocSubmitResponse,
} from "../types/ioc";
import type { ScanResponse, ScanUrlRequest } from "../types/scan";
import type { LoginRequest, MeResponse, TokenResponse } from "../types/user";

export function postScanUrl(payload: ScanUrlRequest): Promise<ScanResponse> {
  return apiRequest<ScanResponse>("/api/v1/scan/url", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export function postScanFile(file: File): Promise<ScanResponse> {
  const body = new FormData();
  body.append("file", file);
  return apiRequest<ScanResponse>("/api/v1/scan/file", {
    method: "POST",
    body,
  });
}

export function getScanById(scanId: string): Promise<ScanResponse> {
  return apiRequest<ScanResponse>(`/api/v1/scan/${scanId}`, { method: "GET" });
}

export function postLogin(payload: LoginRequest): Promise<TokenResponse> {
  return apiRequest<TokenResponse>("/api/v1/auth/login", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export function getMe(token: string): Promise<MeResponse> {
  return apiRequest<MeResponse>("/api/v1/auth/me", { method: "GET" }, token);
}

export function postSubmitIoc(payload: IocSubmitRequest, token: string): Promise<IocSubmitResponse> {
  return apiRequest<IocSubmitResponse>(
    "/api/v1/ioc/submit",
    {
      method: "POST",
      body: JSON.stringify(payload),
    },
    token
  );
}

export function getDashboardSummary(token: string): Promise<DashboardSummaryResponse> {
  return apiRequest<DashboardSummaryResponse>("/api/v1/dashboard/summary", { method: "GET" }, token);
}
