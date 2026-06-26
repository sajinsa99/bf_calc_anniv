# Checks Report — bf_calc_anniv — 2026-06-26 19:16:46

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
| pytest  tests/ | ❌ FAIL |
| semgrep  calc-anniv.py + JS sources | ✅ PASS |
| checkov  (tmp/Dockerfile not found) | ⏭ SKIP |
| trivy  HIGH/CRITICAL CVEs | ✅ PASS |
| gitleaks  secrets in repo | ✅ PASS |
| detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline) | ⏭ SKIP |
| **Total** | PASS: 6 · FAIL: 2 · SKIP: 5 |

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

**Status:** ❌ FAIL (exit 127)

```
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "pylint": executable file not found in $PATH

Run 'docker run --help' for more information
```

---

### `pytest  tests/`

**Status:** ❌ FAIL (exit 127)

```
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "pytest": executable file not found in $PATH

Run 'docker run --help' for more information
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
2026-06-26T17:16:39Z	INFO	[vulndb] Need to update DB
2026-06-26T17:16:39Z	INFO	[vulndb] Downloading vulnerability DB...
2026-06-26T17:16:39Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
25.48 MiB / 97.58 MiB [--------------->_____________________________________________] 26.11% ? p/s ?61.66 MiB / 97.58 MiB [-------------------------------------->______________________] 63.20% ? p/s ?90.82 MiB / 97.58 MiB [-------------------------------------------------------->____] 93.08% ? p/s ?97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 120.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 120.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 120.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 112.37 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 112.37 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 112.37 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 105.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 105.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [--------------------------------------------->] 100.00% 105.12 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 98.34 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 98.34 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 98.34 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 91.99 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 91.99 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 91.99 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 86.06 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 86.06 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 86.06 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [---------------------------------------------->] 100.00% 80.50 MiB p/s ETA 0s97.58 MiB / 97.58 MiB [-------------------------------------------------] 100.00% 22.94 MiB p/s 4.5s2026-06-26T17:16:44Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-06-26T17:16:44Z	INFO	[vuln] Vulnerability scanning is enabled
2026-06-26T17:16:44Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-06-26T17:16:44Z	INFO	Number of language-specific files	num=1
2026-06-26T17:16:44Z	INFO	[npm] Detecting vulnerabilities...

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

[90m5:16PM[0m [32mINF[0m [1m5 commits scanned.[0m
[90m5:16PM[0m [32mINF[0m [1mscanned ~81020 bytes (81.02 KB) in 268ms[0m
[90m5:16PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

