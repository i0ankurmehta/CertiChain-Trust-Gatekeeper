> **Prototype-readiness update — 15 November 2026:** The Streamlit app now opens a curated BBSBEC 2018–19 analyst case workspace by default. It includes a switch between an IT course-closure review and a CSE positive control, a dated evidence timeline, source cards with direct links and custody limitations, claim-by-claim findings, an analyst next step, and downloadable JSON/CSV plus a registrar-request draft. The candidate is fictional; the institutional sources are public. This is manually curated and not live OCR/source ingestion. Six new demo tests were added; the combined suite is 33 tests. See [the short demo script](../../DEMO_WALKTHROUGH.md).

> **Worked-case update — 15 November 2026:** Added [18 — BBSBEC Historical Approval Case](cases/18_bbsbec_2018_temporal_approval_case.md), a source-driven 2015–19 reconstruction for Baba Banda Singh Bahadur Engineering College, Fatehgarh Sahib. The AICTE EoA dated 10 April 2018 records IKGPTU as the affiliating body for 2018–19, B.Tech CSE intake 180, and approved closure status for B.Tech IT in that session. Added a six-source evidence register, synthetic benchmark fixture and a precise registrar-query template. The college-specific 2018 affiliation-choice acceptance order, original 30 June 2015 State notification and student-level award record remain open. App code remains untouched.

> **Punjab source-pilot update — 15 November 2026:** Added [17 — Punjab Temporal Affiliation Source Pilot](17_punjab_temporal_source_pilot.md) and [the 16-record source register](data/punjab_source_register.csv). The pilot found a real 2015 territorial affiliation transition to MRSPTU and a 2018 statutory one-time college choice between MRSPTU and IKGPTU, with a distinct transition provision for 2015–16 students. This supports a temporal research benchmark, but college-specific choice/acceptance records and branch-specific AICTE approval letters remain missing. PDF screenshot retrieval was not available for several reviewed documents; the report records those limits. No app code was changed. Gate A remains open.

# 05 — First-Stage Research Plan

> **Execution status — 14 November 2026:** Trust Gatekeeper now has its own standalone repository. The deterministic rules engine, three synthetic demo cases, Streamlit demonstration UI and 25 unit tests are present as a baseline prototype. This does not mean the research gates have passed. The next action remains **Workstream A — validate the analyst workflow and assumed gap**. Do not expand the graph, ingestion or production feature set until practitioner evidence and ontology review justify that work. Use [12 — BGV Workflow Validation Guide](12_bgv_workflow_validation_guide.md) to conduct and document the exploratory conversations.

> **Fieldwork update — 14 November 2026:** One senior BGV-industry practitioner has described a potentially important exception-handling problem: uneven ease of checking newer versus older/smaller-college credentials, manual registrar/courier follow-up, and difficulty resolving historical affiliation, programme-approval timing and study-centre jurisdiction from present-day checks alone. The recollection is recorded in [13 — Practitioner Interview 01](13_practitioner_interview_01.md). This is one qualitative account, not market-wide validation. Gate A remains open; continue with additional conversations, a workflow map, and independent review of vendor/source coverage.

> **Workflow-mapping update — 15 November 2026:** Added [15 — Preliminary BGV Workflow Map](15_preliminary_bgv_workflow_map.md), structured from Practitioner Interview 01. It separates the reported faster digital lookup route from the reported legacy/manual exception route, identifies the historical claim families, and defines metrics and follow-up questions. This is a hypothesis map from one account, not a validated workflow. Gate A remains open; the current application and rules engine remain unchanged.

> **Source-feasibility update — 15 November 2026:** Added [16 — India Historical Source Feasibility Assessment](16_india_historical_source_feasibility.md). The desk review found relevant official source families for UGC university/regulatory status, UGC-DEB ODL/online recognition, AICTE technical-education approval material, university-level affiliation lists and Gazette/statute records. Coverage is fragmented and claim-specific; AISHE is discovery/context only, not recognition evidence. The document proposes a small manually curated pilot. Gate A remains open, and no application or live-ingestion changes are authorised by this research finding.

**Version:** 0.1  
**Status:** Execution plan  
**Date:** 14 November 2026

## Objective

Decide whether the proposed temporal/provenance graph addresses a real BGV workflow problem and whether its added reasoning value can be demonstrated on a controlled benchmark—before changing the current CertiChain application.

## Workstream A — Competitor and workflow validation

### Tasks
1. Review the public product pages listed in the competitor matrix.
2. Arrange 5–8 exploratory conversations with education-verification analysts, BGV operations leads or product managers, if access is available.
3. Map their current case flow from candidate submission to final result.
4. Identify what is already automated and what is escalated to human review.
5. Ask for anonymised example problem categories, not candidate documents.
6. Request product demonstrations or technical descriptions from providers where possible.

### Required output
- A validated BGV workflow map.
- A feature-by-feature competitor matrix updated with demo/interview evidence.
- A list of operational pain points ranked by frequency and impact.
- A record of features that are already solved by existing vendor tools.

### Gate A — Customer/problem fit
Proceed only if practitioners identify a recurring problem involving historical status, affiliation/programme relationships, source conflicts, source traceability or evidence insufficiency. If they do not, revisit the product problem before implementation.

## Workstream B — Ontology review

### Tasks
1. Review the entity and relationship definitions with one domain-informed reviewer, if available.
2. Ensure recognition, accreditation, approval, affiliation and individual award verification are separate.
3. Confirm that the time model can represent academic sessions as well as exact dates.
4. Define what constitutes a source copy, derivative, conflict or independent source.
5. Identify which claims require human review.

### Required output
- Versioned ontology specification.
- Example graph records for each scenario family.
- Written rules for temporal applicability and abstention.

### Gate B — Model adequacy
Do not generate the final benchmark until each scenario family can be represented without inventing missing facts or collapsing distinct concepts.

## Workstream C — Synthetic benchmark

### Tasks
1. Implement a deterministic case generator in a research-only directory or standalone research project.
2. Generate 240 cases with scan-only, structured-only and paired-input modes.
3. Mark every synthetic document clearly and visibly.
4. Create labels independently from the assessment code.
5. Create template-group-aware development, validation and locked test splits.
6. Validate a sample of labels manually.

### Required output
- Dataset generator specification.
- Synthetic case manifest.
- Ground-truth label file.
- Benchmark data dictionary.
- Locked test split.

### Gate C — Benchmark quality
No model or graph result should be reported until the test cases are reproducible, the labels are auditable and template leakage has been checked.

## Workstream D — Baseline and proposed-method evaluation

### Tasks
1. Implement B0–B2 first.
2. Add time-bounded relationships for B3.
3. Add source lineage and dependency handling for B4.
4. Add an explicit abstention policy for B5.
5. Run all methods on the same cases.
6. Report family-level metrics and inspect false-clear/false-flag failures.

### Required output
- Reproducible baseline results.
- Ablation/comparison report.
- Error analysis.
- Threats-to-validity section.

### Gate D — Research contribution
Proceed with product/application integration only if B3/B4/B5 provide measurable value on their target cases compared with simpler alternatives, and do not achieve that value merely by using extra hidden information.

## Workstream E — Product and application decision

After Gates A–D:
- If customers recognise the problem and the method adds value, decide whether to develop an API/reviewer workflow.
- If customer pain exists but the graph adds no measurable value, simplify the product and do not force graph complexity.
- If the synthetic benchmark passes but customer evidence is weak, keep it as an academic prototype rather than claiming commercial readiness.
- If customer demand and research performance are both weak, stop or redefine the direction.

## Repository discipline

For the current phase:
- Research files live under `research/trust-gatekeeper/`.
- The separate Trust Gatekeeper application now has a showable BBSBEC analyst walkthrough, but the original blockchain repository remains untouched.
- The BBSBEC view is a curated source-backed case workspace; it is not a live document-ingestion or automated legal-decision system.
- No new Python dependencies are added; the runtime remains Streamlit only.
- Further automation should be based on practitioner feedback about whether the case brief reduces investigation effort.

This research track now lives in the standalone repository `i0ankurmehta/CertiChain-Trust-Gatekeeper`. Keep it separate from the original CertiChain blockchain demonstration repository. Do not copy Trust Gatekeeper research or application changes back into the original project unless the user explicitly requests that integration.

## Immediate next action

Use the BBSBEC worked case as a practical analyst test. First, request the college-specific 2018 one-time affiliation-choice acceptance order and the original State Government notification dated 30 June 2015. Second, obtain the AICTE/IKGPTU order explaining the approved 2018-19 Information Technology closure and any teach-out arrangement. Third, have one BGV analyst review the synthetic CSE positive-control and IT course-closure cases, then record handling time, source retrieval time, registrar-query count and false-escalation observations. Do not implement a crawler, graph store or app feature until the evidence gaps and analyst workflow are reviewed.
