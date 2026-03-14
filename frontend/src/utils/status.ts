export function statusTone(status: string): "accent" | "warning" | "neutral" {
  if (status.includes("published") || status.includes("completed") || status.includes("approved")) {
    return "accent";
  }
  if (status.includes("pending") || status.includes("review") || status.includes("queued")) {
    return "warning";
  }
  return "neutral";
}
