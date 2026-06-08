import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function MethodologyPage() {
  return (
    <AppShell active="Methodology" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Methodology"
        description="Scoring model, value levers, KPI library, evidence treatment, control exposure, and recommendation logic."
        items={[
          "Scoring dimensions",
          "Decision thresholds",
          "Value lever library",
          "Evidence strength rules",
        ]}
      />
    </AppShell>
  );
}
