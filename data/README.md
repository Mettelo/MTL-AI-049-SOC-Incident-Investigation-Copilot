# Data Guidance — MTL-AI-049

## Core resources

### R1 — MITRE Enterprise ATT&CK 17.1 STIX 2.1

Exact URL:

https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json

Freeze the downloaded file and record filename, bytes, SHA-256, retrieval UTC, ATT&CK version and licence/terms reference.

### R2 — Frozen security-event scenario pack

The core Mettelo project uses a version-controlled safe event pack containing simulated authentication, process, network and alert records. It is designed for analysis only and must not include executable malware, credentials or instructions for offensive activity.

Each scenario records:

- scenario ID/version;
- event files and hashes;
- event source/schema;
- timezone convention;
- expected ordering;
- supported entity links;
- supported/unsupported ATT&CK techniques;
- essential unknowns;
- reviewer-approved next-step expectations.

## Minimum scenario set

Final evaluation must contain at least 10 scenarios and include:

- suspicious script/process chain;
- authorised administration;
- incomplete telemetry;
- duplicate timestamps;
- out-of-order records;
- shared host/user ambiguity;
- conflicting alerts;
- benign lookalike;
- multi-host sequence;
- insufficient-evidence case.

## Raw handling

Keep complete raw telemetry outside Git if large; commit small safe fixtures intentionally. Preserve manifests/hashes and do not silently modify scenario truth after evaluation begins.

## Analytical grain

Primary grain:

**event → evidence ID → host/user/process/network entities**

Derived grain:

**investigation finding → evidence set → ATT&CK candidate → reviewer state**

## ATT&CK rule

ATT&CK mappings are hypotheses supported by evidence, not proof of compromise. Cross-technique relationships and version changes must not be inferred from model memory when the frozen ATT&CK file is available.

## Optional external validation

Teams may add selected publicly released, pre-recorded security-event datasets only after recording source, licence, version, hash and why they improve evaluation. Live attack generation is not required and is outside core scope.
