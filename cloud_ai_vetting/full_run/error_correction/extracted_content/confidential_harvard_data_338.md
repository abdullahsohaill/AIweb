# confidential Harvard data
**URL:** https://privsec.harvard.edu/classify-risk
**Page Title:** Classify Risk | University Information Security and Data Privacy
--------------------


## Classify Risk

Risk classification helps determine how to protect Harvard’s data and systems. It involves assessing both impact and likelihood of harm, whether from a minor incident or a major cyberattack.
Understanding how assets are classified helps everyone, from system administrators to researchers, take the right steps to protect them.
- If you're managing a system or application, use the classification to apply the correct standards .
- If you're working with confidential or sensitive information, use it to handle data appropriately .
Classifying the asset is the first step in managing risk effectively.

## University Risk Classifications

Always use the "high watermark", a system storing Level 1 (public) data but requiring Level 4 (mission critical) availability should be classified as Level 4.

### Level 1: No impact on university operations, research, reputation, or finances.

- Data: Non-sensitive information that is intentionally made available to the public and can be used, reused, or redistributed without restriction.
- Systems: Failure could impact a Non-critical (Critical 4) service.

### Level 2:  Minimal impact on university operations, research, reputation, or finances.

- Data: Non-sensitive confidential information that may be shared internally within the Harvard community, or within a school, unit or specific department.
- Systems: Failure could impact an Important (Critical 3) service.

### Level 3: Moderate impact on university operations, research, reputation, or finances.

- Data: Sensitive information that must be safeguarded as confidential and shared only with individuals with a need to know.*
- Systems: Failure could impact a Critical (Critical 2) service.
*Most university data falls into this broad classification, including most personal data.

### Level 4: Significant impact on university operations, research, reputation, or finances.

- Data: Sensitive " Restricted Personal Information ", credentials, security secrets, or contractually restricted data.
- Systems: Failure could impact a Foundational (Critical 0) or Mission Critical (Critical 1) service.

### Level 5: Severe impact on university-wide operations, research, life safety systems, reputation, or finances.

- Data: Sensitive information that must be safeguarded in accordance with federal requirements.
- Systems: Failure could impact life safety services.

### Key

" Restricted Personal Information " - Specific to privacy regulations, laws or sensitivity.
- Government IDs (e.g., Social Security, passport, driver's license)
- Personal financial details (e.g., bank or credit card numbers)
- HIPAA-protected health information
- GDPR/PIPL- extra sensitive data (e.g., biometric, health info)
- Identifiable genetic data
- Disclosure could put a subject at risk (e.g. legal, political, physical)
"Systems: Critical 0-4" - Specific to University availability needs.
- Disaster Recovery Criticality Ratings

## Privacy Considerations

### Why Privacy Matters in Risk Classification

When classifying data or systems, it’s important to consider privacy alongside security. If you’re handling any information about a person that can identify them, that’s personal information (PI) — and it requires careful handling. Many of the examples below involve PI (Level 2 - Level 5).
Some types of PI carry more risk than others. The University Privacy Principles apply to all personal data, with more attention needed when data is especially sensitive or used at a larger scale. In those situations, you need to take additional steps to protect an individual's privacy.
To learn more, see the University Privacy Principles , the Companion Guide, or contact your SPSO or the ISDP team.

## Data Examples

Choose the type below to view examples for each risk classification category.

### Level 1

- Course catalogs
- Published faculty and staff information
- University publications
- Published marketing materials
- Marketing materials
- Regulatory and legal filings
- Published annual reports
- Plans of public university spaces
- Press releases
- University-wide policies
- Released Patents
- FERPA defined Student Directory information only when there is legitimate business need 1
1 Student Directory Information as defined by FERPA may be disclosed publicly in accordance with the regulation in cases where there is a legitimate university business need. However, Harvard has chosen to limit the Student Directory to an internal university audience by default as a privacy safeguard. For students with FERPA blocks, their educational record including Student Directory information must be classified and handled as Level 3, at minimum. Seek guidance from the relevant Registrar's Office when needed.

### Level 2

- School/unit specific intranet
- Student handbooks
- Instructional materials intended for general university audience
- Non-public building plans or layouts (excluding Level 3/4 data) 2
- Information about physical plant (excluding Level 3/4 data) 2
- Non-sensitive administrative survey data
- OGC model contracts/riders
- Pre-publication findings or similar shared in university seminar, talk, colloquiums, poster sessions, or similar
- Course syllabi, recordings of presentations and lectures made available to university affiliates
- FERPA defined Student Directory information 3
2 Exclusions may include specific subsets such as toxic gas infrastructure details, substation/switch relay information, and PLC programming/configurations, as these contain sensitive passwords and device codes and should be safeguarded accordingly.
3 Student Directory Information as defined by FERPA may be disclosed publicly in accordance with the regulation in cases where there is a legitimate university business need. However, Harvard has chosen to limit the Student Directory to an internal university audience by default as a privacy safeguard. For students with FERPA blocks, their educational record including Student Directory information must be classified and handled as L3, at minimum. Seek guidance from the relevant Registrar's Office when needed.

### Level 3

- HUIDs
- Personally identifiable information (PII) not classified as Level 4
- Personnel records not containing Level 4 data 4
- Donor information not classified as Level 4
- Non-public legal work and litigation information
- Budget/financial transactions information
- Non-public financial statements
- University contracts
- Research Administration and Compliance records not otherwise classified
- Security findings or reports (e.g. SSAE16, vulnerability assessment and penetration test results)
- Most Harvard source code
- Non-security related technical specifications
- Library/museum object valuations
- Sensitive administrative survey data, such as performance reviews or course feedback, especially if free text response is permitted
- Course materials not otherwise classified
- General use technology assets not otherwise classified
- FERPA defined non-directory education record data not containing Level 4 data 5
4 Employees have the right to discuss terms and conditions of their own employment, including salary and benefits, with each other or with third parties.
5 For students with FERPA blocks, their educational record including Student Directory information must be classified and handled as Level 3, at minimum.

### Level 4

- Government issued identifiers* (e.g. Social Security Number, Passport number, driver’s license)
- Individually identifiable financial account information (e.g. bank account, credit or debit card numbers)
- Individually identifiable health or medical information 6
- Criminal Justice Information Systems (CJIS) data
- Data specified by GDPR or PIPL considered “extra sensitive” – biometric, genetic, or health information
- System credentials incl Passwords and PINs, encryption keys, etc.
- Contractual third-party data data specified as Restricted
- Trade secrets
- Security controls, security system procedures and architectures
* Classification applies to both full or partial Government IDs like SSNs. 6 Harvard is a HIPAA hybrid entity. Units that qualify as "covered functions" must comply with the HIPAA regulation and related compliance obligations.

## Level 5

- Information with federal security and compliance requirements such as NIST SP 800-171 (CUI), CMS, CMMC, FISMA, FedRAMP
- Contracts and other research administration designated as Federal Contract Information (FCI)

## Level 1

- Published research
- Deidentified or anonymized data intended for contribution to open-science data repositories
- Open licensed research products shared in accordance with NIH sharing requirements, or similar, such as software or source code
- Non-restricted, publicly available data sets (e.g., Behavioral Risk Factor Surveillance System (BRFSS); NHIS: National Health Interview Survey) when the following criteria are met: Research use will NOT involve merging any of the data sets in such a way that individuals might be identified Research use will NOT enhance the public data set with identifiable, or potentially identifiable data
- Research use will NOT involve merging any of the data sets in such a way that individuals might be identified
- Research use will NOT enhance the public data set with identifiable, or potentially identifiable data

## Level 2

- Pre-publication findings or similar shared in university seminar, talk, colloquiums, poster sessions, or similar
- Course syllabi, recordings of presentations and lectures made broadly available to university affiliates
- Self-collected de-identified data, anonymized survey data or aggregate statistics
- Self-collected, de-identified biospecimens or genomic data
- Self-collected non-sensitive survey data, qualitative data such as interviews, or intervention outcome data
- Usability data
- Non-sensitive audio or video recordings
- Non-sensitive observational notes
- Other self-collected research data that is identifiable but is not considered sensitive by IRB

### Level 3

- Research administration and compliance records not designated CUI or FCI, including research protocols and IRB records
- Contractual agreements (DUAs, NDAs, Sponsored Research Agreements, etc.) not classified as FCI
- Active and unpublished sensitive research, including data, metadata, methods, notes, drafts, etc., as well as research products or technology such as software, source code, devices, etc.
- Sensitive self-collected data not classified as L4
- All contractual third-party data 2 not specified as Restricted or Federally Restricted data
Personally identifiable information (PII) not classified as L4, including:
- Student data subject to FERPA
- Employment records (incl. performance)
- Sensitive self-reported health history (U.S.)
- Personal or family financial circumstances
- U.S. criminal conduct details (incl. prison data), which would not lead to reputational harm or criminal punishment
GDPR or PIPL data not reaching level of “extra sensitive” including racial or ethnic origin, political opinions, religious, or philosophical beliefs, trade union membership, sex life or sexual orientation
2 All third-party research data is subject to the OVPR DUA Policy. Data exchanged subject to contractual terms must be classified, handled and shared in accordance with the contract terms throughout the data lifecycle.

### Level 4

Data specified by MA CMR 17.00, HIPAA, other relevant federal or state laws/regs, including:
- Government issued identifiers* (e.g. Social Security Number, Passport number, driver’s license)
- Individually identifiable financial account information (e.g., bank account, credit or debit card numbers)
- Medical records/clinical data, whether directly regulated by HIPAA (US) or not, including “HIPAA limited data sets”, as they contain HIPAA Protected Health Information (PHI)
- Self-collected information that, if disclosed, could place the subject at risk of significant criminal punishment, or violent reprisals 3
- Individually identifiable genetic information that is not DSL5
- Trade secrets
- All contractual third-party data 4 specified as Restricted
Data specified by GDPR or PIPL considered “extra sensitive” – biometric, genetic, or health information
* Classification applies to both full or partial Government IDs like SSNs.
3 Investigators must consider the criminal laws applicable to subjects when developing their protocols and identifying necessary study data elements. Collect the minimum necessary, carefully safeguard all data that could place a subject at risk of prosecution or punishment if disclosed. Information about conduct that is punishable by civil or even criminal fines, but not imprisonment, may not merit L4 classification. Seek supplemental guidance from the IRB as necessary.
4 All third-party research data is subject to the OVPR DUA Policy. Data exchanged subject to contractual terms must be classified, handled and shared in accordance with the contract terms throughout the data lifecycle.

### Level 5

- Information with federal security and compliance requirements such as NIST SP 800-171 (CUI), CMS, CMMC, FISMA, FedRAMP
- Contractual data with Federal data classifications such as CUI, or with CMS, DFARS 252.204-7012, NIST SP 800-171, CMMC, FISMA, or FEDRAMP requirements, or similar
- Contracts and other research administration designated as Federal Contract Information (FCI)
Seek guidance from the Information Security and Data Privacy (ISDP) team.

--------------------