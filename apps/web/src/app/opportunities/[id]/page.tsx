import Link from "next/link";
import { notFound } from "next/navigation";
import { AppShell } from "@/components/app-shell";
import { MethodologyPanel } from "@/components/methodology-panel";
import { DecisionBadge, EvidenceTag, Panel, PanelHeader } from "@/components/ui-primitives";
import { opportunities } from "@/lib/demo-data";

type OpportunityDetailPageProps = {
  params: Promise<{ id: string }>;
};

export default async function OpportunityDetailPage({
  params,
}: OpportunityDetailPageProps) {
  const { id } = await params;
  const opportunity = opportunities.find((item) => item.id === id);

  if (!opportunity) {
    notFound();
  }

  return (
    <AppShell active="Opportunities" rightPanel={<MethodologyPanel />}>
      <div className="space-y-5">
        <div className="flex flex-col justify-between gap-4 xl:flex-row xl:items-start">
          <div>
            <Link href="/executive-cockpit" className="text-xs font-semibold text-[var(--accent)]">
              Back to cockpit
            </Link>
            <h1 className="mt-2 max-w-4xl text-3xl font-semibold tracking-tight">
              {opportunity.title}
            </h1>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-[var(--muted)]">
              {opportunity.problem}
            </p>
          </div>
          <DecisionBadge decision={opportunity.decision} />
        </div>

        <div className="grid gap-4 xl:grid-cols-3">
          {[
            ["Fundability", `${opportunity.fundability}%`],
            ["Value range", opportunity.estimatedValue],
            ["Confidence", `${opportunity.confidence}%`],
          ].map(([label, value]) => (
            <Panel key={label} className="p-4">
              <div className="text-xs font-medium uppercase tracking-[0.12em] text-[var(--muted)]">
                {label}
              </div>
              <div className="mt-2 text-2xl font-semibold">{value}</div>
            </Panel>
          ))}
        </div>

        <Panel>
          <PanelHeader title="Business Case Structure" />
          <div className="grid gap-4 p-4 md:grid-cols-2">
            {[
              ["Workflow", opportunity.workflow],
              ["KPI", opportunity.kpi],
              ["Value lever", opportunity.valueLever],
              ["Owner", opportunity.owner],
              ["Data assets", opportunity.dataAssets.join(", ")],
              ["Systems", opportunity.systems.join(", ")],
              ["Controls", opportunity.controls.join(", ")],
              ["Missing information", opportunity.missingInfo.join(", ")],
            ].map(([label, value]) => (
              <div key={label}>
                <div className="text-xs font-semibold uppercase tracking-[0.1em] text-[var(--muted)]">
                  {label}
                </div>
                <div className="mt-1 text-sm leading-6 text-[var(--ink-soft)]">{value}</div>
              </div>
            ))}
          </div>
        </Panel>

        <Panel>
          <PanelHeader title="Evidence, Assumptions, and Gaps" />
          <div className="divide-y divide-[var(--border)]">
            {opportunity.evidence.map((evidence) => (
              <div key={evidence.label} className="grid gap-3 px-4 py-3 md:grid-cols-[120px_1fr_180px]">
                <EvidenceTag type={evidence.type} />
                <div className="text-sm leading-6 text-[var(--ink-soft)]">{evidence.label}</div>
                <div className="text-xs leading-6 text-[var(--muted)]">{evidence.source}</div>
              </div>
            ))}
          </div>
        </Panel>
      </div>
    </AppShell>
  );
}
