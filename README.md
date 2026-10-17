# MTL-AI-049 — SOC Incident Investigation Copilot

## Business problem and user
SOC analysts spend time joining alerts and event records into a defensible incident narrative. Alert severity alone does not explain chronology, related entities, uncertainty or the next investigation step.

**Primary users:** SOC analyst, incident investigator and shift handover lead.

## Working product
Reconstruct incidents from events and alerts. Preserve observed evidence separately from correlations and hypotheses. Map supported behaviour to frozen MITRE ATT&CK techniques. Produce timeline, correlation evidence, unknowns, recommendations and analyst handover.

**Workflow:** Frozen event scenarios → schema/time validation → UTC-aware chronology → shared-entity correlation → versioned ATT&CK hypothesis → investigation recommendations → analyst handover → reviewed CSV.

This repository includes a runnable Python command-line application, source importers, a small frozen demonstration input, automated control tests, optional local AI explanations and a hash-bound review/export workflow. The baseline is deterministic; it is not represented as an evaluated language model. Meeting extraction and ATT&CK mappings are candidates. AI quality acceptance still requires the held-out evaluation specified below.

## Run locally at zero cost
Install Python 3.11 or newer. No paid APIs, accounts, cloud hosting or Python packages are required. Run commands from this repository root, with normal Python (never `python -O`). Windows users may use `py -3` in place of `python`.

```text
python -m unittest discover -s tests -v
python app.py run --input data/reference/demo.json --output runs/draft.json
python app.py review-template --draft runs/draft.json --output runs/decisions.json
```

Open `runs/draft.json` alongside its source. For every record in `runs/decisions.json`, change `pending` to `accept` or `reject`, and write a substantive `note`. Review all AI proposals attached to that record as well. To correct factual content, edit the draft, then review that final draft. Approval is a local attestation, not an identity-authenticated signature.

```text
python app.py approve --draft runs/draft.json --decisions runs/decisions.json --reviewer "Reviewer Name" --output runs/approval.json
python app.py export --draft runs/draft.json --approval runs/approval.json --output runs/reviewed.csv
```

Export blocks incomplete review, unknown citations, quote mismatches and edits after approval. CSV includes evidence, details, AI proposals and review notes. JSON remains the detailed evidence-linked minutes, handover or change register. Keep draft/approval together for audit.

## Use the complete official resources
Source: **Repository-authored synthetic frozen event scenarios plus MITRE Enterprise ATT&CK 17.1 STIX 2.1**. See [data guidance](data/README.md) and [source register](data/SOURCE_REGISTER.md).

```text
python scripts/fetch_sources.py
python app.py prepare --source data/raw/attack.json --output runs/attack.json
python app.py run --input data/reference/demo.json --output runs/full-draft.json
```

Raw downloads are local and ignored by Git. The bundled input is a frozen reproducible demonstration; it is not a held-out benchmark.

## Optional local AI
Install the open-source Ollama runtime and download a locally runnable model, for example the Apache-2.0 `qwen2.5:3b`. A 3B quantised model generally needs several GB of RAM/disk; CPU execution is slower. Record the exact model digest from your runtime, hardware and generation settings. Model/runtime downloads need internet once; inference stays at `127.0.0.1:11434` and requires no API key.

```text
ollama pull qwen2.5:3b
python app.py run --input data/reference/demo.json --output runs/ai-draft.json --model qwen2.5:3b
```

AI adds cited explanation proposals to existing records; it cannot approve, overwrite source evidence or execute operational actions. Missing/invalid citations reject the AI result. Quote validity does **not** prove semantic entailment: a reviewer must inspect every proposal. Large meetings/registers may exceed model context; select a documented bounded subset, record excluded items, or use the deterministic full run. No silent truncation is performed. If Ollama is absent or returns invalid JSON, use the baseline and report AI unavailable; do not claim AI evaluation passed.

## Evaluation and completion
Use six frozen, version-controlled synthetic scenarios: suspicious script chain, authorised administration, incomplete telemetry, duplicate timestamps/out-of-order records, unrelated users on a shared host, and conflicting alerts. Keep two scenarios for development, two for validation and two locked for test; add at least four unseen variants before final submission. Analyst gold must label event ordering, supported entity links, acceptable ATT&CK candidates, unsupported conclusions, evidence IDs and essential next steps. Score ordering pair accuracy, correlation precision/recall, ATT&CK micro precision/recall/F1, citation validity and unsupported factual claim rate. Human reviewers score handover usefulness 1–5; report median and disagreements.

**Delivery gates:** Timeline ordering 100% for parseable timezone-aware records; correlation precision ≥0.95; ATT&CK precision ≥0.90 and recall ≥0.80 on gold-supported techniques; citation validity 100%; unsupported accepted compromise/exfiltration claims 0; analyst handover median ≥4/5; all recommendations reviewed. Targets require held-out evidence.

See [project pack](project/README.md), [evaluation protocol](evaluation/README.md), [UAT](project/UAT_AND_DEMO.md) and [submission guide](submission/SUBMISSION_GUIDE.md). Automated integrity checks and a frozen demonstration are supplied; human acceptance, semantic gold and local-model evaluation are not fabricated.

## Scope boundary
Distinct from MTL-XF-039 vulnerability prioritisation: no CVE ranking, scanner scoring or patch prioritisation. Distinct from MTL-XF-040 phishing detection: no URL/email classifier. No live monitoring, threat execution, automated containment, credential collection or response commands.

## Repository map
`app.py` review/export/AI orchestration; `engine.py` domain logic and ingestion; `scripts/` source acquisition and evaluation; `tests/` executable checks; `data/reference/` frozen small inputs; `data/metadata/` provenance and schemas; `project/` delivery contract; `evaluation/` metrics/results; `submission/` final evidence standards.
