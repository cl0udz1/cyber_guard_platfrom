import type { ArtifactOption, PipelineStage } from "../../types/scan";

export const artifactOptions: ArtifactOption[] = [
  { type: "file", label: "File Upload", detail: "hash and inspect without executing content" },
  { type: "hash", label: "Hash Lookup", detail: "fast path for known samples or duplicate submissions" },
  { type: "url", label: "URL", detail: "normalize before dedupe and enrichment" },
  { type: "email_signal", label: "Email Signal", detail: "paste sender, subject, or suspicious content" },
];

export const pipelineStages: PipelineStage[] = [
  { name: "Normalize", detail: "Convert artifact input into a stable internal form." },
  { name: "Extract IOCs", detail: "Pull out hashes, URLs, domains, and email clues." },
  { name: "Enrich", detail: "Query multiple threat-intel adapters instead of one source." },
  { name: "Optional AI", detail: "Use local or API mode depending on privacy and convenience." },
  { name: "Report", detail: "Assemble a threat report for private review and possible sharing." },
];
