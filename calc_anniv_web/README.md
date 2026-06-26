# calc_anniv_web — Interface web pour calc-anniv

Interface web pour le script Python `calc-anniv.py` — calcul d'informations d'anniversaire à partir d'une date de naissance.

## Fonctionnalités

- Saisie de la date de naissance au format JJ-MM-AAAA
- Trois modes : **Vivant·e**, **Décès**, **Date future**
- Support date complète ou année seule pour les modes Décès et Date future
- Rendu immédiat sans rechargement de page

## Stack

| Composant | Technologie |
|-----------|-------------|
| Backend | Node.js + Express 4 (ES modules) |
| Frontend | HTML / CSS / JS vanilla |
| Logique | Python 3.10+ (`calc-anniv.py`, invoqué en sous-processus) |
| Déploiement | systemd + nginx (reverse proxy) |

---

## Prérequis

- Node.js 20.20.2 (voir [.nvmrc](.nvmrc))
- Python 3.10 ou supérieur
- Aucune dépendance Python externe

---

## Démarrage local

```bash
cd bf_calc_anniv/calc_anniv_web
cp .env.example .env          # ajuster PORT si nécessaire
npm install
npm start
```

L'application est disponible à : http://localhost:6001/

### Vérification API

```bash
curl 'http://localhost:6001/api/calc?date=14-10-1938'
curl 'http://localhost:6001/api/calc?date=14-10-1938&deces=02-04-2024'
curl 'http://localhost:6001/api/calc?date=14-10-1938&deces=2024'
curl 'http://localhost:6001/api/calc?date=14-10-1938&futur=25-12-2030'
curl 'http://localhost:6001/api/calc?date=14-10-1938&futur=2030'
```

---

## Déploiement (systemd + nginx)

### 1. Copier le projet sur le serveur

```bash
rsync -av --exclude=node_modules bf_calc_anniv/ user@server:/opt/bf_calc_anniv/
```

### 2. Installer les dépendances

```bash
ssh user@server
cd /opt/bf_calc_anniv/calc_anniv_web
npm install --production
```

### 3. Configurer le service systemd

```bash
sudo cp deploy/calc_anniv_web.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable calc_anniv_web
sudo systemctl start calc_anniv_web
```

### 4. Configurer nginx

```bash
sudo cp deploy/nginx-calc_anniv_web.conf /etc/nginx/snippets/calc_anniv_web_location.conf
sudo nginx -t && sudo systemctl reload nginx
```

L'application est ensuite accessible à : `https://votre-domaine/calc-anniv/`

---

## Gestion du service

```bash
sudo systemctl status calc_anniv_web
sudo systemctl restart calc_anniv_web
sudo journalctl -u calc_anniv_web -f
```

---

## Structure

```text
calc_anniv_web/
├── server.js                   Serveur Express (GET /api/calc)
├── package.json
├── eslint.config.js
├── .nvmrc                      20.20.2
├── .env.example
├── .gitignore
├── public/
│   ├── index.html              Interface utilisateur
│   ├── app.js                  Logique frontend
│   └── style.css               Thème dark (palette bf_loterie)
└── deploy/
    ├── calc_anniv_web.service  Unité systemd
    └── nginx-calc_anniv_web.conf  Snippet nginx (location /calc-anniv/)
```

---

## API

### `GET /api/calc`

| Paramètre | Format | Requis | Description |
|-----------|--------|--------|-------------|
| `date`    | `JJ-MM-AAAA` | Oui | Date de naissance |
| `deces`   | `JJ-MM-AAAA` ou `AAAA` | Non | Date / année de décès |
| `futur`   | `JJ-MM-AAAA` ou `AAAA` | Non | Date / année future de référence |

`deces` et `futur` sont mutuellement exclusifs.

**Réponse succès (200)** : objet JSON `{ naissance, mode, data }`.

**Réponse erreur (400/500)** : `{ error: "..." }`.

**Rate-limiting** : 60 requêtes par minute par IP. Au-delà, le serveur retourne HTTP 429 avec `{ error: "Trop de requêtes — réessayez dans une minute." }`.

### Sécurité

- En-têtes de sécurité posés sur toutes les réponses : `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer`, `Content-Security-Policy: default-src 'self'`.
- `X-Powered-By` désactivé.
- Validation côté serveur des dates (format + cohérence calendaire) avant l'invocation Python.