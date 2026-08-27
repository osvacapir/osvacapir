# 📊 Portal TIC-DASH — Business Intelligence

<p align="left">
    <a href="../README.md">
        <img alt="Voltar ao Portfólio" src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=flat-square" />
    </a>
</p>

**Tipo:** Caso de estudo · Full-stack · Ciclo completo de desenvolvimento  
**Contexto:** Projeto profissional em que o programador participou em todas as fases — desde a análise de dados e alimentação do Power BI até ao portal web, administração e colocação em produção.

<p align="left">
    <img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
    <img alt="PHP" src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" />
    <img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
    <img alt="Azure" src="https://img.shields.io/badge/Azure%20Gateway-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" />
</p>

<!-- GITHUB_REPO_STATS_START -->
## 🔗 Dados GitHub (repositórios reais)

_Sincronizado em 2026-08-27 via GitHub API — execute `python3 scripts/sync-github-portfolio.py` para atualizar._

<p align="left"><img alt="Repositórios" src="https://img.shields.io/badge/Repositórios-1-blue?style=flat-square&logo=github" /> <img alt="Commits" src="https://img.shields.io/badge/Commits-2-green?style=flat-square" /> <img alt="Tamanho" src="https://img.shields.io/badge/Tamanho-10MB+-informational?style=flat-square" /> </p>

| Repositório | Visibilidade | Linguagem | Commits | Último push |
|-------------|--------------|-----------|---------|-------------|
| [`power-bi-na-web`](https://github.com/osvacapir/power-bi-na-web) | privado | PHP | 2 | 2026-02-02 |

**Distribuição de linguagens (média ponderada):** PHP (64%), HTML (30%), CSS (4%), JavaScript (2%), Dockerfile (0%)
<!-- GITHUB_REPO_STATS_END -->

---

## Visão geral

Este caso ilustra as **competências** aplicadas na conceção e entrega de um portal interno de Business Intelligence: utilizadores finais acedem a dashboards Power BI por empresa, com autenticação, gestão multi-empresa e área de administração. O foco deste documento é **o que o programador soube fazer** — ferramentas, técnicas e qualificações — e não a exposição interna do projeto.

---

## Competências em análise e engenharia de dados

- **Extração e tratamento de dados:** identificação e extração de dados a partir de bases onde coexistem informações de ERP; tratamento e modelação para consumo em BI.
- **Stored procedures (SP):** conceção e implementação de procedimentos armazenados para alimentar os modelos de dados do Power BI, garantindo fontes estáveis e performantes.
- **Relatórios Power BI:** criação e desenho de relatórios e dashboards no Power BI a partir dos modelos alimentados pelas SP.
- **Atualização dinâmica:** configuração da atualização dos datasets no Power BI através do **Power BI Gateway (Azure)** — agendamento e refresh em ambiente cloud.

---

## Competências em desenvolvimento e integração

- **Backend:** PHP (procedural e modular), autenticação e autorização, gestão de sessão, APIs internas, preparação de queries e segurança (prepared statements, validação de entrada/saída).
- **Base de dados:** MySQL — desenho de esquema, migrações e integração com a aplicação.
- **Frontend:** HTML5, CSS3 (layout responsivo, flex/grid), JavaScript — interfaces consistentes para portal e painel administrativo.
- **Integração:** embed de relatórios Power BI (iframe), consumo de dados por perfil e por empresa; e-mail transacional (PHPMailer/SMTP) para recuperação de palavra-passe, boas-vindas e avisos.
- **Servidor e deploy:** Apache, mod_rewrite, configuração em **servidor de hosting convencional**, com **ferramentas convencionais** (sem requisitos de infraestrutura proprietária).

---

## Ciclo de desenvolvimento

O programador esteve envolvido em **todo o ciclo** do projeto: análise de requisitos, desenho da solução de dados (extração, SP, modelos), criação dos relatórios no Power BI, desenvolvimento do portal (auth, multi-tenant, admin), integração com Power BI e Gateway, e **deploy em produção** num ambiente de hosting standard.

---

## Resumo de qualificações evidenciadas

| Área | Competências / ferramentas |
|------|----------------------------|
| **Dados e BI** | Extração e tratamento de dados (incl. fontes ERP), stored procedures, Power BI (relatórios e dashboards), Power BI Gateway / Azure (refresh dinâmico) |
| **Backend** | PHP, MySQL, autenticação, sessões, APIs, segurança (prepared statements, validação) |
| **Frontend** | HTML5, CSS3, JavaScript, interfaces responsivas |
| **Integração** | Embed Power BI, SMTP/e-mail transacional |
| **Deploy** | Apache, hosting convencional, ferramentas standard |

---

<p align="center">
    <a href="../README.md">
        <img alt="Voltar ao Portfólio" src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=for-the-badge" />
    </a>
</p>

*Documento de portfólio profissional. Redigido para demonstrar qualificações do programador para futuros projetos, sem expor detalhes de implementação ou dados sensíveis do negócio.*
