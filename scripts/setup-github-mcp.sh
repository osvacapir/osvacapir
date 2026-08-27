#!/usr/bin/env bash
# Configura GITHUB_TOKEN para o MCP GitHub no Cursor (via gh CLI).
set -euo pipefail

ENV_FILE="${HOME}/.cursor/github.env"
CURSOR_MCP="${HOME}/.cursor/mcp.json"

if ! command -v gh >/dev/null 2>&1; then
  echo "Erro: GitHub CLI (gh) não encontrado. Instale em https://cli.github.com/"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Erro: gh não autenticado. Execute: gh auth login"
  exit 1
fi

TOKEN="$(gh auth token)"
install -d -m 700 "$(dirname "$ENV_FILE")"
printf 'GITHUB_TOKEN=%s\n' "$TOKEN" > "$ENV_FILE"
chmod 600 "$ENV_FILE"

if [[ -f "$CURSOR_MCP" ]] && grep -q '"github"' "$CURSOR_MCP"; then
  echo "✓ Entrada 'github' já existe em ~/.cursor/mcp.json"
else
  echo "⚠ Adicione manualmente a entrada 'github' em ~/.cursor/mcp.json (ver README ou documentação GitHub MCP)"
fi

echo "✓ Token gravado em ~/.cursor/github.env (chmod 600)"
echo ""
echo "Próximo passo: reinicie o Cursor para activar o MCP GitHub."
echo "Verifique em: Cursor Settings → Tools & MCP → github"
