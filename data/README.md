# Data and exact acquisition

Primary resource: Repository-authored synthetic frozen event scenarios plus MITRE Enterprise ATT&CK 17.1 STIX 2.1.

| Local raw filename | Resource/version | Exact URL |
|---|---|---|
| attack.json | MITRE Enterprise ATT&CK 17.1; retain MITRE terms and attribution | https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.1.json |

From the root, run `python scripts/fetch_sources.py`. This downloads into ignored `data/raw/` and creates `data/metadata/download_manifest.json` with URL, byte count, SHA-256 and access time. It reuses existing local files; explicitly remove/replace a file only when you intend to refresh it, then compare hashes and rerun validation. Never silently overwrite the frozen cohort.

Prepare using:
```text
python app.py prepare --source data/raw/attack.json --output runs/attack.json
```

The bundled `data/reference/demo.json` is a small frozen input for offline reproduction. Its provenance is recorded in `data/metadata/baseline_manifest.json`. Never describe synthetic examples as real incidents or demo subsets as benchmark test sets.

Raw archives, complete STIX bundles, audio/video and model weights must not be committed. Commit only small derived fixtures, manifests, gold labels and scripts. Read [source register](SOURCE_REGISTER.md) before redistributing.
