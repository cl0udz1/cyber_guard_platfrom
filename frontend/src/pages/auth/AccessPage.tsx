import { authMilestones } from "../../features/auth/authPlan";
import PlaceholderPanel from "../../components/shared/PlaceholderPanel";

export default function AccessPage() {
  return (
    <PlaceholderPanel
      title="Account Access Scaffold"
      ownerHint="Frontend auth owner + backend auth owner"
      summary="This page represents account creation, login, and current-user context for both individual users and organization members."
      todo={authMilestones.map((item) => `${item.title}: ${item.note}`)}
    />
  );
}
