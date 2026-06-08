import { Panel } from "./ui-primitives";

export function PlaceholderPage({
  title,
  description,
  items,
}: {
  title: string;
  description: string;
  items: string[];
}) {
  return (
    <div className="space-y-5">
      <div>
        <h1 className="text-3xl font-semibold tracking-tight">{title}</h1>
        <p className="mt-2 max-w-3xl text-sm leading-6 text-[var(--muted)]">
          {description}
        </p>
      </div>
      <Panel className="p-4">
        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {items.map((item) => (
            <div key={item} className="rounded-md border border-[var(--border)] bg-[#fbfbf8] p-4">
              <div className="text-sm font-semibold">{item}</div>
              <p className="mt-2 text-xs leading-5 text-[var(--muted)]">
                Planned in the seeded implementation tasks and ready for the
                next build slice.
              </p>
            </div>
          ))}
        </div>
      </Panel>
    </div>
  );
}
