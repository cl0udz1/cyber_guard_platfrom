/**
 * Purpose:
 *   Base fetch wrapper for backend API requests.
 * Inputs:
 *   Endpoint path, request options, optional auth token.
 * Outputs:
 *   Parsed JSON response or thrown Error.
 * Dependencies:
 *   Browser Fetch API + Vite env variables.
 * TODO Checklist:
 *   - [ ] Add retry logic for transient network failures.
 *   - [ ] Add centralized toast/error reporting integration.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export async function apiRequest<T>(
  path: string,
  options: RequestInit = {},
  token?: string
): Promise<T> {
  const headers = new Headers(options.headers ?? {});

  const isFormData = options.body instanceof FormData;
  if (!isFormData) {
    headers.set("Content-Type", "application/json");
  }
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    let detail = `${response.status} ${response.statusText}`;
    try {
      const payload = await response.json();
      if (typeof payload?.detail === "string") {
        detail = payload.detail;
      }
    } catch {
      // Keep fallback detail text.
    }
    throw new Error(detail);
  }

  return (await response.json()) as T;
}
