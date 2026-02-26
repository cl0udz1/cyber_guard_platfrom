/**
 * Purpose:
 *   Shared TypeScript types for auth requests and user identity payloads.
 * Inputs:
 *   Data from auth endpoints.
 * Outputs:
 *   Type-safe auth objects for pages and API helpers.
 * Dependencies:
 *   None (type declarations only).
 * TODO Checklist:
 *   - [ ] Add refresh token and role-based permission types later.
 */

export interface LoginRequest {
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: "bearer" | string;
}

export interface MeResponse {
  email: string;
  role: string;
}
