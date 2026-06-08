# AI Output Schemas

## OpportunityExtractionSchema

Fields: name, business_problem, function, workflow, user_group, value_lever, kpi_hints, data_assets, systems, controls, evidence, assumptions, missing_information, confidence.

## RiskAssessmentSchema

Fields: category, description, severity, required_control, human_review_required.

## ValueModelSchema

Fields: value_lever, kpis, financial_value conservative/base/upside, assumptions, missing_inputs.

## DecisionRecommendationSchema

Fields: recommended_decision, rationale, evidence_summary, assumptions, blockers, next_actions, confidence.

Codex should implement formal schemas using Zod/Pydantic depending on stack.
