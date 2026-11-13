# Checks Report — bf_calc_anniv — 2026-11-13 11:45:24

## Summary

| Check | Status |
|---|---|
| shellcheck  install.sh | ✅ PASS |
| jsonlint  calc_anniv_web/package.json | ✅ PASS |
| hadolint  (tmp/Dockerfile not found) | ⏭ SKIP |
| markdownlint-cli2  (tmp/README.md not found) | ⏭ SKIP |
| eslint  calc_anniv_web/server.js  calc_anniv_web/public/app.js | ✅ PASS |
| yamllint  (no *.yaml / *.yml files found) | ⏭ SKIP |
| pylint  calc-anniv.py | ✅ PASS |
| pytest  tests/ | ✅ PASS |
| semgrep  calc-anniv.py + JS sources | ✅ PASS |
| checkov  (tmp/Dockerfile not found) | ⏭ SKIP |
| trivy  HIGH/CRITICAL CVEs | ✅ PASS |
| gitleaks  secrets in repo | ✅ PASS |
| detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline) | ⏭ SKIP |
| **Total** | PASS: 8 · FAIL: 0 · SKIP: 5 |

---

## Shell

### `shellcheck  install.sh`

**Status:** ✅ PASS

```
Unable to find image 'xmake-deploy-milestone.int.repositories.cloud.sap/com.sap.internal.prd.xmk.tools/xmk_linters:2.0.4' locally
2.0.4: Pulling from com.sap.internal.prd.xmk.tools/xmk_linters
517b871c26ea: Already exists
96aae9022e0e: Already exists
93cbc450b015: Pulling fs layer
333115460fd0: Pulling fs layer
983bd05b917d: Pulling fs layer
0e77df7aa202: Pulling fs layer
03bf8cd13bd5: Pulling fs layer
cb8b6dea2700: Pulling fs layer
b0d2b241f93d: Pulling fs layer
c297d27bff78: Pulling fs layer
4f4fb700ef54: Pulling fs layer
a7334588d880: Pulling fs layer
0e77df7aa202: Waiting
03bf8cd13bd5: Waiting
cb8b6dea2700: Waiting
b0d2b241f93d: Waiting
4f4fb700ef54: Waiting
c297d27bff78: Waiting
a7334588d880: Waiting
983bd05b917d: Verifying Checksum
983bd05b917d: Download complete
0e77df7aa202: Verifying Checksum
0e77df7aa202: Download complete
93cbc450b015: Verifying Checksum
93cbc450b015: Download complete
cb8b6dea2700: Verifying Checksum
cb8b6dea2700: Download complete
b0d2b241f93d: Verifying Checksum
b0d2b241f93d: Download complete
03bf8cd13bd5: Verifying Checksum
4f4fb700ef54: Verifying Checksum
4f4fb700ef54: Download complete
c297d27bff78: Download complete
a7334588d880: Download complete
333115460fd0: Verifying Checksum
333115460fd0: Download complete
93cbc450b015: Pull complete
333115460fd0: Pull complete
983bd05b917d: Pull complete
0e77df7aa202: Pull complete
03bf8cd13bd5: Pull complete
cb8b6dea2700: Pull complete
b0d2b241f93d: Pull complete
c297d27bff78: Pull complete
4f4fb700ef54: Pull complete
a7334588d880: Pull complete
Digest: sha256:d1381aa184dd9744b8980785fabce46fe49cdcffcf2fb6a42c264fbdc42287be
Status: Downloaded newer image for xmake-deploy-milestone.int.repositories.cloud.sap/com.sap.internal.prd.xmk.tools/xmk_linters:2.0.4
```

---

## JSON

### `jsonlint  calc_anniv_web/package.json`

**Status:** ✅ PASS

```
{
  "name": "calc_anniv_web",
  "version": "1.0.0",
  "description": "Web UI for bf_calc_anniv calc-anniv.py",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "lint": "eslint server.js public/app.js"
  },
  "engines": {
    "node": "22.22.1",
    "npm": "9.2.0"
  },
  "dependencies": {
    "express": "^5.3.0",
    "express-rate-limit": "^8.7.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.5",
    "globals": "^17.14.0"
  }
}
```

---

## Dockerfile

### `hadolint  (tmp/Dockerfile not found)`

**Status:** ⏭ SKIP

---

## Markdown

### `markdownlint-cli2  (tmp/README.md not found)`

**Status:** ⏭ SKIP

---

## JavaScript

### `eslint  calc_anniv_web/server.js  calc_anniv_web/public/app.js`

**Status:** ✅ PASS

_no output_

---

## YAML

### `yamllint  (no *.yaml / *.yml files found)`

**Status:** ⏭ SKIP

---

## Python

### `pylint  calc-anniv.py`

**Status:** ✅ PASS

```
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: pip install --upgrade pip

------------------------------------
Your code has been rated at 10.00/10
```

---

### `pytest  tests/`

**Status:** ✅ PASS

```
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: pip install --upgrade pip
============================= test session starts ==============================
platform linux -- Python 3.12.16, pytest-9.2.0, pluggy-1.7.0
rootdir: /work
configfile: pyproject.toml
collected 28 items

tests/test_calc_anniv.py ............................                    [100%]

============================== 28 passed in 0.34s ==============================
```

---

## Static Analysis

### `semgrep  calc-anniv.py + JS sources`

**Status:** ✅ PASS

```
               
               
┌─────────────┐
│ Scan Status │
└─────────────┘
  Scanning 3 files tracked by git with 1074 Code rules:
                                                                                                                        
  Language      Rules   Files          Origin      Rules                                                                
 ─────────────────────────────        ───────────────────                                                               
  <multilang>      47       3          Community    1074                                                                
  js              153       2                                                                                           
  python          243       1                                                                                           
                                                                                                                        
                
                
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 0 (0 blocking)
 • Rules run: 442
 • Targets scanned: 3
 • Parsed lines: ~100.0%
 • No ignore information available
Ran 442 rules on 3 files: 0 findings.
(need more rules? `semgrep login` for additional free Semgrep Registry rules)

If Semgrep missed a finding, please send us feedback to let us know!
See https://semgrep.dev/docs/reporting-false-negatives/
```

---

## IaC Policy

### `checkov  (tmp/Dockerfile not found)`

**Status:** ⏭ SKIP

---

## Dependency CVEs

### `trivy  HIGH/CRITICAL CVEs`

**Status:** ✅ PASS

```
2026-11-13T10:45:15Z	INFO	[vulndb] Need to update DB
2026-11-13T10:45:15Z	INFO	[vulndb] Downloading vulnerability DB...
2026-11-13T10:45:15Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
23.75 MiB / 133.47 MiB [---------->_________________________________________________] 17.80% ? p/s ?58.95 MiB / 133.47 MiB [-------------------------->_________________________________] 44.16% ? p/s ?101.07 MiB / 133.47 MiB [-------------------------------------------->______________] 75.72% ? p/s ?133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 183.04 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 183.04 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 183.04 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 171.23 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 171.23 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 171.23 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 160.19 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 160.19 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 160.19 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 149.85 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 149.85 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 149.85 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 140.18 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 140.18 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 140.18 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 131.14 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 131.14 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 131.14 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 122.68 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 122.68 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 122.68 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 114.76 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 114.76 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [------------------------------------------->] 100.00% 114.76 MiB p/s ETA 0s133.47 MiB / 133.47 MiB [-----------------------------------------------] 100.00% 25.20 MiB p/s 5.5s2026-11-13T10:45:21Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-11-13T10:45:21Z	INFO	[vuln] Vulnerability scanning is enabled
2026-11-13T10:45:21Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-11-13T10:45:21Z	INFO	Number of language-specific files	num=1
2026-11-13T10:45:21Z	INFO	[npm] Detecting vulnerabilities...

Report Summary

┌──────────────────────────────────┬──────┬─────────────────┐
│              Target              │ Type │ Vulnerabilities │
├──────────────────────────────────┼──────┼─────────────────┤
│ calc_anniv_web/package-lock.json │ npm  │        0        │
└──────────────────────────────────┴──────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)
```

---

## Secrets

### `gitleaks  secrets in repo`

**Status:** ✅ PASS

```

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m10:45AM[0m [32mINF[0m [1m34 commits scanned.[0m
[90m10:45AM[0m [32mINF[0m [1mscanned ~189251 bytes (189.25 KB) in 235ms[0m
[90m10:45AM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

