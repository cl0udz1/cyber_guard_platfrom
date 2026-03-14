import PublicThreatFeed from "../../components/public-threats/PublicThreatFeed";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";
import { publicThreatPrinciples } from "../../features/public-threats/publicThreatMocks";
import { publicThreatCards } from "../../mocks/overview";

export default function PublicThreatsPage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <PublicThreatFeed items={publicThreatCards} />
      <PlaceholderPanel
        title="Disconnect by Design"
        ownerHint="Privacy/security owner + public threats owner"
        summary="Public content is a different layer, not a view into private workspace records. That separation should stay visible in both frontend copy and backend contracts."
        todo={publicThreatPrinciples}
      />
    </div>
  );
}
