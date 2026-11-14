# CertiChain Trust Gatekeeper — Research Track

**Track status:** Rules engine v0.1, synthetic demo UI and 27 unit tests  
**Market under study:** Indian background-verification (BGV) providers  
**Data:** Synthetic only

## Research proposition

Investigate whether a **temporal, provenance-aware evidence graph** can help BGV analysts assess difficult academic-credential cases more explainably and avoid unsupported conclusions.

This is an analyst-assist research direction for cases where institution/programme relationships, recognition periods, affiliation history, source lineage, or submitted data are ambiguous or contradictory. It is not another credential repository, issuing service, blockchain ledger, or standalone fake-certificate detector.

## Research pack

| Document | Purpose |
|---|---|
| [01 — Problem definition](01_problem_definition.md) | Initial scope, user, problem, research questions and boundaries |
| [02 — Competitor and gap analysis](02_competitor_gap_analysis.md) | Publicly documented market capabilities and research hypotheses requiring validation |
| [03 — Temporal provenance ontology](03_temporal_provenance_ontology.md) | Entities, relationships, temporal fields and evidence lineage |
| [04 — Synthetic benchmark protocol](04_synthetic_benchmark_protocol.md) | Dataset design, labels, baselines, metrics and validity safeguards |
| [05 — First-stage research plan](05_first_stage_research_plan.md) | Work sequence, gates and evidence required before application changes |
| [06 — Operational standards](06_operational_standards.md) | Case lifecycle, source classes, temporal checks, dispositions, escalation, privacy, security and release gates |
| [07 — Analyst case-handling checklist](07_analyst_case_handling_checklist.md) | Practical case-by-case checklist aligned to the operational standard |
| [08 — Worked synthetic case](08_worked_synthetic_case.md) | End-to-end affiliation transition example with evidence register, temporal analysis and escalation |
| [09 — Worked temporal approval case](09_worked_synthetic_case_temporal_approval.md) | Later-session programme approval, current-status trap, source dependency and scoped abstention |
| [10 — Evidence adjudication rules](10_evidence_adjudication_rules.md) | Deterministic scope-specific outcomes, temporal/source rules, precedence, abstention and unit-test requirements |
| [11 — Project boundary](11_project_boundary.md) | Why Trust Gatekeeper is independent from the original blockchain ledger project |
| [12 — BGV workflow validation guide](12_bgv_workflow_validation_guide.md) | Interview script, workflow map, problem evidence log and Gate A decision worksheet |
| [13 — Practitioner Interview 01](13_practitioner_interview_01.md) | First senior-practitioner account, workflow bottlenecks, product implications, evidence limits and follow-up questions |
| [14 — Worked historical programme-approval case](14_worked_case_historical_programme_approval.md) | Synthetic case separating institutional existence, affiliation, programme authorisation and individual award verification; includes targeted registrar query |

## Current implementation

- ../../tg_rules.py — deterministic TG-RULES-001 assessment engine.
- ../../tg_demo_cases.py — fictional synthetic case fixtures.
- ../../tests/test_tg_rules.py — 27 unit tests.
- ../../app.py — minimal synthetic-case Streamlit interface.

## Current limitations

The current UI runs prebuilt synthetic cases, displays findings, and includes an evidence source register for fixture metadata. Actual source ingestion and live citation fetching are not implemented. It does not yet implement actual PDF/image upload, OCR, CSV/JSON case intake, regulator-source ingestion, graph visualisation, or issuer verification.

The 240-case benchmark is a protocol only; the dataset has not yet been generated. Synthetic test success is not evidence of real-world fraud-detection performance.

## Decision boundaries

- Keep individual award verification separate from institution/programme context.
- Do not treat public-source absence as proof that a qualification is invalid.
- Do not treat related sources as independent confirmations without lineage evidence.
- Abstain or escalate when the evidence does not support a scoped conclusion.
- Do not use real candidate/student data in this prototype.

## Source discipline

Public vendor pages are descriptions of vendor-claimed capabilities, not independent performance evidence. Official regulator and NAD pages support only the specific rules and responsibilities they publish. Interpretations and proposed technical distinctions remain research hypotheses until tested.
