# 12 — BGV Workflow Validation Guide

**Document ID:** TG-RESEARCH-012  
**Version:** 1.0  
**Status:** Fieldwork preparation  
**Date:** 14 November 2026  
**Purpose:** Workstream A — validate the analyst workflow and the assumed problem before expanding the product.

## 1. Research objective

Understand how education-verification work is actually performed by background-verification (BGV) teams, where cases become difficult, what is already automated, and when analysts escalate to a person or an external authority.

This is exploratory discovery, not a sales pitch and not a validation exercise designed to prove that Trust Gatekeeper is needed. Findings may confirm, narrow, change or reject the current product hypothesis.

## 2. Suggested participants

The first-stage research plan proposes **5–8 exploratory conversations**, subject to access:

- Education-verification analysts.
- BGV operations leads or quality reviewers.
- Product managers or solution architects responsible for education checks.

Record the participant's role and relevant experience only to the extent they are comfortable sharing. Do not collect candidate identities, employer-confidential case data, or proprietary vendor material.

A small exploratory sample can reveal workflow patterns and questions for further research. It is not a statistically representative survey of the BGV industry.

## 3. Interview setup

Suggested length: 30–40 minutes.

### Opening script

"I'm studying how education-verification cases are handled in practice. I'm interested in the workflow, evidence sources, exceptions and human-review steps—not in any individual candidate's documents. Please keep examples anonymous and avoid sharing names, roll numbers, contact details, scans, or confidential client information. You can skip any question."

Ask permission before taking notes or recording. Do not record without explicit permission.

## 4. Interview questions

Use the questions conversationally. Ask for a recent, anonymised example of a workflow or problem category where possible, not an actual document.

### A. Current workflow

1. Could you walk me through an education-verification case from the moment it arrives to the final result?
2. What information and document types normally arrive with a case?
3. Which steps are automated, which are manual, and which systems or sources are used?
4. At what points does a case move from an analyst to a senior reviewer, institution, regulator or another external party?

### B. Difficult cases and exceptions

5. What types of education-verification cases take the longest or require the most back-and-forth?
6. How do you handle a college, campus or institution whose name, affiliation or status changed over time?
7. How do you check whether a programme, mode or relationship applied to the relevant academic session?
8. What happens when two sources disagree, a source is undated, or a source appears to repeat information from another source?
9. How do you distinguish an institution-level status check from confirmation that a particular person's award was issued?

### C. Existing tools and decision-making

10. Which of these issues are already handled by your current software or provider workflow? Where does the current process still require manual judgement?
11. What evidence is sufficient to close a case, and what conditions require abstention or escalation?
12. What explanations or audit trail do clients, quality reviewers or candidates need when a case cannot be conclusively resolved?

### D. Frequency and impact

13. Roughly how often do these exception categories occur? A range or qualitative estimate is fine.
14. What is the practical impact: turnaround time, analyst effort, repeated requests, unresolved cases, quality risk or something else?
15. Which problem would be most valuable to improve, and which is already adequately solved?

Avoid asking participants to estimate industry-wide rates unless they have a credible basis for doing so. Record whether an answer is measured data, an estimate or an impression.

## 5. Workflow mapping worksheet

Complete one row for each step. Use generic process labels and anonymised descriptions.

| Stage | Actor | Input/evidence | System or source | Decision made | Manual work | Escalation / output |
|---|---|---|---|---|---|---|
| Case receipt |  |  |  |  |  |  |
| Document / data review |  |  |  |  |  |  |
| Entity identification |  |  |  |  |  |  |
| Institution / affiliation check |  |  |  |  |  |  |
| Programme / session check |  |  |  |  |  |  |
| Individual award check |  |  |  |  |  |  |
| Quality review |  |  |  |  |  |  |
| Final response / closure |  |  |  |  |  |  |

Do not assume every organisation follows these exact stages. Add, remove or rename rows to match what the participant describes.

## 6. Problem evidence log

For each distinct issue described, capture:

| Field | What to record |
|---|---|
| Issue ID | Anonymous reference such as INT-01-P02 |
| Issue category | Historical status, affiliation, programme/mode, entity identity, source conflict, source lineage, award verification, input mismatch, other |
| Participant role | Analyst, operations lead, reviewer, product, other |
| Example | Anonymised description in the participant's own terms |
| Frequency | Measured count, estimated range, occasional, rare, unknown |
| Impact | Delay, analyst effort, rework, unresolved result, quality concern, other |
| Current workaround | Manual research, phone/email, escalation, vendor feature, no workaround, other |
| Existing automation | What the current system already does |
| Evidence strength | Direct observation, measured data, participant estimate, opinion |
| Follow-up | Evidence or clarification needed |

Keep distinct issues separate. Do not combine "missing historical evidence" with "an explicit historical contradiction"; they are different research cases.

## 7. Validation matrix

After the conversations, assess each hypothesis without presuming the answer.

| Hypothesis to test | Evidence that supports it | Evidence that weakens it | Result |
|---|---|---|---|
| Historical institutional status creates recurring work | Multiple participants describe concrete session-specific cases and current process gaps | Existing tools resolve the cases reliably, or cases are extremely rare | Pending |
| Affiliation / constituent relationships are difficult to resolve over time | Analysts describe name/relationship transitions that affect decisions | Current institutional records or provider workflows already resolve them | Pending |
| Programme or mode applicability is distinct from institution-level status | Participants describe needing separate evidence for programme/session/mode | Participants do not make this distinction in real workflow | Pending |
| Source lineage and copied evidence affect confidence | Participants identify derivative sources or repeated copies as a practical problem | Independence is not decision-relevant or already handled adequately | Pending |
| Explainable abstention/escalation is valuable | Teams need targeted questions and traceable reasons for unresolved cases | Existing reports and escalation process already meet the need | Pending |

A hypothesis should be marked "supported" only when the notes contain concrete evidence and the limits of that evidence are recorded. A single opinion is not enough to establish recurring workflow pain.

## 8. Post-interview synthesis

Within 24 hours of each conversation, capture:
- the workflow as described, without imposing the Trust Gatekeeper model;
- the three most difficult case types;
- what the current systems already do;
- what requires human judgement;
- any observed distinction between historical absence of evidence and explicit contradiction;
- frequency/impact information and whether it is measured or estimated;
- direct evidence that challenges the product hypothesis;
- unanswered questions for the next conversation.

Do not put identifying details into the repository. Keep any participant contact information, scheduling notes or consent records outside this research repo and handle them appropriately.

## 9. Gate A decision

After the initial conversations and public-product review, write a short decision note answering:

1. Do practitioners recognise a recurring problem involving historical status, affiliation/programme relationships, source conflict, source traceability or evidence insufficiency?
2. Which one problem category has the clearest evidence of frequency and operational impact?
3. Which parts are already solved by current products or operating procedures?
4. Is the proposed temporal/provenance approach relevant to that specific problem?
5. What evidence is still missing?
6. Should the project proceed, narrow the scope, revise the hypothesis or stop?

**Proceed to deeper ontology/benchmark work only when the practitioner evidence supports a real recurring problem.** If the evidence does not support it, update the problem definition rather than forcing the current design.
