# 11 — Project Boundary and Repository Separation

**Document ID:** TG-BOUNDARY-001  
**Version:** 1.0  
**Date:** 14 November 2026

## Purpose

CertiChain began as a blockchain-based academic-credential ledger. Trust Gatekeeper is a distinct research direction: an explainable analyst-assist system for temporal and provenance-aware academic evidence triage in Indian background-verification workflows.

The two ideas share an academic-credential domain, but they have different product goals, architectures, users, runtime dependencies, evaluation methods and claims. They are maintained as **two separate GitHub repositories**.

- Original blockchain ledger: https://github.com/i0ankurmehta/CertiChain-Blockchain-Project
- New research prototype: https://github.com/i0ankurmehta/CertiChain-Trust-Gatekeeper

## Product boundary

Trust Gatekeeper is not a blockchain-ledger upgrade, replacement UI, credential issuer, credential wallet, or public credential repository. Its first research question concerns whether scoped, time-aware, provenance-aware evidence assessment can make difficult BGV cases more explainable and support appropriate human review.

The original blockchain project remains independently available and should continue to be developed, tested, documented and versioned on its own merits.

## Separation rules

1. Do not merge the Trust Gatekeeper codebase into the original blockchain repository.
2. Do not replace the original blockchain repository's active application or default branch with Trust Gatekeeper.
3. Keep each repository's dependencies, tests, CI workflow, README, issues and release history independent.
4. Transfer only explicitly selected Trust Gatekeeper application and research files into this repository.
5. Do not copy the original ledger's active runtime code into this repository merely to preserve history. The original project remains the canonical home for that work.
6. Keep research claims bounded: neither project should imply that a blockchain hash authenticates an issuer or that contextual evidence triage authenticates an individual award.

## Trust Gatekeeper scope today

The active prototype contains a deterministic rules module, fictional case fixtures, a Streamlit interface and unit tests. The interface uses synthetic records only. Actual document upload/OCR, structured case intake, graph visualisation, source ingestion and issuer verification remain future work.

## Development principle

Treat the Trust Gatekeeper repository as a clean, separately testable research prototype. Any future relationship between the two projects should be an explicit architectural decision supported by a concrete requirement—not an assumption based on their shared name or domain.
