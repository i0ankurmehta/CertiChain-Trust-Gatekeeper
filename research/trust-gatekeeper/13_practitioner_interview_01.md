# 13 — Practitioner Interview 01: Historical Education Verification Bottlenecks

**Record ID:** TG-INT-001  
**Date recorded:** 14 November 2026  
**Participant:** Senior practitioner in the BGV industry (identity intentionally not recorded)  
**Record basis:** User's post-conversation recollection; not a verbatim transcript  
**Evidence type:** Single qualitative practitioner account  
**Validation status:** Preliminary signal only — not independently corroborated

## 1. Executive summary

The practitioner described a workflow in which newer degrees can be checked quickly through DigiLocker, while older credentials and degrees from smaller colleges are more likely to be routed into a manual analyst queue. According to the practitioner's account, analysts may spend weeks emailing registrars and sending physical courier requests to resolve these cases.

The practitioner also described a limitation in existing BGV tools: they may check whether a PDF appears manipulated and whether a college exists today, while failing to resolve whether the institution's relationships, programme approvals or study-centre permissions were valid during the student's actual period of study.

The proposed opportunity is a pre-analyst evidence-research layer that reconstructs the relevant historical context, shows the source for each fact, identifies timeline contradictions and tells the analyst exactly which unresolved detail needs direct confirmation from the registrar or another competent authority.

This is a promising problem signal. It is not yet proof that all providers, tools or institutions behave this way.

## 2. Practitioner-reported workflow problem

### 2.1 Newer versus older credentials

The practitioner said:
- newer degrees can be checked quickly through DigiLocker;
- older degrees and degrees from smaller colleges are more likely to be placed in a human-review queue;
- analysts may spend weeks emailing registrars and sending couriers to obtain confirmation.

**Research interpretation:** Digitised verification coverage may be uneven across institution type, credential age or record availability. The operational cost may be concentrated in exceptions rather than routine cases.

**Still to validate:** Which credential categories are affected, how often they occur, which providers use this workflow, whether DigiLocker coverage is the cause or only one factor, and what the actual turnaround-time distribution looks like.

### 2.2 Limits of current checks

The practitioner characterised existing checks as focused on:
- whether a submitted PDF appears photoshopped or manipulated; and
- whether the college exists today.

The practitioner said these checks can miss historical and jurisdictional questions such as:
- a college changing its parent or affiliating university during a student's degree;
- a course being taught before the relevant government approval was granted;
- an out-of-state study centre operating without the required authorisation.

These are practitioner-reported examples, not findings independently established by this interview note. Each would require case-specific, authoritative evidence and careful identification of the relevant jurisdiction, academic session, programme, mode and study location.

## 3. Proposed product opportunity described by the practitioner

The practitioner's proposed value was a "smart detective" stage that works before the human analyst has to perform manual research.

The described workflow would:

1. Establish the relevant institution, college, parent/affiliating university, programme, mode and study location.
2. Reconstruct what the available authoritative records establish for the relevant historical period.
3. Show where each material fact came from, including the source's date and scope.
4. Compare time-bounded relationships and approvals against the candidate's relevant academic events or session.
5. Flag contradictions, missing historical coverage and unresolved identity or jurisdiction questions separately.
6. Produce a precise, limited question for the registrar or other competent authority when direct confirmation is still needed.

The intended output is not an automatic fraud verdict or candidate decision. It is a traceable preliminary assessment that reduces avoidable manual searching and makes the remaining human verification more targeted.

## 4. Product-research implications

| Practitioner signal | Research implication | Candidate capability to test |
|---|---|---|
| Newer records are easier to verify than older/smaller-college records | Record availability and digitisation may be uneven | Evidence-coverage status and explicit "not found" semantics |
| Analysts spend weeks contacting registrars and using couriers | Manual research and external follow-up may dominate exception handling | Pre-analyst evidence pack and targeted registrar query |
| Current college existence is not enough | Present-day entity status cannot establish historical status | Time-bounded institution and entity relationships |
| Parent university may change during a degree | The relevant relationship may vary by academic session | Historical affiliation / parent-relationship timeline |
| Course may predate its approval | Institution-level recognition and programme-specific approval are different claims | Programme, mode and session-specific approval checks |
| Study centre may be outside the permitted jurisdiction | Location and territorial scope may be material | Study-centre location and jurisdiction/permission evidence |
| Analyst needs to know where each fact came from | Conclusions need source-level traceability | Claim-to-source provenance, excerpts, dates and lineage |
| Analyst needs the exact remaining question | The system should assist rather than replace expert review | Explainable abstention and narrowly scoped escalation request |

## 5. Important temporal modelling point

Do not model this as a single "valid in graduation year" checkbox.

The relevant date or session may differ by claim. Depending on the question and applicable rule, the assessment may need to distinguish:
- admission / enrolment session;
- period of programme delivery or study;
- examination period;
- completion date; and
- award / issuance date.

For example, a parent-university relationship, a programme approval and an individual award record may each have different effective periods and competent sources. The rules must identify which event the source applies to rather than selecting one convenient date for every check.

## 6. What this interview does and does not establish

### Supported as a report of what the practitioner said

- The practitioner described a faster route for some newer degrees and a slower manual route for some older or smaller-college credentials.
- The practitioner reported weeks of registrar email/courier follow-up in some cases.
- The practitioner identified historical affiliation, programme approval timing and study-centre jurisdiction as possible blind spots in current checks.
- The practitioner saw potential value in a source-traceable, timeline-aware pre-analyst research layer.

### Not established by this interview

- The percentage of cases affected or the average number of weeks lost.
- That all BGV products only perform document-forgery and current-existence checks.
- That DigiLocker is available or sufficient for every newer credential category.
- Whether the examples are common across providers, institutions, states or qualification types.
- The exact legal or regulatory requirements for any particular institution, programme or study centre.
- Whether Trust Gatekeeper can access enough authoritative historical records to resolve these cases reliably.
- Whether a graph-based method outperforms a simpler, well-structured historical evidence register.

## 7. Follow-up questions for the next practitioner conversations

1. What does "older degree" mean operationally: pre-digitisation year, legacy university, closed institution, paper-only register or something else?
2. Which exact workflow step causes the longest delay: locating a source, identifying the correct authority, waiting for a registrar response, or interpreting conflicting records?
3. What proportion of cases are resolved through DigiLocker, institutional portals, third-party databases and direct manual confirmation?
4. Do existing providers already maintain historical affiliation, programme approval and study-centre records? If so, what coverage or quality limitations remain?
5. Which academic event determines the relevant period for each type of check?
6. What official records are accepted as sufficient evidence for historical affiliation, course approval and study-centre permission?
7. What is a useful, acceptable analyst output: a timeline, source register, exception report, draft registrar query or all of these?
8. What must always remain a human or issuer confirmation step?

Ask for anonymised process descriptions and broad ranges only. Do not request candidate documents, names, roll numbers, confidential client records or proprietary vendor materials.

## 8. Gate A status

**Status: OPEN — early positive qualitative signal, not passed.**

This first account supports continuing discovery. Before treating the problem as validated:
- conduct additional conversations across distinct BGV roles or organisations;
- map the actual workflow from receipt to closure;
- distinguish measured turnaround data from estimates and impressions;
- review vendor capabilities and request demonstrations where possible;
- identify which historical facts can be established through authoritative, accessible sources; and
- document counterexamples where current tools already solve the problem.

Proceed with the research direction provisionally, but do not claim market-wide validation or commercial readiness.

## 9. Working problem statement (provisional)

For some education-verification cases—particularly older credentials and credentials involving complex institutional histories—present-day document checks and entity lookups may not resolve what was authorised during the relevant period. Analysts may then have to reconstruct historical relationships and approvals manually, sometimes waiting for direct institutional confirmation.

Trust Gatekeeper's research hypothesis is that a temporal, provenance-aware evidence assessment can prepare a traceable historical context, flag contradictions or missing evidence, and identify the precise unresolved question for a human analyst or competent authority.

**This problem statement remains provisional until supported by additional practitioner evidence and source validation.**
