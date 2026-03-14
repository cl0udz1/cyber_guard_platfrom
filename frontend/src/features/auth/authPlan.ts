import type { AuthMilestone } from "../../types/auth";

export const authMilestones: AuthMilestone[] = [
  {
    title: "Registration + login",
    ownerHint: "Backend API + frontend auth owner",
    note: "Support account creation for users and organization-linked members.",
  },
  {
    title: "Membership-aware /me",
    ownerHint: "Backend services owner",
    note: "Expose org/workspace context so the UI can switch views correctly.",
  },
  {
    title: "Role gates",
    ownerHint: "Security/testing owner",
    note: "Protect admin review and publish workflows with simple RBAC first.",
  },
];
