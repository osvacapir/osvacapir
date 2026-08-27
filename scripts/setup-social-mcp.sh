#!/usr/bin/env bash
# Configura credenciais para MCP LinkedIn e Google Workspace no Cursor.
set -euo pipefail

ENV_FILE="${HOME}/.cursor/social.env"
GOOGLE_CREDS_DIR="${HOME}/.google-workspace-mcp"
CURSOR_MCP="${HOME}/.cursor/mcp.json"

install -d -m 700 "$(dirname "$ENV_FILE")"
install -d -m 700 "$GOOGLE_CREDS_DIR"

if [[ ! -f "$ENV_FILE" ]]; then
  cat >"$ENV_FILE" <<'EOF'
# Credenciais LinkedIn (https://www.linkedin.com/developers/)
LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=
EOF
  chmod 600 "$ENV_FILE"
  echo "✓ Criado ${ENV_FILE} — preencha LINKEDIN_CLIENT_ID e LINKEDIN_CLIENT_SECRET"
else
  echo "✓ ${ENV_FILE} já existe"
fi

if [[ ! -f "${GOOGLE_CREDS_DIR}/credentials.json" ]]; then
  echo ""
  echo "Google Workspace MCP:"
  echo "  1. Crie um projeto em https://console.cloud.google.com/"
  echo "  2. Ative Gmail, Calendar, Drive, Docs, Sheets, Slides e People APIs"
  echo "  3. Crie credenciais OAuth tipo «Desktop app»"
  echo "  4. Guarde o JSON em: ${GOOGLE_CREDS_DIR}/credentials.json"
else
  echo "✓ Google credentials em ${GOOGLE_CREDS_DIR}/credentials.json"
fi

if [[ -f "$CURSOR_MCP" ]] && grep -q '"linkedin"' "$CURSOR_MCP" && grep -q '"google-workspace"' "$CURSOR_MCP"; then
  echo "✓ Entradas 'linkedin' e 'google-workspace' em ~/.cursor/mcp.json"
else
  echo "⚠ Confirme que ~/.cursor/mcp.json tem as entradas linkedin e google-workspace"
fi

echo ""
echo "Próximos passos:"
echo "  1. Preencha ${ENV_FILE} (LinkedIn)"
echo "  2. Coloque credentials.json em ${GOOGLE_CREDS_DIR}/ (Google)"
echo "  3. Exporte as variáveis no shell ou adicione ao ~/.bashrc:"
echo "       set -a; source ${ENV_FILE}; set +a"
echo "  4. Reinicie o Cursor"
echo "  5. Verifique em: Cursor Settings → Tools & MCP"
