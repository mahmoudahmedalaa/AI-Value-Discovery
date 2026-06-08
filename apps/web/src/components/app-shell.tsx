import Link from "next/link";
import {
  Archive,
  BookOpen,
  ClipboardList,
  FileText,
  Gauge,
  Landmark,
  Layers3,
  LockKeyhole,
  Network,
  ShieldCheck,
} from "lucide-react";
import { workspace } from "@/lib/demo-data";

const navItems = [
  { label: "Executive Cockpit", href: "/executive-cockpit", icon: Gauge },
  { label: "Intake", href: "/intake", icon: ClipboardList },
  { label: "Opportunities", href: "/opportunities", icon: Layers3 },
  { label: "Portfolio", href: "/portfolio", icon: Network },
  { label: "Documents", href: "/documents", icon: Archive },
  { label: "Decision Packs", href: "/decision-packs", icon: FileText },
  { label: "Methodology", href: "/methodology", icon: BookOpen },
  { label: "Audit", href: "/audit", icon: ShieldCheck },
  { label: "Security Posture", href: "/security-posture", icon: LockKeyhole },
];

type AppShellProps = {
  active: string;
  children: React.ReactNode;
  rightPanel?: React.ReactNode;
};

export function AppShell({ active, children, rightPanel }: AppShellProps) {
  return (
    <div className="min-h-screen bg-[var(--background)] text-[var(--foreground)]">
      <div className="grid min-h-screen grid-cols-1 lg:grid-cols-[260px_minmax(0,1fr)]">
        <aside className="border-r border-[var(--border)] bg-[#18201d] text-white">
          <div className="flex h-full flex-col px-4 py-5">
            <Link
              href="/"
              className="focus-ring flex items-center gap-3 rounded-md px-2 py-2"
            >
              <span className="flex size-9 items-center justify-center rounded-md bg-[#dce8dd] text-[#18201d]">
                <Landmark size={18} strokeWidth={2.2} />
              </span>
              <span>
                <span className="block text-sm font-semibold leading-5">
                  AI Value Discovery
                </span>
                <span className="block text-xs text-white/55">
                  Investment cockpit
                </span>
              </span>
            </Link>

            <nav className="mt-8 flex flex-1 flex-col gap-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = item.label === active;
                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    className={`focus-ring flex items-center gap-3 rounded-md px-3 py-2.5 text-sm transition ${
                      isActive
                        ? "bg-white shadow-sm"
                        : "text-white/70 hover:bg-white/8 hover:text-white"
                    }`}
                    style={isActive ? { color: "#18201d" } : undefined}
                  >
                    <Icon size={16} strokeWidth={2} />
                    {item.label}
                  </Link>
                );
              })}
            </nav>

            <div className="rounded-md border border-white/10 bg-white/6 p-3 text-xs text-white/62">
              <div className="font-medium text-white">Local demo mode</div>
              <div className="mt-1 leading-5">
                Deterministic mock AI. No paid services. No external model calls.
              </div>
            </div>
          </div>
        </aside>

        <div className="min-w-0">
          <header className="sticky top-0 z-10 border-b border-[var(--border)] bg-[rgba(245,246,243,0.92)] px-5 py-3 backdrop-blur md:px-7">
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div>
                <div className="text-xs font-medium uppercase tracking-[0.14em] text-[var(--muted)]">
                  Workspace
                </div>
                <div className="mt-1 flex flex-wrap items-center gap-2">
                  <span className="text-sm font-semibold">
                    {workspace.name}
                  </span>
                  <span className="rounded-sm border border-[var(--border)] bg-white px-2 py-1 text-xs text-[var(--muted)]">
                    {workspace.sector}
                  </span>
                </div>
              </div>
              <div className="flex flex-wrap gap-2 text-xs">
                <span className="rounded-sm bg-[#e5eee8] px-2.5 py-1 font-medium text-[var(--accent-strong)]">
                  {workspace.deploymentMode}
                </span>
                <span className="rounded-sm bg-white px-2.5 py-1 font-medium text-[var(--ink-soft)] ring-1 ring-[var(--border)]">
                  {workspace.dataBoundary}
                </span>
                <span className="rounded-sm bg-[#eef3f5] px-2.5 py-1 font-medium text-[var(--blue)]">
                  {workspace.aiProvider}
                </span>
              </div>
            </div>
          </header>

          <main className="grid min-h-[calc(100vh-73px)] grid-cols-1 xl:grid-cols-[minmax(0,1fr)_320px]">
            <section className="min-w-0 px-5 py-6 md:px-7">{children}</section>
            {rightPanel ? (
              <aside className="border-l border-[var(--border)] bg-[#fbfbf8] px-5 py-6">
                {rightPanel}
              </aside>
            ) : null}
          </main>
        </div>
      </div>
    </div>
  );
}
