# calc-anniv

Script Python en ligne de commande pour calculer les informations d'anniversaire à partir d'une date de naissance, avec support optionnel d'une date de décès ou d'une date future de référence.

---

## Objectif

Donner rapidement, à partir d'une date de naissance, des informations utiles : âge actuel, prochain anniversaire, et — en cas de décès — l'âge au moment du décès, l'âge qu'aurait eu la personne aujourd'hui, ainsi que les prochains anniversaires de naissance et de décès.

---

## Prérequis

- Python 3.10 ou supérieur (utilisation des types `X | Y` et `tuple[...]`)
- Aucune dépendance externe

---

## Utilisation

```bash
# Personne vivante
python calc-anniv.py --date JJ-MM-AAAA

# Avec date de décès complète
python calc-anniv.py --date JJ-MM-AAAA --deces JJ-MM-AAAA

# Avec année de décès seule
python calc-anniv.py --date JJ-MM-AAAA --deces AAAA

# Date future de référence (date complète)
python calc-anniv.py --date JJ-MM-AAAA --futur JJ-MM-AAAA

# Date future de référence (année seule)
python calc-anniv.py --date JJ-MM-AAAA --futur AAAA
```

### Exemples

```bash
python calc-anniv.py --date 14-10-1938
python calc-anniv.py --date 14-10-1938 --deces 02-04-2024
python calc-anniv.py --date 14-10-1938 --deces 2024
python calc-anniv.py --date 14-10-1938 --futur 25-12-2030
python calc-anniv.py --date 14-10-1938 --futur 2030
```

---

## Paramètres

| Paramètre | Format | Obligatoire | Description |
|-----------|--------|-------------|-------------|
| `--date`  | `JJ-MM-AAAA` | Oui (toujours si `--deces` ou `--futur` est présent) | Date de naissance |
| `--deces` | `JJ-MM-AAAA` ou `AAAA` | Non | Date ou année de décès |
| `--futur` | `JJ-MM-AAAA` ou `AAAA` | Non | Date ou année future de référence |
| `--json`  | — | Non | Sortie JSON sur stdout (erreurs sur stderr, exit ≠ 0) |

---

## Sortie JSON (`--json`)

Ajouter `--json` sérialise le résultat sur stdout sous la forme :

```json
{
  "naissance": "AAAA-MM-JJ",
  "mode": "vivant | deces | deces_annee | futur | futur_annee",
  "data": { ... }
}
```

Les erreurs partent sur **stderr** et le script sort en code ≠ 0, ce qui permet au processus appelant (ex. Express) de distinguer succès et échec.

```bash
python calc-anniv.py --json --date 14-10-1938
python calc-anniv.py --json --date 14-10-1938 --deces 02-04-2024
python calc-anniv.py --json --date 14-10-1938 --deces 2024
python calc-anniv.py --json --date 14-10-1938 --futur 25-12-2030
python calc-anniv.py --json --date 14-10-1938 --futur 2030
```

---

## Informations affichées

### Sans `--deces` ni `--futur`

- Date de naissance avec jour de la semaine
- Âge actuel
- Date du prochain anniversaire et nombre de jours restants
- Message spécial si c'est le jour même

### Avec `--deces` (date complète)

- Date du décès avec jour de la semaine
- Âge au moment du décès
- Âge qu'aurait la personne aujourd'hui
- Date de l'anniversaire de naissance dans l'année du décès
- Prochain anniversaire de naissance depuis aujourd'hui
- Nombre d'anniversaires écoulés depuis le décès
- Prochain anniversaire du décès

### Avec `--deces` (année seule)

Identique à la date complète, avec les adaptations suivantes :
- L'âge au décès est exprimé en fourchette (avant ou après l'anniversaire dans l'année)
- Le prochain anniversaire du décès indique l'année sans date précise

### Avec `--futur` (date complète)

- Date de référence avec jour de la semaine
- Âge à cette date
- Prochain anniversaire à partir de cette date

### Avec `--futur` (année seule)

- Année de référence
- Âge en fourchette (avant/après l'anniversaire dans l'année)
- Date de l'anniversaire dans cette année

---

## Validations et erreurs

Le script vérifie et rejette les cas suivants :

- Date de naissance dans le futur
- Format de date invalide (`JJ-MM-AAAA` attendu)
- `--deces` ou `--futur` utilisé sans `--date`
- Date de décès antérieure à la date de naissance
- Date ou année de décès dans le futur
- Date future `--futur` antérieure à aujourd'hui (la date doit être dans le futur)
- Date ou année future antérieure à la date de naissance

---

## Limitations connues

**Année de décès seule** — quand seule l'année est fournie via `--deces`, l'âge au décès ne peut être qu'une fourchette (la date exacte étant inconnue), et le prochain anniversaire du décès ne peut pas être daté précisément.

**29 février** — les personnes nées un 29 février voient leur anniversaire décalé au 1er mars les années non bissextiles. Ce comportement est signalé dans la sortie mais reste une convention arbitraire (certains fêtent le 28 février).

**Pas de prise en compte du fuseau horaire** — le script utilise la date locale de la machine. Si le script est exécuté à minuit autour d'un changement de jour, le résultat peut différer d'un fuseau à l'autre.

**Python 3.10 minimum** — la syntaxe `X | Y` pour les unions de types et `tuple[...]` en annotation ne sont pas disponibles sur les versions antérieures. Sur Python 3.9 ou moins, il faudrait remplacer ces annotations par `Optional` et `Tuple` issus du module `typing`.

---

## Linting & tests

Le projet inclut un fichier `.pylintrc` qui désactive deux règles non pertinentes :

- `C0103` — nom de module avec tiret (imposé par le nom du fichier)
- `C0301` — lignes trop longues

```bash
pylint calc-anniv.py  # doit retourner 10.00/10
```

Les tests unitaires utilisent **pytest** :

```bash
pip install pytest
pytest tests/ -v
```

Les tests couvrent : `age_a_la_date`, `prochain_anniversaire` (dont 29 février), `nb_anniversaires_entre`, helpers `note_bissextile_*`, builders `data_deces_complet`/`data_deces_annee`/`data_futur_annee`, ainsi que les codes de sortie CLI (date invalide, `--futur` dans le passé, `--json` sans pollution stdout).
