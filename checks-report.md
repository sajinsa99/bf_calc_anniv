# Checks Report — bf_calc_anniv — 2026-11-13 16:28:58

## Summary

| Check | Status |
|---|---|
| shellcheck  install.sh | ✅ PASS |
| jsonlint  calc_anniv_web/package.json | ✅ PASS |
| hadolint  (tmp/Dockerfile not found) | ⏭ SKIP |
| markdownlint-cli2  (tmp/README.md not found) | ⏭ SKIP |
| eslint  calc_anniv_web/server.js  calc_anniv_web/public/app.js | ✅ PASS |
| htmlhint  HTML files | ✅ PASS |
| stylelint  CSS files | ✅ PASS |
| yamllint  (no *.yaml / *.yml files found) | ⏭ SKIP |
| pylint  calc-anniv.py | ✅ PASS |
| pytest  tests/ | ✅ PASS |
| bandit  calc-anniv.py | ✅ PASS |
| semgrep  calc-anniv.py + JS sources | ✅ PASS |
| checkov  (tmp/Dockerfile not found) | ⏭ SKIP |
| trivy  HIGH/CRITICAL CVEs | ✅ PASS |
| gitleaks  secrets in repo | ✅ PASS |
| detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline) | ⏭ SKIP |
| **Total** | PASS: 11 · FAIL: 0 · SKIP: 5 |

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

Scanned 1 files, no errors found (13 ms).
```

---

## CSS

### `stylelint  CSS files`

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
Run started:2026-11-13 15:28:31.507703

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
2026-11-13T15:28:36Z	INFO	[vulndb] Need to update DB
2026-11-13T15:28:36Z	INFO	[vulndb] Downloading vulnerability DB...
2026-11-13T15:28:36Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
1.09 MiB / 133.77 MiB [>_____________________________________________________________] 0.82% ? p/s ?2.55 MiB / 133.77 MiB [->____________________________________________________________] 1.90% ? p/s ?4.00 MiB / 133.77 MiB [->____________________________________________________________] 2.99% ? p/s ?5.45 MiB / 133.77 MiB [->_______________________________________________] 4.08% 7.27 MiB p/s ETA 17s7.02 MiB / 133.77 MiB [-->______________________________________________] 5.24% 7.27 MiB p/s ETA 17s8.58 MiB / 133.77 MiB [--->_____________________________________________] 6.41% 7.27 MiB p/s ETA 17s10.09 MiB / 133.77 MiB [--->____________________________________________] 7.55% 7.30 MiB p/s ETA 16s11.55 MiB / 133.77 MiB [---->___________________________________________] 8.63% 7.30 MiB p/s ETA 16s13.17 MiB / 133.77 MiB [---->___________________________________________] 9.85% 7.30 MiB p/s ETA 16s14.75 MiB / 133.77 MiB [----->_________________________________________] 11.03% 7.33 MiB p/s ETA 16s16.34 MiB / 133.77 MiB [----->_________________________________________] 12.22% 7.33 MiB p/s ETA 16s17.91 MiB / 133.77 MiB [------>________________________________________] 13.39% 7.33 MiB p/s ETA 15s19.36 MiB / 133.77 MiB [------>________________________________________] 14.47% 7.35 MiB p/s ETA 15s20.72 MiB / 133.77 MiB [------->_______________________________________] 15.49% 7.35 MiB p/s ETA 15s21.99 MiB / 133.77 MiB [------->_______________________________________] 16.44% 7.35 MiB p/s ETA 15s23.24 MiB / 133.77 MiB [-------->______________________________________] 17.37% 7.30 MiB p/s ETA 15s24.24 MiB / 133.77 MiB [-------->______________________________________] 18.12% 7.30 MiB p/s ETA 15s25.23 MiB / 133.77 MiB [-------->______________________________________] 18.86% 7.30 MiB p/s ETA 14s26.12 MiB / 133.77 MiB [--------->_____________________________________] 19.52% 7.14 MiB p/s ETA 15s26.93 MiB / 133.77 MiB [--------->_____________________________________] 20.13% 7.14 MiB p/s ETA 14s27.73 MiB / 133.77 MiB [--------->_____________________________________] 20.73% 7.14 MiB p/s ETA 14s28.54 MiB / 133.77 MiB [---------->____________________________________] 21.33% 6.94 MiB p/s ETA 15s29.35 MiB / 133.77 MiB [---------->____________________________________] 21.94% 6.94 MiB p/s ETA 15s30.13 MiB / 133.77 MiB [---------->____________________________________] 22.53% 6.94 MiB p/s ETA 14s30.97 MiB / 133.77 MiB [---------->____________________________________] 23.15% 6.75 MiB p/s ETA 15s31.73 MiB / 133.77 MiB [----------->___________________________________] 23.72% 6.75 MiB p/s ETA 15s32.44 MiB / 133.77 MiB [----------->___________________________________] 24.25% 6.75 MiB p/s ETA 15s33.01 MiB / 133.77 MiB [----------->___________________________________] 24.68% 6.53 MiB p/s ETA 15s33.60 MiB / 133.77 MiB [----------->___________________________________] 25.12% 6.53 MiB p/s ETA 15s34.16 MiB / 133.77 MiB [------------>__________________________________] 25.54% 6.53 MiB p/s ETA 15s34.71 MiB / 133.77 MiB [------------>__________________________________] 25.95% 6.29 MiB p/s ETA 15s35.51 MiB / 133.77 MiB [------------>__________________________________] 26.55% 6.29 MiB p/s ETA 15s37.97 MiB / 133.77 MiB [------------->_________________________________] 28.38% 6.29 MiB p/s ETA 15s40.84 MiB / 133.77 MiB [-------------->________________________________] 30.53% 6.55 MiB p/s ETA 14s43.51 MiB / 133.77 MiB [--------------->_______________________________] 32.53% 6.55 MiB p/s ETA 13s46.25 MiB / 133.77 MiB [---------------->______________________________] 34.57% 6.55 MiB p/s ETA 13s48.86 MiB / 133.77 MiB [----------------->_____________________________] 36.52% 6.99 MiB p/s ETA 12s51.53 MiB / 133.77 MiB [------------------>____________________________] 38.52% 6.99 MiB p/s ETA 11s54.08 MiB / 133.77 MiB [------------------>____________________________] 40.42% 6.99 MiB p/s ETA 11s56.61 MiB / 133.77 MiB [------------------->___________________________] 42.32% 7.37 MiB p/s ETA 10s58.25 MiB / 133.77 MiB [-------------------->__________________________] 43.54% 7.37 MiB p/s ETA 10s60.06 MiB / 133.77 MiB [--------------------->_________________________] 44.90% 7.37 MiB p/s ETA 10s62.64 MiB / 133.77 MiB [---------------------->_________________________] 46.82% 7.54 MiB p/s ETA 9s65.17 MiB / 133.77 MiB [----------------------->________________________] 48.72% 7.54 MiB p/s ETA 9s67.89 MiB / 133.77 MiB [------------------------>_______________________] 50.75% 7.54 MiB p/s ETA 8s70.51 MiB / 133.77 MiB [------------------------->______________________] 52.71% 7.90 MiB p/s ETA 8s73.29 MiB / 133.77 MiB [-------------------------->_____________________] 54.79% 7.90 MiB p/s ETA 7s75.89 MiB / 133.77 MiB [--------------------------->____________________] 56.73% 7.90 MiB p/s ETA 7s78.59 MiB / 133.77 MiB [---------------------------->___________________] 58.75% 8.26 MiB p/s ETA 6s81.46 MiB / 133.77 MiB [----------------------------->__________________] 60.90% 8.26 MiB p/s ETA 6s83.89 MiB / 133.77 MiB [------------------------------>_________________] 62.71% 8.26 MiB p/s ETA 6s86.51 MiB / 133.77 MiB [------------------------------->________________] 64.67% 8.58 MiB p/s ETA 5s88.83 MiB / 133.77 MiB [------------------------------->________________] 66.40% 8.58 MiB p/s ETA 5s91.53 MiB / 133.77 MiB [-------------------------------->_______________] 68.42% 8.58 MiB p/s ETA 4s94.08 MiB / 133.77 MiB [--------------------------------->______________] 70.33% 8.84 MiB p/s ETA 4s96.47 MiB / 133.77 MiB [---------------------------------->_____________] 72.11% 8.84 MiB p/s ETA 4s98.97 MiB / 133.77 MiB [----------------------------------->____________] 73.98% 8.84 MiB p/s ETA 3s101.50 MiB / 133.77 MiB [----------------------------------->___________] 75.87% 9.07 MiB p/s ETA 3s104.03 MiB / 133.77 MiB [------------------------------------>__________] 77.77% 9.07 MiB p/s ETA 3s106.55 MiB / 133.77 MiB [------------------------------------->_________] 79.65% 9.07 MiB p/s ETA 3s109.00 MiB / 133.77 MiB [-------------------------------------->________] 81.48% 9.29 MiB p/s ETA 2s111.45 MiB / 133.77 MiB [--------------------------------------->_______] 83.32% 9.29 MiB p/s ETA 2s114.12 MiB / 133.77 MiB [---------------------------------------->______] 85.31% 9.29 MiB p/s ETA 2s116.55 MiB / 133.77 MiB [---------------------------------------->______] 87.12% 9.50 MiB p/s ETA 1s118.95 MiB / 133.77 MiB [----------------------------------------->_____] 88.92% 9.50 MiB p/s ETA 1s121.48 MiB / 133.77 MiB [------------------------------------------>____] 90.81% 9.50 MiB p/s ETA 1s123.12 MiB / 133.77 MiB [------------------------------------------->___] 92.04% 9.60 MiB p/s ETA 1s124.51 MiB / 133.77 MiB [------------------------------------------->___] 93.08% 9.60 MiB p/s ETA 0s126.23 MiB / 133.77 MiB [-------------------------------------------->__] 94.36% 9.60 MiB p/s ETA 0s127.98 MiB / 133.77 MiB [-------------------------------------------->__] 95.67% 9.50 MiB p/s ETA 0s129.70 MiB / 133.77 MiB [--------------------------------------------->_] 96.96% 9.50 MiB p/s ETA 0s131.92 MiB / 133.77 MiB [---------------------------------------------->] 98.62% 9.50 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 9.51 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 9.51 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 9.51 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.90 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.90 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.90 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.32 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.32 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 8.32 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.78 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.78 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.78 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.28 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.28 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 7.28 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.81 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.81 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.81 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.37 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.37 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 6.37 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 5.96 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [--------------------------------------------->] 100.00% 5.96 MiB p/s ETA 0s133.77 MiB / 133.77 MiB [-------------------------------------------------] 100.00% 7.11 MiB p/s 19s2026-11-13T15:28:55Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-11-13T15:28:55Z	INFO	[vuln] Vulnerability scanning is enabled
2026-11-13T15:28:55Z	INFO	Suppressing dependencies for development and testing. To display them, try the '--include-dev-deps' flag.
2026-11-13T15:28:55Z	INFO	Number of language-specific files	num=1
2026-11-13T15:28:55Z	INFO	[npm] Detecting vulnerabilities...

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

[90m3:28PM[0m [32mINF[0m [1m38 commits scanned.[0m
[90m3:28PM[0m [32mINF[0m [1mscanned ~201855 bytes (201.85 KB) in 233ms[0m
[90m3:28PM[0m [32mINF[0m [1mno leaks found[0m
```

---

### `detect-secrets  (run: detect-secrets scan > .secrets.baseline  to create baseline)`

**Status:** ⏭ SKIP

---

