import type { OrganizationOverview, WorkspaceRoleGuide } from "../../types/org";

export const organizationOverview: OrganizationOverview = {
  organizationName: "Cyber Guard Demo Org",
  workspaceName: "Threat Research Workspace",
  identityBoundary: "Identity and workspace data stay private; only sanitized threat outputs may leave.",
};

export const workspaceRoleGuide: WorkspaceRoleGuide[] = [
  {
    role: "org_owner",
    scope: "organization + workspace",
    responsibilities: "Own structure, invites, and governance decisions.",
  },
  {
    role: "org_admin",
    scope: "workspace operations",
    responsibilities: "Manage workspace settings, integrations, and review requests.",
  },
  {
    role: "analyst",
    scope: "analysis pipeline",
    responsibilities: "Submit artifacts, review reports, and request public publication.",
  },
  {
    role: "viewer",
    scope: "read-only",
    responsibilities: "Read dashboard and report outputs without mutating data.",
  },
];
