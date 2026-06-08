import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function SecurityPosturePage() {
  return (
    <AppShell active="Security Posture" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Security Posture"
        description="Deployment mode, data boundary, storage policy, AI inference policy, logging, retention, and document classification posture."
        items={[
          "UAE data boundary",
          "Client-hosted deployment path",
          "Mock AI provider policy",
          "Audit and retention controls",
        ]}
      />
    </AppShell>
  );
}
