#!/usr/bin/env python3
"""
calc-anniv.py — Calcule les informations d'anniversaire à partir d'une date de naissance.

Usage :
  python calc-anniv.py --date JJ-MM-AAAA
  python calc-anniv.py --date JJ-MM-AAAA --deces JJ-MM-AAAA
  python calc-anniv.py --date JJ-MM-AAAA --deces AAAA
  python calc-anniv.py --date JJ-MM-AAAA --futur JJ-MM-AAAA
  python calc-anniv.py --date JJ-MM-AAAA --futur AAAA
  python calc-anniv.py --json --date JJ-MM-AAAA [--deces ...] [--futur ...]
"""

import argparse
import json
import sys
from datetime import date


# ──────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────

def parse_date(date_str: str) -> date:
    """Parse une date complète au format JJ-MM-AAAA."""
    try:
        parties = date_str.split("-")
        if len(parties) != 3:
            raise ValueError
        jour, mois, annee = parties
        return date(int(annee), int(mois), int(jour))
    except (ValueError, TypeError):
        print(f"❌ Format de date invalide : « {date_str} »", file=sys.stderr)
        print("   Format attendu : JJ-MM-AAAA  (ex: 14-10-1938)", file=sys.stderr)
        sys.exit(1)


def parse_date_ou_annee(s: str, label: str) -> tuple[date | None, int | None, bool]:
    """
    Parse une valeur acceptant soit JJ-MM-AAAA soit AAAA.
    label est utilisé dans les messages d'erreur (ex: « décès », « future »).
    Retourne (date_complete, annee_seule, est_annee_seule).
    """
    parties = s.split("-")

    if len(parties) == 1 and parties[0].isdigit() and len(parties[0]) == 4:
        return None, int(parties[0]), True

    try:
        if len(parties) != 3:
            raise ValueError
        jour, mois, annee = parties
        return date(int(annee), int(mois), int(jour)), None, False
    except (ValueError, TypeError):
        print(f"❌ Format de date {label} invalide : « {s} »", file=sys.stderr)
        print(f"   Formats attendus : JJ-MM-AAAA  ou  AAAA  (ex: 02-04-2024 ou 2024)", file=sys.stderr)
        sys.exit(1)


def parse_deces(deces_str: str) -> tuple[date | None, int | None, bool]:
    return parse_date_ou_annee(deces_str, "de décès")


def parse_futur(futur_str: str) -> tuple[date | None, int | None, bool]:
    return parse_date_ou_annee(futur_str, "future")


# ──────────────────────────────────────────────
# Calculs
# ──────────────────────────────────────────────

def age_a_la_date(naissance: date, reference: date) -> int:
    """Calcule l'âge en années entières à une date de référence donnée."""
    return (
        reference.year
        - naissance.year
        - ((reference.month, reference.day) < (naissance.month, naissance.day))
    )


def prochain_anniversaire(reference: date, depuis: date) -> tuple[date, int]:
    """Prochain occurrence annuelle d'une date (naissance ou décès) à partir d'une date de référence."""
    try:
        prochain = reference.replace(year=depuis.year)
    except ValueError:
        prochain = date(depuis.year, 3, 1)

    if prochain < depuis:
        try:
            prochain = reference.replace(year=depuis.year + 1)
        except ValueError:
            prochain = date(depuis.year + 1, 3, 1)

    return prochain, (prochain - depuis).days


def anniversaire_annee(naissance: date, annee: int) -> date | None:
    """Retourne la date d'anniversaire dans une année donnée (None si impossible)."""
    try:
        return naissance.replace(year=annee)
    except ValueError:
        # 29 fév sur année non bissextile
        return date(annee, 3, 1)


def nb_anniversaires_entre(naissance: date, deces: date, today: date) -> int:
    """
    Nombre d'anniversaires de naissance survenus entre le décès (exclu) et today (exclu).
    Compte uniquement les anniversaires réellement passés après le décès.
    """
    nb = today.year - deces.year
    # Si l'anniversaire de cette année n'est pas encore passé, ne pas le compter
    if (today.month, today.day) < (naissance.month, naissance.day):
        nb -= 1
    # Si l'anniversaire de l'année du décès n'avait pas encore eu lieu au moment du décès,
    # il ne doit pas être décompté (il aurait eu lieu après le décès)
    if (deces.month, deces.day) < (naissance.month, naissance.day):
        nb += 1
    return max(nb, 0)


def note_bissextile_str(naissance: date, anniv: date) -> str:
    """Retourne la note bissextile textuelle ou chaîne vide."""
    if naissance.month == 2 and naissance.day == 29 and anniv.month == 3:
        return " (→ 01/03, année non bissextile)"
    return ""


def note_bissextile_flag(naissance: date, anniv: date) -> bool:
    return naissance.month == 2 and naissance.day == 29 and anniv.month == 3


# ──────────────────────────────────────────────
# Affichage
# ──────────────────────────────────────────────

def jour_semaine_fr(d: date) -> str:
    """Retourne le nom du jour de la semaine en français."""
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    return jours[d.weekday()]


def fmt_date(d: date) -> str:
    """Formate une date en JJ/MM/AAAA (jour de la semaine)."""
    return f"{d.strftime('%d/%m/%Y')} ({jour_semaine_fr(d)})"


def affiche_section_vivant(naissance: date, aujourd_hui: date):
    """Affiche les infos d'anniversaire pour une personne encore en vie."""
    age_actuel = age_a_la_date(naissance, aujourd_hui)
    est_anniv = (aujourd_hui.month == naissance.month and aujourd_hui.day == naissance.day)
    prochain, jours_restants = prochain_anniversaire(naissance, aujourd_hui)
    age_prochain = age_actuel + (0 if est_anniv else 1)

    print(f"  Âge actuel        : {age_actuel} ans")
    if est_anniv:
        print()
        print(f"  🎉 Joyeux anniversaire ! C'est aujourd'hui ({age_actuel} ans) !")
    else:
        print()
        print(f"  Prochain anniversaire : {fmt_date(prochain)}")
        print(f"  Dans                  : {jours_restants} jour{'s' if jours_restants > 1 else ''}")
        print(f"  Âge atteint           : {age_prochain} ans")


def affiche_section_deces_complet(naissance: date, deces: date, aujourd_hui: date):
    """Section décès avec date complète."""
    age_deces = age_a_la_date(naissance, deces)
    age_aurait = age_a_la_date(naissance, aujourd_hui)

    anniv_annee_deces = anniversaire_annee(naissance, deces.year)
    note_biss = note_bissextile_str(naissance, anniv_annee_deces)

    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    nb_anniv_depuis = nb_anniversaires_entre(naissance, deces, aujourd_hui)

    print(f"  Date du décès     : {fmt_date(deces)}")
    print(f"  Âge au décès      : {age_deces} ans")
    print(f"  Âge aujourd'hui   : {age_aurait} ans (si vivant·e)")
    print()
    print(f"  Anniversaire dans l'année du décès : {fmt_date(anniv_annee_deces)}{note_biss}")
    print()
    prochain_deces, jours_deces = prochain_anniversaire(deces, aujourd_hui)

    print(f"  Prochain anniversaire de naissance  : {fmt_date(anniv_depuis_deces)}")
    print(f"  Dans                                : {jours_prochain} jour{'s' if jours_prochain > 1 else ''}")
    if nb_anniv_depuis > 0:
        print(f"  Anniversaires écoulés depuis décès  : {nb_anniv_depuis}")
    print()
    print(f"  Prochain anniversaire du décès      : {fmt_date(prochain_deces)}")
    print(f"  Dans                                : {jours_deces} jour{'s' if jours_deces > 1 else ''}")


def affiche_section_futur_complet(naissance: date, futur: date, aujourd_hui: date):
    """Section date future avec date complète."""
    age_a_futur = age_a_la_date(naissance, futur)
    est_anniv = (futur.month == naissance.month and futur.day == naissance.day)

    print(f"  Date de référence : {fmt_date(futur)}")
    print(f"  Âge à cette date  : {age_a_futur} ans")
    print()
    prochain, jours_restants = prochain_anniversaire(naissance, futur)
    age_prochain = age_a_futur + (0 if est_anniv else 1)
    if est_anniv:
        print(f"  🎂 C'est jour d'anniversaire ! ({age_a_futur} ans)")
    else:
        print(f"  Prochain anniversaire : {fmt_date(prochain)}")
        print(f"  Dans                  : {jours_restants} jour{'s' if jours_restants > 1 else ''}")
        print(f"  Âge atteint           : {age_prochain} ans")


def affiche_section_futur_annee(naissance: date, annee_futur: int, aujourd_hui: date):
    """Section date future avec année seule."""
    anniv_cette_annee = anniversaire_annee(naissance, annee_futur)
    age_avant = max(annee_futur - naissance.year - 1, 0)
    age_apres = annee_futur - naissance.year
    note_biss = note_bissextile_str(naissance, anniv_cette_annee)

    print(f"  Année de référence   : {annee_futur}")
    print(f"  Âge dans cette année : {age_avant} ans (avant le {anniv_cette_annee.strftime('%d/%m')})"
          f" ou {age_apres} ans (après){note_biss}")
    print()
    print(f"  Anniversaire dans cette année : {fmt_date(anniv_cette_annee)}{note_biss}")


def affiche_section_deces_annee(naissance: date, annee_deces: int, aujourd_hui: date):
    """Section décès avec année seule."""
    anniv_cette_annee = anniversaire_annee(naissance, annee_deces)
    age_avant = max(annee_deces - naissance.year - 1, 0)
    age_apres = annee_deces - naissance.year
    note_biss = note_bissextile_str(naissance, anniv_cette_annee)

    print(f"  Année du décès    : {annee_deces}")
    print(f"  Âge au décès      : {age_avant} ans (avant le {anniv_cette_annee.strftime('%d/%m')})"
          f" ou {age_apres} ans (après){note_biss}")
    print(f"  Âge aujourd'hui   : {age_a_la_date(naissance, aujourd_hui)} ans (si vivant·e)")
    print()
    print(f"  Anniversaire dans l'année du décès : {fmt_date(anniv_cette_annee)}{note_biss}")
    print()

    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    print(f"  Prochain anniversaire de naissance  : {fmt_date(anniv_depuis_deces)}")
    print(f"  Dans                                : {jours_prochain} jour{'s' if jours_prochain > 1 else ''}")

    # Approximation du nombre d'anniversaires depuis le décès (pivote sur anniv de l'année du décès)
    deces_pivot = anniv_cette_annee  # date de l'anniversaire dans l'année du décès
    nb_approx = nb_anniversaires_entre(naissance, deces_pivot, aujourd_hui)
    if nb_approx > 0:
        print(f"  Anniversaires depuis le décès       : ≈ {nb_approx} (approx.)")
    print()

    anniv_deces_ref = date(annee_deces, 12, 31)
    prochain_deces, _ = prochain_anniversaire(anniv_deces_ref, aujourd_hui)
    print(f"  Prochain anniversaire du décès      : courant {prochain_deces.year} (date exacte inconnue)")
    print(f"  Dans                                : d'ici le {prochain_deces.strftime('%d/%m/%Y')}")


# ──────────────────────────────────────────────
# JSON data builders
# ──────────────────────────────────────────────

def _fmt_iso(d: date) -> str:
    return d.isoformat()


def data_vivant(naissance: date, aujourd_hui: date) -> dict:
    age_actuel = age_a_la_date(naissance, aujourd_hui)
    est_anniv = (aujourd_hui.month == naissance.month and aujourd_hui.day == naissance.day)
    prochain, jours_restants = prochain_anniversaire(naissance, aujourd_hui)
    age_prochain = age_actuel + (0 if est_anniv else 1)
    return {
        "age_actuel": age_actuel,
        "est_anniversaire": est_anniv,
        "prochain_anniversaire": _fmt_iso(prochain),
        "prochain_anniversaire_jours": jours_restants,
        "age_prochain": age_prochain,
    }


def data_deces_complet(naissance: date, deces: date, aujourd_hui: date) -> dict:
    age_deces = age_a_la_date(naissance, deces)
    age_aurait = age_a_la_date(naissance, aujourd_hui)
    anniv_annee_deces = anniversaire_annee(naissance, deces.year)
    note_biss = note_bissextile_flag(naissance, anniv_annee_deces)

    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    nb_anniv_depuis = nb_anniversaires_entre(naissance, deces, aujourd_hui)

    prochain_deces, jours_deces = prochain_anniversaire(deces, aujourd_hui)
    return {
        "date_deces": _fmt_iso(deces),
        "age_deces": age_deces,
        "age_aurait": age_aurait,
        "anniv_annee_deces": _fmt_iso(anniv_annee_deces),
        "anniv_annee_deces_note_bissextile": note_biss,
        "prochain_anniv_naissance": _fmt_iso(anniv_depuis_deces),
        "prochain_anniv_naissance_jours": jours_prochain,
        "nb_anniv_depuis_deces": nb_anniv_depuis,
        "prochain_anniv_deces": _fmt_iso(prochain_deces),
        "prochain_anniv_deces_jours": jours_deces,
    }


def data_deces_annee(naissance: date, annee_deces: int, aujourd_hui: date) -> dict:
    anniv_cette_annee = anniversaire_annee(naissance, annee_deces)
    age_avant = max(annee_deces - naissance.year - 1, 0)
    age_apres = annee_deces - naissance.year
    note_biss = note_bissextile_flag(naissance, anniv_cette_annee)
    age_aurait = age_a_la_date(naissance, aujourd_hui)
    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    anniv_deces_ref = date(annee_deces, 12, 31)
    prochain_deces, _ = prochain_anniversaire(anniv_deces_ref, aujourd_hui)

    # Approximation du nombre d'anniversaires depuis le décès (pivot sur l'anniv de l'année du décès)
    nb_approx = nb_anniversaires_entre(naissance, anniv_cette_annee, aujourd_hui)

    return {
        "annee_deces": annee_deces,
        "age_deces_avant": age_avant,
        "age_deces_apres": age_apres,
        "age_aurait": age_aurait,
        "anniv_annee_deces": _fmt_iso(anniv_cette_annee),
        "anniv_annee_deces_note_bissextile": note_biss,
        "prochain_anniv_naissance": _fmt_iso(anniv_depuis_deces),
        "prochain_anniv_naissance_jours": jours_prochain,
        "nb_anniv_depuis_deces_approx": nb_approx,
        "nb_anniv_depuis_deces_approx_flag": True,
        "prochain_anniv_deces_annee": prochain_deces.year,
    }


def data_futur_complet(naissance: date, futur: date, aujourd_hui: date) -> dict:
    age_a_futur = age_a_la_date(naissance, futur)
    est_anniv = (futur.month == naissance.month and futur.day == naissance.day)
    prochain, jours_restants = prochain_anniversaire(naissance, futur)
    age_prochain = age_a_futur + (0 if est_anniv else 1)
    return {
        "date_futur": _fmt_iso(futur),
        "age_a_futur": age_a_futur,
        "est_anniversaire": est_anniv,
        "prochain_anniversaire": _fmt_iso(prochain),
        "prochain_anniversaire_jours": jours_restants,
        "age_prochain": age_prochain,
    }


def data_futur_annee(naissance: date, annee_futur: int, aujourd_hui: date) -> dict:
    anniv_cette_annee = anniversaire_annee(naissance, annee_futur)
    age_avant = max(annee_futur - naissance.year - 1, 0)
    age_apres = annee_futur - naissance.year
    note_biss = note_bissextile_flag(naissance, anniv_cette_annee)
    return {
        "annee_futur": annee_futur,
        "age_avant": age_avant,
        "age_apres": age_apres,
        "anniv_cette_annee": _fmt_iso(anniv_cette_annee),
        "anniv_note_bissextile": note_biss,
    }


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    """Point d'entrée principal : parse les arguments et orchestre l'affichage."""
    parser = argparse.ArgumentParser(
        description="Calcule les informations d'anniversaire à partir d'une date de naissance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  %(prog)s --date 14-10-1938\n"
            "  %(prog)s --date 14-10-1938 --deces 02-04-2024\n"
            "  %(prog)s --date 14-10-1938 --deces 2024\n"
            "  %(prog)s --date 14-10-1938 --futur 25-12-2030\n"
            "  %(prog)s --date 14-10-1938 --futur 2030\n"
        ),
    )
    parser.add_argument(
        "--date",
        metavar="JJ-MM-AAAA",
        help="Date de naissance (ex: 14-10-1938)",
    )
    parser.add_argument(
        "--deces",
        metavar="JJ-MM-AAAA ou AAAA",
        help="Date de décès complète ou année seule (ex: 02-04-2024 ou 2024)",
    )
    parser.add_argument(
        "--futur",
        metavar="JJ-MM-AAAA ou AAAA",
        help="Date ou année future de référence (ex: 25-12-2030 ou 2030)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Sortie JSON sur stdout (erreurs sur stderr, exit ≠ 0)",
    )
    args = parser.parse_args()

    def err(msg: str):
        if args.json:
            print(msg, file=sys.stderr)
        else:
            print(msg)

    aujourd_hui = date.today()

    # --date obligatoire si --deces ou --futur fourni
    if (args.deces or args.futur) and not args.date:
        err("❌ --date est obligatoire quand --deces ou --futur est utilisé.")
        sys.exit(1)

    if not args.date:
        # En mode --json, ne pas polluer stdout avec print_help()
        if args.json:
            print("❌ --date est obligatoire.", file=sys.stderr)
        else:
            parser.print_help()
        sys.exit(1)

    naissance = parse_date(args.date)

    # Validation date de naissance
    if naissance > aujourd_hui:
        err(f"❌ La date de naissance « {args.date} » est dans le futur.")
        sys.exit(1)

    # ── Mode JSON ──
    if args.json:
        result = {"naissance": _fmt_iso(naissance)}

        if args.deces:
            deces_date, annee_deces, est_annee_seule = parse_deces(args.deces)
            if est_annee_seule:
                if annee_deces > aujourd_hui.year:
                    print(f"❌ L'année de décès « {annee_deces} » est dans le futur.", file=sys.stderr)
                    sys.exit(1)
                if annee_deces < naissance.year:
                    print(f"❌ L'année de décès « {annee_deces} » est antérieure à la naissance ({naissance.year}).", file=sys.stderr)
                    sys.exit(1)
                result["mode"] = "deces_annee"
                result["data"] = data_deces_annee(naissance, annee_deces, aujourd_hui)
            else:
                if deces_date > aujourd_hui:
                    print(f"❌ La date de décès « {args.deces} » est dans le futur.", file=sys.stderr)
                    sys.exit(1)
                if deces_date < naissance:
                    print("❌ La date de décès est antérieure à la date de naissance.", file=sys.stderr)
                    sys.exit(1)
                result["mode"] = "deces"
                result["data"] = data_deces_complet(naissance, deces_date, aujourd_hui)

        elif args.futur:
            futur_date, annee_futur, est_annee_seule = parse_futur(args.futur)
            if est_annee_seule:
                if annee_futur < naissance.year:
                    print(f"❌ L'année de référence « {annee_futur} » est antérieure à la naissance ({naissance.year}).", file=sys.stderr)
                    sys.exit(1)
                result["mode"] = "futur_annee"
                result["data"] = data_futur_annee(naissance, annee_futur, aujourd_hui)
            else:
                if futur_date < naissance:
                    print("❌ La date de référence est antérieure à la date de naissance.", file=sys.stderr)
                    sys.exit(1)
                if futur_date < aujourd_hui:
                    print(f"❌ La date future « {args.futur} » est dans le passé.", file=sys.stderr)
                    sys.exit(1)
                result["mode"] = "futur"
                result["data"] = data_futur_complet(naissance, futur_date, aujourd_hui)

        else:
            result["mode"] = "vivant"
            result["data"] = data_vivant(naissance, aujourd_hui)

        json.dump(result, sys.stdout, ensure_ascii=False)
        return

    # ── Affichage en-tête ──
    print()
    print("🎂  Informations d'anniversaire")
    print("─" * 44)
    print(f"  Date de naissance : {fmt_date(naissance)}")
    print()

    # ── Cas avec décès ──
    if args.deces:
        deces_date, annee_deces, est_annee_seule = parse_deces(args.deces)

        if est_annee_seule:
            if annee_deces > aujourd_hui.year:
                err(f"❌ L'année de décès « {annee_deces} » est dans le futur.")
                sys.exit(1)
            if annee_deces < naissance.year:
                err(f"❌ L'année de décès « {annee_deces} » est antérieure à la naissance ({naissance.year}).")
                sys.exit(1)
            affiche_section_deces_annee(naissance, annee_deces, aujourd_hui)

        else:
            if deces_date > aujourd_hui:
                err(f"❌ La date de décès « {args.deces} » est dans le futur.")
                sys.exit(1)
            if deces_date < naissance:
                err("❌ La date de décès est antérieure à la date de naissance.")
                sys.exit(1)
            affiche_section_deces_complet(naissance, deces_date, aujourd_hui)

    # ── Cas avec date future ──
    elif args.futur:
        futur_date, annee_futur, est_annee_seule = parse_futur(args.futur)

        if est_annee_seule:
            if annee_futur < naissance.year:
                err(f"❌ L'année de référence « {annee_futur} » est antérieure à la naissance ({naissance.year}).")
                sys.exit(1)
            affiche_section_futur_annee(naissance, annee_futur, aujourd_hui)

        else:
            if futur_date < naissance:
                err("❌ La date de référence est antérieure à la date de naissance.")
                sys.exit(1)
            if futur_date < aujourd_hui:
                err(f"❌ La date future « {args.futur} » est dans le passé.")
                sys.exit(1)
            affiche_section_futur_complet(naissance, futur_date, aujourd_hui)

    # ── Cas sans décès ──
    else:
        affiche_section_vivant(naissance, aujourd_hui)

    print()


if __name__ == "__main__":
    main()
