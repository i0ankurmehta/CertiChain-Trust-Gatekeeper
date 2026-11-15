import unittest

import fitz

from tg_document_intake import (
    MAX_UPLOAD_BYTES,
    compare_claims_to_reference_pack,
    extract_pdf_document,
)


def make_pdf(text: str) -> bytes:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((60, 70), text, fontsize=11)
    data = document.tobytes()
    document.close()
    return data


class TestDocumentIntake(unittest.TestCase):
    def setUp(self):
        self.it_pdf = make_pdf(
            "Baba Banda Singh Bahadur Engineering College\n"
            "Candidate Name: Rohan Kumar\n"
            "Roll No: 18BTECH123\n"
            "Degree: Bachelor of Technology\n"
            "Branch: Information Technology\n"
            "Academic Session: 2018-19\n"
            "Affiliated to: I.K. Gujral Punjab Technical University\n"
            "Date of Award: 15 July 2022\n"
        )

    def test_01_extracts_claims_with_page_and_evidence_line(self):
        result = extract_pdf_document(self.it_pdf, ocr_scanned_pages=False)
        claims = result["claims"]
        self.assertEqual(claims["candidate_name"]["value"], "Rohan Kumar")
        self.assertEqual(claims["roll_number"]["value"], "18BTECH123")
        self.assertEqual(claims["institution"]["value"], "Baba Banda Singh Bahadur Engineering College")
        self.assertEqual(claims["programme"]["value"], "Information Technology")
        self.assertEqual(claims["academic_session"]["value"], "2018–19")
        self.assertEqual(claims["university_or_affiliating_body"]["value"], "I.K. Gujral Punjab Technical University")
        self.assertEqual(claims["award_year"]["value"], "2022")
        self.assertEqual(claims["programme"]["page"], 1)
        self.assertIn("Information Technology", claims["programme"]["quote"])

    def test_02_it_upload_triggers_review_required_not_fraud_label(self):
        result = extract_pdf_document(self.it_pdf, ocr_scanned_pages=False)
        report = compare_claims_to_reference_pack(result["claims"])
        self.assertEqual(report["finding"], "REVIEW REQUIRED — COURSE CLOSURE SIGNAL")
        self.assertEqual(report["individual_award"], "NOT VERIFIED")
        self.assertIn("teach-out", report["detail"].lower())
        self.assertNotIn("fraud", report["finding"].lower())
        self.assertIn("SRC-04", report["sources"])
        self.assertIn("SRC-06", report["sources"])

    def test_03_cse_positive_control_is_context_only(self):
        claims = {
            "institution": {"value": "BBSBEC"},
            "programme": {"value": "Computer Science & Engineering"},
            "academic_session": {"value": "2018-19"},
            "university_or_affiliating_body": {"value": "IKGPTU"},
        }
        report = compare_claims_to_reference_pack(claims)
        self.assertEqual(
            report["finding"],
            "CONTEXT SUPPORTED — INDIVIDUAL AWARD UNVERIFIED",
        )
        self.assertEqual(report["individual_award"], "NOT VERIFIED")
        self.assertIn("180", report["detail"])

    def test_04_unknown_institution_is_not_treated_as_invalid(self):
        claims = {
            "institution": {"value": "Apex Institute of Technology"},
            "programme": {"value": "Artificial Intelligence & Data Science"},
            "academic_session": {"value": "2018-19"},
        }
        report = compare_claims_to_reference_pack(claims)
        self.assertEqual(report["finding"], "NO MATCH IN CURRENT REFERENCE PACK")
        self.assertIn("No conclusion", report["detail"])

    def test_05_bbsbec_without_session_requests_scope(self):
        claims = {"institution": {"value": "BBSBEC"}, "programme": {"value": "Information Technology"}}
        report = compare_claims_to_reference_pack(claims)
        self.assertIn("SESSION NOT IDENTIFIED", report["finding"])

    def test_06_pdf_fingerprint_and_page_limits(self):
        result = extract_pdf_document(self.it_pdf, ocr_scanned_pages=False)
        self.assertEqual(len(result["file_sha256"]), 64)
        self.assertEqual(result["page_count"], 1)
        self.assertEqual(result["text_pages"], 1)

    def test_07_rejects_non_pdf_input(self):
        with self.assertRaises(ValueError):
            extract_pdf_document(b"not a pdf", ocr_scanned_pages=False)

    def test_08_enforces_upload_size_limit(self):
        with self.assertRaises(ValueError):
            extract_pdf_document(b"x" * (MAX_UPLOAD_BYTES + 1), ocr_scanned_pages=False)


if __name__ == "__main__":
    unittest.main()
