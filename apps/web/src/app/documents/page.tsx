import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { PlaceholderPage } from "@/components/placeholder-page";

export default function DocumentsPage() {
  return (
    <AppShell active="Documents" rightPanel={<MethodologyPanel />}>
      <PlaceholderPage
        title="Documents"
        description="Seeded source documents, extraction status, evidence references, and mock AI opportunity extraction."
        items={[
          "Document metadata",
          "Residency classification",
          "Run mock extraction",
          "Draft opportunity queue",
        ]}
      />
    </AppShell>
  );
}
