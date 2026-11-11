# CLAUDE.md

Guidance for working in this repo.

## What this is

A birthday/anniversary calculator with two layers:

- **`calc-anniv.py`** — the whole business logic. A self-contained Python 3.10+ CLI (no external deps) that, given a birth date, computes age, next birthday, and — optionally — death-related or future-reference info. It can print a human-readable French report or, with `--json`, emit a single JSON object on stdout.
- **`calc_anniv_web/`** — a thin Node.js + Express front end. `server.js` validates query params and shells out to `calc-anniv.py --json` via `execFile`, returning its JSON. The browser UI is vanilla HTML/CSS/JS in `public/`.

The Python script is the source of truth for all calculations. The web layer adds no logic beyond input validation — it only invokes the script and relays its output.

**Language note:** all user-facing strings, docstrings, comments, and commit messages are in French. Keep that convention when editing.

## Layout

```
calc-anniv.py              CLI + all calculation logic
tests/test_calc_anniv.py   pytest suite (loads calc-anniv.py via importlib — name has a hyphen)
pyproject.toml             pytest config (testpaths = ["tests"])
.pylintrc                  disables C0103 (hyphen module name) + C0301 (line length)
checks.sh                  runs all linters/scanners in Docker → writes checks-report.md
install.sh                 root install to /opt (systemd + nginx); run on the server
calc_anniv_web/
  server.js                Express app, GET /api/calc
  public/                  index.html, app.js, style.css
  deploy/                  systemd unit + nginx location snippet
  .nvmrc                   Node 20.20.2
```

## Commands

Python:
```bash
pytest tests/ -v            # run tests
pylint calc-anniv.py        # must score 10.00/10
python calc-anniv.py --date 14-10-1938            # smoke test
python calc-anniv.py --json --date 14-10-1938     # JSON output
```

Web (from `calc_anniv_web/`):
```bash
npm install
npm start                   # serves on http://localhost:6001/
npm run lint                # eslint server.js public/app.js
```

Full quality gate (needs Docker — pulls an internal SAP linter image):
```bash
bash checks.sh              # pylint, pytest, eslint, semgrep, trivy, gitleaks, … → checks-report.md
```

## Modes & contracts

`calc-anniv.py` has exactly four result modes, keyed by flags:

| Flags | `mode` in JSON |
|---|---|
| `--date` only | `vivant` |
| `--date --deces JJ-MM-AAAA` | `deces` |
| `--date --deces AAAA` | `deces_annee` |
| `--date --futur JJ-MM-AAAA` | `futur` |
| `--date --futur AAAA` | `futur_annee` |

`--deces` and `--futur` are mutually exclusive (enforced in the web layer; the CLI prefers `--deces` if both are passed). Date format is always `JJ-MM-AAAA` (day-month-year), or a bare 4-digit year where allowed.

JSON contract: `{ "naissance": "AAAA-MM-JJ", "mode": ..., "data": {...} }` on stdout, exit 0. On any error, a message goes to **stderr** and the process exits non-zero — `--json` must never write help text or anything else to stdout. The web layer and the CLI-exit-code tests depend on this split.

For each display function (`affiche_section_*`) there is a parallel JSON builder (`data_*`). When you change one, keep the other in sync.

## Conventions & gotchas

- **Feb 29 births** fall back to Mar 1 in non-leap years (`prochain_anniversaire`, `anniversaire_annee`). Flagged in output via `note_bissextile_*`. Tests lock this in.
- **Year-only modes** (`deces_annee`, `futur_annee`) express age as a before/after range since the exact day is unknown; death-anniversary dates are approximate.
- The hyphen in `calc-anniv.py` means it can't be imported normally — tests load it with `importlib.util`. `.pylintrc` disables the resulting name warning.
- `main()` carries `# pylint: disable=too-many-branches,too-many-statements` by design; pylint must stay at 10.00.
- Server reads `PORT` and `PYTHON` from env or `calc_anniv_web/.env` (never committed; copy from `.env.example`). `install.sh` never overwrites an existing `.env`.
- Deployment reverse-proxies the app under `/calc-anniv/` via nginx; the Express app itself serves from `/`.

## When you change calculation logic

1. Update both the `affiche_section_*` and matching `data_*` function.
2. Add/adjust tests in `tests/test_calc_anniv.py` (helpers, data builders, and CLI exit codes are all covered).
3. Run `pytest tests/ -v` and `pylint calc-anniv.py` (expect 10.00/10).
4. If the JSON shape changed, check `calc_anniv_web/public/app.js` renders the new fields.
