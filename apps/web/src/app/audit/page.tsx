import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function AuditPage() {
  return (
    <AppShell active="Audit" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Audit"
        description="Traceable event history for workspace selection, extraction, review, recommendation, export, and security posture changes."
        items={[
          "Workspace events",
          "Mock AI extraction events",
          "Review decisions",
          "Decision-pack access",
        ]}
      />
    </AppShell>
  );
}
