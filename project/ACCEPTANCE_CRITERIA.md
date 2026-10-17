# Acceptance criteria

## Functional gates
1. Fresh checkout runs the bundled example with Python 3.11+ and no paid dependency.
2. Official-source preparation succeeds and records provenance; source identifiers survive into output citations.
3. Every candidate has at least one resolvable exact quotation. Missing data stays explicit.
4. Each record receives accept/reject and a reviewer note. Pending or partial review blocks export.
5. Editing any part of the draft after approval invalidates export.
6. Repeated baseline runs on identical input yield the same content hash.

## Semantic and AI quality gates
Timeline ordering 100% for parseable timezone-aware records; correlation precision ≥0.95; ATT&CK precision ≥0.90 and recall ≥0.80 on gold-supported techniques; citation validity 100%; unsupported accepted compromise/exfiltration claims 0; analyst handover median ≥4/5; all recommendations reviewed. Targets require held-out evidence.

## Measurement protocol
Use six frozen, version-controlled synthetic scenarios: suspicious script chain, authorised administration, incomplete telemetry, duplicate timestamps/out-of-order records, unrelated users on a shared host, and conflicting alerts. Keep two scenarios for development, two for validation and two locked for test; add at least four unseen variants before final submission. Analyst gold must label event ordering, supported entity links, acceptable ATT&CK candidates, unsupported conclusions, evidence IDs and essential next steps. Score ordering pair accuracy, correlation precision/recall, ATT&CK micro precision/recall/F1, citation validity and unsupported factual claim rate. Human reviewers score handover usefulness 1–5; report median and disagreements.

## Evidence for sign-off
Attach test output, source/split hashes, raw predictions, metric report with denominators, independently reviewed failures, model/no-model comparison, UAT results and known limitations. A 100% citation match is only structural grounding, never proof that the claim follows from that quote. Evaluate factual entailment separately by domain review.
