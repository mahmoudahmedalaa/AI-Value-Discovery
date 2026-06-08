import { AppShell } from "@/components/app-shell";
import { ExecutiveCockpit } from "@/components/executive-cockpit";
import { MethodologyPanel } from "@/components/methodology-panel";

export default function ExecutiveCockpitPage() {
  return (
    <AppShell active="Executive Cockpit" rightPanel={<MethodologyPanel />}>
      <ExecutiveCockpit />
    </AppShell>
  );
}
