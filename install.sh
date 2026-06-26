#!/usr/bin/env bash
set -euo pipefail

INSTALL_DIR="/opt/bf_calc_anniv/calc_anniv_web"
CALC_ANNIV_DIR="/opt/bf_calc_anniv"
SERVICE_NAME="calc_anniv_web"
NGINX_SNIPPET="/etc/nginx/snippets/calc_anniv_web_location.conf"
BRUNO_CONF="/etc/nginx/sites-available/bruno"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ $EUID -ne 0 ]]; then
  echo "Run as root: sudo bash install.sh" >&2
  exit 1
fi

echo "==> Installing Node.js, npm and python3..."
if ! command -v node &>/dev/null; then
  apt-get update -q
  apt-get install -y nodejs npm
else
  echo "    node $(node --version) already installed, skipping."
fi
if ! command -v python3 &>/dev/null; then
  apt-get update -q
  apt-get install -y python3
else
  echo "    python3 $(python3 --version) already installed, skipping."
fi

echo "==> Copying bf_calc_anniv to $CALC_ANNIV_DIR..."
mkdir -p "$CALC_ANNIV_DIR"
rsync -a --exclude='.git' --exclude='__pycache__' --exclude='calc_anniv_web' \
  "$SCRIPT_DIR/" "$CALC_ANNIV_DIR/"
chown -R www-data:www-data "$CALC_ANNIV_DIR"

echo "==> Copying calc_anniv_web to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
rsync -a --exclude='.git' --exclude='node_modules' --exclude='.env' \
  "$SCRIPT_DIR/calc_anniv_web/" "$INSTALL_DIR/"

# .env : ne jamais écraser ; créer depuis .env.example si absent
ENV_FILE="$INSTALL_DIR/.env"
if [[ ! -f "$ENV_FILE" ]]; then
  if [[ -f "$INSTALL_DIR/.env.example" ]]; then
    cp "$INSTALL_DIR/.env.example" "$ENV_FILE"
    echo "    ⚠️  Created $ENV_FILE from .env.example — review before use!"
  else
    echo "    ⚠️  $ENV_FILE absent and no .env.example found — create it manually."
  fi
else
  echo "    .env already present on server, not overwritten."
fi

echo "==> Installing npm dependencies..."
cd "$INSTALL_DIR"
npm install --production --silent

chown -R www-data:www-data "$INSTALL_DIR"

echo "==> Installing systemd service..."
cp "$INSTALL_DIR/deploy/calc_anniv_web.service" "/etc/systemd/system/${SERVICE_NAME}.service"
systemctl daemon-reload
systemctl enable "$SERVICE_NAME"
systemctl restart "$SERVICE_NAME"
systemctl status "$SERVICE_NAME" --no-pager

echo "==> Configuring nginx..."
mkdir -p /etc/nginx/snippets
cp "$INSTALL_DIR/deploy/nginx-calc_anniv_web.conf" "$NGINX_SNIPPET"

# Défaire tous les includes individuels de snippets (le glob les couvre tous)
if [[ -f "$BRUNO_CONF" ]]; then
  if grep -qP 'include\s+/etc/nginx/snippets/[^*].*_location\.conf' "$BRUNO_CONF"; then
    sed -i -E '/include[[:space:]]+\/etc\/nginx\/snippets\/[^*].*_location\.conf/d' "$BRUNO_CONF"
    echo "    Removed per-project snippet includes from $BRUNO_CONF"
  fi
fi

# Le vhost bruno doit contenir : include /etc/nginx/snippets/*_location.conf;
# Ajouter ce glob include s'il n'est pas encore présent
if [[ -f "$BRUNO_CONF" ]]; then
  if ! grep -q 'snippets/\*_location\.conf' "$BRUNO_CONF"; then
    sed -i '/listen 443 ssl/a\    include /etc/nginx/snippets/*_location.conf;' "$BRUNO_CONF"
    echo "    Added glob include to $BRUNO_CONF"
  else
    echo "    Glob include already present in $BRUNO_CONF"
  fi
else
  echo "  WARNING: $BRUNO_CONF not found. Add manually to your nginx vhost:" >&2
  echo "    include /etc/nginx/snippets/*_location.conf;" >&2
fi

nginx -t
systemctl restart nginx

echo ""
echo "Done. Calc Anniv available at https://bfablet92.hd.free.fr/calc-anniv/"
