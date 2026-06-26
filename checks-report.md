# Checks Report — bf_calc_anniv — 2026-06-26 19:24:36

## Summary

| Check | Status |
|---|---|
| shellcheck  install.sh | ✅ PASS |
| jsonlint  calc_anniv_web/package.json | ✅ PASS |
| hadolint  (tmp/Dockerfile not found) | ⏭ SKIP |
| markdownlint-cli2  (tmp/README.md not found) | ⏭ SKIP |
| eslint  calc_anniv_web/server.js  calc_anniv_web/public/app.js | ✅ PASS |
| yamllint  (no *.yaml / *.yml files found) | ⏭ SKIP |
| pylint  calc-anniv.py | ❌ FAIL |
| pytest  tests/ | ✅ PASS |
| semgrep  calc-anniv.py + JS sources | ✅ PASS |
| checkov  (tmp/Dockerfile not found) | ⏭ SKIP |
| trivy  HIGH/CRITICAL CVEs | ✅ PASS |
| gitleaks  secrets in repo | ✅ PASS |
| detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline) | ⏭ SKIP |
| **Total** | PASS: 7 · FAIL: 1 · SKIP: 5 |

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

**Status:** ❌ FAIL (exit 28)

```
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
************* Module calc-anniv
calc-anniv.py:56:14: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
calc-anniv.py:60:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:129:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:194:64: W0613: Unused argument 'aujourd_hui' (unused-argument)
calc-anniv.py:212:67: W0613: Unused argument 'aujourd_hui' (unused-argument)
calc-anniv.py:266:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:280:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:304:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:332:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:332:53: W0613: Unused argument 'aujourd_hui' (unused-argument)
calc-anniv.py:347:0: C0116: Missing function or method docstring (missing-function-docstring)
calc-anniv.py:347:56: W0613: Unused argument 'aujourd_hui' (unused-argument)
calc-anniv.py:365:0: R0912: Too many branches (34/12) (too-many-branches)
calc-anniv.py:365:0: R0915: Too many statements (109/50) (too-many-statements)

-----------------------------------
Your code has been rated at 9.49/10
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
2026-06-26T17:24:30Z	INFO	[vulndb] Need to update DB
2026-06-26T17:24:30Z	INFO	[vulndb] Downloading vulnerability DB...
2026-06-26T17:24:30Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
23.74 MiB / 97.58 MiB [-------------->______________________________________________] 24.32% ? p/s ?55.57 MiB / 97.58 MiB [---------------------------------->__________________________] 56.95% ? p/s ?80.61 MiB / 97.58 MiB [-------------------------------------------------->__________] 82.61% ? p/s ?97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 122.97 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 122.97 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 122.97 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 115.04 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 115.04 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 115.04 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 107.62 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 107.62 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 107.62 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 100.67 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 100.67 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 100.67 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 94.18 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 94.18 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 94.18 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 88.10 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 88.10 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 88.10 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [-------------------------------------------------] 100.00% 23.46 MiB p/s 4.4s2026-06-26T17:24:34Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-06-26T17:24:34Z	INFO	[vuln] Vulnerability scanning is enabled
2026-06-26T17:24:34Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-26T17:24:34Z	INFO	Number of language-specific files	num=1
2026-06-26T17:24:34Z	INFO	[npm] Detecting vulnerabilities...

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

[90m5:24PM[0m [32mINF[0m [1m8 commits scanned.[0m
[90m5:24PM[0m [32mINF[0m [1mscanned ~127770 bytes (127.77 KB) in 272ms[0m
[90m5:24PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

