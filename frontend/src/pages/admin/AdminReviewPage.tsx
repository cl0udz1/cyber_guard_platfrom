import ReviewQueuePanel from "../../components/admin-review/ReviewQueuePanel";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";
import { reviewChecklist } from "../../features/admin-reviews/reviewPlan";
import { reviewQueue } from "../../mocks/overview";

export default function AdminReviewPage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <ReviewQueuePanel items={reviewQueue} />
      <PlaceholderPanel
        title="Review Workflow Rules"
        ownerHint="Backend admin-review owner + docs/testing owner"
        summary="Moderation should stay simple for the student team: clear queue states, simple decisions, and visible sanitizer expectations."
        todo={reviewChecklist}
      />
    </div>
  );
}
