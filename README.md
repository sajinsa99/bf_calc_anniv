# calc-anniv

Script Python en ligne de commande pour calculer les informations d'anniversaire à partir d'une date de naissance, avec support optionnel d'une date de décès.

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
```

### Exemples

```bash
python calc-anniv.py --date 14-10-1938
python calc-anniv.py --date 14-10-1938 --deces 02-04-2024
python calc-anniv.py --date 14-10-1938 --deces 2024
```

---

## Paramètres

| Paramètre | Format | Obligatoire | Description |
|-----------|--------|-------------|-------------|
| `--date`  | `JJ-MM-AAAA` | Oui (toujours si `--deces` est présent) | Date de naissance |
| `--deces` | `JJ-MM-AAAA` ou `AAAA` | Non | Date ou année de décès |

---

## Informations affichées

### Sans `--deces`

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

---

## Validations et erreurs

Le script vérifie et rejette les cas suivants :

- Date de naissance dans le futur
- Format de date invalide (`JJ-MM-AAAA` attendu)
- `--deces` utilisé sans `--date`
- Date de décès antérieure à la date de naissance
- Date ou année de décès dans le futur

---

## Limitations connues

**Année de décès seule** — quand seule l'année est fournie via `--deces`, l'âge au décès ne peut être qu'une fourchette (la date exacte étant inconnue), et le prochain anniversaire du décès ne peut pas être daté précisément.

**29 février** — les personnes nées un 29 février voient leur anniversaire décalé au 1er mars les années non bissextiles. Ce comportement est signalé dans la sortie mais reste une convention arbitraire (certains fêtent le 28 février).

**Pas de prise en compte du fuseau horaire** — le script utilise la date locale de la machine. Si le script est exécuté à minuit autour d'un changement de jour, le résultat peut différer d'un fuseau à l'autre.

**Python 3.10 minimum** — la syntaxe `X | Y` pour les unions de types et `tuple[...]` en annotation ne sont pas disponibles sur les versions antérieures. Sur Python 3.9 ou moins, il faudrait remplacer ces annotations par `Optional` et `Tuple` issus du module `typing`.

---

## Linting

Le projet inclut un fichier `.pylintrc` qui désactive deux règles non pertinentes :

- `C0103` — nom de module avec tiret (imposé par le nom du fichier)
- `C0301` — lignes trop longues

```bash
pylint calc-anniv.py  # doit retourner 10.00/10
```
