import ArtifactSubmissionPanel from "../../components/scan/ArtifactSubmissionPanel";
import QueueSnapshot from "../../components/scan/QueueSnapshot";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";

export default function ScanWorkspacePage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "16px" }}>
        <ArtifactSubmissionPanel />
        <QueueSnapshot />
      </div>
      <PlaceholderPanel
        title="Scan Job Integration TODOs"
        ownerHint="Backend scan orchestration owner + frontend scan page owner"
        summary="The implementation target is an async scan job flow with artifact normalization, multi-source enrichment, optional AI, and a generated report."
        todo={[
          "Connect file/hash/url/email_signal submission UI to `/scan-jobs`.",
          "Show queued, enriching, reporting, completed, and failed states clearly.",
          "Use duplicate-submission caching before adding more UI complexity.",
        ]}
      />
    </div>
  );
}
