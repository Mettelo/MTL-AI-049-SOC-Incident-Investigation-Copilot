# Submission Guide — MTL-AI-049

## Final release sequence

1. Complete D1–D12 and reconcile requirements → deliverables → acceptance criteria → tests → evidence.
2. Freeze ATT&CK resource, scenario pack, gold labels, model/runtime, prompts and dependencies.
3. Run deterministic correlation/ATT&CK baseline and local-AI held-out evaluation; retain raw outputs and failures.
4. Execute guardrail tests, ≥10 domain tests and 3 UAT tasks; retain defects/retests.
5. Demonstrate evidence-linked timeline, ambiguous correlation, rejected unsupported mapping, analyst edit/approval and final handover.
6. Have a different member perform the clean local rerun.
7. Produce the security decision brief and demo.
8. Complete FINAL_SUBMISSION.md, CONTRIBUTIONS.md and evidence index.
9. Tag the evaluated commit `v1.0-mettelo-submission` and verify reviewer access.

## Required evidence bundle

- final repository/SHA/tag;
- requirements and traceability;
- ATT&CK/source manifests;
- scenario/split manifests;
- parser/correlation test logs;
- gold mappings and predictions;
- baseline vs AI metrics;
- raw model outputs and rejected cases;
- UAT/defect/retest records;
- reviewed handover exports;
- independent rerun record;
- zero-cost declaration;
- technical handover;
- individual contribution evidence.

## Completion rule

Screenshots or a fluent incident story are insufficient. Reviewers must be able to reproduce the core workflow and trace every accepted finding to event evidence, frozen ATT&CK references and human review.

Unmet gates remain REWORK/BLOCKED.
