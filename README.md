# CertiChain — Trust Gatekeeper

**Research focus:** Explainable academic-credential evidence triage for Indian background-verification (BGV) workflows  
**Data:** Synthetic fixtures only  
**Current stage:** Deterministic rules engine and synthetic demonstration UI

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

- `app.py` — Streamlit interface for synthetic Trust Gatekeeper cases.
- `tg_rules.py` — deterministic TG-RULES-001 evidence-adjudication engine.
- `tg_demo_cases.py` — fictional demonstration cases.
- `tests/test_tg_rules.py` — 25 unit tests for intake, temporal reasoning, source dependencies, conflicts, mismatches, and award-verification boundaries.
- `research/trust-gatekeeper/` — problem definition, competitor gap analysis, ontology, benchmark protocol, research plan, operational standards, analyst checklist, worked cases, adjudication rules, and project-boundary note.

## Current limitations

The Streamlit interface runs prebuilt synthetic cases and displays their findings. It does not yet implement actual PDF/image upload, OCR, CSV/JSON case intake, regulator-source ingestion, graph visualisation, or issuer verification. These are later milestones and should be built only after the rules engine and benchmark are validated.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

GitHub Actions compiles the active application and runs the unit tests on pushes to `main` and pull requests.

## Research boundaries

The benchmark design is a protocol; the 240-case dataset has not yet been generated. Passing synthetic tests does not establish real-world fraud-detection accuracy. Public-source absence does not prove a qualification is invalid, and this prototype does not authenticate an individual's award without the issuer.

See the [research index](research/trust-gatekeeper/README.md) for the research pack and implementation boundaries.
