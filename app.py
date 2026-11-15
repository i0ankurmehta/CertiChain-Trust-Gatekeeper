"""CertiChain Trust Gatekeeper — document intake and evidence review UI."""

import json
from datetime import datetime, timezone

import streamlit as st

from tg_demo_cases import DEMO_CASES, get_demo_case
from tg_rules import OUTCOME_LABELS, assess_case
from tg_bbsbec_demo import render_bbsbec_demo
from tg_document_intake import render_document_intake


st.set_page_config(
    page_title="CertiChain | Trust Gatekeeper",
    page_icon="🧭",
    layout="wide",
)

st.title("CertiChain | Trust Gatekeeper")
st.caption("Temporal and provenance-aware academic credential evidence triage")
st.warning(
    "RESEARCH PROTOTYPE — document analysis currently supports text-based AICTE EoA PDFs. "
    "The historical case view uses curated public records and fictional candidate profiles. "
    "Do not upload real candidate/student personal data. Individual awards are not authenticated."
)

with st.sidebar:
    st.header("Workspace")
    workspace = st.radio(
        "Open",
        ["Document analysis", "Historical case review"],
        index=0,
    )

if workspace == "Document analysis":
    render_document_intake(st)
    st.stop()

with st.sidebar:
    st.divider()
    st.header("Case workspace")
    case_options = ["BBSBEC 2018–19 — analyst demo", *DEMO_CASES.keys()]
    selected_case = st.selectbox("Choose a case", case_options)
    if selected_case == "BBSBEC 2018–19 — analyst demo":
        st.caption("Source-backed institution case with a fictional candidate profile.")
        st.caption("Switch between an IT course-closure review and a CSE positive control.")
    else:
        demo_case = get_demo_case(selected_case)
        st.caption(demo_case["description"])
        st.divider()
        st.subheader("Intake gates")
        authority_ok = st.checkbox("Processing authority documented (fixture)", value=True)
        input_safe = st.checkbox("Input passed safety checks (fixture)", value=True)
        st.caption("These controls test the intake gate. They are not a legal consent workflow.")

if selected_case == "BBSBEC 2018–19 — analyst demo":
    render_bbsbec_demo(st)
    st.stop()

case = get_demo_case(selected_case)
case["processing_authority_documented"] = authority_ok
case["input_safe"] = input_safe
assessment = assess_case(case)

primary = assessment["primary_outcome"]
primary_label = assessment["primary_label"]

summary_cols = st.columns(4)
summary_cols[0].metric("Case ID", assessment["case_id"])
summary_cols[1].metric("Primary finding", primary)
summary_cols[2].metric("Assessment state", assessment["case_state"].replace("_", " ").title())
summary_cols[3].metric("Human review", "Required" if assessment["review_required"] else "Not required")

st.subheader(primary_label)
st.write(assessment["explanation"])
if primary == "EV-01":
    st.success("The scoped contextual checks are consistent. Individual award verification remains a separate check.")
elif primary == "EV-07":
    st.error("Intake is blocked. No substantive evidence assessment was performed.")
else:
    st.warning("This is a preliminary evidence finding, not a fraud verdict or candidate decision.")

if assessment["secondary_findings"]:
    st.write("**Additional findings:** " + ", ".join(
        f"{code} — {OUTCOME_LABELS[code]}" for code in assessment["secondary_findings"]
    ))

st.subheader("Claim-by-claim assessment")
if assessment["scope_results"]:
    st.dataframe(
        [
            {
                "Claim ID": row["claim_id"],
                "Scope": row["scope"],
                "Outcome": row["outcome"],
                "Finding": row["label"],
                "Evidence IDs": ", ".join(row["evidence_ids"]) or "None",
                "Explanation": row["explanation"],
            }
            for row in assessment["scope_results"]
        ],
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No claim-level checks were run because intake is blocked.")

st.subheader("Evidence source register")
evidence_records = case.get("evidence", [])
if evidence_records:
    st.caption(
        "Inspect which source is attached to each claim, its stated effective period, "
        "reference identifier and supporting excerpt."
    )
    if any(item.get("source_record_status", "").startswith("SYNTHETIC") for item in evidence_records):
        st.warning(
            "SYNTHETIC SOURCE RECORDS — the titles, publishers, reference numbers and excerpts below "
            "are fabricated test placeholders. They are not government citations and have no live source URLs."
        )

    source_rows = []
    for item in evidence_records:
        sessions = item.get("valid_sessions")
        if sessions:
            effective_period = ", ".join(str(value) for value in sessions)
        elif item.get("valid_from"):
            end = item.get("valid_to")
            if end:
                effective_period = f"{item['valid_from']} to {end}"
            elif item.get("open_ended") is True:
                effective_period = f"From {item['valid_from']} (open-ended in fixture)"
            else:
                effective_period = f"From {item['valid_from']} (end date unknown)"
        else:
            effective_period = "Not specified"

        source_rows.append(
            {
                "Evidence ID": item.get("evidence_id", "Not supplied"),
                "Source": item.get("source_title", "Source title not supplied"),
                "Publisher / issuer": item.get("publisher", "Not supplied"),
                "Reference": item.get("reference_number", "Not supplied"),
                "Source class": item.get("source_class", "Not supplied"),
                "Effective period": effective_period,
                "Review state": item.get("review_state", "Not supplied"),
            }
        )
    st.dataframe(source_rows, use_container_width=True, hide_index=True)

    for item in evidence_records:
        evidence_label = item.get("evidence_id", "Evidence record")
        source_label = item.get("source_title", item.get("source_id", "Untitled source"))
        with st.expander(f"{evidence_label} — {source_label}"):
            st.write(f"**Publisher / issuer:** {item.get('publisher', 'Not supplied')}")
            st.write(f"**Reference number:** {item.get('reference_number', 'Not supplied')}")
            st.write(
                f"**Claim scope:** {item.get('claim_scope', 'Not supplied')} · "
                f"**Subject:** {item.get('subject_id', 'Not supplied')}"
            )
            st.write(
                f"**Assertion:** {item.get('predicate', 'Not supplied')} = "
                f"{item.get('value', 'Not supplied')}"
            )
            st.write(f"**Source class:** {item.get('source_class', 'Not supplied')}")
            st.write(f"**Review state:** {item.get('review_state', 'Not supplied')}")
            if item.get("parent_source_id"):
                st.write(f"**Parent source:** {item['parent_source_id']}")
            st.markdown("**Supporting excerpt / fixture note**")
            st.write(item.get("source_excerpt", "No excerpt supplied for this evidence record."))
            if item.get("source_url"):
                st.link_button("Open source record", item["source_url"])
            else:
                st.caption("No source URL supplied. Do not treat this entry as an independently accessible citation.")
            if item.get("source_record_status"):
                st.warning(item["source_record_status"])
else:
    st.info("No evidence source records were supplied for this synthetic case.")

st.subheader("Source lineage")
if assessment["dependency_groups"]:
    st.dataframe(
        [
            {
                "Lineage root": group["root_source_id"],
                "Source IDs": ", ".join(group["source_ids"]),
                "Evidence IDs": ", ".join(group["evidence_ids"]),
                "Relationship": group["relationship"],
            }
            for group in assessment["dependency_groups"]
        ],
        use_container_width=True,
        hide_index=True,
    )
    st.caption("Related sources are grouped by known parent-source lineage; they are not counted as independent confirmations.")
else:
    st.info("No known multi-source lineage group was identified. Unknown dependency is not assumed to be independence.")

left, right = st.columns(2)
with left:
    st.subheader("Unresolved questions")
    if assessment["unresolved_questions"]:
        for item in assessment["unresolved_questions"]:
            st.markdown(f"- {item}")
    else:
        st.write("No unresolved question was produced for this synthetic fixture.")
with right:
    st.subheader("Recommended next actions")
    if assessment["recommended_actions"]:
        for item in assessment["recommended_actions"]:
            st.markdown(f"- {item}")
    else:
        st.write("No additional action was produced.")

with st.expander("Inspect synthetic case evidence and inputs"):
    st.markdown(f"**Input mode:** {case.get('input_mode', 'not specified')}")
    st.markdown("**Field comparisons**")
    st.dataframe(case.get("field_comparisons", []), use_container_width=True, hide_index=True)
    st.markdown("**Required claims**")
    st.json(case.get("required_claims", []))
    st.markdown("**Evidence records**")
    st.json(case.get("evidence", []))

with st.expander("Inspect complete assessment output"):
    st.json(assessment)

report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "case_fixture": case,
    "assessment": assessment,
}
st.download_button(
    "Download synthetic assessment JSON",
    data=json.dumps(report, indent=2, ensure_ascii=False),
    file_name=f"{assessment['case_id'].lower()}_assessment.json",
    mime="application/json",
)

st.divider()
st.caption(
    "TG-RULES-001 v0.1 · Synthetic-only rules-engine cases · Human review required for unresolved findings. "
    "The document-analysis workspace is a separate text-PDF EoA parser; it does not perform OCR or award authentication."
)
