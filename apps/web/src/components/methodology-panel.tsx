import { EvidenceTag } from "./ui-primitives";

export function MethodologyPanel() {
  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-sm font-semibold">Methodology Guardrails</h2>
        <p className="mt-2 text-sm leading-6 text-[var(--muted)]">
          Recommendations are draft until human review confirms KPI, owner,
          evidence strength, data path, and control posture.
        </p>
      </div>

      <div className="space-y-2">
        <h3 className="text-xs font-semibold uppercase tracking-[0.12em] text-[var(--muted)]">
          Provenance Labels
        </h3>
        <div className="flex flex-wrap gap-2">
          {["Evidence", "Assumption", "Inference", "Missing"].map((type) => (
            <EvidenceTag key={type} type={type} />
          ))}
        </div>
      </div>

      <div className="space-y-3 text-sm leading-6 text-[var(--ink-soft)]">
        <div>
          <div className="font-semibold">Evidence strength</div>
          <p className="text-[var(--muted)]">
            Measures how strongly an opportunity is supported by source
            documents, user inputs, or verified data.
          </p>
        </div>
        <div>
          <div className="font-semibold">Data readiness</div>
          <p className="text-[var(--muted)]">
            Measures whether required data exists, has an owner, can be
            accessed, and is usable for pilot.
          </p>
        </div>
        <div>
          <div className="font-semibold">Control exposure</div>
          <p className="text-[var(--muted)]">
            Covers privacy, regulatory, cyber, model-risk, explainability,
            audit, and human-review requirements.
          </p>
        </div>
      </div>
    </div>
  );
}
