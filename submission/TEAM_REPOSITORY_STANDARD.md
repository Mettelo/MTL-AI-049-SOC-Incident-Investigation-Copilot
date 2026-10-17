# MTL-AI-049 — Team repository standard

Create **MTL-AI-049-<team-name>** under the **Mettelo GitHub organisation** and add individual member accounts.

Record in the team README: master URL/reviewed commit, members/responsibilities, frozen ATT&CK/scenario versions, environment/run instructions, final team SHA/tag and limitations.

## Required repository structure

```text
README.md
CONTRIBUTIONS.md
.gitignore
requirements.txt or equivalent lock
config/
src/
app/
tests/
prompts/
evaluation/
outputs/
data/
  SOURCE_REGISTER.md
  raw/
    README.md
  reference/
  metadata/
  curated/
docs/
  01-discovery/
  02-data-governance/
  03-data-model/
  04-data-quality/
  05-evidence/
  06-ai/
  07-decision-framework/
  08-assurance-uat/
  09-technical-handover/
deliverables/
submission/
  FINAL_SUBMISSION.md
```

Equivalent tool-specific folders require an explicit mapping.

## Data handling

Use the approved MITRE ATT&CK version and frozen safe scenario pack described in the master. The team must create its own manifest for every source/scenario used, including version, filename, hash, date, licence/terms, schema/timezone assumptions and reviewer.

Large telemetry and model weights should remain outside Git unless cohort guidance permits them. Never add credentials, live attack tooling or executable malware.

## README and contribution evidence

State:

> Reconstruct a security incident from frozen telemetry, distinguish evidence from hypothesis and produce an analyst-reviewed investigation handover.

Simulated sponsor: **SOC Shift Lead**.

Preserve this limitation:

> ATT&CK mappings are evidence-supported hypotheses, not proof of compromise. Do not rank CVEs, classify phishing URLs, execute response actions or claim exfiltration without supporting evidence.

Every member links authored artefacts, at least one substantive review and UAT/demo/handover contribution. Commit count alone is not Proof.

## Required project-specific artefacts

- **D5 Incident evidence/ATT&CK ledger:** `data/curated/incident-evidence-ledger.csv` and `docs/05-evidence/attack-mapping-contract.md`.
- **D6 Incident-copilot evaluation:** `docs/06-ai/incident-evaluation.md` and `evaluation/results.csv`.
- **D7 Investigation/escalation policy:** `docs/07-decision-framework/investigation-policy.md` plus `case-register.csv`.
- **D8 Analyst investigation/review product:** `app/README.md` and `outputs/examples/`.
- **D11 SOC handover/recommendation pack:** `deliverables/soc-handover-pack.pdf` plus editable slides.

Maintain D1–D12 / acceptance / test / UAT evidence with owner, reviewer, result/state and final-commit link.

Recommended team size: **3–5 people**.
