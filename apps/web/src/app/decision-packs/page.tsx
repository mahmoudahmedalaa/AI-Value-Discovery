import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function DecisionPacksPage() {
  return (
    <AppShell active="Decision Packs" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Decision Packs"
        description="Draft executive decision-pack preview with portfolio summary, opportunity recommendations, blockers, risks, and assumptions."
        items={[
          "Executive summary",
          "Decision lane narrative",
          "Top opportunities",
          "Human-review gate",
        ]}
      />
    </AppShell>
  );
}
