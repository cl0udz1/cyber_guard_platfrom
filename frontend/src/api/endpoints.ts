/**
 * Purpose:
 *   Centralize route groups for the refreshed Cyber Guard contract.
 * Inputs:
 *   Used by future frontend integration work and assignment planning.
 * Outputs:
 *   A clear list of backend endpoints by domain.
 * Dependencies:
 *   Optional shared `apiRequest` wrapper for future wiring.
 * TODO Checklist:
 *   - [ ] Add typed wrappers once individual pages move from mocks to live data.
 *   - [ ] Keep these paths aligned with `docs/API_CONTRACT.md`.
 */

export const apiGroups = {
  auth: {
    register: "/api/v1/auth/register",
    login: "/api/v1/auth/login",
    me: "/api/v1/auth/me",
  },
  users: {
    me: "/api/v1/users/me",
    memberships: "/api/v1/users/me/memberships",
  },
  orgs: {
    create: "/api/v1/orgs",
    detail: (orgId: string) => `/api/v1/orgs/${orgId}`,
    memberships: (orgId: string) => `/api/v1/orgs/${orgId}/memberships`,
  },
  workspaces: {
    list: "/api/v1/workspaces",
    create: "/api/v1/workspaces",
    detail: (workspaceId: string) => `/api/v1/workspaces/${workspaceId}`,
  },
  scanJobs: {
    list: "/api/v1/scan-jobs",
    create: "/api/v1/scan-jobs",
    detail: (scanJobId: string) => `/api/v1/scan-jobs/${scanJobId}`,
  },
  reports: {
    detail: (reportId: string) => `/api/v1/reports/${reportId}`,
    publishRequest: (reportId: string) => `/api/v1/reports/${reportId}/publish-request`,
    externalUpload: "/api/v1/reports/external-upload",
  },
  dashboard: {
    overview: "/api/v1/dashboard/overview",
  },
  publicThreats: {
    list: "/api/v1/public-threats",
    detail: (publicReportId: string) => `/api/v1/public-threats/${publicReportId}`,
  },
  adminReviews: {
    queue: "/api/v1/admin-reviews/queue",
    decision: (reviewId: string) => `/api/v1/admin-reviews/${reviewId}/decision`,
  },
  integrations: {
    catalog: "/api/v1/integrations/catalog",
    publicApi: "/api/v1/integrations/public-threats-api",
  },
} as const;
