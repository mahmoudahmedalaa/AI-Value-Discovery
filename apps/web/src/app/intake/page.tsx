import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function IntakePage() {
  return (
    <AppShell active="Intake" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Intake"
        description="Document selection, manual opportunity capture, mock extraction jobs, and draft opportunity review."
        items={[
          "Seeded document library",
          "Manual opportunity intake",
          "Mock extraction queue",
          "Human review workflow",
        ]}
      />
    </AppShell>
  );
}
