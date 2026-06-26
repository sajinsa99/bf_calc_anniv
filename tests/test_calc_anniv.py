"""Tests for calc-anniv.py helpers and data builders."""

import importlib.util
import sys
import subprocess
from datetime import date
from pathlib import Path

# Load calc-anniv.py as a module despite the hyphen in its name
_spec = importlib.util.spec_from_file_location(
    "calc_anniv",
    Path(__file__).parent.parent / "calc-anniv.py",
)
calc_anniv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(calc_anniv)

age_a_la_date = calc_anniv.age_a_la_date
prochain_anniversaire = calc_anniv.prochain_anniversaire
anniversaire_annee = calc_anniv.anniversaire_annee
nb_anniversaires_entre = calc_anniv.nb_anniversaires_entre
note_bissextile_str = calc_anniv.note_bissextile_str
note_bissextile_flag = calc_anniv.note_bissextile_flag
data_vivant = calc_anniv.data_vivant
data_deces_complet = calc_anniv.data_deces_complet
data_deces_annee = calc_anniv.data_deces_annee
data_futur_complet = calc_anniv.data_futur_complet
data_futur_annee = calc_anniv.data_futur_annee

CALC_PY = str(Path(__file__).parent.parent / "calc-anniv.py")


# ── age_a_la_date ─────────────────────────────────────────────────────────────

def test_age_veille_anniv():
    naissance = date(1990, 6, 15)
    veille = date(2026, 6, 14)
    assert age_a_la_date(naissance, veille) == 35


def test_age_jour_anniv():
    naissance = date(1990, 6, 15)
    jour = date(2026, 6, 15)
    assert age_a_la_date(naissance, jour) == 36


def test_age_lendemain_anniv():
    naissance = date(1990, 6, 15)
    lendemain = date(2026, 6, 16)
    assert age_a_la_date(naissance, lendemain) == 36


def test_age_zero_jour_naissance():
    naissance = date(2000, 1, 1)
    assert age_a_la_date(naissance, naissance) == 0


# ── prochain_anniversaire ─────────────────────────────────────────────────────

def test_prochain_anniv_normal():
    naissance = date(1990, 10, 14)
    depuis = date(2026, 1, 1)
    prochain, jours = prochain_anniversaire(naissance, depuis)
    assert prochain == date(2026, 10, 14)
    assert jours == (date(2026, 10, 14) - depuis).days


def test_prochain_anniv_apres_anniv_courant():
    naissance = date(1990, 3, 1)
    depuis = date(2026, 4, 1)  # après l'anniv 2026
    prochain, jours = prochain_anniversaire(naissance, depuis)
    assert prochain == date(2027, 3, 1)


def test_prochain_anniv_29_fev_annee_non_biss():
    naissance = date(2000, 2, 29)
    depuis = date(2026, 1, 1)  # 2026 not leap
    prochain, jours = prochain_anniversaire(naissance, depuis)
    assert prochain == date(2026, 3, 1)


def test_prochain_anniv_29_fev_annee_biss():
    naissance = date(2000, 2, 29)
    depuis = date(2028, 1, 1)  # 2028 is leap
    prochain, jours = prochain_anniversaire(naissance, depuis)
    assert prochain == date(2028, 2, 29)


# ── nb_anniversaires_entre ────────────────────────────────────────────────────

def test_nb_anniv_entre_deces_avant_anniv():
    # naissance 14-10-1938, décès 02-04-2024 (avant l'anniv 2024)
    # today 26-06-2026 (avant l'anniv 2026 : Oct pas encore passé)
    # annivs passés après le décès : Oct 2024, Oct 2025 → 2
    naissance = date(1938, 10, 14)
    deces = date(2024, 4, 2)
    today = date(2026, 6, 26)
    assert nb_anniversaires_entre(naissance, deces, today) == 2


def test_nb_anniv_entre_deces_apres_anniv():
    # naissance 14-10-1938, décès 20-11-2024 (après l'anniv 2024)
    # today 26-06-2026 (avant l'anniv 2026)
    # 2025 a eu lieu, 2026 pas encore → 1
    naissance = date(1938, 10, 14)
    deces = date(2024, 11, 20)
    today = date(2026, 6, 26)
    assert nb_anniversaires_entre(naissance, deces, today) == 1


def test_nb_anniv_entre_zero():
    # Décès 10-12-2025, today 01-01-2026 (l'anniv 2026 n'a pas encore eu lieu)
    naissance = date(1980, 3, 15)
    deces = date(2025, 12, 10)
    today = date(2026, 1, 1)
    assert nb_anniversaires_entre(naissance, deces, today) == 0


# ── note_bissextile ───────────────────────────────────────────────────────────

def test_note_biss_str_vrai():
    naissance = date(2000, 2, 29)
    anniv = date(2026, 3, 1)
    assert "01/03" in note_bissextile_str(naissance, anniv)


def test_note_biss_str_faux():
    naissance = date(1990, 6, 15)
    anniv = date(2026, 6, 15)
    assert note_bissextile_str(naissance, anniv) == ""


def test_note_biss_flag_vrai():
    assert note_bissextile_flag(date(2000, 2, 29), date(2026, 3, 1)) is True


def test_note_biss_flag_faux():
    assert note_bissextile_flag(date(1990, 6, 15), date(2026, 6, 15)) is False


# ── data_deces_complet ────────────────────────────────────────────────────────

def test_data_deces_deces_avant_anniv():
    naissance = date(1938, 10, 14)
    deces = date(2024, 4, 2)
    today = date(2026, 6, 26)
    d = data_deces_complet(naissance, deces, today)
    assert d["age_deces"] == 85
    assert d["nb_anniv_depuis_deces"] == 2  # Oct 2024 et Oct 2025 passés, Oct 2026 pas encore


def test_data_deces_deces_apres_anniv():
    naissance = date(1938, 10, 14)
    deces = date(2024, 11, 20)
    today = date(2026, 6, 26)
    d = data_deces_complet(naissance, deces, today)
    assert d["age_deces"] == 86
    assert d["nb_anniv_depuis_deces"] == 1


def test_data_deces_today_avant_anniv():
    naissance = date(1980, 10, 14)
    deces = date(2020, 4, 2)
    today = date(2026, 3, 1)  # avant l'anniv 2026
    d = data_deces_complet(naissance, deces, today)
    # annivs post-deces : 2020(oct), 2021, 2022, 2023, 2024, 2025 → 6 (2026 pas encore passé)
    assert d["nb_anniv_depuis_deces"] == 6


# ── data_deces_annee ──────────────────────────────────────────────────────────

def test_data_deces_annee_age_clamp():
    # année décès == année naissance → age_avant doit être 0, pas -1
    naissance = date(2000, 6, 15)
    today = date(2026, 6, 26)
    d = data_deces_annee(naissance, 2000, today)
    assert d["age_deces_avant"] == 0
    assert d["age_deces_apres"] == 0


def test_data_deces_annee_nb_approx():
    naissance = date(1938, 10, 14)
    today = date(2026, 6, 26)
    d = data_deces_annee(naissance, 2024, today)
    assert "nb_anniv_depuis_deces_approx" in d
    assert d["nb_anniv_depuis_deces_approx_flag"] is True
    assert d["nb_anniv_depuis_deces_approx"] >= 0


# ── data_futur_annee ──────────────────────────────────────────────────────────

def test_data_futur_annee_age_clamp():
    # année futur == année naissance → age_avant doit être 0
    naissance = date(2000, 6, 15)
    today = date(2026, 6, 26)
    d = data_futur_annee(naissance, 2000, today)
    assert d["age_avant"] == 0
    assert d["age_apres"] == 0


# ── CLI exit codes ────────────────────────────────────────────────────────────

def _run(*args):
    return subprocess.run(
        [sys.executable, CALC_PY, *args],
        capture_output=True, text=True
    )


def test_cli_date_invalide_exit1():
    r = _run("--date", "99-99-9999")
    assert r.returncode != 0


def test_cli_date_future_exit1():
    r = _run("--date", "01-01-2099")
    assert r.returncode != 0


def test_cli_futur_dans_le_passe_exit1():
    r = _run("--date", "14-10-1938", "--futur", "01-01-2020")
    assert r.returncode != 0


def test_cli_json_sans_date_pas_de_stdout():
    r = _run("--json")
    assert r.returncode != 0
    # stdout ne doit pas contenir de texte d'aide (pollution)
    assert "usage" not in r.stdout.lower()
    assert r.stdout.strip() == ""


def test_cli_json_valide():
    import json as _json
    r = _run("--json", "--date", "14-10-1938")
    assert r.returncode == 0
    data = _json.loads(r.stdout)
    assert data["mode"] == "vivant"
    assert "age_actuel" in data["data"]


def test_cli_json_deces():
    import json as _json
    r = _run("--json", "--date", "14-10-1938", "--deces", "02-04-2024")
    assert r.returncode == 0
    data = _json.loads(r.stdout)
    assert data["mode"] == "deces"
    assert data["data"]["age_deces"] == 85


def test_cli_json_deces_annee():
    import json as _json
    r = _run("--json", "--date", "14-10-1938", "--deces", "2024")
    assert r.returncode == 0
    data = _json.loads(r.stdout)
    assert data["mode"] == "deces_annee"
    assert "nb_anniv_depuis_deces_approx" in data["data"]
