# MTL-AI-049 — Submission guide

## Release sequence

1. Complete D1–D12 and map all agreed user requirements to deliverables, acceptance criteria, tests and final evidence.
2. Confirm the approved source/data manifest, rights/attribution, exact cohort/version and reviewer restore access.
3. Freeze deterministic rules, prompts, model/runtime version, evaluation split, schemas and dependency lock before final held-out evaluation.
4. Run the deterministic baseline and local-AI workflow. Preserve raw outputs, invalid outputs, retries/fallbacks, rejected claims and measured results; do not replace weak runs with hand-written examples.
5. Execute the project-specific domain/guardrail tests and **three UAT tasks** with expected/actual results, tester/reviewer, defects and retests. Resolve all critical/high defects.
6. Have a distinct member perform a clean rerun from the documented source and environment. Record hashes, versions, entry point, elapsed time, discrepancies and reconciliation.
7. Produce a **2-page decision brief**, **8–12 slides** and a **5–10 minute reproducible demo** for SOC Shift Lead. Include five evidence-backed findings, three next actions and at least one defer/unknown case.
8. Complete `submission/FINAL_SUBMISSION.md`, `CONTRIBUTIONS.md` and the immutable evidence index.
9. Tag the evaluated commit **`v1.0-mettelo-submission`** and verify reviewer access. Do not silently move the assessed tag.

## Required walkthrough

Answer the commissioned decision:

> Reconstruct a security incident from frozen telemetry, distinguish evidence from hypothesis and produce an analyst-reviewed investigation handover.

Demonstrate one suspicious sequence, one benign/authorised lookalike, one incomplete-telemetry case, one rejected unsupported ATT&CK/compromise claim and one reviewed shift handover.

Show one failure/edge case and explain what the evidence **does not** support.

Preserve this project boundary:

> ATT&CK mappings are evidence-supported hypotheses, not proof of compromise. Do not rank CVEs, classify phishing URLs, execute response actions or claim exfiltration without supporting evidence.

## Required evidence bundle

- team repository URL, final commit SHA and release tag;
- reviewed master commit;
- requirements/traceability index;
- source/data manifest and restore instructions;
- deterministic baseline outputs;
- local model/runtime/prompt/config versions;
- held-out evaluation results with denominators;
- failed/rejected/guarded examples;
- UAT records and defect/retest log;
- independent clean-rerun record;
- technical/operational handover;
- final decision brief and demo;
- individual contribution evidence.

## Reviewer decision

The reviewer records **ACCEPTED / REWORK / BLOCKED**, actual reviewer, simulated sponsor role, date, unresolved issues and owners/due dates.

A filled template, screenshot, video or fluent AI output without executed evidence is not acceptance.
