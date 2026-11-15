# Trust Gatekeeper — Working Prototype Walkthrough

**Audience:** BGV practitioner, faculty reviewer or project evaluator  
**Primary demo:** Upload a PDF, extract its claims, correct them, and compare them with the available historical evidence  
**Reference coverage:** Curated BBSBEC records for 2018–19 only

## Before the demo

On macOS, enable scanned-PDF OCR:

    brew install tesseract

Install Python packages and launch:

    python3 -m pip install -r requirements.txt
    streamlit run app.py --server.port 8502

The Document intake workspace opens by default. Use a synthetic PDF or a document you are authorised to process. Do not use a real candidate's personal document in a public demo deployment.

## 0:00–0:30 — State the problem

Say:

"Trust Gatekeeper is an analyst-assist workflow. It reads the claims printed on an academic document, points back to the page and text line it used, and compares the analyst-confirmed claims with a scoped set of historical institutional records. It does not decide whether a person is eligible or whether a degree is genuine."

## 0:30–1:15 — Upload and extract

1. Upload a PDF degree certificate or marksheet.
2. Select **Extract claims and run historical check**.
3. Show the page count, embedded-text pages, OCR pages and unreadable pages.
4. Open the extraction table and point out the source page and source line for each field.
5. Open **Review extracted page text** to show what the parser actually read.

Say:

"This is document processing, not a hard-coded candidate screen. The claims come from the uploaded PDF. OCR is used only for image-only pages, and extraction can be wrong, so every field remains editable."

## 1:15–1:45 — Correct and confirm claims

Show the editable fields for candidate name, roll number, degree title, institution, programme, admission session, university/affiliating body and award year.

Correct one field if needed, then select **Apply corrections and rerun check**.

Say:

"The analyst stays in control. The system shows what it extracted and lets the analyst correct it before the historical comparison runs."

## 1:45–2:30 — Show the historical check

For a BBSBEC 2018–19 Information Technology document, the current reference pack should return:

**REVIEW REQUIRED — COURSE CLOSURE SIGNAL**

Show the linked AICTE EoA source and the limitation. The EoA says the IT closure status was approved, but it does not settle prior-cohort continuation, teach-out or an individual student's entitlement.

For a BBSBEC 2018–19 CSE document, the positive-control path returns contextual support based on the EoA and IKGPTU brochure. The individual award remains unverified.

For another institution, show **NO MATCH IN CURRENT REFERENCE PACK**. Explain that this means the institution is not covered by this initial source set; it is not a negative verdict.

## 2:30–3:00 — Show the analyst handoff

Show the unresolved registrar question, expand the source cards and download the JSON analyst review.

Say:

"The value we are testing is a shorter, more traceable investigation: what did the document claim, where did the extraction come from, which historical sources support or complicate it, and what exact question remains for the issuer?"

## 3:00–3:30 — Compare with the curated case workspace

Use the sidebar to open **BBSBEC 2018–19 — analyst demo**.

Switch between Information Technology and Computer Science & Engineering. Open the timeline and source cards. Use **Analyst next step** to show the scoped registrar request and evidence-register export.

The earlier synthetic rules-engine cases remain available below these two workspaces.

## Questions to expect

**Does this authenticate the degree?**  
No. It extracts document text and compares institution/programme claims to a limited source pack. Individual award verification remains with the issuer or its authorised records.

**Does OCR guarantee the extracted text is correct?**  
No. Scan quality, skew, stamps and handwriting can reduce accuracy. The analyst must inspect the page text and confirm the extracted fields.

**Does an IT course-closure entry prove that a particular student could not graduate?**  
No. The included EoA does not settle prior-cohort or teach-out arrangements. The tool raises the precise question that still needs an official record.

**What if the document is from an institution other than BBSBEC?**  
The current research pack does not cover it. The tool reports no match and asks for source collection; it does not treat missing coverage as invalidity.

**Does it check QR codes, signatures, seals or roll numbers with the university?**  
No. Those are not implemented. The SHA-256 fingerprint only identifies the uploaded file bytes; it is not issuer authentication.

## Do not claim

- that a candidate is fraudulent or their degree is invalid;
- that the tool verifies individual admission, examinations or awards;
- that the BBSBEC source pack covers every academic year or every programme;
- that OCR has perfect accuracy;
- that government records are fetched live;
- that the system is production-ready for real candidate PII.

## Layman's one-line explanation

"Trust Gatekeeper reads a degree PDF, shows the claims it found, checks those claims against the historical records currently in its source pack, and gives the analyst the next question to verify."
