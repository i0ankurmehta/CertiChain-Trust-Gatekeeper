"""Streamlit surface for the PDF intake workflow."""

from __future__ import annotations

import json
from typing import Any, Dict

import streamlit as st

from tg_document_intake import (
    compare_claims_to_reference_pack,
    extract_pdf_document,
    get_sources,
)


EDITABLE_FIELDS = (
    ("candidate_name", "Candidate name"),
    ("roll_number", "Roll / registration number"),
    ("degree_title", "Degree title"),
    ("institution", "Institution"),
    ("programme", "Programme / branch"),
    ("academic_session", "Admission academic session"),
    ("university_or_affiliating_body", "University / affiliating body"),
    ("award_year", "Award year"),
)


def _render_extraction_table(claims: Dict[str, Dict[str, Any]]) -> None:
    rows = []
    for key, label in EDITABLE_FIELDS:
        item = claims.get(key, {})
        rows.append({
            "Field": label,
            "Extracted value": item.get("value") or "Not detected",
            "Page": item.get("page") or "—",
            "Method": item.get("method", "not_detected"),
            "Evidence line": item.get("quote") or "—",
        })
    st.dataframe(rows, use_container_width=True, hide_index=True)


def render_document_intake() -> None:
    st.title("Document intake")
    st.caption("PDF → extracted claims → analyst corrections → historical evidence check")

    st.info(
        "Prototype intake. PDFs are processed in the running app session and are not saved by this feature. "
        "Use synthetic documents or documents you are authorised to process. Do not use this prototype for "
        "production candidate data."
    )

    uploaded = st.file_uploader(
        "Upload a degree / marksheet PDF",
        type=["pdf"],
        accept_multiple_files=False,
        help="Maximum 15 MB and 12 pages. Scanned pages use Tesseract OCR when installed.",
    )

    if uploaded is None:
        st.markdown("#### What this feature does")
        st.write(
            "Reads embedded PDF text, attempts OCR on image-only pages, extracts reviewable fields with page "
            "references, and compares the analyst-confirmed institution, programme and admission session "
            "against the BBSBEC 2018–19 research pack."
        )
        st.caption(
            "The reference pack currently covers selected BBSBEC records only. A missing match is not evidence "
            "that a college, course or degree is invalid."
        )
        return

    pdf_bytes = uploaded.getvalue()
    st.caption(f"Selected file: {uploaded.name} · {len(pdf_bytes) / 1024:.1f} KB")

    if st.button("Extract claims and run historical check", type="primary"):
        try:
            extracted = extract_pdf_document(pdf_bytes)
            st.session_state["tg_document_intake"] = {
                "filename": uploaded.name,
                "extracted": extracted,
            }
            st.session_state.pop("tg_document_reviewed_claims", None)
            st.session_state.pop("tg_document_reviewed_report", None)
        except ValueError as exc:
            st.error(str(exc))
            return

    saved = st.session_state.get("tg_document_intake")
    if not saved or saved.get("filename") != uploaded.name:
        st.caption("Select Extract claims and run historical check to process this PDF.")
        return

    extracted = saved["extracted"]
    claims = extracted["claims"]

    if extracted["warnings"]:
        for warning in extracted["warnings"]:
            st.warning(warning)

    found_count = sum(1 for item in claims.values() if item.get("value"))
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("PDF pages", extracted["page_count"])
    k2.metric("Text pages", extracted["text_pages"])
    k3.metric("OCR pages", extracted["ocr_pages"])
    k4.metric("Fields extracted", f"{found_count}/{len(claims)}")

    st.caption(
        f"SHA-256 fingerprint: {extracted['file_sha256'][:24]}… · "
        "A file fingerprint helps identify this upload; it does not prove issuer authenticity or integrity before upload."
    )

    st.subheader("1 · Extracted claims")
    st.caption("Each field includes the source page and the text line that triggered extraction.")
    _render_extraction_table(claims)

    with st.expander("Review extracted page text"):
        for page in extracted["pages"]:
            st.markdown(f"**Page {page['page']} · {page['method']} · {page['character_count']} characters**")
            st.text((page["text"] or "[No readable text on this page]")[:5000])

    st.subheader("2 · Confirm or correct the claims")
    st.caption("Extraction can be imperfect, especially on low-quality scans. Correct the fields before relying on the comparison.")
    with st.form("tg_document_claim_review"):
        edited: Dict[str, str] = {}
        cols = st.columns(2)
        for index, (key, label) in enumerate(EDITABLE_FIELDS):
            with cols[index % 2]:
                edited[key] = st.text_input(
                    label,
                    value=claims.get(key, {}).get("value") or "",
                    key=f"tg_claim_{key}",
                )
        submitted = st.form_submit_button("Apply corrections and rerun check", type="primary")

    if submitted:
        reviewed_claims = {}
        for key, _label in EDITABLE_FIELDS:
            reviewed_claims[key] = dict(claims.get(key, {}))
            reviewed_claims[key]["value"] = edited[key].strip() or None
            if edited[key].strip() and not reviewed_claims[key].get("quote"):
                reviewed_claims[key]["quote"] = "Analyst-entered correction"
                reviewed_claims[key]["method"] = "analyst corrected"
        st.session_state["tg_document_reviewed_claims"] = reviewed_claims
        st.session_state["tg_document_reviewed_report"] = compare_claims_to_reference_pack(reviewed_claims)

    reviewed_claims = st.session_state.get("tg_document_reviewed_claims", claims)
    report = st.session_state.get("tg_document_reviewed_report")
    if report is None:
        report = compare_claims_to_reference_pack(reviewed_claims)

    st.subheader("3 · Historical reference check")
    st.markdown(f"### {report['finding']}")
    st.write(report["detail"])

    if report["checks"]:
        st.dataframe(
            [
                {
                    "Claim": item["claim"],
                    "Finding": item["finding"],
                    "Basis": item["basis"],
                    "Source IDs": ", ".join(item["source_ids"]) or "—",
                }
                for item in report["checks"]
            ],
            use_container_width=True,
            hide_index=True,
        )

    if report["unresolved_questions"]:
        st.markdown("**Analyst follow-up**")
        for question in report["unresolved_questions"]:
            st.markdown(f"- {question}")

    if report["sources"]:
        st.markdown("**Linked source records**")
        for source in get_sources(report["sources"]):
            with st.expander(f"{source['id']} · {source['title']}"):
                st.write(f"**Publisher:** {source['publisher']} · **Date:** {source['date']}")
                st.write(f"**Relevant fact:** {source['fact']}")
                st.warning(f"**Limitation:** {source['limitation']}")
                st.link_button("Open source record", source["url"])

    st.warning(
        "Individual award status: NOT VERIFIED. This workflow does not verify roll numbers, admission registers, "
        "examination results, award registers, signatures or seals. It does not label a document fraudulent and "
        "must not auto-reject a candidate."
    )

    export = {
        "filename": saved["filename"],
        "file_sha256": extracted["file_sha256"],
        "extraction": {
            "page_count": extracted["page_count"],
            "text_pages": extracted["text_pages"],
            "ocr_pages": extracted["ocr_pages"],
            "warnings": extracted["warnings"],
            "claims": reviewed_claims,
        },
        "historical_check": report,
    }
    st.download_button(
        "Download analyst review (JSON)",
        data=json.dumps(export, indent=2, ensure_ascii=False),
        file_name="trust_gatekeeper_document_review.json",
        mime="application/json",
    )
