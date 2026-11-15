# CertiChain — Trust Gatekeeper

**Research focus:** Explainable academic-credential evidence triage for Indian background-verification (BGV) workflows  
**Data:** Public institutional records with fictional candidate profiles  
**Current stage:** Deterministic rules engine and showable analyst case-review prototype

## Independent project boundary

This repository is the standalone **Trust Gatekeeper** project. The earlier blockchain academic-credential ledger remains in its own repository: [CertiChain-Blockchain-Project](https://github.com/i0ankurmehta/CertiChain-Blockchain-Project).

These are two separate projects and codebases. This repository does not replace, merge into, or contain a copy of the original blockchain application's active code.

## What this project does

Trust Gatekeeper is an explainable analyst-assist research prototype. It evaluates scoped evidence claims about institutional relationships, programme status, historical periods, source conflicts, and source lineage. It keeps individual award verification separate from institution/programme context.

It is **not** a degree-issuing platform, credential repository, blockchain ledger, automated candidate-rejection system, or proof-of-fraud detector.

## Run locally

```bash
python3 -m pip install -r requirements.txt
streamlit run app.py
```

The active interface uses prebuilt synthetic cases only. Do not enter or upload real candidate, student, university, or other personal data.

## Repository contents

- `app.py` — Streamlit case workspace; opens the BBSBEC 2018–19 evidence walkthrough by default and retains the synthetic rules-engine cases.
- `tg_bbsbec_demo.py` — curated BBSBEC case view, public-source register, timeline, IT closure review, CSE positive control, analyst brief and registrar-request export.
- `tg_rules.py` — deterministic TG-RULES-001 evidence-adjudication engine.
- `tg_demo_cases.py` — fictional rules-engine demonstration cases.
- `tests/test_tg_rules.py` — 27 rules-engine tests.
- `tests/test_bbsbec_demo.py` — 6 tests for the BBSBEC case brief, source register and expected review boundaries.
- `DEMO_WALKTHROUGH.md` — short presenter script for showing the prototype.
- `research/trust-gatekeeper/` — problem definition, competitor gap analysis, ontology, benchmark protocol, research plan, operational standards, analyst checklist, worked cases, adjudication rules, and project-boundary note.

## Current limitations

The Streamlit interface now includes a curated, source-linked BBSBEC case workspace with an IT closure-review scenario and a CSE positive control. It displays the historical timeline, claim-by-claim findings, evidence-source limitations and a targeted registrar question. This is a manually curated demonstration, not live automated research. It still does not implement candidate PDF/image upload, OCR, automatic CSV/JSON intake, live regulator-source ingestion, a dynamically generated graph, or individual issuer verification.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

GitHub Actions compiles the active application and runs the unit tests on pushes to `main` and pull requests. The current suite contains 33 tests: 27 rules-engine tests and 6 BBSBEC-demo tests.

## Research boundaries

The benchmark design is a protocol; the 240-case dataset has not yet been generated. Passing synthetic tests does not establish real-world fraud-detection accuracy. Public-source absence does not prove a qualification is invalid, and this prototype does not authenticate an individual's award without the issuer.

See the [research index](research/trust-gatekeeper/README.md) for the research pack and implementation boundaries.
