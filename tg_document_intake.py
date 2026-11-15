"""Text-PDF intake and scoped extraction for AICTE Extension of Approval reports."""
from __future__ import annotations

import hashlib
import io
import re
from typing import Any, Dict, List

from pypdf import PdfReader

MAX_UPLOAD_BYTES = 20 * 1024 * 1024
MAX_PAGES = 40
SOURCE_PDF_URL = (
    "https://bbsbec.edu.in/wp-content/uploads/2019/04/"
    "AICTE-EOA-Report_2018-19.pdf"
)

# Selected fields from the publicly linked AICTE-generated BBSBEC EoA report.
# This is a source excerpt for parser testing, not a fabricated candidate record.
PUBLIC_SAMPLE_TEXT = """
All India Council for Technical Education
A Statutory body under Ministry of HRD, Govt. of India
APPROVAL PROCESS 2018-19
Extension of Approval (EoA)
F.No. North-West/1-3517507353/2018/EOA
Date: 10-Apr-2018
Sub: Extension of Approval for the Academic Year 2018-19
Permanent Id Name of the Institute | 1-14182101 BABA BANDA SINGH BAHADUR ENGINEERING COLLEGE | Application Id Name of the Society/Trust | 1-3517507353 BABA BANDA SINGH BAHADUR EDUCATION TRUST
To conduct following Courses with the Intake indicated below for the Academic Year 2018-19
Program ENGINEERING AND TECHNOLOGY | Shift 1st | Level UNDER GRADUATE | Course COMPUTER SCIENCE & ENGINEERING | FT/PT+ FT | Affiliating Body (Univ/Body) I.K Gujral Punjab Technical University, Jalandhar | Intake Approved for 2018-19 180
Program ENGINEERING AND TECHNOLOGY | Shift 1st | Level UNDER GRADUATE | Course ELECTRONICS & COMMUNICATION ENGG | FT/PT+ FT | Affiliating Body (Univ/Body) I.K Gujral Punjab Technical University, Jalandhar | Intake Approved for 2018-19 60
Application No:1-3517507353
Course(s) Applied for Closure by the Institute for the Academic Year 2018-19
Program ENGINEERING AND TECHNOLOGY | Shift 1st | Level UNDER GRADUATE | Course INFORMATION TECHNOLOGY | FT/PT+ FT | Affiliating Body (Univ/Body) I.K Gujral Punjab Technical University, Jalandhar | Course Closure Status Approved
In case of any differences in content in this Computer generated Extension of Approval Letter, the content/information as approved by the Executive Council / General Council as available on the record of AICTE shall be final and binding.
"""

_COURSE_APPROVED_RE = re.compile(
    r"Course\s+(.+?)\s*\|\s*FT/PT\+?\s*([^|]+?)\s*\|\s*"
    r"Affiliating Body\s*\([^)]*\)\s*([^|]+?)\s*\|\s*"
    r"Intake Approved for\s*(?:20\d{2}\s*[-–]\s*\d{2,4}\s*)?(\d+)",
    re.IGNORECASE,
)
_COURSE_CLOSURE_RE = re.compile(
    r"Course\s+(.+?)\s*\|\s*FT/PT\+?\s*([^|]+?)\s*\|\s*"
    r"Affiliating Body\s*\([^)]*\)\s*([^|]+?)\s*\|\s*"
    r"Course Closure Status\s*(Approved|Not Approved|Rejected|Pending)",
    re.IGNORECASE,
)


def _compact(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _unique(values: List[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        cleaned = _compact(value).strip(" ,;|")
        key = cleaned.casefold()
        if cleaned and key not in seen:
            seen.add(key)
            result.append(cleaned)
    return result


def extract_pdf_text(pdf_bytes: bytes) -> Dict[str, Any]:
    """Extract selectable text from a bounded PDF upload; never writes the file."""
    if not isinstance(pdf_bytes, bytes) or not pdf_bytes:
        raise ValueError("Choose a PDF file first.")
    if len(pdf_bytes) > MAX_UPLOAD_BYTES:
        raise ValueError("The PDF is larger than the 20 MB prototype limit.")
    if not pdf_bytes.startswith(b"%PDF"):
        raise ValueError("The uploaded file does not have a valid PDF signature.")

    try:
        reader = PdfReader(io.BytesIO(pdf_bytes), strict=False)
        if reader.is_encrypted:
            try:
                unlocked = reader.decrypt("")
            except Exception as exc:
                raise ValueError("This PDF is encrypted and cannot be opened.") from exc
            if not unlocked:
                raise ValueError("This PDF is password-protected.")
        page_count = len(reader.pages)
        if page_count > MAX_PAGES:
            raise ValueError(
                f"The PDF has {page_count} pages; the prototype limit is {MAX_PAGES}."
            )
        text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError(f"The PDF could not be read: {exc}") from exc

    if len(text) < 80:
        raise ValueError(
            "No usable text layer was found. This appears to be a scanned/image-only PDF; "
            "OCR is not implemented in this prototype."
        )

    return {
        "text": text,
        "page_count": page_count,
        "sha256": hashlib.sha256(pdf_bytes).hexdigest(),
        "extraction_method": "pypdf text-layer extraction",
    }


def parse_aicte_eoa_text(text: str) -> Dict[str, Any]:
    """Extract explicit fields and course rows from an AICTE EoA text layer."""
    compact = _compact(text)
    is_aicte_eoa = (
        "all india council for technical education" in compact.casefold()
        and "extension of approval" in compact.casefold()
        and "approval process" in compact.casefold()
    )
    if not is_aicte_eoa:
        return {
            "recognised": False,
            "document_type": "Unsupported document",
            "extraction_notes": [
                "This parser currently supports AICTE Extension of Approval (EoA) reports only."
            ],
            "approved_courses": [],
            "closure_courses": [],
            "affiliating_bodies": [],
        }

    file_number_match = re.search(
        r"F\.?\s*No\.?\s*([A-Za-z0-9./-]+)", compact, re.IGNORECASE
    )
    application_match = re.search(
        r"Application\s+No\s*:?\s*(1-\d+)", compact, re.IGNORECASE
    )
    if not application_match:
        application_match = re.search(
            r"Application\s+Id.{0,80}?(1-\d+)", compact, re.IGNORECASE
        )
    permanent_match = re.search(
        r"Permanent\s+Id.{0,100}?(1-\d+)", compact, re.IGNORECASE
    )
    institution_match = re.search(
        r"Permanent\s+Id\s+Name\s+of\s+the\s+Institute\s*\|\s*"
        r"\d+-\d+\s+(.+?)\s*\|\s*Application\s+Id",
        compact,
        re.IGNORECASE,
    )
    institution = _compact(institution_match.group(1)) if institution_match else None

    year_match = re.search(
        r"Academic\s+Year\s*(20\d{2}\s*[-–]\s*\d{2,4})",
        compact,
        re.IGNORECASE,
    )
    session = (
        re.sub(r"\s+", "", year_match.group(1)).replace("–", "-")
        if year_match else None
    )
    date_match = re.search(
        r"\bDate\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
        compact,
        re.IGNORECASE,
    )

    approved_courses = []
    for match in _COURSE_APPROVED_RE.finditer(compact):
        approved_courses.append(
            {
                "course": _compact(match.group(1)).upper(),
                "study_mode": _compact(match.group(2)).upper(),
                "affiliating_body": _compact(match.group(3)),
                "approved_intake": int(match.group(4)),
                "source_excerpt": _compact(match.group(0)),
            }
        )

    closure_courses = []
    closure_heading = re.search(
        r"Course\(s\)\s+Applied\s+for\s+Closure", compact, re.IGNORECASE
    )
    if closure_heading:
        closure_text = compact[closure_heading.start():]
        closure_text = re.split(
            r"In\s+case\s+of\s+any\s+differences|Note\s*:\s*Validity",
            closure_text,
            maxsplit=1,
            flags=re.IGNORECASE,
        )[0]
        for match in _COURSE_CLOSURE_RE.finditer(closure_text):
            closure_courses.append(
                {
                    "course": _compact(match.group(1)).upper(),
                    "study_mode": _compact(match.group(2)).upper(),
                    "affiliating_body": _compact(match.group(3)),
                    "closure_status": _compact(match.group(4)).title(),
                    "source_excerpt": _compact(match.group(0)),
                }
            )

    all_bodies = [row["affiliating_body"] for row in approved_courses + closure_courses]
    if not all_bodies:
        all_bodies = re.findall(
            r"Affiliating\s+Body\s*\([^)]*\)\s*([^|]+)",
            compact,
            re.IGNORECASE,
        )

    notes = []
    if not approved_courses:
        notes.append("No approved-course rows were parsed; inspect the original PDF table layout.")
    if not closure_courses and closure_heading:
        notes.append("A course-closure section exists, but no closure row was parsed.")
    if not institution:
        notes.append("The institution name could not be isolated from the PDF text layer.")

    return {
        "recognised": True,
        "document_type": "AICTE Extension of Approval (EoA)",
        "institution": institution,
        "permanent_institute_id": permanent_match.group(1) if permanent_match else None,
        "application_id": application_match.group(1) if application_match else None,
        "file_number": file_number_match.group(1) if file_number_match else None,
        "approval_date": date_match.group(1) if date_match else None,
        "academic_session": session,
        "affiliating_bodies": _unique(all_bodies),
        "approved_courses": approved_courses,
        "closure_courses": closure_courses,
        "extraction_notes": notes,
    }


def _normalise(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).strip()


def _course_matches(extracted_course: str, requested_course: str) -> bool:
    left = _normalise(extracted_course)
    right = _normalise(requested_course)
    aliases = {
        "information technology": {"information technology", "it"},
        "computer science engineering": {
            "computer science engineering",
            "computer science and engineering",
            "cse",
        },
    }
    options = aliases.get(right, {right})
    return bool(left and right and (left in options or any(option in left for option in options)))


def build_programme_review(parsed: Dict[str, Any], requested_programme: str) -> Dict[str, Any]:
    """Create a bounded analyst finding for one programme in the uploaded EoA."""
    if not parsed.get("recognised"):
        return {
            "status": "UNSUPPORTED DOCUMENT",
            "finding": "This file was not recognised as an AICTE EoA report.",
            "registrar_question": (
                "Please provide the official approval/affiliation record for the claimed "
                "institution, programme and academic session."
            ),
            "matching_approved_rows": [],
            "matching_closure_rows": [],
        }

    approved = [
        row for row in parsed.get("approved_courses", [])
        if _course_matches(row["course"], requested_programme)
    ]
    closures = [
        row for row in parsed.get("closure_courses", [])
        if _course_matches(row["course"], requested_programme)
    ]
    session = parsed.get("academic_session") or "the session stated in the report"

    if closures:
        row = closures[0]
        status = "REVIEW REQUIRED — COURSE CLOSURE ENTRY"
        finding = (
            f"The uploaded EoA lists {row['course']} in the section for courses applied "
            f"for closure for {session}; the recorded closure status is {row['closure_status']}. "
            "This is a programme-level signal. It does not establish what happened to "
            "students already admitted, whether teach-out or migration applied, or whether "
            "a particular student's award is valid."
        )
        registrar_question = (
            f"For the claimed {requested_programme} cohort in {session}, please confirm "
            "whether the candidate's admission/registration was valid and whether an "
            "approved continuation, teach-out or migration arrangement applied. Please "
            "identify the governing order and separately confirm the candidate's entry "
            "in the official award register."
        )
    elif approved:
        row = approved[0]
        status = "PROGRAMME LISTED IN APPROVED-COURSE TABLE"
        finding = (
            f"The uploaded EoA lists {row['course']} with approved intake "
            f"{row['approved_intake']} for {session}. This supports only the programme "
            "entry in this EoA; it does not verify a student's admission, attendance or award."
        )
        registrar_question = (
            f"Please confirm the candidate's admission and registration for "
            f"{requested_programme} in {session}, then verify the exact degree title, "
            "award date and roll number against the official award register."
        )
    else:
        status = "NOT FOUND IN THIS EoA"
        finding = (
            f"No matching {requested_programme} row was extracted from this EoA. "
            "That is a document-coverage gap, not proof that the programme was unauthorised. "
            "Check the correct institution, session, part/annexure and any separate approval."
        )
        registrar_question = (
            f"Please provide the authoritative approval/affiliation record covering "
            f"{requested_programme} for {session}, including any annexure, continuation "
            "or transition order applicable to the candidate's cohort."
        )

    return {
        "status": status,
        "finding": finding,
        "registrar_question": registrar_question,
        "matching_approved_rows": approved,
        "matching_closure_rows": closures,
    }


def analyse_eoa_pdf(pdf_bytes: bytes, file_name: str) -> Dict[str, Any]:
    extracted = extract_pdf_text(pdf_bytes)
    parsed = parse_aicte_eoa_text(extracted["text"])
    return {
        "file_name": file_name,
        "page_count": extracted["page_count"],
        "sha256": extracted["sha256"],
        "extraction_method": extracted["extraction_method"],
        "parsed": parsed,
    }


def analyse_public_sample() -> Dict[str, Any]:
    """Run the same parser over selected text from the public BBSBEC EoA."""
    parsed = parse_aicte_eoa_text(PUBLIC_SAMPLE_TEXT)
    return {
        "file_name": "AICTE_BBSBEC_EoA_2018-19_public_source_excerpt.txt",
        "page_count": None,
        "sha256": hashlib.sha256(PUBLIC_SAMPLE_TEXT.encode("utf-8")).hexdigest(),
        "extraction_method": "public-source text excerpt (not a PDF upload)",
        "parsed": parsed,
    }


def render_document_intake(st) -> None:
    """Render upload, extraction, programme review and registrar-query workflow."""
    import json

    st.subheader("Document analysis")
    st.caption(
        "AICTE Extension of Approval (EoA) reports · PDF text extraction · "
        "programme-level historical review"
    )
    st.markdown(
        "Upload an AICTE EoA PDF. The parser extracts institutional identifiers, "
        "academic session, affiliating body, approved-course rows and closure entries."
    )
    st.warning(
        "Text-based PDFs only. Scanned/image-only PDFs are not OCR-processed. "
        "Do not upload real candidate/student personal documents; individual awards are not authenticated."
    )
    st.link_button("Open public BBSBEC 2018–19 AICTE EoA source PDF", SOURCE_PDF_URL)

    uploaded = st.file_uploader("Upload AICTE EoA PDF", type=["pdf"], key="tg_eoa_upload")
    col_upload, col_sample = st.columns([1, 1])
    with col_upload:
        analyse_upload = st.button(
            "Extract and analyse PDF",
            type="primary",
            disabled=uploaded is None,
            use_container_width=True,
        )
    with col_sample:
        run_sample = st.button(
            "Try public-source sample",
            use_container_width=True,
            help="Runs the same parser on selected text from the linked public BBSBEC EoA report.",
        )

    if analyse_upload and uploaded is not None:
        try:
            st.session_state["tg_eoa_result"] = analyse_eoa_pdf(uploaded.getvalue(), uploaded.name)
            st.session_state.pop("tg_eoa_error", None)
        except Exception as exc:
            st.session_state["tg_eoa_error"] = str(exc)
            st.session_state.pop("tg_eoa_result", None)

    if run_sample:
        st.session_state["tg_eoa_result"] = analyse_public_sample()
        st.session_state.pop("tg_eoa_error", None)

    if st.session_state.get("tg_eoa_error"):
        st.error(st.session_state["tg_eoa_error"])

    result = st.session_state.get("tg_eoa_result")
    if not result:
        st.info(
            "Start by uploading an AICTE EoA PDF, or run the public-source sample to see "
            "the extraction and review workflow."
        )
        return

    parsed = result["parsed"]
    if not parsed.get("recognised"):
        st.error("Unsupported document type")
        st.write(parsed.get("extraction_notes", []))
        return

    st.divider()
    st.markdown("#### Extracted document fields")
    fields = [
        ("Institution", parsed.get("institution") or "Not extracted"),
        ("Permanent institute ID", parsed.get("permanent_institute_id") or "Not extracted"),
        ("Application ID", parsed.get("application_id") or "Not extracted"),
        ("AICTE file number", parsed.get("file_number") or "Not extracted"),
        ("Approval date", parsed.get("approval_date") or "Not extracted"),
        ("Academic session", parsed.get("academic_session") or "Not extracted"),
        ("Affiliating body", "; ".join(parsed.get("affiliating_bodies", [])) or "Not extracted"),
    ]
    st.dataframe(
        [{"Field": name, "Extracted value": value} for name, value in fields],
        use_container_width=True,
        hide_index=True,
    )

    approved_rows = parsed.get("approved_courses", [])
    closure_rows = parsed.get("closure_courses", [])
    m1, m2, m3 = st.columns(3)
    m1.metric("Approved-course rows", len(approved_rows))
    m2.metric("Closure rows", len(closure_rows))
    m3.metric("PDF pages", result.get("page_count") or "Sample")

    st.markdown("#### Review a programme against this EoA")
    programme = st.selectbox(
        "Programme",
        ["Information Technology", "Computer Science & Engineering"],
        key="tg_eoa_programme",
    )
    review = build_programme_review(parsed, programme)
    if review["status"].startswith("REVIEW REQUIRED"):
        st.warning(review["status"])
    elif review["status"].startswith("PROGRAMME LISTED"):
        st.success(review["status"])
    else:
        st.info(review["status"])
    st.write(review["finding"])

    rows = []
    for row in approved_rows:
        rows.append(
            {
                "Section": "Approved courses",
                "Course": row["course"],
                "Affiliating body": row["affiliating_body"],
                "Intake / status": row["approved_intake"],
            }
        )
    for row in closure_rows:
        rows.append(
            {
                "Section": "Courses applied for closure",
                "Course": row["course"],
                "Affiliating body": row["affiliating_body"],
                "Intake / status": row["closure_status"],
            }
        )
    if rows:
        st.dataframe(rows, use_container_width=True, hide_index=True)
    elif parsed.get("extraction_notes"):
        for note in parsed["extraction_notes"]:
            st.caption(note)

    st.markdown("#### Exact analyst follow-up")
    st.info(review["registrar_question"])
    st.caption(
        "This is an evidence-triage aid, not a fraud finding. A course-closure entry "
        "does not by itself determine prior-cohort or teach-out rights."
    )

    with st.expander("Document trace"):
        st.write(f"File: {result['file_name']}")
        st.write(f"Extraction: {result['extraction_method']}")
        st.write(f"SHA-256: {result['sha256']}")
        if result.get("page_count"):
            st.write(f"Pages processed: {result['page_count']}")
        st.write(f"Source PDF: {SOURCE_PDF_URL}")
        if closure_rows:
            st.markdown("**Extracted closure row**")
            st.code(closure_rows[0]["source_excerpt"], language="text")
        if approved_rows:
            st.markdown("**Extracted approved-course row**")
            st.code(approved_rows[0]["source_excerpt"], language="text")

    export = {
        "document": {
            "file_name": result["file_name"],
            "page_count": result.get("page_count"),
            "sha256": result["sha256"],
            "extraction_method": result["extraction_method"],
        },
        "extracted_claims": parsed,
        "programme_review": {"programme": programme, **review},
        "source_reference": SOURCE_PDF_URL,
        "limitations": [
            "Parser supports AICTE EoA reports only.",
            "PDF must contain selectable text; scanned PDFs are not OCR-processed.",
            "Course approval/closure entries do not establish an individual student's admission or award.",
            "Public-source absence is not treated as proof of invalidity.",
            "Issuer confirmation is still required for individual award verification.",
        ],
    }
    st.download_button(
        "Download analysis report (JSON)",
        data=json.dumps(export, indent=2, ensure_ascii=False),
        file_name="trust_gatekeeper_eoa_analysis.json",
        mime="application/json",
    )
