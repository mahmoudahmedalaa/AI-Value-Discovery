import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function OpportunitiesPage() {
  return (
    <AppShell active="Opportunities" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Opportunities"
        description="Filterable backlog of AI opportunities with KPI, owner, value lever, readiness, evidence, and recommendation."
        items={[
          "Backlog table",
          "Decision filters",
          "Manual create/edit",
          "Evidence and assumption labels",
        ]}
      />
    </AppShell>
  );
}
