#!/usr/bin/env python3
"""Sincroniza dados do GitHub (via gh CLI) com o portfólio README.md e docs/."""

from __future__ import annotations

import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "github-repos.json"
README = ROOT / "README.md"
DOCS_DIR = ROOT / "docs"

PORTFOLIO_PROJECTS = [
    {
        "name": "VOSIKOLA",
        "summary": "Gestão escolar SUP — multitenancy, web, mobile e agente IA",
        "repos": [
            "Zeta-Byte/vosikola-sup-web",
            "Zeta-Byte/vosikola-sup-api",
            "Zeta-Byte/workspace-sup",
            "Zeta-Byte/vosikola-sup-agent",
            "Zeta-Byte/StudentApp-sup",
            "Zeta-Byte/TeacherApp-sup",
            "Zeta-Byte/FinanceApp-sup",
            "Zeta-Byte/vosikola-online",
        ],
        "stack": "Laravel · PHP · .NET MAUI · FastAPI · Python",
    },
    {
        "name": "ISPREILUHUNA",
        "summary": "Sistema digital para ensino superior (Instituto Cunene)",
        "repos": ["Zeta-Byte/vosikola-isprl"],
        "stack": "Laravel · PHP · Blade",
    },
    {
        "name": "OMILU ERP",
        "summary": "Gestão comercial, facturação e RH",
        "repos": ["osvacapir/omilu"],
        "stack": "Java",
    },
    {
        "name": "CRM Multiplataforma",
        "summary": ".NET MAUI + Blazor (Android, iOS, Windows, Mac)",
        "repos": ["osvacapir/CrmAppBM", "osvacapir/Crm", "osvacapir/maui_crm"],
        "stack": "C# · .NET MAUI · Blazor",
        "doc": "docs/PORTFOLIO_PROJETO_CRM.md",
    },
    {
        "name": "CRM API REST",
        "summary": "Laravel 12, ERP, OpenAPI",
        "repos": ["osvacapir/php"],
        "stack": "Laravel · PHP · Redis · Docker",
        "doc": "docs/PORTFOLIO_PROJETO_CRM_API.md",
    },
    {
        "name": "Gestão Universitária",
        "summary": "SaaS multi-tenant Laravel, Alpine.js, Tailwind, Docker",
        "repos": [
            "Zeta-Byte/vosikola-sup-web",
            "Zeta-Byte/vosikola-sup-api",
            "Zeta-Byte/workspace-sup",
        ],
        "stack": "Laravel · Alpine.js · Tailwind · Docker",
        "doc": "docs/PORTFOLIO_Gestão%20Universitária.md",
    },
    {
        "name": "Portal TIC-DASH (BI)",
        "summary": "Power BI, PHP, MySQL",
        "repos": ["osvacapir/power-bi-na-web"],
        "stack": "Power BI · PHP · MySQL · Azure Gateway",
        "doc": "docs/PORTFOLIO-TIC-DASH.md",
    },
    {
        "name": "JurisForge",
        "summary": "RAG jurídico Angola — assistente legal com IA",
        "repos": ["Zeta-Byte/jurisforge"],
        "stack": "Python · RAG · FastAPI",
    },
    {
        "name": "Okutanga PDF",
        "summary": "Leitor PDF offline (.NET MAUI + Blazor)",
        "repos": ["osvacapir/okutanga-pdf"],
        "stack": "C# · .NET MAUI · Blazor",
        "public": True,
    },
    {
        "name": "Meet",
        "summary": "App de encontros (NestJS + React + Docker)",
        "repos": ["osvacapir/meet"],
        "stack": "TypeScript · NestJS · React · Docker",
    },
    {
        "name": "My OCR IA",
        "summary": "SaaS verificação BI angolano",
        "repos": ["Zeta-Byte/my-ocr-ia"],
        "stack": "Python · OCR · IA",
    },
]

DOC_REPO_MAP = {
    "PORTFOLIO_PROJETO_CRM.md": ["osvacapir/CrmAppBM", "osvacapir/Crm"],
    "PORTFOLIO_PROJETO_CRM_API.md": ["osvacapir/php"],
    "PORTFOLIO_Gestão Universitária.md": [
        "Zeta-Byte/vosikola-sup-web",
        "Zeta-Byte/vosikola-sup-api",
    ],
    "PORTFOLIO-TIC-DASH.md": ["osvacapir/power-bi-na-web"],
}


def run_gh(*args: str, retries: int = 3) -> str:
    last_error: subprocess.CalledProcessError | None = None
    for attempt in range(retries):
        result = subprocess.run(
            ["gh", *args],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout
        last_error = subprocess.CalledProcessError(
            result.returncode, result.args, result.stdout, result.stderr
        )
        if attempt < retries - 1:
            time.sleep(2 ** attempt)
    raise last_error  # type: ignore[misc]


def fetch_repos() -> list[dict]:
    raw = run_gh("api", "user/repos?per_page=100&sort=updated", "--paginate")
    return json.loads(raw)


def fetch_user() -> dict:
    return json.loads(run_gh("api", "user"))


def repo_index(repos: list[dict]) -> dict[str, dict]:
    return {r["full_name"]: r for r in repos}


def format_date(iso: str | None) -> str:
    if not iso:
        return "—"
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m")


def fetch_repo_metrics(full_name: str) -> dict:
    owner, name = full_name.split("/", 1)
    repo = json.loads(run_gh("api", f"repos/{full_name}"))
    langs_raw = json.loads(run_gh("api", f"repos/{full_name}/languages"))
    total_bytes = sum(langs_raw.values()) or 1
    languages = sorted(
        ((lang, round(bytes_ / total_bytes * 100, 1)) for lang, bytes_ in langs_raw.items()),
        key=lambda item: -item[1],
    )[:6]

    query = (
        f'query {{ repository(owner:"{owner}", name:"{name}") '
        f"{{ defaultBranchRef {{ target {{ ... on Commit {{ history {{ totalCount }} }} }} }} }} }}"
    )
    try:
        gql = json.loads(run_gh("api", "graphql", "-f", f"query={query}"))
        commits = (
            gql["data"]["repository"]["defaultBranchRef"]["target"]["history"]["totalCount"]
        )
    except (subprocess.CalledProcessError, KeyError, TypeError):
        commits = None

    return {
        "full_name": full_name,
        "html_url": repo["html_url"],
        "description": repo.get("description"),
        "private": repo["private"],
        "primary_language": repo.get("language"),
        "size_kb": repo.get("size", 0),
        "pushed_at": (repo.get("pushed_at") or "")[:10],
        "commits": commits,
        "languages": languages,
    }


def build_stats(user: dict, repos: list[dict]) -> dict:
    public = sum(1 for r in repos if not r["private"])
    private = sum(1 for r in repos if r["private"])
    langs: dict[str, int] = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            langs[lang] = langs.get(lang, 0) + 1
    return {
        "synced_at": datetime.now(timezone.utc).isoformat(),
        "username": user["login"],
        "name": user.get("name"),
        "followers": user["followers"],
        "following": user["following"],
        "public_repos_account": user["public_repos"],
        "total_repos": len(repos),
        "public_repos": public,
        "private_repos": private,
        "total_stars": sum(r.get("stargazers_count", 0) for r in repos),
        "top_languages": sorted(langs.items(), key=lambda x: -x[1])[:8],
        "repos": [
            {
                "full_name": r["full_name"],
                "name": r["name"],
                "owner": r["owner"]["login"],
                "description": r.get("description"),
                "private": r["private"],
                "language": r.get("language"),
                "stars": r.get("stargazers_count", 0),
                "updated_at": r.get("updated_at"),
                "html_url": r.get("html_url"),
            }
            for r in repos
        ],
    }


def render_stats_section(stats: dict) -> str:
    return f"""**Estatística de repositórios (públicos + privados)** · _Atualizado: {stats['synced_at'][:10]} via GitHub API_

<p align="left">
    <img alt="Total de repositórios" title="Total: públicos + privados (conta + organizações)" src="https://img.shields.io/badge/Total-{stats['total_repos']}-blue?style=for-the-badge&logo=github&logoColor=white" />
    <img alt="Públicos" title="Repositórios públicos" src="https://img.shields.io/badge/Públicos-{stats['public_repos']}-blue?style=for-the-badge&logo=github&logoColor=white" />
    <img alt="Privados" title="Repositórios privados (incl. organizações)" src="https://img.shields.io/badge/Privados-{stats['private_repos']}-blue?style=for-the-badge&logo=github&logoColor=white" />
    <img alt="Experiência" title="Anos de experiência" src="https://img.shields.io/badge/Experiência-10%2B%20anos-orange?style=for-the-badge&logo=code&logoColor=white" />
</p>"""


def render_projects_section(index: dict[str, dict]) -> str:
    lines = [
        "### 📋 Principais Projetos",
        "",
        "_Dados sincronizados com repositórios GitHub reais (conta `osvacapir` + org `Zeta-Byte`)._",
        "",
    ]
    for project in PORTFOLIO_PROJECTS:
        matched = [index[r] for r in project["repos"] if r in index]
        last_update = max(
            (r["updated_at"] for r in matched if r.get("updated_at")),
            default=None,
        )
        updated_label = format_date(last_update)
        doc = project.get("doc")
        doc_link = f" · [detalhes]({doc})" if doc else ""
        public_badge = " 🌐" if project.get("public") or any(not r["private"] for r in matched) else ""
        lines.append(
            f"- **{project['name']}**{public_badge} — {project['summary']} · "
            f"`{project['stack']}` · _atualizado {updated_label}_"
            f"{doc_link}"
        )
        if matched:
            repo_links = ", ".join(
                f"[`{r['name']}`]({r['html_url']})" for r in matched[:4]
            )
            extra = len(matched) - 4
            if extra > 0:
                repo_links += f" (+{extra})"
            lines.append(f"  - Repositórios: {repo_links}")
    lines.append("")
    lines.append(
        "**Repositórios públicos destacados:** "
        "[okutanga-pdf](https://github.com/osvacapir/okutanga-pdf) · "
        "[angolan-localization-api](https://github.com/osvacapir/angolan-localization-api) · "
        "[SenhaFortePro](https://github.com/osvacapir/SenhaFortePro) · "
        "[python-mini-proj-dir](https://github.com/osvacapir/python-mini-proj-dir)"
    )
    return "\n".join(lines)


def render_doc_github_section(metrics_list: list[dict], synced_at: str) -> str:
    lines = [
        "## 🔗 Dados GitHub (repositórios reais)",
        "",
        f"_Sincronizado em {synced_at[:10]} via GitHub API — execute `python3 scripts/sync-github-portfolio.py` para atualizar._",
        "",
    ]
    total_commits = sum(m["commits"] or 0 for m in metrics_list)
    total_size = sum(m["size_kb"] for m in metrics_list)

    lines.append(
        f"<p align=\"left\">"
        f"<img alt=\"Repositórios\" src=\"https://img.shields.io/badge/Repositórios-{len(metrics_list)}-blue?style=flat-square&logo=github\" /> "
        f"<img alt=\"Commits\" src=\"https://img.shields.io/badge/Commits-{total_commits}-green?style=flat-square\" /> "
        f"<img alt=\"Tamanho\" src=\"https://img.shields.io/badge/Tamanho-{total_size // 1024}MB+-informational?style=flat-square\" /> "
        f"</p>"
    )
    lines.append("")
    lines.append("| Repositório | Visibilidade | Linguagem | Commits | Último push |")
    lines.append("|-------------|--------------|-----------|---------|-------------|")

    for m in metrics_list:
        visibility = "privado" if m["private"] else "público"
        commits = str(m["commits"]) if m["commits"] is not None else "—"
        lang = m["primary_language"] or "—"
        short = m["full_name"].split("/", 1)[1]
        lines.append(
            f"| [`{short}`]({m['html_url']}) | {visibility} | {lang} | {commits} | {m['pushed_at']} |"
        )

    all_langs: dict[str, float] = {}
    total_weight = sum(m["size_kb"] or 1 for m in metrics_list)
    for m in metrics_list:
        weight = m["size_kb"] or 1
        for lang, pct in m["languages"]:
            all_langs[lang] = all_langs.get(lang, 0) + pct * weight
    if all_langs and total_weight:
        lang_summary = ", ".join(
            f"{lang} ({all_langs[lang] / total_weight:.0f}%)"
            for lang in sorted(all_langs, key=all_langs.get, reverse=True)[:5]
        )
        lines.extend(["", f"**Distribuição de linguagens (média ponderada):** {lang_summary}"])

    return "\n".join(lines)


def replace_section(content: str, start: str, end: str, body: str) -> str:
    if start not in content or end not in content:
        raise SystemExit(f"Marcadores {start} / {end} não encontrados")
    before, rest = content.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + "\n" + body + "\n" + end + after


def sync_docs(synced_at: str) -> int:
    updated = 0
    for filename, repo_names in DOC_REPO_MAP.items():
        doc_path = DOCS_DIR / filename
        if not doc_path.exists():
            print(f"⚠ Doc não encontrado: {filename}")
            continue
        metrics = [fetch_repo_metrics(name) for name in repo_names]
        body = render_doc_github_section(metrics, synced_at)
        content = doc_path.read_text(encoding="utf-8")
        content = replace_section(
            content,
            "<!-- GITHUB_REPO_STATS_START -->",
            "<!-- GITHUB_REPO_STATS_END -->",
            body,
        )
        doc_path.write_text(content, encoding="utf-8")
        updated += 1
        print(f"✓ {filename}")
    return updated


def main() -> None:
    user = fetch_user()
    repos = fetch_repos()
    stats = build_stats(user, repos)

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    index = repo_index(repos)
    readme = replace_section(
        readme,
        "<!-- GITHUB_PROJECTS_START -->",
        "<!-- GITHUB_PROJECTS_END -->",
        render_projects_section(index),
    )
    readme = replace_section(
        readme,
        "<!-- GITHUB_STATS_START -->",
        "<!-- GITHUB_STATS_END -->",
        render_stats_section(stats),
    )
    README.write_text(readme, encoding="utf-8")

    docs_updated = sync_docs(stats["synced_at"])

    print(f"✓ {stats['total_repos']} repositórios ({stats['public_repos']} públicos, {stats['private_repos']} privados)")
    print(f"✓ Dados gravados em {DATA_FILE.relative_to(ROOT)}")
    print(f"✓ README.md atualizado")
    print(f"✓ {docs_updated} documentos de portfólio atualizados")


if __name__ == "__main__":
    main()
