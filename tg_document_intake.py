"""PDF intake, claim extraction and scoped historical-record comparison.

This module processes PDFs in memory. It does not persist uploads, authenticate
a degree, or make candidate decisions. Scanned-page OCR is optional and requires
the Tesseract executable to be installed on the host.
"""

from __future__ import annotations

import hashlib
import io
import re
from typing import Any, Dict, List, Optional, Tuple

import fitz  # PyMuPDF

from tg_bbsbec_demo import SOURCES

MAX_UPLOAD_BYTES = 15 * 1024 * 1024
MAX_PDF_PAGES = 12

INSTITUTION_ALIASES = {
    "Baba Banda Singh Bahadur Engineering College": (
        "Baba Banda Singh Bahadur Engineering College",
        "Baba Banda Singh Bahadur Engg College",
        "BBSBEC",
    ),
}

UNIVERSITY_ALIASES = {
    "I.K. Gujral Punjab Technical University": (
        "I.K. Gujral Punjab Technical University",
        "IKGPTU",
        "Punjab Technical University",
        "PTU",
    ),
    "Maharaja Ranjit Singh Punjab Technical University": (
        "Maharaja Ranjit Singh Punjab Technical University",
        "MRSPTU",
        "MRS Punjab Technical University",
    ),
}

PROGRAMME_PATTERNS = (
    (r"computer\s+science\s*(?:&|and)\s*engineering", "Computer Science & Engineering"),
    (r"\bCSE\b", "Computer Science & Engineering"),
    (r"information\s+technology", "Information Technology"),
    (r"\bB\.?\s*TECH\s*\(?\s*IT\s*\)?", "Information Technology"),
    (r"artificial\s+intelligence\s*(?:&|and)\s*data\s+science", "Artificial Intelligence & Data Science"),
    (r"\bAI\s*(?:&|and)\s*DS\b", "Artificial Intelligence & Data Science"),
    (r"mechanical\s+engineering", "Mechanical Engineering"),
    (r"civil\s+engineering", "Civil Engineering"),
    (r"electronics\s*(?:&|and)\s*communication\s+engineering", "Electronics & Communication Engineering"),
)

FIELD_PATTERNS = {
    "candidate_name": (
        r"(?:candidate|student|graduate)\s+name\s*[:\-]\s*([^\n]{3,80})",
        r"name\s+of\s+(?:the\s+)?(?:candidate|student)\s*[:\-]\s*([^\n]{3,80})",
    ),
    "roll_number": (
        r"(?:roll\s*(?:no\.?|number)|registration\s*(?:no\.?|number)|enrol(?:ment)?\s*(?:no\.?|number))\s*[:#\-]?\s*([A-Z0-9\/\-]{3,30})",
    ),
    "degree_title": (
        r"\b(Bachelor\s+of\s+Technology|B\.?\s*Tech\.?|Master\s+of\s+Technology|M\.?\s*Tech\.?|Bachelor\s+of\s+Engineering|B\.?\s*E\.?)\b",
    ),
    "academic_session": (
        r"(?:academic\s+session|session|admission\s+batch|batch)\s*[:\-]?\s*((?:19|20)\d{2}\s*[-–/]\s*(?:\d{2}|(?:19|20)\d{2}))",
    ),
    "award_year": (
        r"(?:date\s+of\s+(?:award|issue|conferral)|awarded\s+on|degree\s+date)\s*[:\-]?\s*(?:\d{1,2}[\/\-. ]+)?(?:[A-Za-z]+\s+)?((?:19|20)\d{2})",
    ),
}

SOURCE_BY_ID = {item["id"]: item for item in SOURCES}


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip(" \t\r\n:;,.|")


def _normalise(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", " ", value.upper()).strip()


def _normalise_session(value: str) -> str:
    match = re.search(r"((?:19|20)\d{2})\s*[-–/]\s*((?:19|20)\d{2}|\d{2})", value)
    if not match:
        return _clean(value)
    start = int(match.group(1))
    end_raw = match.group(2)
    end = int(end_raw) if len(end_raw) == 4 else (start // 100) * 100 + int(end_raw)
    if end < start:
        end += 100
    return f"{start}–{str(end)[-2:]}"


def _make_field(value: Optional[str] = None, page: Optional[int] = None,
                quote: str = "", method: str = "not_detected") -> Dict[str, Any]:
    return {
        "value": value,
        "page": page,
        "quote": quote,
        "method": method,
    }


def _find_pattern(pages: List[Dict[str, Any]], patterns: Tuple[str, ...],
                  normalise_session: bool = False) -> Dict[str, Any]:
    for page in pages:
        for line in page["text"].splitlines():
            for pattern in patterns:
                match = re.search(pattern, line, flags=re.IGNORECASE)
                if match:
                    value = _clean(match.group(1))
                    if normalise_session:
                        value = _normalise_session(value)
                    return _make_field(value, page["page"], _clean(line)[:240], page["method"])
    return _make_field()


def _find_known_name(pages: List[Dict[str, Any]], alias_map: Dict[str, Tuple[str, ...]]) -> Dict[str, Any]:
    for page in pages:
        for line in page["text"].splitlines():
            normalised_line = _normalise(line)
            for canonical, aliases in alias_map.items():
                for alias in sorted(aliases, key=len, reverse=True):
                    if _normalise(alias) and _normalise(alias) in normalised_line:
                        return _make_field(canonical, page["page"], _clean(line)[:240], page["method"])
    return _make_field()


def _find_labelled_institution(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    patterns = (
        r"(?:name\s+of\s+)?(?:college|institution|institute)\s*[:\-]\s*([^\n]{4,100})",
        r"(?:college|institution|institute)\s+name\s*[:\-]\s*([^\n]{4,100})",
    )
    return _find_pattern(pages, patterns)


def _find_programme(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    for page in pages:
        for line in page["text"].splitlines():
            for pattern, canonical in PROGRAMME_PATTERNS:
                if re.search(pattern, line, flags=re.IGNORECASE):
                    return _make_field(canonical, page["page"], _clean(line)[:240], page["method"])
    return _make_field()


def _find_university(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    known = _find_known_name(pages, UNIVERSITY_ALIASES)
    if known["value"]:
        return known
    return _find_pattern(
        pages,
        (
            r"(?:affiliated\s+to|affiliating\s+university|awarding\s+university|university\s+name)\s*[:\-]?\s*([^\n]{4,100})",
        ),
    )


def extract_claims(pages: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Extract reviewable fields with a page and source-line pointer."""
    claims = {
        "candidate_name": _find_pattern(pages, FIELD_PATTERNS["candidate_name"]),
        "roll_number": _find_pattern(pages, FIELD_PATTERNS["roll_number"]),
        "degree_title": _find_pattern(pages, FIELD_PATTERNS["degree_title"]),
        "institution": _find_known_name(pages, INSTITUTION_ALIASES),
        "programme": _find_programme(pages),
        "academic_session": _find_pattern(
            pages, FIELD_PATTERNS["academic_session"], normalise_session=True
        ),
        "university_or_affiliating_body": _find_university(pages),
        "award_year": _find_pattern(pages, FIELD_PATTERNS["award_year"]),
    }
    if not claims["institution"]["value"]:
        claims["institution"] = _find_labelled_institution(pages)
    return claims


def extract_pdf_document(pdf_bytes: bytes, ocr_scanned_pages: bool = True) -> Dict[str, Any]:
    """Extract text from a PDF and OCR image-only pages when Tesseract is available."""
    if not pdf_bytes:
        raise ValueError("The uploaded PDF is empty.")
    if len(pdf_bytes) > MAX_UPLOAD_BYTES:
        raise ValueError("PDF exceeds the 15 MB prototype limit.")

    try:
        document = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception as exc:
        raise ValueError("The file could not be opened as a valid PDF.") from exc

    if document.is_encrypted:
        document.close()
        raise ValueError("Password-protected PDFs are not supported.")
    if len(document) > MAX_PDF_PAGES:
        document.close()
        raise ValueError(f"PDF has more than {MAX_PDF_PAGES} pages. Upload a shorter extract.")

    page_records: List[Dict[str, Any]] = []
    warnings: List[str] = []
    ocr_pages = 0
    text_pages = 0

    try:
        for index, page in enumerate(document):
            text = page.get_text("text") or ""
            method = "embedded text"
            compact_text = re.sub(r"\W", "", text)

            if len(compact_text) < 18 and ocr_scanned_pages:
                try:
                    import pytesseract
                    from PIL import Image

                    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                    image = Image.open(io.BytesIO(pixmap.tobytes("png")))
                    ocr_text = pytesseract.image_to_string(image, lang="eng", config="--psm 6")
                    if len(re.sub(r"\W", "", ocr_text)) > len(compact_text):
                        text = ocr_text
                        method = "OCR"
                        ocr_pages += 1
                    else:
                        text_pages += 1
                except Exception as exc:
                    warnings.append(
                        f"Page {index + 1}: OCR could not run ({type(exc).__name__}). "
                        "Install Tesseract OCR to process scanned pages."
                    )
                    text_pages += 1
            else:
                text_pages += 1

            page_records.append({
                "page": index + 1,
                "method": method,
                "text": text,
                "character_count": len(text.strip()),
            })
    finally:
        document.close()

    if not any(item["text"].strip() for item in page_records):
        warnings.append("No readable text was extracted. Check scan quality, orientation and OCR availability.")

    claims = extract_claims(page_records)
    return {
        "file_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
        "file_size_bytes": len(pdf_bytes),
        "page_count": len(page_records),
        "text_pages": text_pages,
        "ocr_pages": ocr_pages,
        "pages": page_records,
        "claims": claims,
        "warnings": warnings,
    }


def compare_claims_to_reference_pack(claims: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Compare user-reviewed claims to the currently curated BBSBEC 2018–19 records."""
    institution = _clean((claims.get("institution") or {}).get("value") or "")
    programme = _clean((claims.get("programme") or {}).get("value") or "")
    session = _normalise_session(_clean((claims.get("academic_session") or {}).get("value") or ""))

    institution_match = "BBSBEC" in _normalise(institution) or (
        "BABA BANDA SINGH BAHADUR" in _normalise(institution)
    )

    report: Dict[str, Any] = {
        "reference_pack": "Punjab / BBSBEC 2018–19",
        "institution": institution or "Not extracted",
        "programme": programme or "Not extracted",
        "academic_session": session or "Not extracted",
        "finding": "",
        "detail": "",
        "checks": [],
        "sources": [],
        "unresolved_questions": [],
        "individual_award": "NOT VERIFIED",
        "decision_boundary": (
            "This comparison is an analyst lead only. It does not authenticate the PDF, "
            "confirm an individual award, establish fraud, or decide a candidate's eligibility."
        ),
    }

    if not institution:
        report["finding"] = "INSUFFICIENT INPUT — INSTITUTION NOT IDENTIFIED"
        report["detail"] = "Confirm the institution name from the document before comparing historical records."
        report["unresolved_questions"].append("What exact institution name appears on the original certificate?")
        return report

    if not institution_match:
        report["finding"] = "NO MATCH IN CURRENT REFERENCE PACK"
        report["detail"] = (
            "The current curated reference set covers BBSBEC, Fatehgarh Sahib, for selected historical records. "
            "No conclusion can be drawn about another institution from this limited pack."
        )
        report["unresolved_questions"].append(
            "Identify the institution's legal name and assemble its university, regulator and State records for the claimed cohort."
        )
        return report

    report["checks"].append({
        "claim": "Institution identity in available source pack",
        "finding": "MATCHED",
        "basis": "BBSBEC is named in the curated IKGPTU 2018–19 brochure and AICTE EoA record.",
        "source_ids": ["SRC-03", "SRC-04"],
    })
    report["sources"].extend(["SRC-03", "SRC-04"])

    if not session:
        report["finding"] = "INSUFFICIENT SCOPE — ADMISSION SESSION NOT IDENTIFIED"
        report["detail"] = "The institution matched, but the available historical comparison is session-specific."
        report["unresolved_questions"].append("Confirm the candidate's admission academic session (for example, 2018–19).")
        return report

    if session != "2018–19":
        report["finding"] = "OUTSIDE CURRENT HISTORICAL COVERAGE"
        report["detail"] = (
            f"The document indicates {session}. This research pack contains a BBSBEC 2018–19 source set, "
            "not a complete year-by-year approval history."
        )
        report["unresolved_questions"].append(
            f"Obtain the institution's affiliation and programme approval records for {session}."
        )
        return report

    if not programme:
        report["finding"] = "INSUFFICIENT SCOPE — PROGRAMME NOT IDENTIFIED"
        report["detail"] = "Institution and session matched; the branch/programme must be confirmed before checking the EoA."
        report["unresolved_questions"].append("Confirm the exact degree branch printed on the certificate and admission record.")
        return report

    programme_norm = _normalise(programme)
    if programme_norm in {"INFORMATION TECHNOLOGY", "B TECH IT"}:
        report["finding"] = "REVIEW REQUIRED — COURSE CLOSURE SIGNAL"
        report["detail"] = (
            "The 2018–19 AICTE EoA lists Information Technology under courses applied for closure "
            "and records the closure status as Approved. The source does not establish the effect on "
            "previously admitted students, teach-out, migration or this individual's entitlement."
        )
        report["checks"].append({
            "claim": "B.Tech Information Technology status for 2018–19",
            "finding": "REVIEW REQUIRED",
            "basis": "AICTE EoA records approved course-closure status; cohort effect is unresolved.",
            "source_ids": ["SRC-04", "SRC-06"],
        })
        report["sources"].extend(["SRC-06"])
        report["unresolved_questions"].append(
            "For the candidate's roll number, was admission/registration to B.Tech Information Technology valid for 2018–19, and did an approved teach-out, continuation or migration arrangement apply?"
        )
    elif programme_norm in {"COMPUTER SCIENCE ENGINEERING", "CSE"}:
        report["finding"] = "CONTEXT SUPPORTED — INDIVIDUAL AWARD UNVERIFIED"
        report["detail"] = (
            "The 2018–19 AICTE EoA lists B.Tech Computer Science & Engineering with approved intake 180, "
            "and the IKGPTU brochure lists BBSBEC. This supports the institution/programme context in this "
            "session only; it does not confirm a student's admission or degree."
        )
        report["checks"].append({
            "claim": "B.Tech Computer Science & Engineering status for 2018–19",
            "finding": "CONTEXT SUPPORTED",
            "basis": "AICTE EoA lists CSE with approved intake 180; IKGPTU brochure lists the college.",
            "source_ids": ["SRC-03", "SRC-04"],
        })
        report["unresolved_questions"].append(
            "Does the candidate's roll number appear in the official 2022 award register, and what exact degree title and award date are recorded?"
        )
    else:
        report["finding"] = "PROGRAMME NOT COVERED BY THIS REFERENCE CHECK"
        report["detail"] = (
            f"The extracted programme is {programme}. The current demo's session-specific programme comparison "
            "only contains CSE and Information Technology evidence."
        )
        report["unresolved_questions"].append(
            "Obtain the applicable AICTE approval, university affiliation and course-intake record for this programme and cohort."
        )

    claimed_body = _clean((claims.get("university_or_affiliating_body") or {}).get("value") or "")
    if claimed_body:
        if _normalise(claimed_body) in {"IKGPTU", "I K GUJRAL PUNJAB TECHNICAL UNIVERSITY", "PUNJAB TECHNICAL UNIVERSITY", "PTU"}:
            body_note = "The extracted university name is consistent with the IKGPTU name in the 2018–19 AICTE EoA."
        else:
            body_note = (
                f"The document text identifies {claimed_body}; the 2018–19 AICTE EoA names IKGPTU as "
                "the affiliating body. Resolve this against the primary university and award records. "
                "An AICTE affiliating-body entry is not itself proof of the individual awarding decision."
            )
        report["checks"].append({
            "claim": "University / affiliating-body text",
            "finding": "NAME TO CONFIRM",
            "basis": body_note,
            "source_ids": ["SRC-04"],
        })

    report["sources"] = list(dict.fromkeys(report["sources"]))
    return report


def get_sources(source_ids: List[str]) -> List[Dict[str, str]]:
    """Return source-register items in requested order."""
    return [SOURCE_BY_ID[source_id] for source_id in source_ids if source_id in SOURCE_BY_ID]
