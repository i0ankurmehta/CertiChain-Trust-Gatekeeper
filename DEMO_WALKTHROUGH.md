# Trust Gatekeeper — 3-Minute Prototype Walkthrough

**Audience:** BGV practitioner, faculty reviewer or project evaluator  
**Demo case:** BBSBEC, Fatehgarh Sahib — 2018–19  
**Data boundary:** Candidate R is fictional; institutional records are public sources. No student record is accessed.

## Before the demo

Run:

```bash
python3 -m pip install -r requirements.txt
streamlit run app.py
```

The BBSBEC case opens by default. Use a desktop browser so the timeline, evidence cards and tabs are easy to see.

## 0:00–0:30 — Explain the workflow

Say:

"Trust Gatekeeper is a pre-analyst evidence workspace for difficult education-verification cases. It does not declare a certificate fake. It reconstructs the institutional context, points to the evidence and identifies the smallest unresolved question for the analyst."

Point out that the candidate is fictional and the institution-level records are linked to public sources.

## 0:30–1:15 — Show the IT closure-review case

Leave **Information Technology** selected.

Show:
- the 2018–19 BBSBEC/IKGPTU context;
- the AICTE EoA's entry for Information Technology under courses applied for closure, with closure status approved;
- the "Review required" disposition;
- the explicit caution that the record does not settle teach-out or prior-cohort rights.

Say:

"The source creates a review signal, not a fraud conclusion. We still need the candidate's admission record and the applicable closure/teach-out order."

## 1:15–1:45 — Switch to the CSE positive control

Select **Computer Science & Engineering**.

Show:
- CSE intake 180 in the same AICTE EoA;
- the IKGPTU brochure's BBSBEC listing;
- the contextual-support result;
- the individual-award status remaining unverified.

Say:

"This is the control case. The tool does not escalate every record just because it is old. It distinguishes what the institutional evidence supports from what still needs issuer confirmation."

## 1:45–2:30 — Show the historical timeline and source cards

Open **Historical timeline**, then **Evidence sources**.

Open the AICTE EoA source card and point out:
- issuer and report date;
- the fact being used;
- where the PDF is hosted;
- why the hosting/custody limitation is shown;
- what the source cannot establish.

Open the MRSPTU Board agenda card and explain that it references a State notification, while the original notification is still missing from the evidence pack.

## 2:30–3:00 — Show the analyst next step

Open **Analyst next step**.

Show:
- the exact unresolved question;
- the registrar request draft;
- the JSON analyst brief and CSV evidence-register downloads.

Close with:

"The value proposition we are testing is not replacing the registrar or the analyst. It is reducing broad manual searching and turning it into a traceable, narrow confirmation request."

## Questions to expect

**Does this authenticate the degree?**  
No. It assesses selected institutional and programme-context evidence. Individual award verification remains with the issuer or authorised award record.

**Does an approved course closure prove that a particular student could not graduate?**  
No. The record in this demo does not explain all prior-cohort or teach-out arrangements. That is why the system requests a narrow follow-up.

**Is this live AI/OCR?**  
No. The current screen is a curated source-backed demonstration. OCR, live regulator retrieval and automatic graph generation are not implemented.

**Why use a real institution with a fictional candidate?**  
It allows us to demonstrate real source handling without exposing or inventing a real student's personal data.

## Do not claim

- that the candidate is fraudulent;
- that the degree is invalid;
- that every student was barred from completion after the IT course-closure entry;
- that the affiliation-choice handoff is fully proved for BBSBEC;
- that the AICTE PDF has been independently retrieved from AICTE's own portal in this demo;
- that the prototype automatically fetches government records or reads uploaded certificates.

## Layman's one-line explanation

"Trust Gatekeeper gathers the history behind a college and course, shows the documents supporting each fact, spots a question that needs checking, and tells the analyst exactly what to ask next."
