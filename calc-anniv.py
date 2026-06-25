#!/usr/bin/env python3
"""
calc-anniv.py — Calcule les informations d'anniversaire à partir d'une date de naissance.

Usage :
  python calc-anniv.py --date JJ-MM-AAAA
  python calc-anniv.py --date JJ-MM-AAAA --deces JJ-MM-AAAA
  python calc-anniv.py --date JJ-MM-AAAA --deces AAAA
"""

import argparse
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
        print(f"❌ Format de date invalide : « {date_str} »")
        print("   Format attendu : JJ-MM-AAAA  (ex: 14-10-1938)")
        sys.exit(1)


def parse_deces(deces_str: str) -> tuple[date | None, int | None, bool]:
    """
    Parse --deces, qui accepte :
      - JJ-MM-AAAA  → date complète
      - AAAA        → année seule

    Retourne (date_complete, annee_seule, est_annee_seule).
    """
    parties = deces_str.split("-")

    # Année seule ?
    if len(parties) == 1 and parties[0].isdigit() and len(parties[0]) == 4:
        return None, int(parties[0]), True

    # Date complète
    try:
        if len(parties) != 3:
            raise ValueError
        jour, mois, annee = parties
        return date(int(annee), int(mois), int(jour)), None, False
    except (ValueError, TypeError):
        print(f"❌ Format de décès invalide : « {deces_str} »")
        print("   Formats attendus : JJ-MM-AAAA  ou  AAAA  (ex: 02-04-2024 ou 2024)")
        sys.exit(1)


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

    # Anniversaire dans l'année du décès
    anniv_annee_deces = anniversaire_annee(naissance, deces.year)
    note_bissextile = " (→ 01/03, année non bissextile)" if (
        naissance.month == 2 and naissance.day == 29
        and anniv_annee_deces.month == 3
    ) else ""

    # Depuis le décès : combien d'anniversaires se sont écoulés ?
    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    nb_anniv_depuis = aujourd_hui.year - deces.year
    # Ajustement : si l'anniversaire de cette année n'est pas encore passé
    if (aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day):
        nb_anniv_depuis -= 1
    # Et on soustrait si l'anniversaire de l'année du décès était déjà passé au moment du décès
    if (deces.month, deces.day) >= (naissance.month, naissance.day):
        pass  # l'anniversaire de l'année du décès était avant le décès, donc compté
    else:
        nb_anniv_depuis += 1  # pas encore eu lieu cette année-là

    print(f"  Date du décès     : {fmt_date(deces)}")
    print(f"  Âge au décès      : {age_deces} ans")
    print(f"  Âge aujourd'hui   : {age_aurait} ans (si vivant·e)")
    print()
    print(f"  Anniversaire dans l'année du décès : {fmt_date(anniv_annee_deces)}{note_bissextile}")
    print()
    prochain_deces, jours_deces = prochain_anniversaire(deces, aujourd_hui)

    print(f"  Prochain anniversaire de naissance  : {fmt_date(anniv_depuis_deces)}")
    print(f"  Dans                                : {jours_prochain} jour{'s' if jours_prochain > 1 else ''}")
    if nb_anniv_depuis > 0:
        print(f"  Anniversaires écoulés depuis décès  : {nb_anniv_depuis}")
    print()
    print(f"  Prochain anniversaire du décès      : {fmt_date(prochain_deces)}")
    print(f"  Dans                                : {jours_deces} jour{'s' if jours_deces > 1 else ''}")


def affiche_section_deces_annee(naissance: date, annee_deces: int, aujourd_hui: date):
    """Section décès avec année seule."""
    # Âge : fourchette (avant/après l'anniversaire dans l'année)
    anniv_cette_annee = anniversaire_annee(naissance, annee_deces)
    age_avant = annee_deces - naissance.year - 1
    age_apres = annee_deces - naissance.year

    note_bissextile = " (→ 01/03, année non bissextile)" if (
        naissance.month == 2 and naissance.day == 29
        and anniv_cette_annee.month == 3
    ) else ""

    print(f"  Année du décès    : {annee_deces}")
    print(f"  Âge au décès      : {age_avant} ans (avant le {anniv_cette_annee.strftime('%d/%m')})"
          f" ou {age_apres} ans (après){note_bissextile}")
    print(f"  Âge aujourd'hui   : {age_a_la_date(naissance, aujourd_hui)} ans (si vivant·e)")
    print()
    print(f"  Anniversaire dans l'année du décès : {fmt_date(anniv_cette_annee)}{note_bissextile}")
    print()

    anniv_depuis_deces, jours_prochain = prochain_anniversaire(naissance, aujourd_hui)
    print(f"  Prochain anniversaire de naissance  : {fmt_date(anniv_depuis_deces)}")
    print(f"  Dans                                : {jours_prochain} jour{'s' if jours_prochain > 1 else ''}")
    print()
    # Pour l'anniversaire du décès on n'a que l'année → on prend le 31 déc comme date symbolique
    anniv_deces_ref = date(annee_deces, 12, 31)
    prochain_deces, _ = prochain_anniversaire(anniv_deces_ref, aujourd_hui)
    print(f"  Prochain anniversaire du décès      : courant {prochain_deces.year} (date exacte inconnue)")
    print(f"  Dans                                : d'ici le {prochain_deces.strftime('%d/%m/%Y')}")


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
    args = parser.parse_args()

    aujourd_hui = date.today()

    # --date obligatoire si --deces fourni
    if args.deces and not args.date:
        print("❌ --date est obligatoire quand --deces est utilisé.")
        sys.exit(1)

    if not args.date:
        parser.print_help()
        sys.exit(1)

    naissance = parse_date(args.date)

    # Validation date de naissance
    if naissance > aujourd_hui:
        print(f"❌ La date de naissance « {args.date} » est dans le futur.")
        sys.exit(1)

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
            # Validation année seule
            if annee_deces > aujourd_hui.year:
                print(f"❌ L'année de décès « {annee_deces} » est dans le futur.")
                sys.exit(1)
            if annee_deces < naissance.year:
                print(f"❌ L'année de décès « {annee_deces} » est antérieure à la naissance ({naissance.year}).")
                sys.exit(1)
            affiche_section_deces_annee(naissance, annee_deces, aujourd_hui)

        else:
            # Validation date complète
            if deces_date > aujourd_hui:
                print(f"❌ La date de décès « {args.deces} » est dans le futur.")
                sys.exit(1)
            if deces_date < naissance:
                print("❌ La date de décès est antérieure à la date de naissance.")
                sys.exit(1)
            affiche_section_deces_complet(naissance, deces_date, aujourd_hui)

    # ── Cas sans décès ──
    else:
        affiche_section_vivant(naissance, aujourd_hui)

    print()


if __name__ == "__main__":
    main()
