# CertiChain — Trust Gatekeeper

**Research focus:** Explainable academic-credential evidence triage for Indian background-verification (BGV) workflows  
**Current stage:** Working PDF intake, claim extraction, analyst correction and a bounded historical-record comparison  
**Reference data:** Public BBSBEC institutional records for selected 2018–19 claims; candidate/document inputs are processed per session

## Independent project boundary

This repository is the standalone **Trust Gatekeeper** project. The earlier blockchain academic-credential ledger remains in its own repository: [CertiChain-Blockchain-Project](https://github.com/i0ankurmehta/CertiChain-Blockchain-Project).

These are two separate projects and codebases. This repository does not replace, merge into, or contain a copy of the original blockchain application's active code.

## What Trust Gatekeeper does now

The primary workspace is an actual PDF intake workflow:

1. Upload a PDF degree certificate or marksheet (15 MB / 12-page limit).
2. Extract embedded PDF text; attempt OCR on image-only pages when Tesseract is installed.
3. Identify candidate name, roll/registration number, degree title, institution, programme, admission session, university/affiliating body and award year when the document contains recognisable labels.
4. Show the page number and supporting text line for each extracted field.
5. Let an analyst correct the extracted claims.
6. Compare the confirmed institution, programme and admission session against the curated BBSBEC 2018–19 evidence pack.
7. Display source references, limitations and the next question for human follow-up; export the review as JSON.

The current reference check has two programme paths for BBSBEC 2018–19:
- **Information Technology:** review-required course-closure signal; the underlying source does not settle existing-student teach-out or transition rights.
- **Computer Science & Engineering:** institution/programme context supported by the included sources; individual award remains unverified.

For an institution not covered by the current pack, the system reports **No match in current reference pack**. It does not interpret missing coverage as invalidity.

## Run locally

On macOS, install Tesseract once to enable OCR for scanned PDFs:

    brew install tesseract

Then install and run the app:

    python3 -m pip install -r requirements.txt
    streamlit run app.py --server.port 8502

Embedded-text PDFs work without Tesseract. The Streamlit Community Cloud build can install the OCR executable using packages.txt.

## Privacy and safety boundary

- This prototype processes the uploaded PDF in the running app session; the document-intake code does not write the original file to a database or permanent storage.
- Do not upload real candidate or student documents to a public demo deployment. Use synthetic documents or records you are authorised to process.
- The app is not a production BGV system and has not undergone security, privacy or legal review.
- It does not authenticate issuer signatures, QR codes, seals, roll numbers, admission registers, examinations or award registers.
- It does not determine fraud, qualification validity or candidate eligibility, and must never auto-reject a candidate.

## Repository contents

- **app.py** — primary workspace selector; Document intake opens by default, with the BBSBEC case walkthrough and synthetic rules-engine cases retained.
- **tg_document_intake.py** — PDF parsing, optional OCR, field extraction and BBSBEC historical-reference comparison.
- **tg_document_intake_ui.py** — upload, correction, result and JSON-export interface.
- **tg_bbsbec_demo.py** — source register, timeline, IT closure review, CSE positive control and registrar-request export.
- **tg_rules.py** — deterministic TG-RULES-001 evidence-adjudication engine.
- **tg_demo_cases.py** — fictional rules-engine demonstration cases.
- **tests/test_document_intake.py** — 8 tests for PDF extraction, field provenance, historical comparisons and input limits.
- **tests/test_tg_rules.py** — 27 rules-engine tests.
- **tests/test_bbsbec_demo.py** — 6 BBSBEC case/source-register tests.
- **DEMO_WALKTHROUGH.md** — walkthrough for the PDF intake and historical case review.
- **research/trust-gatekeeper/** — problem definition, competitor gap analysis, ontology, benchmark protocol, research plan, operational standards, analyst checklist, worked cases and project boundaries.

## Tests

Run:

    python3 -m unittest discover -s tests -v

GitHub Actions compiles the active application and runs the test suite on relevant changes to main and pull requests. The suite contains 41 tests: 27 rules-engine tests, 6 BBSBEC-demo tests and 8 document-intake tests.

## Current limitations and next build boundary

The PDF parser uses deterministic text patterns, not a trained document-understanding model. OCR quality depends on scan quality and the local Tesseract language pack. Extracted fields always require analyst review.

The historical matcher is deliberately narrow: it currently checks only the curated BBSBEC 2018–19 evidence pack and two programme paths. It does not yet support a general institution registry, automatic discovery of government records, a live temporal graph, bulk case queues, or issuer verification.

Passing synthetic unit tests demonstrates code behaviour, not real-world extraction accuracy or BGV time savings. A broader institution registry should be added only after its source records, temporal validity and evidence limitations are independently assembled.

See the research index in research/trust-gatekeeper/README.md for the research pack.
