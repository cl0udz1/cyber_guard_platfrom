export interface ArtifactOption {
  type: "file" | "hash" | "url" | "email_signal";
  label: string;
  detail: string;
}

export interface PipelineStage {
  name: string;
  detail: string;
}

export interface QueueItem {
  id: string;
  artifactType: string;
  state: string;
  aiMode: string;
}
