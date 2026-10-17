# Evaluation protocol and results

## Domain benchmark
Use six frozen, version-controlled synthetic scenarios: suspicious script chain, authorised administration, incomplete telemetry, duplicate timestamps/out-of-order records, unrelated users on a shared host, and conflicting alerts. Keep two scenarios for development, two for validation and two locked for test; add at least four unseen variants before final submission. Analyst gold must label event ordering, supported entity links, acceptable ATT&CK candidates, unsupported conclusions, evidence IDs and essential next steps. Score ordering pair accuracy, correlation precision/recall, ATT&CK micro precision/recall/F1, citation validity and unsupported factual claim rate. Human reviewers score handover usefulness 1–5; report median and disagreements.

Targets: Timeline ordering 100% for parseable timezone-aware records; correlation precision ≥0.95; ATT&CK precision ≥0.90 and recall ≥0.80 on gold-supported techniques; citation validity 100%; unsupported accepted compromise/exfiltration claims 0; analyst handover median ≥4/5; all recommendations reviewed. Targets require held-out evidence.

Use precision=TP/(TP+FP), recall=TP/(TP+FN), F1=2PR/(P+R); report zero-denominator metrics as undefined, with counts. Macro F1 averages class F1; micro F1 pools counts. Citation validity=valid nonempty exact quotations / all quotations. Unsupported claim rate=reviewer-labelled unsupported factual claims / reviewed factual claims. Abstentions and nulls must be counted separately, never silently discarded.

## Supplied executable checks
`python -m unittest discover -s tests -v` exercises domain invariants and review/grounding controls. `python scripts/evaluate.py` reports frozen-demo structural checks to `evaluation/baseline_results.json`. This is a smoke/integrity evaluation, not a measured semantic AI benchmark. See the generated report for actual results and scope.

## Final experiment record
Save gold, split manifest, baseline predictions, local-model proposals, per-case adjudication and metric report. Record model digest, prompt hash/settings, hardware, latency and all invalid AI outputs. Include negative controls with missing facts, contradictory evidence, quoted prompt injection and unsupported conclusions. A valid citation is necessary but not sufficient for acceptance. Human evaluation and UAT remain pending until executed by reviewers.
