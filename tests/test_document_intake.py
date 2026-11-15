import unittest

from tg_document_intake import (
    PUBLIC_SAMPLE_TEXT,
    analyse_public_sample,
    build_programme_review,
    parse_aicte_eoa_text,
)


class TestAictEoaDocumentIntake(unittest.TestCase):
    def setUp(self):
        self.parsed = parse_aicte_eoa_text(PUBLIC_SAMPLE_TEXT)

    def test_01_recognises_public_aicte_eoa(self):
        self.assertTrue(self.parsed["recognised"])
        self.assertEqual(self.parsed["document_type"], "AICTE Extension of Approval (EoA)")

    def test_02_extracts_institution_and_identifiers(self):
        self.assertIn("BABA BANDA SINGH", self.parsed["institution"])
        self.assertEqual(self.parsed["permanent_institute_id"], "1-14182101")
        self.assertEqual(self.parsed["application_id"], "1-3517507353")
        self.assertEqual(self.parsed["academic_session"], "2018-19")
        self.assertEqual(self.parsed["approval_date"], "10-Apr-2018")

    def test_03_extracts_affiliating_body(self):
        self.assertTrue(
            any("I.K Gujral Punjab Technical University" in body
                for body in self.parsed["affiliating_bodies"])
        )

    def test_04_extracts_cse_approved_intake(self):
        rows = self.parsed["approved_courses"]
        cse = [row for row in rows if "COMPUTER SCIENCE" in row["course"]]
        self.assertEqual(len(cse), 1)
        self.assertEqual(cse[0]["approved_intake"], 180)

    def test_05_extracts_it_course_closure_signal(self):
        rows = self.parsed["closure_courses"]
        it = [row for row in rows if row["course"] == "INFORMATION TECHNOLOGY"]
        self.assertEqual(len(it), 1)
        self.assertEqual(it[0]["closure_status"], "Approved")

    def test_06_closure_produces_scoped_registrar_question(self):
        review = build_programme_review(self.parsed, "Information Technology")
        self.assertIn("REVIEW REQUIRED", review["status"])
        self.assertIn("teach-out", review["registrar_question"].lower())
        self.assertIn("individual", review["finding"].lower())

    def test_07_positive_control_reports_listed_not_award_verified(self):
        review = build_programme_review(self.parsed, "Computer Science & Engineering")
        self.assertIn("PROGRAMME LISTED", review["status"])
        self.assertIn("180", review["finding"])
        self.assertIn("does not verify a student's admission", review["finding"])

    def test_08_missing_course_is_not_treated_as_invalid(self):
        review = build_programme_review(self.parsed, "Civil Engineering")
        self.assertEqual(review["status"], "NOT FOUND IN THIS EoA")
        self.assertIn("not proof", review["finding"].lower())

    def test_09_rejects_unrelated_document(self):
        parsed = parse_aicte_eoa_text("A university degree certificate for a student")
        self.assertFalse(parsed["recognised"])
        review = build_programme_review(parsed, "Information Technology")
        self.assertEqual(review["status"], "UNSUPPORTED DOCUMENT")

    def test_10_sample_analysis_has_hash_and_source_method(self):
        result = analyse_public_sample()
        self.assertEqual(result["extraction_method"], "public-source text excerpt (not a PDF upload)")
        self.assertEqual(len(result["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
