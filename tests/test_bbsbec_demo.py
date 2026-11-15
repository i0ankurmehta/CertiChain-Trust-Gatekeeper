import csv
import io
import unittest

from tg_bbsbec_demo import CASE_ID, SOURCES, TIMELINE, build_case_report, build_sources_csv


class TestBBSBECDemo(unittest.TestCase):
    def test_01_it_case_requires_human_review(self):
        report = build_case_report("Information Technology")
        self.assertEqual(report["case_id"], CASE_ID)
        self.assertEqual(report["disposition"], "REVIEW REQUIRED")
        self.assertIn("closure", report["programme_detail"].lower())
        self.assertIn("teach-out", report["programme_detail"].lower())

    def test_02_cse_positive_control_has_no_programme_contradiction(self):
        report = build_case_report("Computer Science & Engineering")
        self.assertIn("CONTEXT SUPPORTED", report["disposition"])
        self.assertIn("180", report["programme_detail"])
        self.assertIn("unverified", report["programme_detail"].lower())

    def test_03_student_award_is_never_marked_verified(self):
        for programme in ("Information Technology", "Computer Science & Engineering"):
            report = build_case_report(programme)
            award = [row for row in report["claims"] if row["claim"].startswith("Candidate-specific")][0]
            self.assertEqual(award["finding"], "NOT VERIFIED")

    def test_04_sources_include_custody_and_limitations(self):
        self.assertGreaterEqual(len(SOURCES), 5)
        for source in SOURCES:
            self.assertTrue(source["id"])
            self.assertTrue(source["publisher"])
            self.assertTrue(source["url"].startswith("https://"))
            self.assertTrue(source["limitation"])
            self.assertTrue(source["custody"])

    def test_05_timeline_keeps_primary_notification_gap_visible(self):
        items = " ".join(row["state"] + " " + row["detail"] for row in TIMELINE)
        self.assertIn("Primary State notification still needed", items)
        self.assertIn("transition proviso", items.lower())

    def test_06_csv_register_is_machine_readable(self):
        rows = list(csv.DictReader(io.StringIO(build_sources_csv())))
        self.assertEqual(len(rows), len(SOURCES))
        self.assertEqual(rows[0]["id"], "SRC-01")


if __name__ == "__main__":
    unittest.main()
