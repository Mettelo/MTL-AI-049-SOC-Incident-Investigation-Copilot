# Acceptance Criteria — MTL-AI-049

| ID | Acceptance gate | Objective pass evidence |
|---|---|---|
| AC1 | Scope and requirements | ≥8 prioritised requirements mapped to D/AC/test evidence; approved SOC investigation workflow |
| AC2 | Resource reproducibility | ATT&CK version/hash and scenario manifest frozen; no hidden live dependency |
| AC3 | Event parsing integrity | all selected scenarios parsed or quarantined explicitly; stable evidence IDs and timezone handling |
| AC4 | Timeline correctness | 100% ordering for parseable timezone-aware records on held-out scenarios |
| AC5 | Correlation quality | correlation precision ≥0.95; recall reported; ambiguous shared-entity cases remain explicit |
| AC6 | ATT&CK quality | precision ≥0.90 and recall ≥0.80 on adjudicated gold-supported techniques |
| AC7 | Local AI execution | actual local model run with pinned model/runtime/settings; raw outputs preserved; no paid dependency |
| AC8 | Grounding safety | citation validity 100%; unsupported accepted compromise/exfiltration claims = 0 |
| AC9 | Review control | every exported finding/recommendation has human decision/note; edits invalidate prior approval |
| AC10 | Evaluation integrity | ≥10 scenarios with development/validation/test separation; gold labels and disagreements preserved |
| AC11 | UAT & defects | ≥10 domain tests + 3 user tasks; zero unresolved critical/high defects; repairs retested |
| AC12 | Reproducibility | different member completes clean rerun; deterministic outputs/hashes reconcile |
| AC13 | Handover usefulness | analyst usefulness median ≥4/5 with sample size and disagreements reported |
| AC14 | Zero-cost completion | no paid SIEM, threat feed, cloud inference, subscription or trial required |
| AC15 | Submission integrity | evaluated tag/SHA fixed; reviewer access, evidence index, limitations and contributions complete |

Final release state: **ACCEPTED, REWORK or BLOCKED**.
