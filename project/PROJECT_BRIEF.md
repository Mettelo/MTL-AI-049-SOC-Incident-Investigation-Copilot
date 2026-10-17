# Project brief

## Objective
Deliver SOC Incident Investigation Copilot for soc analyst, incident investigator and shift handover lead.

## Required use case
SOC analysts spend time joining alerts and event records into a defensible incident narrative. Alert severity alone does not explain chronology, related entities, uncertainty or the next investigation step.

## Product requirements
Reconstruct incidents from events and alerts. Preserve observed evidence separately from correlations and hypotheses. Map supported behaviour to frozen MITRE ATT&CK techniques. Produce timeline, correlation evidence, unknowns, recommendations and analyst handover.

## Architecture
Frozen event scenarios → schema/time validation → UTC-aware chronology → shared-entity correlation → versioned ATT&CK hypothesis → investigation recommendations → analyst handover → reviewed CSV. Python owns source parsing, stable identifiers, candidate records and validations. An optional local LLM only adds bounded explanations with exact quotations. A separate reviewer attests to the final content hash before export.

## Scope and constraints
Distinct from MTL-XF-039 vulnerability prioritisation: no CVE ranking, scanner scoring or patch prioritisation. Distinct from MTL-XF-040 phishing detection: no URL/email classifier. No live monitoring, threat execution, automated containment, credential collection or response commands.

Source: Repository-authored synthetic frozen event scenarios plus MITRE Enterprise ATT&CK 17.1 STIX 2.1. No large raw data commits. Standard-library baseline runs offline after checkout; source acquisition and optional model download require a connection once.

## Failure handling
Malformed input, duplicate IDs, absent source evidence, wrong source inventories and unknown citations fail closed. Do not repair missing facts using model guesses. Record exclusions and source/parser errors in the run report. Keep previous runs immutable for comparison.
