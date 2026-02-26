/**
 * Purpose:
 *   Small frontend formatting helpers for dates/status labels.
 * Inputs:
 *   Raw ISO strings and status values.
 * Outputs:
 *   User-friendly strings/colors.
 * Dependencies:
 *   Browser Intl APIs.
 * TODO Checklist:
 *   - [ ] Add localization support if required by project scope.
 */

import type { ScanStatus } from "../types/scan";

export function formatIsoDate(iso: string): string {
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) {
    return iso;
  }
  return new Intl.DateTimeFormat("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}

export function getStatusColor(status: ScanStatus): string {
  if (status === "SAFE") return "#1f7a3f";
  if (status === "SUSPICIOUS") return "#ad7f00";
  return "#b12828";
}
