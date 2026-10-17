# MTL-AI-049 — SOC Incident Investigation Copilot

**Mettelo Project Studio**  
**Track:** AI Engineering / Security Operations  
**Engagement:** Simulated SOC investigation product  
**Team:** 3–5 people  
**Delivery window:** 8 weeks  
**Core completion cost:** £0 incremental software/service spend using existing equipment

## Business problem

Security operations teams often receive fragmented alerts and event records that must be manually correlated into a defensible incident narrative. Alert severity alone does not establish chronology, common entities, likely ATT&CK behaviours, evidence gaps or the next investigation step.

The organisation needs a local copilot that helps an analyst reconstruct an incident from frozen telemetry while preserving a strict boundary between **observed evidence, supported correlation and analyst hypothesis**.

## Commissioned decision

> Can a local AI-assisted investigation workflow improve incident reconstruction and handover quality without inventing compromise, overstating ATT&CK mappings or taking autonomous response action?

## What the team will build

Build a working local product that:

1. ingests frozen security-event scenarios and validates timestamp/schema quality;
2. normalises events into a common evidence model;
3. reconstructs event chronology;
4. correlates related hosts, users, processes and alerts using explicit rules;
5. maps only evidence-supported behaviour to a frozen MITRE ATT&CK version;
6. marks unsupported mappings and unknowns explicitly;
7. runs a local open-weight model for bounded investigation summaries and next-step suggestions;
8. validates every citation, ATT&CK reference and critical claim before display;
9. lets an analyst accept, reject or edit proposed findings;
10. exports a reviewed incident timeline and shift-handover pack;
11. preserves model outputs, reviewer decisions and uncertainty;
12. evaluates the deterministic baseline and AI-assisted workflow on locked scenarios.

This project does not execute malware, monitor live systems, collect credentials, patch assets or automate containment.

## Practical use case

A SOC analyst opens a case containing authentication, process and network events. The product orders the events, identifies shared entities, proposes evidence-supported ATT&CK techniques, lists unresolved questions and drafts a shift-handover note. The analyst follows every evidence link, rejects unsupported conclusions, edits the narrative and approves the final handover.

## Approved resources

Core knowledge:
**MITRE Enterprise ATT&CK 17.1 STIX 2.1**  
https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

Core event data:
a frozen repository-authored safe scenario pack for deterministic assessment. Teams may additionally validate on selected pre-recorded public security-event scenarios, but no live attack execution is required.

## Required workflow

```text
Frozen event bundle
      ↓
Schema / time validation
      ↓
Normalised evidence model
      ↓
Timeline reconstruction
      ↓
Entity correlation
      ↓
ATT&CK candidate mapping
      ↓
Local AI investigation draft
      ↓
Claim / citation validation
      ↓
Analyst review
      ↓
Incident handover
```

## Minimum evaluation standard

The final evaluation must cover at least 10 frozen scenarios, including suspicious activity, authorised administration, incomplete telemetry, duplicate/out-of-order timestamps, shared-host ambiguity and conflicting alerts.

Release targets:

- timeline ordering = 100% for parseable timezone-aware records;
- correlation precision ≥ 0.95;
- ATT&CK precision ≥ 0.90;
- ATT&CK recall ≥ 0.80;
- citation validity = 100%;
- unsupported accepted compromise/exfiltration claims = 0;
- analyst handover usefulness median ≥ 4/5;
- every exported recommendation reviewed by a human.

## Distinction from existing projects

This is **not** MTL-XF-039 vulnerability prioritisation and does not rank CVEs or patches. It is **not** MTL-XF-040 phishing detection and does not classify URLs/emails. Its core problem is incident reconstruction and analyst handover from event evidence.

## Zero-cost implementation

Use Python, local files/SQLite, Streamlit or CLI, pytest/unittest, MITRE ATT&CK STIX data and a local open-weight model via Ollama or llama.cpp. No paid API, cloud inference, SIEM subscription, paid threat-intelligence service or hosted database is required.

## Delivery standard

Final acceptance requires reproducible event ingestion, evidence lineage, baseline logic, local AI inference, guarded ATT&CK mapping, human review, measured evaluation, UAT, independent rerun, technical handover and individual contribution evidence.

See [Deliverables](project/DELIVERABLES.md), [Acceptance Criteria](project/ACCEPTANCE_CRITERIA.md), [Data Guidance](data/README.md) and [Submission Guide](submission/SUBMISSION_GUIDE.md).

---
**Mettelo — Built for What’s Next**
