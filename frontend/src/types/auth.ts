export type RoleTone = "org_owner" | "org_admin" | "analyst" | "viewer" | "platform_admin";

export interface AuthMilestone {
  title: string;
  ownerHint: string;
  note: string;
}
