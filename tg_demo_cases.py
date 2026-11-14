"""Clearly fictional demonstration cases for the Trust Gatekeeper UI."""
from copy import deepcopy

DEMO_CASES = {
    "Later-session programme approval": {
        "case_id": "TG-DEMO-002",
        "description": "A programme is approved for 2022–2023, while the candidate claims admission in 2021–2022.",
        "processing_authority_documented": True, "input_safe": True,
        "input_mode": "paired", "entity_resolution_status": "resolved",
        "field_comparisons": [
            {"field": "programme", "submitted_value": "BBA", "extracted_value": "BBA", "ocr_confidence": 0.98},
            {"field": "admission_session", "submitted_value": "2021-2022", "extracted_value": "2021-2022", "ocr_confidence": 0.99},
        ],
        "required_claims": [
            {"claim_id": "CL-PROGRAMME-01", "scope": "programme_status", "subject_id": "SYN-RIVERGATE-BBA-ONLINE", "predicate": "approved_for_admission", "expected_value": "approved", "relevant_session": "2021-2022", "required_source_classes": ["B"]},
            {"claim_id": "CL-AWARD-01", "scope": "individual_award", "subject_id": "SYN-CANDIDATE-002", "predicate": "award_confirmed", "expected_value": "confirmed", "relevant_date": "2024-08-20", "required_source_classes": ["A"]},
        ],
        "evidence": [
            {"evidence_id": "SYN2-E01", "source_id": "SYN2-SRC-ORDER", "subject_id": "SYN-RIVERGATE-BBA-ONLINE", "predicate": "approved_for_admission", "claim_scope": "programme_status", "value": "approved", "source_class": "B", "review_state": "reviewed", "valid_sessions": ["2022-2023"], "excluded_sessions": ["2021-2022"], "period_scope_complete": True},
            {"evidence_id": "SYN2-E02", "source_id": "SYN2-SRC-REGISTER", "parent_source_id": "SYN2-SRC-ORDER", "subject_id": "SYN-RIVERGATE-BBA-ONLINE", "predicate": "approved_for_admission", "claim_scope": "programme_status", "value": "approved", "source_class": "B", "review_state": "reviewed", "valid_sessions": ["2022-2023"], "excluded_sessions": ["2021-2022"], "period_scope_complete": True},
            {"evidence_id": "SYN2-E03", "source_id": "SYN2-SRC-DIRECTORY-A", "parent_source_id": "SYN2-SRC-REGISTER", "subject_id": "SYN-RIVERGATE-BBA-ONLINE", "predicate": "approved_for_admission", "claim_scope": "programme_status", "value": "approved", "source_class": "D", "review_state": "reviewed", "valid_sessions": ["2022-2023"], "excluded_sessions": ["2021-2022"], "period_scope_complete": True},
            {"evidence_id": "SYN2-E04", "source_id": "SYN2-SRC-DIRECTORY-B", "parent_source_id": "SYN2-SRC-DIRECTORY-A", "subject_id": "SYN-RIVERGATE-BBA-ONLINE", "predicate": "approved_for_admission", "claim_scope": "programme_status", "value": "approved", "source_class": "D", "review_state": "reviewed", "valid_sessions": ["2022-2023"], "excluded_sessions": ["2021-2022"], "period_scope_complete": True},
        ],
    },
    "Affiliation transition ambiguity": {
        "case_id": "TG-DEMO-001",
        "description": "A college affiliation changes, but the continuing cohort's awarding authority is not established.",
        "processing_authority_documented": True, "input_safe": True,
        "input_mode": "paired", "entity_resolution_status": "ambiguous",
        "field_comparisons": [{"field": "awarding_institution", "submitted_value": "Aster State University", "extracted_value": "Aster State University", "ocr_confidence": 0.97}],
        "required_claims": [
            {"claim_id": "CL-COHORT-01", "scope": "cohort_awarding_authority", "subject_id": "SYN-NORTHBRIDGE-COHORT-2020", "predicate": "awarding_authority", "expected_value": "Aster State University", "relevant_date": "2023-08-15", "required_source_classes": ["B", "C"]},
            {"claim_id": "CL-AWARD-02", "scope": "individual_award", "subject_id": "SYN-CANDIDATE-001", "predicate": "award_confirmed", "expected_value": "confirmed", "relevant_date": "2023-08-15", "required_source_classes": ["A"]},
        ],
        "evidence": [
            {"evidence_id": "SYN-E01", "source_id": "SYN-SRC-ASTER-AFFILIATION", "subject_id": "SYN-NORTHBRIDGE", "predicate": "affiliated_with", "claim_scope": "college_affiliation", "value": "Aster State University", "source_class": "C", "review_state": "reviewed", "valid_sessions": ["2020-2021", "2021-2022"]},
            {"evidence_id": "SYN-E02", "source_id": "SYN-SRC-MERIDIAN-AFFILIATION", "subject_id": "SYN-NORTHBRIDGE", "predicate": "affiliated_with", "claim_scope": "college_affiliation", "value": "Meridian University", "source_class": "C", "review_state": "reviewed", "valid_sessions": ["2022-2023"]},
        ],
    },
    "Context supported, award unverified": {
        "case_id": "TG-DEMO-003",
        "description": "Institution/programme context is supported for the relevant session, but no award-specific issuer evidence is supplied.",
        "processing_authority_documented": True, "input_safe": True,
        "input_mode": "structured", "entity_resolution_status": "resolved", "field_comparisons": [],
        "required_claims": [
            {"claim_id": "CL-AFFILIATION-03", "scope": "college_affiliation", "subject_id": "SYN-COLLEGE-003", "predicate": "affiliated_with", "expected_value": "SYN-UNIVERSITY-003", "relevant_session": "2021-2022", "required_source_classes": ["C"]},
            {"claim_id": "CL-PROGRAMME-03", "scope": "programme_status", "subject_id": "SYN-PROGRAMME-003", "predicate": "approved_for_admission", "expected_value": "approved", "relevant_session": "2021-2022", "required_source_classes": ["B"]},
            {"claim_id": "CL-AWARD-03", "scope": "individual_award", "subject_id": "SYN-CANDIDATE-003", "predicate": "award_confirmed", "expected_value": "confirmed", "relevant_date": "2024-06-30", "required_source_classes": ["A"]},
        ],
        "evidence": [
            {"evidence_id": "SYN3-E01", "source_id": "SYN3-SRC-AFFILIATION", "subject_id": "SYN-COLLEGE-003", "predicate": "affiliated_with", "claim_scope": "college_affiliation", "value": "SYN-UNIVERSITY-003", "source_class": "C", "review_state": "reviewed", "valid_sessions": ["2021-2022"]},
            {"evidence_id": "SYN3-E02", "source_id": "SYN3-SRC-PROGRAMME", "subject_id": "SYN-PROGRAMME-003", "predicate": "approved_for_admission", "claim_scope": "programme_status", "value": "approved", "source_class": "B", "review_state": "reviewed", "valid_sessions": ["2021-2022"]},
        ],
    },
}

DEMO_CASES["Historical programme approval — Rohan"] = {
    "case_id": "TG-DEMO-004",
    "description": "A fictional 2018 BTech AI and Data Science award claim conflicts with an official programme-approval record whose first applicable approval is in 2020; the individual award remains unverified.",
    "processing_authority_documented": True,
    "input_safe": True,
    "input_mode": "scan_claims_with_historical_sources",
    "entity_resolution_status": "resolved",
    "field_comparisons": [
        {"field": "candidate_name", "submitted_value": "Rohan (fictional)", "extracted_value": "Rohan (fictional)", "ocr_confidence": 0.98},
        {"field": "degree_title", "submitted_value": "BTech Artificial Intelligence and Data Science", "extracted_value": "BTech Artificial Intelligence and Data Science", "ocr_confidence": 0.96},
        {"field": "award_year", "submitted_value": "2018", "extracted_value": "2018", "ocr_confidence": 0.99},
    ],
    "required_claims": [
        {
            "claim_id": "CL-ROHAN-INSTITUTE-01", "scope": "institution_existence",
            "subject_id": "SYN4-APEX-INSTITUTE", "predicate": "existed",
            "expected_value": "yes", "relevant_date": "2018-06-01",
            "required_source_classes": ["A"],
        },
        {
            "claim_id": "CL-ROHAN-UNIVERSITY-01", "scope": "institution_existence",
            "subject_id": "SYN4-STATE-TECHNICAL-UNIVERSITY", "predicate": "existed",
            "expected_value": "yes", "relevant_date": "2018-06-01",
            "required_source_classes": ["A"],
        },
        {
            "claim_id": "CL-ROHAN-AFFILIATION-01", "scope": "college_affiliation",
            "subject_id": "SYN4-APEX-INSTITUTE", "predicate": "affiliated_with",
            "expected_value": "SYN4-STATE-TECHNICAL-UNIVERSITY",
            "relevant_session": "2017-2018", "required_source_classes": ["C"],
        },
        {
            "claim_id": "CL-ROHAN-PROGRAMME-01", "scope": "programme_status",
            "subject_id": "SYN4-BTECH-AI-DS", "predicate": "approved_for_admission",
            "expected_value": "approved", "relevant_date": "2018-06-01",
            "required_source_classes": ["B"],
            "recommended_action": "Reviewer: inspect SYN4-E04's effective date, programme identity, mode and location. Confirm that the official record explicitly excludes the 2014–2018 cohort and is not merely the first record located.",
        },
        {
            "claim_id": "CL-ROHAN-AWARD-01", "scope": "individual_award",
            "subject_id": "SYN4-ROHAN-ROLL-001", "predicate": "award_confirmed",
            "expected_value": "confirmed", "relevant_date": "2018-06-30",
            "required_source_classes": ["A"],
            "recommended_action": "Registrar confirmation only: ask whether fictional roll number SYN4-ROHAN-ROLL-001 appears in the 2018 award register and request the exact degree title / branch recorded (including whether it was BTech Computer Science). Do not ask the registrar to decide programme approval.",
        },
    ],
    "evidence": [
        {
            "evidence_id": "SYN4-E01", "source_id": "SYN4-SRC-INSTITUTE-REGISTER",
            "subject_id": "SYN4-APEX-INSTITUTE", "predicate": "existed",
            "claim_scope": "institution_existence", "value": "yes",
            "source_class": "A", "review_state": "reviewed",
            "valid_from": "2000-01-01", "valid_to": "2030-12-31",
        },
        {
            "evidence_id": "SYN4-E02", "source_id": "SYN4-SRC-UNIVERSITY-REGISTER",
            "subject_id": "SYN4-STATE-TECHNICAL-UNIVERSITY", "predicate": "existed",
            "claim_scope": "institution_existence", "value": "yes",
            "source_class": "A", "review_state": "reviewed",
            "valid_from": "1990-01-01", "valid_to": "2030-12-31",
        },
        {
            "evidence_id": "SYN4-E03", "source_id": "SYN4-SRC-AFFILIATION-ORDER",
            "subject_id": "SYN4-APEX-INSTITUTE", "predicate": "affiliated_with",
            "claim_scope": "college_affiliation",
            "value": "SYN4-STATE-TECHNICAL-UNIVERSITY",
            "source_class": "C", "review_state": "reviewed",
            "valid_sessions": ["2014-2015", "2015-2016", "2016-2017", "2017-2018"],
        },
        {
            "evidence_id": "SYN4-E04", "source_id": "SYN4-SRC-PROGRAMME-APPROVAL-ORDER",
            "subject_id": "SYN4-BTECH-AI-DS", "predicate": "approved_for_admission",
            "claim_scope": "programme_status", "value": "approved",
            "source_class": "B", "review_state": "reviewed",
            "valid_from": "2020-01-01", "valid_to": None, "open_ended": True,
            "period_scope_complete": True,
        },
    ],
}



def get_demo_case(label: str) -> dict:
    if label not in DEMO_CASES:
        raise KeyError(f"Unknown demonstration case: {label}")
    return deepcopy(DEMO_CASES[label])
