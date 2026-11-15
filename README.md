# CertiChain — Trust Gatekeeper

**Research focus:** Explainable academic-credential evidence triage for Indian background-verification (BGV) workflows  
**Current stage:** AICTE EoA PDF intake, deterministic extraction and programme-scope review, plus research case workspace

## Independent project boundary

This repository is the standalone **Trust Gatekeeper** project. The earlier blockchain academic-credential ledger remains in its own repository: [CertiChain-Blockchain-Project](https://github.com/i0ankurmehta/CertiChain-Blockchain-Project).

These are two separate projects and codebases. This repository does not replace, merge into, or contain a copy of the original blockchain application's active code.

## What works now

### 1. AICTE EoA document analysis

The default workspace accepts an AICTE Extension of Approval (EoA) PDF and performs a real text-layer extraction. It extracts available identifiers and institutional fields, including:

- institution name and permanent institute ID;
- application ID and AICTE file number;
- approval date and academic session;
- affiliating body;
- approved-course rows and approved intake;
- course-closure rows and stated closure status.

The user selects a programme. The rules then produce a scoped finding and a targeted registrar question. For the real BBSBEC 2018–19 AICTE-generated EoA record, the intended demonstration is to identify the CSE approved-intake entry and the Information Technology closure entry, then explain what the latter does **not** establish about prior cohorts or teach-out rights.

This is a document-specific deterministic parser, not a general AI document-understanding system. It supports text-based AICTE EoA PDFs only. It does not OCR scanned PDFs, process arbitrary degree certificates, fetch live sources, or authenticate individual awards. A public-source text excerpt is available as a one-click parser test; the linked original PDF can be downloaded and uploaded to exercise the PDF extraction path.

### 2. Historical case workspace

The historical case workspace retains the BBSBEC source review, public-source timeline, IT closure review, CSE positive control, registrar request and downloads. Its fictional candidate is only a presentation fixture. The older synthetic rules-engine cases remain available there too.

## Run locally

Install the dependencies from requirements.txt and run Streamlit with app.py.

Start in **Document analysis**. Download the [public BBSBEC 2018–19 AICTE EoA PDF](https://bbsbec.edu.in/wp-content/uploads/2019/04/AICTE-EOA-Report_2018-19.pdf), upload it, and choose Information Technology or Computer Science & Engineering.

Do not upload real candidate/student personal data. The prototype is not approved for operational BGV decisions.

## Repository contents

- app.py — Streamlit workspaces and navigation.
- tg_document_intake.py — PDF text extraction, AICTE EoA parser, scoped programme review, sample runner and UI.
- tests/test_document_intake.py — document-parser and programme-review tests.
- tg_bbsbec_demo.py — curated BBSBEC case and analyst brief builders.
- tg_rules.py — deterministic TG-RULES-001 rules engine.
- tg_demo_cases.py — fictional rules-engine test cases.
- tests/test_tg_rules.py — rules-engine tests.
- tests/test_bbsbec_demo.py — BBSBEC research-case tests.
- DEMO_WALKTHROUGH.md — walkthrough for the historical case workspace.
- research/trust-gatekeeper/ — research pack and source registers.

## Important interpretation boundaries

- A course appearing in an AICTE EoA approved-course table is not proof of a particular student's admission or award.
- A course-closure entry is a programme-level signal; it does not by itself establish the position of already-admitted cohorts, teach-out, migration or individual award validity.
- A course not found in one uploaded EoA is a document-coverage gap, not proof of non-approval.
- Public-source absence is not proof that a qualification is invalid.
- Individual award verification still requires issuer or authorised award-register confirmation.
- The parser reports extracted text and source excerpts; it does not independently validate the authenticity of the uploaded PDF against AICTE's database.

## Tests

Run the suite with python3 -m unittest discover -s tests -v.

GitHub Actions compiles the application and runs all unit tests on pushes to main and pull requests. Passing parser tests demonstrates expected behaviour on the included public-source text fixture, not real-world extraction accuracy across arbitrary AICTE PDFs.
