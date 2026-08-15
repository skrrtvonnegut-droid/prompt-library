# Contractor Registry Builder

## Purpose

Transform an exported list of contractors, vendors, consultants, temporary staff, or other non-employees into a **lightweight, operational governance registry** that makes ownership, access, licensing, privilege, and review obligations visible.

Use this when contractor data is scattered across HR exports, identity systems, licensing reports, spreadsheets, ticketing tools, or informal records and needs to become a usable governance artifact.

## Prompt

Act as an identity governance and access management analyst.

Using the source data I provide, build a **Contractor Governance Registry** that makes each non-employee account traceable to:

- a legitimate business relationship,
- an internal sponsor,
- a defined engagement period,
- assigned access and licenses,
- privilege level,
- and a recurring review obligation.

Your goal is not just formatting. Identify governance gaps such as missing ownership, stale accounts, excessive privilege, ambiguous records, and other issues requiring follow-up.

### Analysis Instructions

1. Treat the provided source as the starting point, not necessarily complete or authoritative.
2. Normalize obvious inconsistencies only when it does not require guessing.
3. Preserve original values when uncertainty exists.
4. Do not invent:
   - internal sponsors,
   - contract dates,
   - business justification,
   - licenses,
   - privilege status,
   - account ownership,
   - or review outcomes.
5. Use `Not specified` or `Unknown` when data is missing.
6. Identify duplicates or likely duplicate contractor identities.
7. Flag accounts that appear active with expired or missing engagement dates.
8. Flag contractors without a named internal sponsor.
9. Flag privileged or elevated access for review.
10. Identify potentially unnecessary licenses or access based on available data.
11. Clearly separate:
    - source data,
    - derived/calculated values,
    - and items requiring validation.
12. If sources conflict, preserve the conflict rather than resolving it.

---

## Registry Fields

Create one row per contractor using only the essential fields below:

| Field              | Description                                                                     |
| ------------------ | ------------------------------------------------------------------------------- |
| Contractor Name    | Full name of the non-employee                                                   |
| Company / Vendor   | External organization or staffing provider                                      |
| Internal Sponsor   | Accountable internal employee (if known)                                        |
| Account / Username | System identity or login                                                        |
| Engagement Status  | Active / Expired / Ending Soon / Unknown                                        |
| Expected End Date  | Contract or access end date (if available)                                      |
| Privileged Access  | Yes / No / Unknown                                                              |
| Assigned Licenses  | Key systems or licenses (if any)                                                |
| Review Status      | Current / Due / Overdue / Not Reviewed                                          |
| Notes / Risks      | Key issues: missing sponsor, stale account, privilege concern, duplicates, etc. |

---

## Review Cadence

Default to a **semiannual review cycle** for active contractors.

- If a last review date exists, calculate the next review date and label it as **derived**.
- If no review history exists, mark as `Not Reviewed` (do not assume compliance).

---

## Risk & Governance Checks

After building the registry, identify issues in the following areas:

### Ownership

- Missing or unclear internal sponsor
- Inconsistent sponsor references

### Lifecycle

- Active accounts with expired or missing end dates
- Missing engagement timelines
- Stale or orphaned accounts

### Privilege

- Any elevated or administrative access
- Privilege without clear justification

### Licensing & Access

- Licenses that appear unnecessary or unaligned with role/status
- Access assigned to expired contractors
- Duplicate or overlapping entitlements

### Review Hygiene

- Missing or overdue access reviews
- Contractors with no review history

---

## Output Format

### 1. Contractor Governance Registry

Provide a clean table suitable for Excel, Google Sheets, or CMDB ingestion.

---

### 2. Governance Summary

Include only supported counts:

- Total contractors
- Active vs expired vs unknown status
- Contractors without sponsors
- Privileged accounts
- Overdue or missing reviews
- Key data quality issues

---

### 3. Exceptions Requiring Attention

List the most important issues first.

For each:

- **Contractor**
- **Issue**
- **Why it matters**
- **Recommended follow-up**
- **Evidence (source field)**

---

### 4. Missing Critical Information

Group missing data into:

- Ownership (sponsor gaps)
- Lifecycle (dates missing)
- Privilege (access clarity)
- Licensing (entitlement clarity)
- Review history

---

### 5. Recommended Governance Actions

Provide practical, non-destructive actions such as:

- sponsor validation
- access recertification
- license review
- account lifecycle cleanup
- privilege review
- stale account investigation
- establishing review cadence

Do **not** recommend removal or deprovisioning solely due to missing data.

---

### 6. Data Quality Check

Confirm:

- no invented values
- derived values are clearly labeled
- stale/privileged accounts are visible
- missing data remains visible (not hidden)
- conflicts are preserved
- every recommendation is traceable to observed data

---

## Source Data

Paste or attach contractor export, spreadsheet, identity report, licensing data, or other input below:

`[SOURCE DATA]`
