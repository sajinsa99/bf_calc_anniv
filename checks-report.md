# Checks Report — bf_calc_anniv — 2026-11-12 15:44:06

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

_no output_

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
    "node": "20.20.2",
    "npm": "10.8.2"
  },
  "dependencies": {
    "express": "^5.3.0",
    "express-rate-limit": "^8.7.4"
  },
  "devDependencies": {
    "@eslint/js": "^9.0.0",
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
Unable to find image 'python:3.12-slim' locally
3.12-slim: Pulling from library/python
37fb86c2a767: Pulling fs layer
68bced9e0afa: Pulling fs layer
2dc99d2d0a39: Pulling fs layer
05e0eee5572e: Pulling fs layer
05e0eee5572e: Waiting
2dc99d2d0a39: Verifying Checksum
2dc99d2d0a39: Download complete
68bced9e0afa: Verifying Checksum
68bced9e0afa: Download complete
05e0eee5572e: Verifying Checksum
05e0eee5572e: Download complete
37fb86c2a767: Verifying Checksum
37fb86c2a767: Download complete
37fb86c2a767: Pull complete
68bced9e0afa: Pull complete
2dc99d2d0a39: Pull complete
05e0eee5572e: Pull complete
Digest: sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b
Status: Downloaded newer image for python:3.12-slim
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

============================== 28 passed in 0.35s ==============================
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


A new version of Semgrep is available. See https://semgrep.dev/docs/upgrading
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
2026-11-12T14:43:57Z	INFO	[vulndb] Need to update DB
2026-11-12T14:43:57Z	INFO	[vulndb] Downloading vulnerability DB...
2026-11-12T14:43:57Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
18.91 MiB / 133.50 MiB [-------->___________________________________________________] 14.17% ? p/s ?47.97 MiB / 133.50 MiB [--------------------->______________________________________] 35.93% ? p/s ?77.70 MiB / 133.50 MiB [---------------------------------->_________________________] 58.20% ? p/s ?110.55 MiB / 133.50 MiB [------------------------------------->_______] 82.81% 152.74 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 152.74 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 152.74 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 145.35 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 145.35 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 145.35 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 135.97 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 135.97 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 135.97 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 127.20 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 127.20 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 127.20 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 119.00 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 119.00 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 119.00 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 111.32 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 111.32 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 111.32 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 104.14 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 104.14 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [------------------------------------------->] 100.00% 104.14 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [-------------------------------------------->] 100.00% 97.42 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [-------------------------------------------->] 100.00% 97.42 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [-------------------------------------------->] 100.00% 97.42 MiB p/s ETA 0s133.50 MiB / 133.50 MiB [-----------------------------------------------] 100.00% 24.84 MiB p/s 5.6s2026-11-12T14:44:03Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-11-12T14:44:03Z	INFO	[vuln] Vulnerability scanning is enabled
2026-11-12T14:44:03Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-11-12T14:44:03Z	INFO	Number of language-specific files	num=1
2026-11-12T14:44:03Z	INFO	[npm] Detecting vulnerabilities...

Report Summary

┌──────────────────────────────────┬──────┬─────────────────┐
│              Target              │ Type │ Vulnerabilities │
├──────────────────────────────────┼──────┼─────────────────┤
│ calc_anniv_web/package-lock.json │ npm  │        0        │
└──────────────────────────────────┴──────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


📣 [34mNotices:[0m
  - Version 0.76.2 of Trivy is now available, current version is 0.76.1

To suppress version checks, run Trivy scans with the --skip-version-check flag
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

[90m2:44PM[0m [32mINF[0m [1m27 commits scanned.[0m
[90m2:44PM[0m [32mINF[0m [1mscanned ~179087 bytes (179.09 KB) in 308ms[0m
[90m2:44PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

