/**
 * Purpose:
 *   Centralized navigation metadata for the scaffold shell.
 * Inputs:
 *   Consumed by the side navigation and view switch logic.
 * Outputs:
 *   View keys and labels used across the frontend.
 * Dependencies:
 *   None.
 */

export type ViewKey =
  | "auth"
  | "workspace"
  | "scan"
  | "reports"
  | "dashboard"
  | "public-threats"
  | "admin";

export const navItems: Array<{ key: ViewKey; label: string; hint: string }> = [
  { key: "scan", label: "Scan Jobs", hint: "file/hash/url/email intake" },
  { key: "reports", label: "Reports", hint: "private report ownership" },
  { key: "dashboard", label: "Dashboard", hint: "workspace metrics" },
  { key: "public-threats", label: "Public Threats", hint: "anonymized public feed" },
  { key: "admin", label: "Admin Review", hint: "moderated publishing" },
  { key: "workspace", label: "Workspace", hint: "orgs, roles, structure" },
  { key: "auth", label: "Auth", hint: "user + org access flows" },
];
