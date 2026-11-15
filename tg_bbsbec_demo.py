"""Showable BBSBEC historical-evidence case study.

The candidate profile is fictional. Institutional evidence links are public
records; some source copies are hosted by the institution rather than issuer.
This module presents a curated case, not a live source-ingestion service.
"""

from __future__ import annotations

import csv
import io
from datetime import datetime, timezone
from typing import Any, Dict, List


CASE_ID = "TG-PB-BBSBEC-2018-001"
CASE_TITLE = "BBSBEC · 2018–19 historical programme review"

SOURCES: List[Dict[str, str]] = [
    {
        "id": "SRC-01",
        "title": "MRSPTU Act, Punjab Act No. 5 of 2015",
        "publisher": "Government of Punjab",
        "date": "12 Feb 2015",
        "scope": "Statutory university identity and territorial area",
        "fact": "Section 5 names Fatehgarh Sahib within MRSPTU's territorial area, sets out an association mechanism with a separate State notification date, and contains a student transition proviso.",
        "limitation": "The Act alone does not prove BBSBEC's exact affiliation or a student's awarding university.",
        "url": "https://punjab.gov.in/wp-content/uploads/2023/01/The-Maharaj-Ranjit-State-Technical-University-Act-2014.pdf",
        "custody": "Government-hosted statutory PDF",
    },
    {
        "id": "SRC-02",
        "title": "MRSPTU 5th Board of Governors agenda, item 5.15",
        "publisher": "Maharaja Ranjit Singh Punjab Technical University",
        "date": "3 Aug 2016",
        "scope": "Reference to State Government notification and 1 Jul 2015 transition date",
        "fact": "The agenda records notification 7/33/2015-4TE2/5230/9/4 dated 30 Jun 2015 and states that technical colleges in MRSPTU's jurisdiction were associated from 1 Jul 2015.",
        "limitation": "This is an official university Board record referring to the State notification; the original notification and college-specific transition order are not in this demo pack.",
        "url": "https://mrsptu.ac.in/images/Files/bos_agenda/Agenda_BOG_5.pdf",
        "custody": "University-hosted Board agenda PDF",
    },
    {
        "id": "SRC-03",
        "title": "IKGPTU Information Brochure 2018–19, Part E",
        "publisher": "I.K. Gujral Punjab Technical University",
        "date": "2018 brochure",
        "scope": "Affiliated-college roster and programme listing",
        "fact": "The brochure lists Baba Banda Singh Bahadur Engineering College, Fatehgarh Sahib, as an IKGPTU affiliated college and provides a college-specific programme list.",
        "limitation": "A brochure roster does not confirm an individual's admission, roll number or award.",
        "url": "https://ptu.ac.in/wp-content/uploads/2020/09/22-6-18-Part-E-Affiliated-Colleges-of-IKGPTU_pdf.pdf",
        "custody": "University-hosted brochure PDF",
    },
    {
        "id": "SRC-04",
        "title": "AICTE Extension of Approval, application 1-3517507353",
        "publisher": "All India Council for Technical Education",
        "date": "10 Apr 2018 (report printed 11 May 2018)",
        "scope": "BBSBEC programme/intake and affiliating-body entries for 2018–19",
        "fact": "The report names IKGPTU as affiliating body; lists B.Tech CSE with intake 180; and lists Information Technology under courses applied for closure for 2018–19, with closure status Approved.",
        "limitation": "This is an AICTE-generated report hosted on the college domain. The record does not explain the effect of closure on prior cohorts, teach-out or an individual student's entitlement. Independently validate against AICTE's own record for operational use.",
        "url": "https://bbsbec.edu.in/wp-content/uploads/2019/04/AICTE-EOA-Report_2018-19.pdf",
        "custody": "College-hosted copy of an AICTE-generated EoA report",
    },
    {
        "id": "SRC-05",
        "title": "BBSBEC official Approvals & Affiliations page",
        "publisher": "Baba Banda Singh Bahadur Engineering College",
        "date": "Current page; accessed 15 Nov 2026",
        "scope": "Source discovery for year-wise EoA reports",
        "fact": "The college page lists an EOA Report 2018–19 and other year-wise approval reports.",
        "limitation": "The page is an index maintained by the college, not the regulator's independent source record.",
        "url": "https://bbsbec.edu.in/approvals-affiliations/",
        "custody": "Institution-hosted public page",
    },
    {
        "id": "SRC-06",
        "title": "IKGPTU Notifications index",
        "publisher": "I.K. Gujral Punjab Technical University",
        "date": "17 May 2018 entry",
        "scope": "Corroborating source-discovery lead for course-closure notification",
        "fact": "The official notifications index lists an item titled 'Notification- Closure of Courses' dated 17 May 2018.",
        "limitation": "The linked attachment was not independently inspected in this demo. The case finding relies on the AICTE EoA text, not this index item alone.",
        "url": "https://ptu.ac.in/notifications/",
        "custody": "University-hosted notification index",
    },
]

TIMELINE: List[Dict[str, str]] = [
    {
        "date": "12 Feb 2015",
        "event": "MRSPTU Act published",
        "detail": "Punjab Act No. 5 of 2015 defines MRSPTU's territorial area, including Fatehgarh Sahib, and an affiliation mechanism.",
        "source_ids": "SRC-01",
        "state": "Statutory context",
    },
    {
        "date": "30 Jun / 1 Jul 2015",
        "event": "State notification referenced by MRSPTU Board",
        "detail": "The 2016 Board agenda cites the State notification and records 1 July 2015 as the association effective date for technical colleges in the university's jurisdiction.",
        "source_ids": "SRC-02",
        "state": "Primary State notification still needed",
    },
    {
        "date": "10 Apr 2018",
        "event": "AICTE EoA for BBSBEC, session 2018–19",
        "detail": "The report identifies IKGPTU as affiliating body, lists CSE intake 180 and records approved closure status for IT under courses applied for closure.",
        "source_ids": "SRC-04",
        "state": "Session-level source",
    },
    {
        "date": "17 May 2018",
        "event": "IKGPTU closure-notification index entry",
        "detail": "The university's notifications index lists a course-closure notification. The underlying attachment is not part of this demo's evidence pack.",
        "source_ids": "SRC-06",
        "state": "Discovery lead",
    },
    {
        "date": "2018 brochure",
        "event": "IKGPTU affiliated-college roster",
        "detail": "BBSBEC appears in Part E of the university's 2018–19 information brochure.",
        "source_ids": "SRC-03",
        "state": "Roster evidence",
    },
]


def build_case_report(programme: str = "Information Technology") -> Dict[str, Any]:
    """Build a display/export report for the selected synthetic programme claim."""
    is_it = programme == "Information Technology"
    if programme not in {"Information Technology", "Computer Science & Engineering"}:
        raise ValueError("Unsupported demonstration programme")

    if is_it:
        programme_finding = "REVIEW REQUIRED — COURSE CLOSURE SIGNAL"
        programme_detail = (
            "The AICTE EoA lists Information Technology under courses applied for "
            "closure for 2018–19 and records closure status as Approved. The record "
            "does not explain whether an existing student could continue under a "
            "teach-out, transition or other arrangement."
        )
        next_question = (
            "For the candidate's roll number, was admission/registration to B.Tech "
            "Information Technology valid for session 2018–19, and did an approved "
            "teach-out, continuation or migration arrangement apply?"
        )
        next_action = (
            "Ask the registrar to check the 2018–19 admission register and the "
            "applicable course-closure / teach-out record. Separately confirm the "
            "exact degree title and award-register entry."
        )
        branch_status = "Closure status approved — cohort effect unresolved"
    else:
        programme_finding = "CONTEXT SUPPORTED — INDIVIDUAL AWARD UNVERIFIED"
        programme_detail = (
            "The 2018–19 AICTE EoA lists Computer Science & Engineering with "
            "approved intake 180. The IKGPTU brochure also lists BBSBEC and CSE. "
            "This supports the institution/programme context for that session, "
            "not the candidate's individual graduation."
        )
        next_question = (
            "Does the candidate's roll number appear in the official 2022 award "
            "register, and what exact degree title and award date are recorded?"
        )
        next_action = (
            "Request issuer confirmation of the roll number, exact degree title "
            "and award date. No programme-level contradiction is identified in "
            "the sources included in this demo."
        )
        branch_status = "Approved intake 180 in 2018–19 EoA"

    claims = [
        {
            "claim": "BBSBEC appears in the 2018–19 IKGPTU college record",
            "finding": "SUPPORTED IN ROSTER",
            "source_ids": ["SRC-03", "SRC-04"],
            "limit": "Does not confirm an individual student's admission or award.",
        },
        {
            "claim": "IKGPTU is named as affiliating body in the 2018–19 AICTE EoA",
            "finding": "SUPPORTED FOR THAT EoA",
            "source_ids": ["SRC-04"],
            "limit": "Does not prove the precise legal date/path of the earlier college affiliation transition.",
        },
        {
            "claim": f"B.Tech {programme} status for 2018–19",
            "finding": "REVIEW REQUIRED" if is_it else "CONTEXT SUPPORTED",
            "source_ids": ["SRC-03", "SRC-04"],
            "limit": programme_detail,
        },
        {
            "claim": "Candidate-specific admission and individual award",
            "finding": "NOT VERIFIED",
            "source_ids": [],
            "limit": "No student admission register, examination record or award-register entry is included.",
        },
    ]

    return {
        "case_id": CASE_ID,
        "case_title": CASE_TITLE,
        "candidate": "Candidate R (fictional)",
        "institution": "Baba Banda Singh Bahadur Engineering College",
        "location": "Fatehgarh Sahib, Punjab, India",
        "session": "2018–19",
        "programme": f"B.Tech {programme}",
        "candidate_data": "Synthetic profile only; no actual candidate record was accessed.",
        "disposition": "REVIEW REQUIRED" if is_it else "CONTEXT SUPPORTED — AWARD UNVERIFIED",
        "programme_finding": programme_finding,
        "programme_detail": programme_detail,
        "branch_status": branch_status,
        "claims": claims,
        "timeline": TIMELINE,
        "sources": SOURCES,
        "next_action": next_action,
        "registrar_question": next_question,
        "limitations": [
            "Candidate R and the roll number in the demonstration are fictional.",
            "The AICTE-generated EoA PDF is hosted on the college domain; independently validate it against AICTE's authoritative record for operational use.",
            "The primary State Government notification referenced in the MRSPTU Board agenda and a college-specific affiliation-choice acceptance order are not included.",
            "The AICTE closure entry does not establish the effect on all previously admitted students or teach-out rights.",
            "No individual student admission, examination or award record was accessed.",
            "This is a manually curated case demonstration; no OCR, live retrieval, automated legal interpretation or candidate decision is performed.",
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def build_sources_csv() -> str:
    output = io.StringIO()
    fields = ["id", "title", "publisher", "date", "scope", "fact", "limitation", "url", "custody"]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(SOURCES)
    return output.getvalue()


def render_bbsbec_demo(st) -> None:
    """Render the showable evidence-review workspace."""
    st.title("Historical case review")
    st.caption("Punjab technical education · BBSBEC · 2018–19 · Public-source demonstration")

    st.info(
        "DEMO CASE — Candidate R is fictional. Institutional facts below are tied to "
        "the linked public records. This is a curated evidence brief, not an automated "
        "degree-authentication or fraud decision."
    )

    programme = st.radio(
        "Select the claim to review",
        ["Information Technology", "Computer Science & Engineering"],
        horizontal=True,
        help="Switch between the course-closure review case and a positive-control programme listed in the same 2018–19 EoA.",
    )
    report = build_case_report(programme)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Case", CASE_ID)
    k2.metric("Institution context", "Supported")
    k3.metric("Programme check", "Review" if programme == "Information Technology" else "Listed")
    k4.metric("Individual award", "Unverified")

    st.subheader(report["programme_finding"])
    st.write(report["programme_detail"])
    if programme == "Information Technology":
        st.warning(
            "Do not infer that every existing student was barred from completion. "
            "The cohort / teach-out effect is not established by the EoA entry alone."
        )
    else:
        st.success(
            "Positive control: the cited sources list CSE for this institution and session. "
            "The student's individual award still requires issuer confirmation."
        )

    overview_tab, timeline_tab, evidence_tab, action_tab = st.tabs(
        ["Case overview", "Historical timeline", "Evidence sources", "Analyst next step"]
    )

    with overview_tab:
        left, right = st.columns([1, 1])
        with left:
            st.markdown("#### Submitted claim")
            st.write("**Candidate:** Candidate R (fictional)")
            st.write("**Document:** Scanned B.Tech degree (not authenticated)")
            st.write("**Institution:** Baba Banda Singh Bahadur Engineering College")
            st.write(f"**Programme:** {report['programme']}")
            st.write("**Claimed admission:** 2018–19")
            st.write("**Claimed completion:** 2022")
            st.write("**Awarding body on claim:** I.K. Gujral Punjab Technical University")
        with right:
            st.markdown("#### Evidence-based assessment")
            st.write("**Institution / college record:** Supported in the cited 2018–19 sources")
            st.write("**Affiliating body:** IKGPTU named in the AICTE EoA for 2018–19")
            st.write(f"**Programme status:** {report['branch_status']}")
            st.write("**Individual award:** Not checked; issuer confirmation required")
        st.markdown("#### Claim-by-claim result")
        st.dataframe(
            [
                {
                    "Claim": row["claim"],
                    "Finding": row["finding"],
                    "Sources": ", ".join(row["source_ids"]) or "None",
                    "Limitation": row["limit"],
                }
                for row in report["claims"]
            ],
            use_container_width=True,
            hide_index=True,
        )

    with timeline_tab:
        st.markdown("#### What the records say over time")
        for item in report["timeline"]:
            with st.container():
                st.markdown(f"**{item['date']} · {item['event']}**")
                st.write(item["detail"])
                st.caption(f"Evidence: {item['source_ids']} · {item['state']}")

    with evidence_tab:
        st.markdown("#### Source register")
        st.caption(
            "Every source is shown with its publisher, scope and limitation. "
            "A source is not treated as proof beyond the claim it actually supports."
        )
        for source in report["sources"]:
            with st.expander(f"{source['id']} · {source['title']}", expanded=source["id"] == "SRC-04"):
                st.write(f"**Publisher:** {source['publisher']}")
                st.write(f"**Date:** {source['date']}")
                st.write(f"**Scope:** {source['scope']}")
                st.write(f"**What it supports:** {source['fact']}")
                st.warning(f"**Limitation:** {source['limitation']}")
                st.caption(f"Source custody: {source['custody']}")
                st.link_button("Open source record", source["url"])

    with action_tab:
        st.markdown("#### Exact unresolved question")
        st.info(report["registrar_question"])
        st.markdown("#### Recommended analyst action")
        st.write(report["next_action"])

        registrar_template = (
            "Subject: Cohort-specific verification request — "
            f"{report['programme']}, academic session 2018–19\n\n"
            "Dear Registrar / Examination Branch,\n\n"
            "We are conducting an authorised academic qualification verification "
            "with the candidate's consent. Please confirm from the official "
            "admission and examination/award records:\n\n"
            f"1. {report['registrar_question']}\n"
            "2. The exact degree title / branch and award date recorded against "
            "the roll number.\n"
            "3. If a course-closure or teach-out arrangement applied, the order "
            "or record governing this candidate's cohort.\n\n"
            "We will provide the minimum required identifying details through "
            "your official secure verification procedure.\n\n"
            "Regards,\n[Authorised BGV organisation]\n[Case reference]"
        )
        st.markdown("#### Draft registrar request")
        st.code(registrar_template, language="text")
        st.download_button(
            "Download registrar request",
            data=registrar_template,
            file_name=f"{CASE_ID.lower()}_registrar_request.txt",
            mime="text/plain",
        )

        st.markdown("#### Download case brief")
        st.download_button(
            "Download analyst case brief (JSON)",
            data=__import__("json").dumps(report, indent=2, ensure_ascii=False),
            file_name=f"{CASE_ID.lower()}_analyst_brief.json",
            mime="application/json",
        )
        st.download_button(
            "Download evidence register (CSV)",
            data=build_sources_csv(),
            file_name="bbsbec_evidence_register.csv",
            mime="text/csv",
        )

    with st.expander("Evidence limitations and non-claims"):
        for item in report["limitations"]:
            st.markdown(f"- {item}")

    st.caption(
        "Prototype boundary: curated public-source case; no real candidate upload, OCR, "
        "live web search, automatic legal conclusion or candidate rejection."
    )
