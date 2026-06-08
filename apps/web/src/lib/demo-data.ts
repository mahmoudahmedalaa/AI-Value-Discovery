export type DecisionState =
  | "Fund Now"
  | "Fix First"
  | "Defer"
  | "Stop"
  | "Explore Further";

export type EvidenceType = "Evidence" | "Assumption" | "Inference" | "Missing";

export type Opportunity = {
  id: string;
  title: string;
  function: string;
  workflow: string;
  owner: string;
  valueLever: string;
  kpi: string;
  decision: DecisionState;
  fundability: number;
  valueScore: number;
  readinessScore: number;
  riskScore: number;
  evidenceStrength: number;
  confidence: number;
  estimatedValue: string;
  dataAssets: string[];
  systems: string[];
  controls: string[];
  problem: string;
  missingInfo: string[];
  evidence: Array<{
    type: EvidenceType;
    label: string;
    source: string;
  }>;
};

export const workspace = {
  id: "gcc-bank-demo",
  name: "GCC Bank Demo Workspace",
  sector: "Tier-1 GCC retail and corporate bank",
  region: "UAE",
  deploymentMode: "Client-hosted ready",
  dataBoundary: "Data residency: UAE boundary",
  aiProvider: "Mock AI",
  reviewPolicy: "Human review required",
  objectives: [
    "Prioritize AI investment by value, readiness, risk, and evidence.",
    "Expose data and control blockers before pilot funding.",
    "Generate executive-ready decision packs from reviewed opportunities.",
  ],
};

export const opportunities: Opportunity[] = [
  {
    id: "opp-001",
    title: "RM next-best-action portfolio assistant",
    function: "Corporate Banking",
    workflow: "Relationship manager portfolio review",
    owner: "Head of Corporate Coverage",
    valueLever: "Revenue uplift",
    kpi: "Cross-sell conversion rate",
    decision: "Fund Now",
    fundability: 86,
    valueScore: 5,
    readinessScore: 4,
    riskScore: 2,
    evidenceStrength: 4,
    confidence: 82,
    estimatedValue: "AED 18M-28M",
    dataAssets: ["CRM activities", "Product holdings", "Transaction signals"],
    systems: ["CRM", "Core banking", "Data warehouse"],
    controls: ["Human approval", "Explainability note", "Relationship-manager override"],
    problem:
      "RMs review fragmented account signals manually, causing missed cross-sell moments and inconsistent prioritization.",
    missingInfo: ["Confirmed baseline conversion by segment", "Product eligibility constraints"],
    evidence: [
      {
        type: "Evidence",
        label: "Workshop backlog notes cite inconsistent portfolio review cadence.",
        source: "Corporate AI workshop notes",
      },
      {
        type: "Assumption",
        label: "Value range assumes 4-6% conversion lift in priority segments.",
        source: "Mal7 value model assumption",
      },
    ],
  },
  {
    id: "opp-002",
    title: "AML alert triage evidence summarization",
    function: "Financial Crime",
    workflow: "Level-1 AML alert investigation",
    owner: "Financial Crime Operations",
    valueLever: "Productivity",
    kpi: "Average handling time",
    decision: "Fix First",
    fundability: 71,
    valueScore: 4,
    readinessScore: 2,
    riskScore: 4,
    evidenceStrength: 4,
    confidence: 76,
    estimatedValue: "AED 9M-14M",
    dataAssets: ["Alert history", "Case notes", "Customer profile"],
    systems: ["AML platform", "Case management", "KYC repository"],
    controls: ["Model-risk review", "Caseworker approval", "Audit evidence retention"],
    problem:
      "Analysts spend significant time gathering context across systems before deciding whether to escalate or close alerts.",
    missingInfo: ["Restricted data handling approval", "False-negative tolerance"],
    evidence: [
      {
        type: "Evidence",
        label: "Operations data identifies alert handling time as a top cost driver.",
        source: "Ops diagnostic extract",
      },
      {
        type: "Missing",
        label: "Need formal approval for regulated case-note processing boundary.",
        source: "Security posture review",
      },
    ],
  },
  {
    id: "opp-003",
    title: "Contact-center complaint intent routing",
    function: "Customer Experience",
    workflow: "Complaint intake and routing",
    owner: "Head of Service Quality",
    valueLever: "Customer experience",
    kpi: "First contact resolution",
    decision: "Explore Further",
    fundability: 64,
    valueScore: 3,
    readinessScore: 3,
    riskScore: 3,
    evidenceStrength: 2,
    confidence: 58,
    estimatedValue: "AED 4M-7M",
    dataAssets: ["Call summaries", "Complaint categories", "Resolution codes"],
    systems: ["Contact center", "CRM", "Quality monitoring"],
    controls: ["PII redaction", "Human routing override", "Quality review sampling"],
    problem:
      "Complaint classification is inconsistent across channels, slowing resolution and weakening root-cause reporting.",
    missingInfo: ["Channel-level baseline", "Arabic dialect quality sample"],
    evidence: [
      {
        type: "Inference",
        label: "Likely value depends on channel-level complaint volume not yet validated.",
        source: "Mock AI extraction",
      },
    ],
  },
  {
    id: "opp-004",
    title: "Branch operations policy chatbot",
    function: "Retail Banking",
    workflow: "Branch policy lookup",
    owner: "Branch Network Operations",
    valueLever: "Productivity",
    kpi: "Policy lookup time",
    decision: "Stop",
    fundability: 32,
    valueScore: 2,
    readinessScore: 2,
    riskScore: 4,
    evidenceStrength: 1,
    confidence: 44,
    estimatedValue: "Not defensible",
    dataAssets: ["Policy PDFs", "Staff FAQs"],
    systems: ["Intranet", "Document repository"],
    controls: ["Policy owner approval", "Version control", "Answer audit"],
    problem:
      "The idea is framed as a generic chatbot without KPI baseline, policy ownership, or control model.",
    missingInfo: ["Named policy owner", "Baseline lookup volume", "Approved source of truth"],
    evidence: [
      {
        type: "Missing",
        label: "No KPI, owner, or evidence base supports funding.",
        source: "Intake quality review",
      },
    ],
  },
  {
    id: "opp-005",
    title: "Credit memo drafting support",
    function: "Credit Risk",
    workflow: "SME credit memo preparation",
    owner: "Chief Credit Officer delegate",
    valueLever: "Cost reduction",
    kpi: "Memo preparation cycle time",
    decision: "Defer",
    fundability: 58,
    valueScore: 4,
    readinessScore: 2,
    riskScore: 5,
    evidenceStrength: 3,
    confidence: 63,
    estimatedValue: "AED 6M-11M",
    dataAssets: ["Financial statements", "Covenants", "Collateral notes"],
    systems: ["Credit workflow", "Document management", "Core banking"],
    controls: ["Credit officer review", "Hallucination checks", "Regulatory audit trail"],
    problem:
      "Credit analysts spend time assembling memo sections, but source data quality and control exposure are not pilot-ready.",
    missingInfo: ["Credit policy sign-off", "Document quality sample", "Model-risk classification"],
    evidence: [
      {
        type: "Evidence",
        label: "Credit workflow interviews show repeated manual memo assembly.",
        source: "Credit discovery interviews",
      },
      {
        type: "Assumption",
        label: "Cycle-time reduction assumes reusable source-data templates.",
        source: "Mal7 readiness model",
      },
    ],
  },
];

export const documents = [
  {
    title: "Corporate Banking AI Workshop Notes",
    owner: "Transformation Office",
    classification: "Confidential",
    status: "Extracted",
    evidenceItems: 14,
  },
  {
    title: "Financial Crime Operations Diagnostic",
    owner: "Operations Excellence",
    classification: "Regulated",
    status: "Human review required",
    evidenceItems: 9,
  },
  {
    title: "Customer Complaints Journey Map",
    owner: "Service Quality",
    classification: "Internal",
    status: "Queued",
    evidenceItems: 6,
  },
];

export const auditEvents = [
  "Workspace selected by Mal7 demo user",
  "Mock AI extraction generated 3 draft opportunities",
  "Financial Crime opportunity flagged for control review",
  "Decision-pack preview opened in draft mode",
];

export const decisionOrder: DecisionState[] = [
  "Fund Now",
  "Fix First",
  "Explore Further",
  "Defer",
  "Stop",
];

export function decisionCounts() {
  return decisionOrder.map((decision) => ({
    decision,
    count: opportunities.filter((opportunity) => opportunity.decision === decision)
      .length,
  }));
}

export function average(values: number[]) {
  return Math.round(values.reduce((total, value) => total + value, 0) / values.length);
}
