import Link from "next/link";
import { AlertTriangle, ArrowRight, CheckCircle2, FileSearch, ShieldCheck } from "lucide-react";
import {
  auditEvents,
  average,
  decisionCounts,
  documents,
  opportunities,
  workspace,
} from "@/lib/demo-data";
import { DecisionBadge, EvidenceTag, MetricCard, Panel, PanelHeader } from "./ui-primitives";

const averageFundability = average(opportunities.map((item) => item.fundability));
const averageReadiness = average(
  opportunities.map((item) => item.readinessScore * 20),
);
const highConfidence = opportunities.filter((item) => item.confidence >= 75).length;

export function ExecutiveCockpit() {
  return (
    <div className="space-y-6">
      <div className="flex flex-col justify-between gap-4 xl:flex-row xl:items-end">
        <div>
          <h1 className="max-w-3xl text-3xl font-semibold tracking-tight text-[var(--foreground)]">
            Executive Cockpit
          </h1>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-[var(--muted)]">
            Ranked AI investment portfolio for a sample GCC bank workspace,
            using seeded documents, deterministic mock extraction, and
            explainable fundability scoring.
          </p>
        </div>
        <Link
          href="/documents"
          className="focus-ring inline-flex h-10 items-center justify-center gap-2 rounded-md bg-[var(--accent)] px-4 text-sm font-semibold text-white transition hover:bg-[var(--accent-strong)] md:whitespace-nowrap"
        >
          Run mock extraction
          <ArrowRight size={16} />
        </Link>
      </div>

      <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
        <MetricCard
          label="Portfolio value range"
          value="AED 37M-60M"
          helper="Range excludes stopped opportunities and unvalidated baselines."
        />
        <MetricCard
          label="Average fundability"
          value={`${averageFundability}%`}
          helper="Composite of value, readiness, risk, evidence, and sponsorship."
        />
        <MetricCard
          label="Readiness posture"
          value={`${averageReadiness}%`}
          helper="Data, workflow, control, and owner readiness across portfolio."
        />
        <MetricCard
          label="High-confidence opportunities"
          value={`${highConfidence}/${opportunities.length}`}
          helper="Supported by evidence and sufficiently clear assumptions."
        />
      </div>

      <div className="grid gap-4 xl:grid-cols-[1.05fr_0.95fr]">
        <Panel>
          <PanelHeader title="Funding Decision Mix" />
          <div className="space-y-3 p-4">
            {decisionCounts().map((item) => (
              <div key={item.decision} className="grid grid-cols-[130px_1fr_28px] items-center gap-3">
                <DecisionBadge decision={item.decision} />
                <div className="h-2 rounded-full bg-[#e8ebe4]">
                  <div
                    className="h-2 rounded-full bg-[var(--accent)]"
                    style={{ width: `${Math.max(18, item.count * 34)}%` }}
                  />
                </div>
                <div className="text-right text-sm font-semibold">{item.count}</div>
              </div>
            ))}
          </div>
        </Panel>

        <Panel>
          <PanelHeader title="Value / Readiness Matrix" />
          <div className="p-4">
            <div className="relative h-64 rounded-md border border-[var(--border)] bg-[linear-gradient(90deg,rgba(15,93,75,0.05)_1px,transparent_1px),linear-gradient(180deg,rgba(15,93,75,0.05)_1px,transparent_1px)] bg-[size:25%_25%]">
              <span className="absolute left-3 top-3 text-xs font-medium text-[var(--muted)]">
                Higher readiness
              </span>
              <span className="absolute bottom-3 right-3 text-xs font-medium text-[var(--muted)]">
                Higher value
              </span>
              {opportunities.map((item) => (
                <Link
                  key={item.id}
                  href={`/opportunities/${item.id}`}
                  className="focus-ring absolute flex size-9 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white bg-[var(--accent)] text-xs font-bold text-white shadow-md"
                  style={{
                    left: `${item.valueScore * 18}%`,
                    top: `${100 - item.readinessScore * 18}%`,
                  }}
                  title={item.title}
                >
                  {item.title
                    .split(" ")
                    .slice(0, 2)
                    .map((word) => word[0])
                    .join("")}
                </Link>
              ))}
            </div>
          </div>
        </Panel>
      </div>

      <Panel>
        <PanelHeader
          title="Top Opportunities"
          action={
            <Link href="/opportunities" className="text-xs font-semibold text-[var(--accent)]">
              Open backlog
            </Link>
          }
        />
        <div className="overflow-hidden">
          <table className="w-full table-fixed border-collapse text-sm">
            <thead>
              <tr className="border-b border-[var(--border)] bg-[#f7f8f4] text-left text-xs font-semibold uppercase tracking-[0.08em] text-[var(--muted)]">
                <th className="w-[46%] px-3 py-3 md:w-[34%] md:px-4">Opportunity</th>
                <th className="hidden px-4 py-3 2xl:table-cell">Workflow</th>
                <th className="hidden px-4 py-3 lg:table-cell">KPI</th>
                <th className="hidden px-4 py-3 2xl:table-cell">Owner</th>
                <th className="w-[30%] px-3 py-3 md:w-[18%] md:px-4">Decision</th>
                <th className="w-[24%] px-3 py-3 text-right md:w-[16%] md:px-4">
                  <span className="hidden sm:inline">Fundability</span>
                  <span className="sm:hidden">Score</span>
                </th>
                <th className="hidden px-4 py-3 2xl:table-cell">Evidence</th>
              </tr>
            </thead>
            <tbody>
              {opportunities.map((item) => (
                <tr key={item.id} className="border-b border-[var(--border)] last:border-b-0">
                  <td className="px-3 py-3 md:px-4">
                    <Link href={`/opportunities/${item.id}`} className="font-semibold text-[var(--foreground)]">
                      {item.title}
                    </Link>
                    <div className="mt-1 text-xs text-[var(--muted)]">{item.function}</div>
                  </td>
                  <td className="hidden px-4 py-3 text-[var(--ink-soft)] 2xl:table-cell">{item.workflow}</td>
                  <td className="hidden px-4 py-3 text-[var(--ink-soft)] lg:table-cell">{item.kpi}</td>
                  <td className="hidden px-4 py-3 text-[var(--ink-soft)] 2xl:table-cell">{item.owner}</td>
                  <td className="px-3 py-3 md:px-4">
                    <DecisionBadge decision={item.decision} />
                  </td>
                  <td className="px-3 py-3 text-right font-semibold md:px-4">{item.fundability}%</td>
                  <td className="hidden px-4 py-3 2xl:table-cell">
                    <div className="flex flex-wrap gap-1.5">
                      {item.evidence.slice(0, 2).map((evidence) => (
                        <EvidenceTag key={`${item.id}-${evidence.type}`} type={evidence.type} />
                      ))}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>

      <div className="grid gap-4 xl:grid-cols-3">
        <Panel>
          <PanelHeader title="Readiness Blockers" />
          <div className="space-y-3 p-4 text-sm">
            {[
              "Restricted AML case-note boundary requires approval",
              "Credit memo source quality not sampled",
              "Complaint baseline missing by channel",
            ].map((blocker) => (
              <div key={blocker} className="flex gap-3">
                <AlertTriangle className="mt-0.5 shrink-0 text-[var(--amber)]" size={16} />
                <span className="leading-6 text-[var(--ink-soft)]">{blocker}</span>
              </div>
            ))}
          </div>
        </Panel>

        <Panel>
          <PanelHeader title="Document Intelligence" />
          <div className="divide-y divide-[var(--border)]">
            {documents.map((document) => (
              <div key={document.title} className="px-4 py-3">
                <div className="flex items-start gap-3">
                  <FileSearch size={16} className="mt-0.5 text-[var(--steel)]" />
                  <div>
                    <div className="text-sm font-semibold">{document.title}</div>
                    <div className="mt-1 text-xs text-[var(--muted)]">
                      {document.classification} · {document.status} · {document.evidenceItems} evidence items
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </Panel>

        <Panel>
          <PanelHeader title="Audit & Security Posture" />
          <div className="space-y-3 p-4">
            <div className="rounded-md bg-[#e8f0ea] p-3 text-sm text-[var(--accent-strong)]">
              <div className="flex items-center gap-2 font-semibold">
                <ShieldCheck size={16} />
                {workspace.reviewPolicy}
              </div>
              <div className="mt-1 text-xs leading-5">
                Draft recommendations cannot enter final decision packs before review.
              </div>
            </div>
            <div className="space-y-2">
              {auditEvents.map((event) => (
                <div key={event} className="flex gap-2 text-xs text-[var(--muted)]">
                  <CheckCircle2 size={14} className="mt-0.5 shrink-0 text-[var(--green)]" />
                  {event}
                </div>
              ))}
            </div>
          </div>
        </Panel>
      </div>
    </div>
  );
}
