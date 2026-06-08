import Link from "next/link";
import { ArrowRight, Building2, ShieldCheck } from "lucide-react";
import { workspace } from "@/lib/demo-data";

export default function WorkspaceSelector() {
  return (
    <main className="min-h-screen bg-[var(--background)] px-5 py-8 text-[var(--foreground)] md:px-10">
      <div className="mx-auto flex min-h-[calc(100vh-4rem)] max-w-6xl flex-col justify-center">
        <div className="max-w-3xl">
          <div className="text-sm font-semibold uppercase tracking-[0.16em] text-[var(--muted)]">
            Local internal partner demo
          </div>
          <h1 className="mt-4 text-4xl font-semibold tracking-tight md:text-6xl">
            AI Value Discovery
          </h1>
          <p className="mt-5 max-w-2xl text-lg leading-8 text-[var(--muted)]">
            Turn scattered AI ideas, pilots, documents, workflows, and pain
            points into a ranked, governed, financially defensible AI
            investment portfolio.
          </p>
        </div>

        <section className="mt-10 max-w-3xl rounded-md border border-[var(--border)] bg-white p-5 shadow-[var(--shadow-soft)]">
          <div className="flex flex-col gap-5 md:flex-row md:items-center md:justify-between">
            <div className="flex gap-4">
              <div className="flex size-12 shrink-0 items-center justify-center rounded-md bg-[#e5eee8] text-[var(--accent)]">
                <Building2 size={22} />
              </div>
              <div>
                <h2 className="text-xl font-semibold">{workspace.name}</h2>
                <p className="mt-1 text-sm leading-6 text-[var(--muted)]">
                  {workspace.sector}. Seeded documents, opportunities, scores,
                  audit events, and security posture.
                </p>
                <div className="mt-3 flex flex-wrap gap-2 text-xs font-medium">
                  <span className="rounded-sm bg-[#e5eee8] px-2.5 py-1 text-[var(--accent-strong)]">
                    {workspace.deploymentMode}
                  </span>
                  <span className="rounded-sm bg-[#eef3f5] px-2.5 py-1 text-[var(--blue)]">
                    {workspace.aiProvider}
                  </span>
                  <span className="rounded-sm bg-[#fff2de] px-2.5 py-1 text-[var(--amber)]">
                    {workspace.reviewPolicy}
                  </span>
                </div>
              </div>
            </div>
            <Link
              href="/executive-cockpit"
              className="focus-ring inline-flex h-11 shrink-0 items-center justify-center gap-2 rounded-md bg-[var(--accent)] px-4 text-sm font-semibold text-white transition hover:bg-[var(--accent-strong)]"
            >
              Open workspace
              <ArrowRight size={16} />
            </Link>
          </div>
        </section>

        <div className="mt-6 flex max-w-3xl items-start gap-3 rounded-md border border-[var(--border)] bg-[#fbfbf8] p-4 text-sm text-[var(--muted)]">
          <ShieldCheck className="mt-0.5 shrink-0 text-[var(--accent)]" size={18} />
          <p>
            Demo mode uses deterministic mock AI and local-only seed data. No
            OpenAI, AWS, Azure, Auth0, or paid dependency is required.
          </p>
        </div>
      </div>
    </main>
  );
}
