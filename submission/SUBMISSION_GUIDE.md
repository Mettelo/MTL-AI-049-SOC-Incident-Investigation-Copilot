# MTL-AI-049 — Submission guide

## Release sequence

1. Finish D1–D12 and map requirements to deliverables, acceptance criteria, tests and evidence.
2. Confirm the frozen ATT&CK version, scenario manifests, schema/time assumptions and reviewer restore access.
3. Freeze correlation rules, ATT&CK mapping policy, prompts, model/runtime, gold labels and dependency lock.
4. Run deterministic timeline/correlation baseline and local-AI workflow. Preserve raw outputs, unsupported mappings, rejected claims and failures.
5. Execute SOC/grounding tests and **three UAT tasks**. Resolve all critical/high defects and retain retests.
6. A distinct member performs a clean rerun from the documented sources/scenarios and reconciles deterministic timeline/evidence results.
7. Produce a 2-page security decision brief, 8–12 slides and a 5–10 minute demo for the **SOC Shift Lead**.
8. Complete `submission/FINAL_SUBMISSION.md`, contribution evidence and evidence index.
9. Tag the evaluated commit **`v1.0-mettelo-submission`** and verify reviewer access.

## Walkthrough

Demonstrate one suspicious sequence, one benign/authorised lookalike, one incomplete-telemetry case, one rejected unsupported ATT&CK/compromise claim and one reviewed shift handover.

Explain which statements are observed evidence, which are correlations and which remain hypotheses.

## Required evidence bundle

Team repo/final SHA/tag; reviewed master commit; ATT&CK/scenario manifests; traceability; baseline and AI outputs; gold labels; held-out metrics with denominators; rejected claims; reviewed handovers; UAT/defects; clean rerun; handover; decision brief/demo; contribution evidence.

Reviewer records **ACCEPTED / REWORK / BLOCKED** with actual reviewer/date, simulated sponsor role and unresolved issues/owners.
