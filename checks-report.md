# Checks Report — bf_calc_anniv — 2026-06-26 19:20:47

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
Unable to find image 'python:3.12-slim' locally
3.12-slim: Pulling from library/python
e95a6c7ea7d4: Pulling fs layer
aff2d9f8dc87: Pulling fs layer
df79d931cd67: Pulling fs layer
b32430367bf0: Pulling fs layer
b32430367bf0: Waiting
aff2d9f8dc87: Download complete
e95a6c7ea7d4: Download complete
b32430367bf0: Verifying Checksum
b32430367bf0: Download complete
df79d931cd67: Verifying Checksum
df79d931cd67: Download complete
e95a6c7ea7d4: Pull complete
aff2d9f8dc87: Pull complete
df79d931cd67: Pull complete
b32430367bf0: Pull complete
Digest: sha256:6c4dd321d176d61ea848dc8c73a4f7dbae8f70e0ee48bb411ea2f045b599fa8e
Status: Downloaded newer image for python:3.12-slim
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

============================== 28 passed in 0.39s ==============================
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
2026-06-26T17:20:40Z	INFO	[vulndb] Need to update DB
2026-06-26T17:20:40Z	INFO	[vulndb] Downloading vulnerability DB...
2026-06-26T17:20:40Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
27.57 MiB / 97.58 MiB [----------------->___________________________________________] 28.26% ? p/s ?62.45 MiB / 97.58 MiB [--------------------------------------->_____________________] 64.00% ? p/s ?97.58 MiB / 97.58 MiB [----------------------------------------------------------->] 100.00% ? p/s ?97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 116.64 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 116.64 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 116.64 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 109.11 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 109.11 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 109.11 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 102.07 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 102.07 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 102.07 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 95.49 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 95.49 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 95.49 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 89.33 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 89.33 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 89.33 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 83.56 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 83.56 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [-------------------------------------------------] 100.00% 25.57 MiB p/s 4.0s2026-06-26T17:20:45Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-06-26T17:20:45Z	INFO	[vuln] Vulnerability scanning is enabled
2026-06-26T17:20:45Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-26T17:20:45Z	INFO	Number of language-specific files	num=1
2026-06-26T17:20:45Z	INFO	[npm] Detecting vulnerabilities...

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

[90m5:20PM[0m [32mINF[0m [1m7 commits scanned.[0m
[90m5:20PM[0m [32mINF[0m [1mscanned ~121192 bytes (121.19 KB) in 319ms[0m
[90m5:20PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

