# Checks Report — bf_calc_anniv — 2026-11-13 14:39:34

## Summary

| Check | Status |
|---|---|
| shellcheck  install.sh | ✅ PASS |
| jsonlint  calc_anniv_web/package.json | ✅ PASS |
| hadolint  (tmp/Dockerfile not found) | ⏭ SKIP |
| markdownlint-cli2  (tmp/README.md not found) | ⏭ SKIP |
| eslint  calc_anniv_web/server.js  calc_anniv_web/public/app.js | ✅ PASS |
| htmlhint  HTML files | ✅ PASS |
| stylelint  CSS files | ❌ FAIL |
| yamllint  (no *.yaml / *.yml files found) | ⏭ SKIP |
| pylint  calc-anniv.py | ✅ PASS |
| pytest  tests/ | ✅ PASS |
| bandit  calc-anniv.py | ✅ PASS |
| semgrep  calc-anniv.py + JS sources | ✅ PASS |
| checkov  (tmp/Dockerfile not found) | ⏭ SKIP |
| trivy  HIGH/CRITICAL CVEs | ✅ PASS |
| gitleaks  secrets in repo | ✅ PASS |
| detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline) | ⏭ SKIP |
| **Total** | PASS: 10 · FAIL: 1 · SKIP: 5 |

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

## HTML

### `htmlhint  HTML files`

**Status:** ✅ PASS

```

Scanned 1 files, no errors found (12 ms).
```

---

## CSS

### `stylelint  CSS files`

**Status:** ❌ FAIL (exit 78)

```
ConfigurationError: No configuration provided for /work/calc_anniv_web/public/style.css
    at getConfigForFile (file:///usr/lib/node_modules/stylelint/lib/getConfigForFile.mjs:80:9)
    at async isPathIgnored (file:///usr/lib/node_modules/stylelint/lib/isPathIgnored.mjs:23:17)
    at async lintSource (file:///usr/lib/node_modules/stylelint/lib/lintSource.mjs:48:20)
    at async file:///usr/lib/node_modules/stylelint/lib/standalone.mjs:262:27
    at async Promise.all (index 0)
    at async standalone (file:///usr/lib/node_modules/stylelint/lib/standalone.mjs:310:22)
```

---

## YAML

### `yamllint  (no *.yaml / *.yml files found)`

**Status:** ⏭ SKIP

---

## Python

### `pylint  calc-anniv.py`

**Status:** ✅ PASS

```

------------------------------------
Your code has been rated at 10.00/10
```

---

### `pytest  tests/`

**Status:** ✅ PASS

```
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-8.3.5, pluggy-1.7.0
rootdir: /work
configfile: pyproject.toml
plugins: platformdirs-4.14.5, anyio-4.16.0
collected 28 items

tests/test_calc_anniv.py ............................                    [100%]

============================== 28 passed in 0.41s ==============================
```

---

### `bandit  calc-anniv.py`

**Status:** ✅ PASS

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.14.4
[manager]	ERROR	Exception occurred when executing tests against ./calc-anniv.py.
[manager]	ERROR	Run "bandit --debug ./calc-anniv.py" to see the full traceback.
Run started:2026-11-13 13:39:21.800168

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 417
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	./calc-anniv.py (exception while scanning file)
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
2026-11-13T13:39:26Z	INFO	[vulndb] Need to update DB
2026-11-13T13:39:26Z	INFO	[vulndb] Downloading vulnerability DB...
2026-11-13T13:39:26Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
18.62 MiB / 133.77 MiB [-------->___________________________________________________] 13.92% ? p/s ?55.92 MiB / 133.77 MiB [------------------------->__________________________________] 41.80% ? p/s ?88.72 MiB / 133.77 MiB [--------------------------------------->____________________] 66.32% ? p/s ?127.56 MiB / 133.77 MiB [------------------------------------------>__] 95.36% 181.82 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 181.82 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 181.82 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 170.75 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 170.75 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 170.75 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 159.74 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 159.74 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 159.74 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 149.43 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 149.43 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 149.43 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 139.79 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 139.79 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 139.79 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 130.77 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 130.77 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 130.77 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 122.34 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 122.34 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 122.34 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 114.44 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [------------------------------------------->] 100.00% 114.44 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [-----------------------------------------------] 100.00% 26.37 MiB p/s 5.3s2026-11-13T13:39:32Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-11-13T13:39:32Z	INFO	[vuln] Vulnerability scanning is enabled
2026-11-13T13:39:32Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-11-13T13:39:32Z	INFO	Number of language-specific files	num=1
2026-11-13T13:39:32Z	INFO	[npm] Detecting vulnerabilities...

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

[90m1:39PM[0m [32mINF[0m [1m36 commits scanned.[0m
[90m1:39PM[0m [32mINF[0m [1mscanned ~195764 bytes (195.76 KB) in 237ms[0m
[90m1:39PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

