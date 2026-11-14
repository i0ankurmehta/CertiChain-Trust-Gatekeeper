# 14 — Worked Synthetic Case: Historical Programme Approval and Targeted Award Confirmation

**Case ID:** TG-DEMO-004  
**Document ID:** TG-CASE-004  
**Version:** 0.1  
**Status:** Implemented as the fourth synthetic demo fixture; rules and workflow validation case  
**Date:** 14 November 2026  
**Data classification:** Entirely fictional; no real candidate or institution is represented

> This is a fictional scenario for testing the product design. "Rohan", "Apex Institute" and "State Technical University" are invented names. No real government order, approval record, institution, programme or legal conclusion is asserted in this document.

## 1. Scenario

A candidate named Rohan submits a scanned PDF purporting to be a **2018 Bachelor of Technology (BTech) degree in Artificial Intelligence and Data Science** from **Apex Institute**, described on the document as affiliated with **State Technical University**.

The candidate's stated study period is 2014–2018.

Trust Gatekeeper receives the unverified scan as a claim-bearing artefact. It must not assume the PDF is authentic, nor treat the candidate's statements as established facts.

The proposed historical evidence graph contains official records that, in this fictional test scenario:
- establish that Apex Institute existed during the relevant period;
- establish that State Technical University existed during the relevant period;
- establish the relevant affiliation relationship for the applicable period, subject to the exact scope and dates in the source; and
- show that the specific BTech Artificial Intelligence and Data Science programme was first approved in 2020, with no applicable retrospective approval covering the candidate's 2014–2018 study period.

The analyst's remaining award-level question is whether the candidate's roll number was actually awarded a BTech in **Computer Science** rather than the AI and Data Science qualification stated on the scan.

## 2. Claim decomposition

The scan must be decomposed into separate, testable claims.

| Claim ID | Claim extracted from the unverified PDF | Required independent check |
|---|---|---|
| CL-004-01 | Awarding / affiliating university is State Technical University | Resolve the legal entity and the university's role in the award |
| CL-004-02 | Apex Institute existed during the relevant period | Historical institutional record for relevant dates |
| CL-004-03 | Apex Institute was affiliated with State Technical University for the relevant cohort / period | Official, time-bounded affiliation record |
| CL-004-04 | BTech Artificial Intelligence and Data Science was an authorised programme for the relevant student cohort and study mode | Competent authority's programme approval / permission record with applicable dates and scope |
| CL-004-05 | Rohan's roll number received the stated individual award in 2018 | Direct award-register / registrar confirmation or other issuer-authorised record |

Do not collapse institutional existence, affiliation, programme authorisation and individual award verification into a single "college verified" result.

## 3. Temporal model

The assessment should not use a vague "graduation-year check". It should preserve the claimed events and the effective dates of each source.

| Event / assertion | Scenario date or period | Why it matters |
|---|---|---|
| Claimed admission | 2014 | May determine the applicable cohort and admission-session approval rules |
| Claimed period of study | 2014–2018 | Programme delivery and study-centre permissions may apply during this interval |
| Claimed completion / graduation | 2018 | Relevant to the stated award date and award-register check |
| First programme approval shown in the synthetic official record | 2020 | Later approval does not by itself establish permission for an earlier cohort |

The rules engine must capture which event date controls each particular regulatory claim. If applicable rules distinguish admission cohort, academic session, programme delivery, examination and award date, assess those separately.

## 4. Evidence register (fictional placeholders)

The evidence IDs below are synthetic placeholders. The final benchmark case must include exact issuing authority, order/reference number, publication/capture date, valid period, scope, excerpt, URL or archive reference and review status. Do not invent a government citation to fill an empty field.

| Evidence ID | Proposed source | Scope it may support | What the scenario says it establishes |
|---|---|---|---|
| SYN4-E01 | Official government / competent-authority institutional record | Existence / status of Apex Institute | Apex Institute existed during the relevant period |
| SYN4-E02 | Official university record | Existence and identity of State Technical University | The university existed during the relevant period |
| SYN4-E03 | Official affiliation order / historical university record | Apex Institute's affiliation to State Technical University | Relevant affiliation applied for the stated period, if the order's dates and scope cover the cohort |
| SYN4-E04 | Official programme approval record | Exact BTech AI and Data Science programme, mode, location and effective date | First applicable approval shown is in 2020; the scenario assumes no retrospective coverage for 2014–2018 |
| SYN4-E05 | Candidate-uploaded scanned degree PDF | What the candidate claims | Unverified claim of a 2018 BTech AI and Data Science award |
| SYN4-E06 | Registrar / authorised award-register response (not yet obtained) | Individual award and roll-number / programme details | The remaining direct verification question |

E01–E04 are not generic proof of all claims. Each source is competent only for the propositions its issuing authority and wording actually establish.

## 5. Expected rule-engine reasoning

### 5.1 Historical institution and university checks

If the official sources establish that Apex Institute and State Technical University existed in 2018, the engine may mark those specific entity-existence claims as supported for that date range.

This does **not** establish:
- that the programme was approved;
- that the institute was affiliated for every year in the claimed period;
- that the study mode or location was authorised; or
- that Rohan personally received the claimed award.

### 5.2 Affiliation check

Evaluate the exact affiliation relationship and its valid-time interval. If the source covers only part of 2014–2018, preserve that distinction and report the uncovered interval. Do not infer continuous affiliation from a current university webpage.

### 5.3 Programme-approval check

If E04 is an authoritative, claim-competent record that explicitly establishes the first applicable approval in 2020 and excludes retrospective application to the 2014–2018 cohort, the programme-scope result should be **EV-02 — Temporal mismatch**.

If the only fact is that a 2020 approval record was found, but historical coverage is absent or the source does not establish non-approval before 2020, the result must instead be **EV-05 — Evidence insufficient**. A first located record is not automatically proof that earlier approval did not exist.

This distinction is mandatory: missing historical evidence is not an explicit historical contradiction.

### 5.4 Individual award check

The government programme record does not establish whether Rohan's roll number was awarded a different qualification. That must remain unverified until an appropriate issuer / registrar source is received.

The individual-award scope should remain **EV-05 — Evidence insufficient / confirmation pending**. It must not inherit a clear result from the entity or affiliation checks.

## 6. Expected analyst-facing output

**Case:** TG-DEMO-004  
**Overall state:** Human review required  
**Programme-scope finding:** EV-02 only if the explicit, non-retrospective exclusion condition in Section 5.3 is met; otherwise EV-05  
**Entity-existence checks:** May be supported for their stated periods  
**Affiliation check:** Depends on the exact historical order dates and scope  
**Individual award check:** EV-05 — issuer confirmation pending

### Plain-language explanation

"The submitted scan claims a 2018 BTech in Artificial Intelligence and Data Science. The reviewed historical records in this synthetic case establish that the institute and university existed during the relevant period. However, the programme-approval record shows an applicable approval beginning in 2020 and, in this scenario, does not cover the earlier 2014–2018 cohort. This creates a programme-timeline inconsistency. The record does not establish whether the candidate's roll number received a different award. Please obtain issuer confirmation of the roll number, exact degree title, programme and award year."

The application must display direct source references beside each statement. Until real, authoritative references have been loaded and reviewed, show these as synthetic evidence IDs, not as clickable or purported government citations.

## 7. Targeted registrar query

If the historical programme finding is established and the remaining unresolved fact is the individual award, the system may draft a narrowly scoped request:

> Subject: Verification of award details — roll number [ROLL NUMBER]
>
> Please confirm whether the above roll number appears in the official award register for the 2018 award cycle. If present, please confirm the exact qualification / degree title, programme or branch, and award date recorded against that roll number. We are seeking confirmation of the award-register entry and programme name only.
>
> Please advise if any additional information is required to locate the record.

The real workflow must use an authorised contact channel, an appropriate legal basis, data minimisation and the institution's required verification procedure. Do not send candidate information to an unverified address.

The query must not tell the registrar that fraud has occurred or ask the registrar to validate a conclusion the source does not establish.

## 8. Required safety and decision boundaries

- A genuine-looking PDF is not proof of authenticity.
- A hash or OCR result does not authenticate the issuing authority.
- Existence of an institution or university does not prove programme approval.
- Programme approval from 2020 does not automatically prove non-approval in 2018; the source must establish the historical proposition and any retrospective effect.
- Affiliation, programme approval, study-centre permission and individual award verification are separate scopes.
- No automated candidate rejection or fraud label is produced.
- The analyst must review any EV-02 finding and the exact source interpretation.
- If a competent source cannot establish the historical period, abstain with EV-05 rather than inventing a contradiction.

## 9. Acceptance tests to add when this case becomes an executable fixture

1. Historical existence of both entities does not clear programme approval.
2. A time-bounded affiliation order supports only the interval and relationship it actually states.
3. An authoritative explicit non-retroactive 2020 approval produces EV-02 for a 2014–2018 applicable programme claim.
4. A 2020 record without explicit historical exclusion produces EV-05, not EV-02.
5. Programme-scope EV-02 does not determine the individual award scope.
6. Missing registrar response keeps the individual award at EV-05.
7. The generated registrar question asks for roll-number, exact programme / branch and award-cycle confirmation—not a fraud opinion.
8. The output shows synthetic source IDs and does not invent government citations.
9. The explanation distinguishes supported entity facts, programme contradiction / insufficiency and the remaining award-level unknown.
10. No outcome is phrased as an automatic candidate rejection or fraud finding.

## 10. Implementation status

This scenario is now available in the Streamlit case selector as **Historical programme approval — Rohan** (`TG-DEMO-004`). The rules engine supports claim-specific recommended actions, including a distinct human-review step for the historical programme record and a narrowly scoped registrar confirmation for the fictional roll number. Regression tests cover the explicit-exclusion versus incomplete-historical-coverage distinction and the evidence metadata boundary. The UI now displays source title, publisher placeholder, reference identifier, effective period, excerpt and review state. The fixture uses only synthetic IDs and placeholder evidence; source URLs are intentionally empty, and no actual government citations or institution records are included.

## 11. Research value

This case tests whether Trust Gatekeeper can turn a broad manual investigation into:
- a historically bounded set of separate claims;
- a traceable source register;
- a correctly scoped temporal finding;
- an explicit distinction between contradiction and missing evidence; and
- a single, precise issuer-confirmation action.

It should be used as a synthetic unit / workflow case only. It does not establish that any real institution, programme, state, regulator or candidate has the described history.
