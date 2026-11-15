# 16 — India Historical Source Feasibility Assessment

**Document ID:** TG-RESEARCH-016  
**Version:** 0.1  
**Date:** 15 November 2026  
**Scope:** Indian BGV education-verification cases; historical institution, affiliation, programme/mode and study-location claims  
**Evidence basis:** Public-source desk review. No live API integration, bulk source capture, legal opinion or institution-specific verification was performed.  
**Status:** Initial feasibility assessment — source families identified; coverage and reliability remain unvalidated.

## 1. Executive finding

There is enough publicly discoverable official material to justify a small source-feasibility pilot. There is **not** enough evidence yet to assume that India has one complete, consistent, machine-readable historical registry from which Trust Gatekeeper can resolve every institution, college, programme, campus and academic session.

The material is fragmented across different authorities and publishers:

- UGC provides university and regulatory information, archived lists and year-wise recognition information for ODL/online programmes.
- UGC-DEB explicitly directs learners to check the HEI and programme recognition for the relevant session; its public material contains year-wise ODL/online programme entries.
- AICTE publishes session-specific approval-process material. Its 2017–18 handbook describes annual Extension of Approval requirements for technical institutions and possible programme/institution approval actions.
- Affiliating universities may publish their own session-wise affiliated-college lists. A reviewed Punjabi University page exposes lists for 2019–20, 2020–21 and 2021–22.
- Gazette and statute repositories can supply foundational legal instruments and notifications, but the relevant state, date, section, authority and legal effect must be interpreted.
- AISHE is useful for institution discovery and sector context, but the Ministry's own report says inclusion in AISHE does not confer recognition.

**Research conclusion:** the source landscape is promising but fragmented. The likely research problem is not simply fetching web pages; it is determining whether a particular source is competent to establish a particular claim, for a particular entity, programme, mode, location and historical period—and preserving exactly what the source does and does not prove.

## 2. Claim-to-source feasibility matrix

| Claim family | Candidate official source family | What the source may establish | Important limitation | Initial feasibility |
|---|---|---|---|---|
| University identity / establishment / statutory status | UGC university lists and annual reports; relevant Central/State Act; Gazette notification | A dated listing, establishment/notification information or statutory basis | A current directory is not a complete historical snapshot. A UGC listing/status field must not be treated as proof of every course, college or individual award | **Moderate** |
| College-to-university affiliation | Affiliating university's College Development Council (CDC), affiliation orders, session-wise college lists and university statutes | Whether a named college appears in a university's published list or order for a stated period | Publication and historical coverage vary by university. A list may not establish the exact programme, campus, cohort or dates unless it says so | **Moderate, fragmented** |
| Programme / technical-course approval | Relevant statutory regulator's dated approval order, annual approval record or programme-specific notification; AICTE material where applicable | Whether a specified programme/institution was approved within a stated scope and period | The applicable regulator and approval requirement must first be identified. An AICTE handbook is a process/rule source, not by itself the approval record for a particular institute and course | **Moderate, conditional** |
| ODL / online programme recognition | UGC-DEB year-wise HEI and programme recognition / entitlement lists and applicable regulations | Recognition/entitlement for a listed HEI, programme and academic session, where the record is explicit | This is specific to ODL/online modes; it must not be applied as a test for ordinary on-campus programmes. Verify the exact session and programme, including prohibited programmes and territorial/franchise conditions | **Relatively strong for listed ODL/online entries** |
| Study-centre / off-campus / territorial permission | Applicable UGC rules, regulator orders, university orders, state notifications and source documents specifying location | A rule or permission relevant to a particular institution type, mode, centre and territory | Rules differ by institution category and mode. A general rule cannot be converted into a case-specific breach without identifying the entity type, applicable date and competent authority | **Moderate to difficult** |
| Individual award / roll-number / graduation confirmation | Issuing university or authorised official award repository/process; registrar response | Whether the individual award/record is confirmed by the issuing authority or authorised repository | Contextual recognition and affiliation records do not establish that a particular person graduated or that a specific roll number received the award | **Not generally resolvable from public context records** |
| Source lineage / copied evidence | Original Gazette/order plus derivative university pages, directories or third-party reproductions | Whether multiple documents/pages refer to or reproduce one underlying source | Dependency often requires document-level inspection; different URLs are not automatically independent evidence | **Technically feasible; manual adjudication needed** |

“Initial feasibility” is a qualitative desk-research judgement, not a measured coverage score or service-level guarantee.

## 3. Reviewed source families and observations

### 3.1 UGC — university directory, regulations and historical lists

Reviewed public material:

- [UGC university details](https://www.ugc.gov.in/universitydetails/university?type=0wBmFB1Rb4JGVzq9UP%2FiOg%3D%3D) — searchable university records with categories, state and status information.
- [UGC Regulations for University](https://www.ugc.gov.in/regulations/UGC_Regulations_university) — the reviewed page lists regulations and notifications across multiple years, including the 2003 Private Universities Regulations and later regulatory instruments.
- [UGC consolidated State University list as at 31 March 2015](https://www.ugc.gov.in/oldpdf/State%20University/Consolidated%20List%20of%20State%20Universities%20as%20on%2031.03.2015.pdf).
- [UGC Annual Report 2019–20](https://www.ugc.gov.in/pdfnews/1120661_UGC-ANNUAL-REPORT-ENGLISH-2019-20.pdf), which includes year-bounded lists of institutions included in the UGC list during that reporting period.

**Useful for:** entity discovery, dated list snapshots, establishment/notification clues, applicable UGC regulatory text and identification of relevant statutory instruments.

**Not sufficient for:** proving a college's affiliation, a particular professional programme's approval, a study centre's permission or an individual's award. Current directory information must not be projected backwards as if it were the exact status in an earlier academic year.

### 3.2 UGC-DEB — year-wise ODL and online recognition

Reviewed public material:

- [UGC-DEB FAQ](https://deb.ugc.ac.in/FAQ) states that year-wise recognition status for HEIs and programme names is in the public domain.
- [UGC-DEB HEI programme list](https://deb.ugc.ac.in/Home/HEI_Prog_List) exposes entries containing an academic year/session, mode, HEI, programme name and level.
- [UGC-DEB Student FAQ](https://deb.ugc.ac.in/StudentDEBId/FAQ) tells learners to check the HEI's recognition for the session of admission, programme details, prohibited programmes, franchising arrangements and territorial-jurisdiction conditions.
- [UGC-DEB instructions for eligible HEIs](https://deb.ugc.ac.in/Instruction) refers to the 2020 ODL/Online Regulations and subsequent amendments.

**Useful for:** a well-scoped ODL/online check where the relevant HEI, programme, mode and admission session are represented in the official list.

**Limitations:** this is not a general programme registry for all regular/on-campus degrees. The list page's accessibility, historical completeness, stable export/API availability and version/archive behaviour still need testing. A later year's listing must not be used to infer recognition for an earlier session.

### 3.3 AICTE — dated technical-education approval material

Reviewed material:

- [AICTE Approval Process Handbook 2017–18](https://aicte-qa.aicte-india.org/sites/default/files/Final-Approval-Process-Handbook-2017_18.pdf).
- The handbook states that institutions offering technical programmes at the covered levels submit annual applications for Extension of Approval. It also describes possible actions including no-admission orders and withdrawal of approval for a programme or institution.
- The handbook is a procedural/rule document. Its presence does not itself prove that a named institution or programme did or did not receive approval in a given session.

**Useful for:** identifying the regulator's historical process/rules and the need to examine session-specific approval records rather than treating one current institution page as enough.

**Limitations:** the exact approval/Extension of Approval record for the institution, programme, campus and year is still required. Applicability must be established before any missing AICTE record is treated as meaningful. The reviewed PDF is hosted on an AICTE QA subdomain; production URL stability and authoritative record access should be confirmed before operational use.

### 3.4 Affiliating universities — session-wise college lists

Reviewed example:

- [Punjabi University — Colleges / College Development Council](https://www.punjabiuniversity.ac.in/pages/Page.aspx?dsenc=Colleges) links to lists of affiliated colleges for 2019–20, 2020–21 and 2021–22, alongside college-development and inspection material.

**Useful for:** demonstrating that an affiliating university may publish historical session-specific college lists and associated administrative documents.

**Limitations:** this is one university example, not evidence of uniform coverage across India. A list may establish that a college is listed for a session, but may not establish programme-specific affiliation, campus, approved intake, exact effective dates or the candidate's cohort. Other universities may publish records differently or may not expose old lists online.

### 3.5 Gazette and statute repositories

Reviewed material:

- [eGazette of India](https://egazette.gov.in/) provides Gazette search and links to Government Gazettes, State Gazettes and recent extraordinary notifications.
- [Central Secretariat Library — Gazette of India](https://csl.nic.in/page/innerpage/gazette-of-india.php) says the Gazette is the Government's official publication for statutory orders and notifications and describes digitised historic Gazette holdings.
- [India Code](https://www.indiacode.nic.in/indiacode/home.jsp) provides searchable Central Acts and subordinate legislation, notifications, orders, ordinances, statutes and circulars.

**Useful for:** primary legal instruments such as university-establishment Acts, amendments, statutory notifications and regulator orders.

**Limitations:** retrieval and interpretation are not trivial. State legislation and state gazettes may require separate search paths. An Act establishes legal powers or structure; it does not, by itself, prove that a particular college/programme/campus complied with all later conditions. Effective dates, amendments, commencement notifications and retrospective provisions must be checked.

### 3.6 AISHE — discovery and context, not recognition evidence

Reviewed material:

- [AISHE dashboard](https://dashboard.aishe.gov.in/) describes the Ministry of Education's Higher Education Institution directory.
- [AISHE 2021–22 report](https://www.education.gov.in/sites/upload_files/mhrd/files/statistics-new/AISHE%20Book_2021-22_4.pdf) says institutions upload data through the survey and places responsibility for accuracy on institutional nodal officers. It expressly cautions that inclusion in an AISHE list/publication does not confer recognition.

**Useful for:** finding institution names, categories, AISHE identifiers and contextual sector information; creating leads for further source research.

**Not sufficient for:** legal recognition, programme approval, affiliation, territorial permission or award authenticity.

## 4. Critical interpretation safeguards

The source inventory reinforces several non-negotiable distinctions:

1. **Entity existence is not programme approval.** A university or college can exist while a specific programme, mode, campus or cohort claim remains unresolved.
2. **Current status is not historical status.** A current directory or current website cannot establish the position in 2014, 2018 or another earlier session unless the source expressly covers that period.
3. **A regulator's remit matters.** Do not ask AICTE to establish a fact outside its applicable remit, or use UGC-DEB ODL/online recognition as a test for a regular/on-campus programme.
4. **A listed college is not automatically proof of every course.** The source must state the relevant relationship and scope.
5. **A rule is not a case fact.** A statutory restriction can indicate what permission was required; it does not prove that a specific institution breached it.
6. **No public result is not proof of invalidity.** It may mean the source is unavailable, undigitised, unindexed, differently named, outside the searched period or held by another competent authority.
7. **Context is not the individual award.** Only appropriate issuer/authorised award evidence can resolve the roll-number or individual graduation claim.
8. **Multiple pages may be one source.** Track original notices and derivative copies; do not count copied pages as independent confirmations.

The UGC public notice concerning private universities is especially important to scope carefully: it discusses affiliation and off-campus restrictions for **private universities**, not every institution category. Rules and amendments in force at the relevant date must be examined before applying it to a case.

## 5. Implications for the Trust Gatekeeper evidence model

Each assertion in a future source register should preserve, where available:

- **source_id** and exact URI or non-web archive reference;
- publisher and issuing authority;
- document title, type, reference/notification number;
- publication/issue date;
- effective-from and effective-to dates, without invented dates;
- academic session and date precision exactly as published;
- entity identifiers and original names as stated;
- claim scope and competent authority;
- programme, qualification level, mode, campus and location where the source specifies them;
- relevant page/paragraph/table/row and a short supporting excerpt;
- retrieval timestamp and capture method;
- captured-byte hash and retained evidence artefact, where lawful;
- source lineage (independent, derived, suspected dependency, unknown);
- reviewer, review state, interpretation note and limitations.

Do not collapse publication date, effective date and retrieval date into one timestamp. Preserve the source as observed, including corrections or later versions. A later correction should create a new evidence version rather than silently overwriting the older capture.

## 6. What was not established in this review

This assessment does **not** establish:

- that all historical UGC, AICTE, state-regulator or university records are digitised;
- that any one source can be fetched programmatically or in bulk on stable terms;
- that a common official API exists across the source families;
- that the reviewed sites have complete records for every year, institution or programme;
- that an absence in a search result means a historical approval or affiliation did not exist;
- that every technical programme is subject to AICTE approval in the same way;
- that private-university off-campus restrictions can be applied without checking the institution category and law in force at the time;
- that Trust Gatekeeper can yet deliver authentic government citations or real-case determinations.

No real institution or candidate case was assessed.

## 7. Recommended feasibility pilot

Do not start by building a national crawler or a live graph database. Run a small, manually curated source pilot first.

### Pilot scope

Use **one state and a small number of fictional test entities**. Punjab is a practical first candidate because a session-wise affiliating-university list was located for Punjabi University, but this is a suggested pilot boundary—not a decision that Punjab represents India.

Select three distinct claim families:

1. **University / entity timeline:** identify the legal instrument and dated UGC listing needed to resolve the university's identity and existence.
2. **College affiliation timeline:** locate the actual session-specific affiliation list/order and determine exactly which college/programme/location it covers.
3. **Programme/mode approval:** identify the competent regulator for the fictional programme and retrieve the correct session-specific approval or recognition source; do not assume AICTE or UGC-DEB applies without a scope check.

Add a fourth test for an ODL/online programme using the UGC-DEB year-wise list.

### Pilot deliverables

- 10–15 manually selected official source documents/pages.
- A source inventory with exact URL, publisher, document ID, publication date, effective period, claim scope and retrieval date.
- At least two examples of sources that appear independent but derive from one original notice, if found.
- At least one explicit historical approval/affiliation record and one incomplete/undated record.
- A record of access failures, broken links, unavailable years, PDF/image-only content and manual interpretation effort.
- An analyst note showing which claims can be resolved and which still require direct registrar/regulator confirmation.

Do not create a synthetic “government citation” for missing evidence. Keep fictional fixtures visibly synthetic and source URLs empty unless they point to real, independently checked public material.

### Pass / revise / stop criteria

**Pass to a larger benchmark** only if the pilot can repeatedly retrieve and correctly scope authoritative records for the target claim families, retain their provenance, and distinguish explicit contradiction from missing coverage.

**Revise the scope** if only one claim family has reliable historical coverage, or if the main bottleneck is issuer response rather than source discovery.

**Stop or narrow the graph ambition** if the needed historical evidence is usually unavailable, cannot be interpreted consistently, or is already resolved by the target BGV provider's existing process.

## 8. Next actions

1. Select one pilot state and one institution/affiliation type.
2. Create a manual source register before writing an automated connector.
3. Ask a BGV practitioner or university-domain reviewer to validate the authority/claim mapping for each source.
4. Record the cases where a direct registrar query remains unavoidable.
5. Only then decide whether graph ingestion, archival capture or additional rules are justified.

**Current decision:** proceed with a small manual source-feasibility pilot. Do not modify the Streamlit application or add live ingestion yet.

## 9. References reviewed

1. UGC university details: https://www.ugc.gov.in/universitydetails/university?type=0wBmFB1Rb4JGVzq9UP%2FiOg%3D%3D
2. UGC regulations for university: https://www.ugc.gov.in/regulations/UGC_Regulations_university
3. UGC consolidated State University list (as at 31.03.2015): https://www.ugc.gov.in/oldpdf/State%20University/Consolidated%20List%20of%20State%20Universities%20as%20on%2031.03.2015.pdf
4. UGC Annual Report 2019–20: https://www.ugc.gov.in/pdfnews/1120661_UGC-ANNUAL-REPORT-ENGLISH-2019-20.pdf
5. UGC-DEB FAQ: https://deb.ugc.ac.in/FAQ
6. UGC-DEB HEI programme list: https://deb.ugc.ac.in/Home/HEI_Prog_List
7. UGC-DEB Student FAQ: https://deb.ugc.ac.in/StudentDEBId/FAQ
8. UGC-DEB Instructions: https://deb.ugc.ac.in/Instruction
9. AICTE Approval Process Handbook 2017–18: https://aicte-qa.aicte-india.org/sites/default/files/Final-Approval-Process-Handbook-2017_18.pdf
10. Punjabi University, Colleges / College Development Council: https://www.punjabiuniversity.ac.in/pages/Page.aspx?dsenc=Colleges
11. eGazette of India: https://egazette.gov.in/
12. Central Secretariat Library, Gazette of India: https://csl.nic.in/page/innerpage/gazette-of-india.php
13. India Code: https://www.indiacode.nic.in/indiacode/home.jsp
14. AISHE dashboard: https://dashboard.aishe.gov.in/
15. AISHE 2021–22 report: https://www.education.gov.in/sites/upload_files/mhrd/files/statistics-new/AISHE%20Book_2021-22_4.pdf

**Accessed:** 15 November 2026.
