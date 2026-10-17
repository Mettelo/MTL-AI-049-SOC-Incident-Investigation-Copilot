# Deliverables — MTL-AI-049

| ID | Required output | Minimum evidence | Default location |
|---|---|---|---|
| D1 | Discovery & SOC workflow | as-is/to-be investigation flow; users; 8+ requirements; scope; traceability | docs/01-discovery/ |
| D2 | Source & governance pack | frozen ATT&CK version/hash; event-scenario manifest; licences; safe-use boundary | docs/02-data-governance/ + data/SOURCE_REGISTER.md |
| D3 | Event normalisation pipeline | schemas; timezone rules; evidence IDs; validation/quarantine; rerun instructions | src/ + docs/03-data-model/ |
| D4 | Deterministic correlation baseline | chronology logic; entity links; ambiguity rules; baseline outputs; test fixtures | docs/04-baseline/ + tests/ |
| D5 | ATT&CK mapping contract | technique dictionary; evidence-to-technique rules; unsupported mapping policy; version pin | docs/05-attack-mapping/ |
| D6 | Local AI investigation layer | pinned model/runtime; prompt/schema; bounded context; raw outputs; failure fallback | prompts/ + docs/06-ai/ |
| D7 | Claim/guardrail layer | citation validation; compromise/exfiltration claim guard; stale/invalid mapping tests | tests/ + docs/07-guardrails/ |
| D8 | Analyst review product | timeline; evidence drill-down; accept/reject/edit; unknowns; handover export; audit history | app/ + outputs/examples/ |
| D9 | Evaluation & assurance | ≥10 scenarios; locked split; per-case metrics; error analysis; reviewer disagreements | evaluation/ |
| D10 | UAT & technical handover | ≥10 domain tests; 3 user tasks; defects/retests; setup/run/restore/troubleshooting | docs/08-assurance-uat/ + docs/09-technical-handover/ |
| D11 | Executive/security briefing & demo | 2-page brief; 8–12 slides; reproducible demo; retain/revise/pilot recommendation | deliverables/ |
| D12 | Final submission & contribution evidence | final SHA/tag; evidence index; CONTRIBUTIONS.md; individual artefacts/reviews | submission/ + CONTRIBUTIONS.md |

## Required demo cases

Show: one correctly reconstructed suspicious sequence; one authorised/admin case; one incomplete-telemetry case; one unsupported ATT&CK mapping rejected; one material edit invalidating approval; one final reviewed handover.
