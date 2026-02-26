/**
 * Purpose:
 *   Client-side validation helpers before API submission.
 * Inputs:
 *   Form field values from UI components.
 * Outputs:
 *   Validation result booleans/messages.
 * Dependencies:
 *   Browser URL parser.
 * TODO Checklist:
 *   - [ ] Add robust IoC format validators by type (IP/hash/domain/email).
 */

export function isValidUrlInput(value: string): boolean {
  const trimmed = value.trim();
  if (!trimmed) return false;

  try {
    const normalized = trimmed.includes("://") ? trimmed : `https://${trimmed}`;
    const parsed = new URL(normalized);
    return parsed.hostname.length > 0;
  } catch {
    return false;
  }
}

export function isConfidenceInRange(value: number): boolean {
  return Number.isFinite(value) && value >= 0 && value <= 100;
}
