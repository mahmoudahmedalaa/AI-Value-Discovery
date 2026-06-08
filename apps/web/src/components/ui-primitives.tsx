type PanelProps = {
  children: React.ReactNode;
  className?: string;
};

export function Panel({ children, className = "" }: PanelProps) {
  return (
    <section
      className={`rounded-md border border-[var(--border)] bg-[var(--surface)] shadow-[var(--shadow-soft)] ${className}`}
    >
      {children}
    </section>
  );
}

export function PanelHeader({
  title,
  action,
}: {
  title: string;
  action?: React.ReactNode;
}) {
  return (
    <div className="flex items-center justify-between gap-3 border-b border-[var(--border)] px-4 py-3">
      <h2 className="text-sm font-semibold text-[var(--foreground)]">{title}</h2>
      {action}
    </div>
  );
}

export function DecisionBadge({ decision }: { decision: string }) {
  const colors: Record<string, string> = {
    "Fund Now": "bg-[#e4f0ea] text-[#0f5d4b] ring-[#bed7cb]",
    "Fix First": "bg-[#fff2de] text-[#8a4d08] ring-[#ebcf9d]",
    Defer: "bg-[#eef2f4] text-[#355c7d] ring-[#cbd7df]",
    Stop: "bg-[#f7e7e4] text-[#9f2f2f] ring-[#e3c3bd]",
    "Explore Further": "bg-[#edf0e7] text-[#4f6241] ring-[#d6dec8]",
  };

  return (
    <span
      className={`inline-flex items-center rounded-sm px-2 py-1 text-xs font-semibold ring-1 ${
        colors[decision] ?? "bg-zinc-100 text-zinc-700 ring-zinc-200"
      }`}
    >
      {decision}
    </span>
  );
}

export function EvidenceTag({ type }: { type: string }) {
  const colors: Record<string, string> = {
    Evidence: "bg-[#e6f0ec] text-[#0f5d4b]",
    Assumption: "bg-[#fff3df] text-[#8a4d08]",
    Inference: "bg-[#edf2f6] text-[#355c7d]",
    Missing: "bg-[#f7e7e4] text-[#9f2f2f]",
  };

  return (
    <span
      className={`rounded-sm px-1.5 py-0.5 text-[11px] font-semibold ${
        colors[type] ?? "bg-zinc-100 text-zinc-600"
      }`}
    >
      {type}
    </span>
  );
}

export function MetricCard({
  label,
  value,
  helper,
}: {
  label: string;
  value: string;
  helper: string;
}) {
  return (
    <div className="rounded-md border border-[var(--border)] bg-white p-4">
      <div className="text-xs font-medium uppercase tracking-[0.12em] text-[var(--muted)]">
        {label}
      </div>
      <div className="mt-2 text-2xl font-semibold tracking-tight text-[var(--foreground)]">
        {value}
      </div>
      <div className="mt-1 text-xs leading-5 text-[var(--muted)]">{helper}</div>
    </div>
  );
}
