import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function PortfolioPage() {
  return (
    <AppShell active="Portfolio" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Portfolio"
        description="Executive portfolio cockpit with decision lanes, value-readiness matrix, risk heatmap, blockers, and roadmap."
        items={[
          "Fund Now / Fix First lanes",
          "Value-readiness matrix",
          "Risk and blocker panels",
          "Portfolio roadmap",
        ]}
      />
    </AppShell>
  );
}
