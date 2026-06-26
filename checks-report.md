# Checks Report — bf_calc_anniv — 2026-06-26 19:28:25

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
    "express": "^4.18.2",
    "express-rate-limit": "^7.0.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.0.0",
    "globals": "^15.0.0"
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

[notice] A new release of pip is available: 25.0.1 -> 26.1.2
[notice] To update, run: pip install --upgrade pip

------------------------------------
Your code has been rated at 10.00/10
```

---

### `pytest  tests/`

**Status:** ✅ PASS

```
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0
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
  Scanning 3 files tracked by git with 1059 Code rules:
                                                                                                                        
  Language      Rules   Files          Origin      Rules                                                                
 ─────────────────────────────        ───────────────────                                                               
  <multilang>      47       3          Community    1059                                                                
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
2026-06-26T17:28:19Z	INFO	[vulndb] Need to update DB
2026-06-26T17:28:19Z	INFO	[vulndb] Downloading vulnerability DB...
2026-06-26T17:28:19Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
30.90 MiB / 97.58 MiB [------------------->_________________________________________] 31.67% ? p/s ?68.89 MiB / 97.58 MiB [------------------------------------------->_________________] 70.60% ? p/s ?97.58 MiB / 97.58 MiB [----------------------------------------------------------->] 100.00% ? p/s ?97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 111.09 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 111.09 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 111.09 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 103.92 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 103.92 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 103.92 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 97.22 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 97.22 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 97.22 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 90.95 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 90.95 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 90.95 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 85.08 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 85.08 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 85.08 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 79.59 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [-------------------------------------------------] 100.00% 25.85 MiB p/s 4.0s2026-06-26T17:28:23Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-06-26T17:28:23Z	INFO	[vuln] Vulnerability scanning is enabled
2026-06-26T17:28:23Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-26T17:28:23Z	INFO	Number of language-specific files	num=1
2026-06-26T17:28:23Z	INFO	[npm] Detecting vulnerabilities...

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

[90m5:28PM[0m [32mINF[0m [1m11 commits scanned.[0m
[90m5:28PM[0m [32mINF[0m [1mscanned ~132093 bytes (132.09 KB) in 277ms[0m
[90m5:28PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

