# 15 — Preliminary India BGV Education-Verification Workflow Map

**Document ID:** TG-RESEARCH-015  
**Version:** 0.1  
**Date:** 15 November 2026  
**Evidence basis:** One senior BGV-industry practitioner's recollection, recorded in [13 — Practitioner Interview 01](13_practitioner_interview_01.md)  
**Status:** Preliminary hypothesis map — not a validated industry workflow  
**Scope:** Indian background-verification providers; education checks; scan and structured-record inputs; synthetic research data only

## 1. Purpose

Translate the first practitioner account into a workflow that can be tested in follow-up conversations. This map is intended to expose where a case moves from automated checks to manual research, what information is missing at each stage, and where Trust Gatekeeper might assist.

It is not a claim that every BGV provider follows this process. The account represents one practitioner recollection, not a representative sample or measured operational dataset.

## 2. Workflow described by the practitioner

### Route A — relatively straightforward, newer credential

| Stage | Reported activity | What is known from Interview 01 | What still needs validation |
|---|---|---|---|
| 1. Case received | Employer/BGV case enters education verification | A candidate's education credential is submitted | Required fields, document formats and intake systems |
| 2. Digital lookup | Newer degrees may be checked through DigiLocker | Practitioner described this route as fast for some newer degrees | Which award years, institutions and credential types are actually covered |
| 3. Result handling | The check can proceed without the same level of manual follow-up | Practitioner contrasted this route with older/smaller-college cases | Exact decision rules and whether any human review remains |

**Important:** The interview does not establish DigiLocker coverage rates or prove that every newer degree is available there.

### Route B — older or smaller-college credential requiring manual follow-up

| Stage | Reported activity | Operational question to test |
|---|---|---|
| 1. Case received | An older credential or one from a smaller college enters the BGV process | How is “older” defined: year, institution, paper-only record, closed institution or another condition? |
| 2. Initial checks | Existing checks may inspect whether the PDF appears manipulated and whether the college exists today | Which checks are actually performed by the provider's current software and which are manual? |
| 3. Exception identified | Present-day existence and document appearance do not resolve a historical question | Which historical facts are missing: affiliation, programme approval, study mode, campus, study-centre permission or another fact? |
| 4. Manual research | Analyst searches for historical records and relevant authorities | Which sources and internal databases are searched? How much active analyst time is spent? |
| 5. External follow-up | Analyst may email the registrar and send a physical courier request | How often is each channel used, what information is requested, and how long does each response take? |
| 6. Analyst review | Available evidence and institutional response are interpreted | Who reviews contradictions, incomplete replies or a mismatch between programme and individual-award facts? |
| 7. Case closure | BGV provider records its final verification outcome | What are the possible closure states, and how are unresolved cases reported? |

Interview 01 reports that some cases can involve weeks of email and courier follow-up. No measured turnaround distribution, case count or average analyst effort was supplied.

## 3. Historical questions that may trigger the manual route

The practitioner identified three examples. They should be treated as separate claim types rather than one generic “college validity” check.

| Historical question | Evidence needed to assess it | Relevant time dimension | What the finding must not imply |
|---|---|---|---|
| Did the college have the claimed parent/affiliating university during the relevant period? | The applicable affiliation or relationship order, including institution identity and effective period | Admission/study period, and any transition date | A current affiliation does not establish historical affiliation |
| Was the specific programme authorised for the relevant cohort? | Programme-specific approval/recognition evidence from the competent authority, including scope and any retrospective effect | Relevant admission session and programme delivery period, as required by the applicable rule | Institution existence or general recognition does not establish approval of every programme |
| Was the study centre permitted at the claimed location? | Permission/territorial-jurisdiction evidence covering the relevant institution, programme, mode and location | Relevant study period/session | Approval of a university or programme at one location does not establish permission at every centre |

The competent authority, source class and legally relevant date must be established for each real case. The table is a research decomposition, not a legal conclusion about any institution or programme.

## 4. Candidate Trust Gatekeeper insertion point

**Hypothesis:** The most useful insertion point is after a case has been received and its submitted claims extracted, but before the analyst begins broad manual research or sends a registrar request.

The intended analyst-assist sequence is:

1. **Capture the submitted claim.** Preserve the original scan or structured record separately from extracted fields. Record extraction confidence and any document-to-record mismatch.
2. **Resolve the entities.** Identify the awarding university, college/institute, campus or study centre, programme, mode and location. Keep uncertain identity matches unresolved.
3. **Identify claim-specific time periods.** Separate admission session, study period, examination/completion date and award date where each is relevant.
4. **Assemble evidence.** Link every material assertion to its source, publisher, reference, publication/observation date, effective period, relevant excerpt and known source lineage.
5. **Compare historical assertions.** Test whether each source actually covers the claim and period. Distinguish explicit contradiction from missing, incomplete or undated evidence.
6. **Produce a scoped analyst brief.** Show supported contextual facts, contradictions, evidence gaps, source dependencies and limitations. Do not produce a fraud verdict or candidate decision.
7. **Narrow the follow-up.** Where direct issuer confirmation remains necessary, draft the smallest claim-specific question—for example, confirmation of a roll number, exact programme/branch and award cycle.

This is the proposed workflow, not a claim that the current application already performs these steps on real documents or live government sources.

## 5. Proposed analyst output to test with practitioners

The following output components are hypotheses. Ask analysts which are useful, redundant or missing.

| Output | Analyst question it should answer |
|---|---|
| Case and claim summary | What exactly does the submitted credential claim? |
| Historical entity timeline | Which institution/college/affiliation relationship applied in each relevant period? |
| Programme/mode/location assessment | Is there evidence for the exact programme, mode and location during the relevant session? |
| Claim-to-source register | Which source supports each statement, and what period/scope does it cover? |
| Source-lineage view | Are multiple pages independent, or do they repeat the same original notice? |
| Finding and limitation | Is the claim supported, explicitly contradicted, ambiguous or insufficiently evidenced? |
| Targeted follow-up | What precise detail still needs confirmation, and which authority is competent to answer it? |

Do not collapse these elements into an opaque trust score. Any future prioritisation score would require a separately specified meaning, calibrated thresholds, validation data and review of its error costs.

## 6. Workflow evidence and metrics to collect

The next practitioner conversations should seek measured data where available. If only an estimate or impression is offered, label it as such.

| Metric / observation | Suggested capture |
|---|---|
| Exception frequency | Number or proportion of education cases routed to manual review, by reason and credential category |
| End-to-end turnaround | Median and range from case receipt to closure; distinguish business days from calendar days |
| Active analyst effort | Approximate hands-on minutes/hours, separate from waiting time |
| External follow-up | Number of emails, calls, courier requests and days awaiting response |
| Resolution route | DigiLocker, institution portal, third-party source, internal database, registrar, regulator or unresolved |
| Source availability | Whether the decisive historical order/list was available, dated, accessible and within scope |
| Existing automation | Exact functions already available in the provider's current tool or supplier |
| Human-review outcome | What the analyst or quality reviewer changed, confirmed or left unresolved |
| Error/rework | Repeated requests, wrong-authority contact, entity confusion, false discrepancy or reopened case |

Do not ask participants for confidential case files or personally identifiable candidate data. Broad counts, ranges and anonymised process descriptions are sufficient for this discovery stage.

## 7. Questions for follow-up interviews

1. Does this two-route workflow match your actual process? Which stages are missing or in the wrong order?
2. What specifically makes a credential “legacy” or difficult to verify in your organisation?
3. At which exact step does the case spend most of its elapsed time, and how much of that is active analyst effort?
4. Which historical facts do your current systems already resolve reliably?
5. How are affiliation transitions, programme/session approval and study-centre jurisdiction checked today?
6. What source is accepted as sufficient for each of those claims, and who decides?
7. Do analysts already receive a source-linked timeline or dossier from their existing vendor?
8. When is a registrar query still unavoidable, and what is the smallest question that closes the gap?
9. Would the proposed brief reduce work, duplicate an existing report, or introduce extra review?
10. What would make the output unsafe or unhelpful for an analyst?

Ask for a recent anonymised process example. Do not ask the participant to share actual candidate records, roll numbers, scans, confidential customer material or proprietary vendor screenshots.

## 8. Current validation status and next gate

**Gate A remains OPEN.** Interview 01 provides one early qualitative signal. This map organises that signal but does not add independent evidence.

Before treating the workflow as validated:

- obtain additional conversations across at least two distinct BGV roles or organisations, aiming toward the 5–8 conversations in the first-stage plan;
- ask participants to correct this map rather than simply endorse it;
- update the competitor comparison with live demonstrations or detailed technical descriptions wherever access is available;
- record concrete frequency, turnaround and analyst-effort ranges with their evidence type;
- capture counterexamples where existing tools already resolve historical status, affiliation, programme approval or source lineage; and
- identify whether the relevant official historical sources can realistically be located, retained and interpreted for the target cases.

**Decision rule:** Continue the research direction only if the evidence shows a recurring and costly exception workflow that current tools do not already resolve adequately, and if the proposed output fits into the analyst's existing process. Narrow or revise the scope if only one claim family is supported. Do not build live ingestion, OCR or a graph expansion merely because the prototype can be extended.

## 9. Research and product boundary

- Current Trust Gatekeeper application remains synthetic-only.
- This workflow map does not authorise real candidate data intake.
- No real government citations, source captures or legal determinations are created by this document.
- Institution/programme context remains distinct from confirmation of an individual's award.
- “Not found” is not proof of non-existence or invalidity.
- A temporal contradiction requires evidence that actually establishes the relevant historical exclusion; an incomplete later record should remain insufficient evidence.
- Final BGV disposition remains with the authorised human reviewer and appropriate issuing authority.
