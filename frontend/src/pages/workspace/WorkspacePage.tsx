import PlaceholderPanel from "../../components/shared/PlaceholderPanel";
import { organizationOverview, workspaceRoleGuide } from "../../features/orgs/orgSummary";
import { mutedTextStyle, panelStyle, sectionTitleStyle } from "../../app/styles";

export default function WorkspacePage() {
  return (
    <div style={{ display: "grid", gap: "16px" }}>
      <section style={panelStyle}>
        <h3 style={sectionTitleStyle}>Organization + Workspace Scope</h3>
        <p style={mutedTextStyle}>
          {organizationOverview.organizationName} / {organizationOverview.workspaceName}
        </p>
        <p style={{ ...mutedTextStyle, marginTop: "10px" }}>{organizationOverview.identityBoundary}</p>
      </section>
      <PlaceholderPanel
        title="Role Ownership"
        ownerHint="Backend RBAC owner + frontend workspace owner"
        summary="Keep role modeling simple and visible. This repo is meant to help assignments land in the right place fast."
        todo={workspaceRoleGuide.map((item) => `${item.role}: ${item.responsibilities}`)}
      />
    </div>
  );
}
