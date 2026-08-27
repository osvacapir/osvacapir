# 🔌 Portfólio — API REST CRM

<p align="left">
    <a href="../README.md">
        <img 
            alt="Voltar ao Portfólio" 
            src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=flat-square"
        />
    </a>
    <a href="PORTFOLIO_PROJETO_CRM.md">
        <img 
            alt="Ver Aplicação Mobile" 
            src="https://img.shields.io/badge/Ver%20App%20Mobile-512BD4?style=flat-square&logo=dotnet&logoColor=white"
        />
    </a>
</p>

Documento de apoio ao portfólio do programador, descrevendo **ferramentas, competências e dimensão** do projeto, sem expor detalhes sensíveis do negócio.

<p align="left">
    <img 
        alt="Laravel" 
        src="https://img.shields.io/badge/Laravel-12-FF2D20?style=for-the-badge&logo=laravel&logoColor=white"
    />
    <img 
        alt="PHP" 
        src="https://img.shields.io/badge/PHP-8.4-777BB4?style=for-the-badge&logo=php&logoColor=white"
    />
    <img 
        alt="SQL Server" 
        src="https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white"
    />
    <img 
        alt="Redis" 
        src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"
    />
    <img 
        alt="Docker" 
        src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"
    />
</p>

<!-- GITHUB_REPO_STATS_START -->
## 🔗 Dados GitHub (repositórios reais)

_Métricas agregadas por origem (conta pessoal ou organização), sem nomes de repositórios._

<p align="left"><img alt="Repositórios" src="https://img.shields.io/badge/Repositórios-1-blue?style=flat-square&logo=github" /> <img alt="Commits" src="https://img.shields.io/badge/Commits-7-green?style=flat-square" /> <img alt="Tamanho" src="https://img.shields.io/badge/Tamanho-1MB+-informational?style=flat-square" /> </p>

| Origem | Visibilidade | Linguagem | Commits |
|--------|--------------|-----------|---------|
| Conta pessoal | privado | PHP | 7 |

**Distribuição de linguagens (média ponderada):** PHP (100%), Shell (0%), TSQL (0%), PowerShell (0%), Dockerfile (0%)
<!-- GITHUB_REPO_STATS_END -->

---

## 📋 Visão geral do projeto

- **Tipo:** API REST para suporte a aplicações de gestão (CRM).
- **Stack principal:** Laravel 12, PHP 8.4.
- **Arquitetura:** API versionada (v1), stateless, autenticação por tokens.

### 📊 Dimensão aproximada (código desenvolvido/maintainado)

<p align="left">
    <img 
        alt="Ficheiros PHP" 
        src="https://img.shields.io/badge/Ficheiros%20PHP-125-blue?style=flat-square"
    />
    <img 
        alt="Rotas API" 
        src="https://img.shields.io/badge/Rotas%20API-170-success?style=flat-square"
    />
    <img 
        alt="Migrações" 
        src="https://img.shields.io/badge/Migrações-30-orange?style=flat-square"
    />
    <img 
        alt="Documentos" 
        src="https://img.shields.io/badge/Documentos-40%2B-purple?style=flat-square"
    />
</p>

- ~125 ficheiros PHP de aplicação (Controllers, Services, Jobs, Mail, Notifications, etc.), excluindo modelos gerados automaticamente.
- Centenas de entidades de domínio mapeadas (modelos Eloquent gerados a partir do esquema de base de dados).
- ~30 migrações Laravel para evolução do esquema.
- ~170 definições de rotas (API v1, auth, web).
- ~40 documentos técnicos (setup, deployment, integrações, refatoração).

---

## 📑 Índice

- [Visão geral do projeto](#-visão-geral-do-projeto)
- [Tecnologias e ferramentas](#️-tecnologias-e-ferramentas)
- [Padrões e princípios aplicados](#-padrões-e-princípios-aplicados)
- [Competências evidenciadas](#-competências-evidenciadas)
- [Linguagens e formatos](#-linguagens-e-formatos)
- [Metodologias e práticas](#-metodologias-e-práticas)
- [Resumo para recrutadores](#-resumo-para-recrutadores-e-entrevistas)

---

## 🛠️ Tecnologias e ferramentas

### Backend e runtime
- **PHP 8.4** — tipagem estrita, atributos, enums quando aplicável.
- **Laravel 12** — framework principal (routing, Eloquent, queues, scheduler, auth).
- **Laravel Sanctum** — autenticação API (tokens, SPA).
- **Laravel Socialite** — SSO (OAuth) para provedores externos.
- **Spatie Laravel Permission** — roles e permissões.
- **2FA (TOTP)** — pragmarx/google2fa-laravel para autenticação em dois fatores.
- **PHPSpreadsheet** — export/import e manipulação de ficheiros Excel.
- **L5-Swagger (OpenAPI)** — documentação da API (Swagger UI + spec JSON).

### Base de dados e cache
- **SQL Server** — base de dados principal (driver `sqlsrv`/`pdo_sqlsrv`).
  - Integração com base de dados do **ERP PHC** (sistema de gestão empresarial).
  - Mapeamento de centenas de entidades do ERP via modelos Eloquent.
  - Compatibilidade com algoritmos de hash do PHC (SHA-256) para autenticação integrada.
- **Redis** — cache e filas (queue driver).
- **Migrações Laravel** — evolução do esquema e seeds (roles, permissões, utilizadores).

### Infraestrutura e DevOps
- **Docker** — orquestração local/produção:
  - PHP 8.4-FPM, Nginx, Redis.
  - Queue worker dedicado (filas `chamadas`, `default`).
  - Scheduler em loop (tarefas agendadas).
- **Docker Compose** — definição de serviços, redes, volumes, healthchecks.
- **Scripts PowerShell** — automação (deploy, health checks, restarts, testes).
- **IIS** — documentação e scripts para deploy em Windows Server (opcional).

### Qualidade e observabilidade
- **PHPUnit** — testes automatizados.
- **Laravel Telescope** (dev) — debugging, requests, jobs, queries.
- **Laravel Pint** — formatação e estilo de código.
- **Laravel Pail** — leitura de logs em tempo real (dev).
- **Logging** — canais configuráveis (stack, daily, etc.).

### Integrações e comunicação
- **ERP PHC** — integração com sistema de gestão empresarial:
  - Leitura/escrita na base de dados do PHC (SQL Server).
  - Sincronização de dados (clientes, artigos, stock, documentos BO/BI).
  - Execução de stored procedures para recálculo de totais de documentos.
  - Compatibilidade com autenticação e hashing do PHC.
- **E-mail** — configuração dinâmica por credenciais (SMTP), Mailables, notificações.
- **SMS** — serviço dedicado (e.g. via e-mail ou gateway).
- **Microsoft Outlook** — integração com API (registar e associar e-mails a entidades).
- **Envio em massa** — Jobs para campanhas (ex.: mensagens sazonais), com filas e controle de concorrência.

---

## 📐 Padrões e princípios aplicados

### Arquitetura e organização
- **API REST** — recursos, verbos HTTP, códigos de estado e respostas JSON consistentes.
- **Versionamento** — `/api/v1/` como primeira versão estável.
- **Separação de responsabilidades:**
  - **Controllers** — orquestração (thin controllers); delegação para Services e Form Requests.
  - **Services** — lógica de negócio (ex.: CRM, E-mail, Utilizadores).
  - **Query Services** — consultas complexas, filtros e reutilização.
  - **Form Requests** — validação de entrada por recurso/ação.
  - **Resources** — transformação de modelos para resposta da API (JSON).

### Princípios SOLID (contexto Laravel)
- **SRP** — controllers, services e query services com responsabilidades bem definidas.
- **OCP** — extensão via novos controllers/services sem alterar os existentes; uso de `BaseCrudController` para CRUD genérico.
- **DIP** — injeção de dependências via construtor (Services no Controller); uso do Service Container.
- **Convenções Laravel** — Form Requests, Facades onde faz sentido, Service Container; evitando over-engineering (interfaces apenas quando há múltiplas implementações).

### Padrões de implementação
- **BaseCrudController** — CRUD genérico com paginação, filtros, `include`, `search` e `sort` reutilizáveis.
- **Service layer** — regras de negócio concentradas em classes de serviço (ex.: Negócios, Contactos, Visitas, Tarefas, E-mail, Outlook).
- **Jobs** — tarefas assíncronas (chamadas, notificações, envio de e-mails em massa).
- **Listeners/Events** — reação a eventos (ex.: aplicar credenciais de e-mail dinâmicas).
- **Middleware** — autenticação (Sanctum), logging de pedidos, restrição por role (ex.: vendedor vs contactos).
- **Policy/Authorization** — controlo de acesso a recursos quando aplicável.

### Segurança e conformidade
- **Autenticação** — tokens Sanctum, refresh, logout.
- **Autorização** — roles e permissões (Spatie), políticas por recurso.
- **Proteção de dados (RGPD)** — endpoint de opt-out de consentimento (rota pública documentada).
- **2FA** — TOTP para utilizadores com MFA ativo.
- **SSO** — ligação/desliga de provedores OAuth (Socialite).

### Documentação e manutenção
- **OpenAPI/Swagger** — especificação e UI da API.
- **Documentação interna** — dezenas de ficheiros sobre SOLID, deployment, filas, e-mail, Outlook, logging, refatoração, relações de entidades, etc.
- **Refatoração** — análise SOLID, guias de refatoração e estado de implementação documentados.

---

## 💼 Competências evidenciadas

### Desenvolvimento backend
- API REST desenhada para consumo por clientes (web, mobile, integrações).
- Uso avançado de Laravel (Eloquent, relações, scopes, accessors, mutators).
- Integração com bases de dados relacionais (SQL Server) e com Redis.
- **Integração com ERP legado (PHC)** — leitura/escrita direta na base de dados, sincronização de dados, compatibilidade com autenticação e stored procedures.
- Filas, jobs e scheduler para processamento assíncrono e tarefas agendadas.
- E-mail e notificações (Mailables, Notifications, configuração dinâmica).

### Arquitetura e código
- Aplicação de princípios SOLID e padrões Laravel (Services, Form Requests, Resources).
- Abstração e reutilização (BaseCrudController, query services).
- Organização por domínio (CRM, Auth, User, Email, etc.).

### Infraestrutura e operação
- Docker e Docker Compose (multi-container: API, queue, scheduler, Redis, Nginx).
- Healthchecks e restarts configurados para serviços críticos.
- Scripts de automação (PowerShell) para deploy e verificação de saúde da API.
- Logging e, em dev, Telescope para diagnóstico.

### Integrações
- **Integração com ERP (PHC)** — sincronização bidirecional de dados, execução de stored procedures, compatibilidade com algoritmos de hash e autenticação do sistema legado.
- OAuth/SSO (Socialite).
- Integração com Microsoft Outlook (registar e associar e-mails).
- Envio de e-mail em massa com filas e controlo de carga.
- Export/import com PHPSpreadsheet.

### Soft skills e processo
- Documentação técnica contínua (setup, deployment, decisões, refatoração).
- **Trabalho com sistemas legados** — integração com ERP existente (PHC), mapeamento de esquemas complexos, compatibilidade com algoritmos e autenticação legados.
- Trabalho com código legado e evolução incremental (migrações, novos endpoints sem quebrar contrato).
- Atenção à segurança (auth, RBAC, RGPD, 2FA) e à observabilidade (logs, health, Telescope).

---

## Linguagens e formatos

- **PHP** — aplicação principal.
- **SQL** — migrações e scripts de inicialização (Docker).
- **YAML** — Docker Compose, configurações.
- **JSON** — composer, configurações, OpenAPI.
- **Markdown** — documentação.
- **PowerShell** — scripts de automação em Windows.
- **INI** — configuração PHP/OPcache no Docker.
- **Nginx config** — configuração do reverse proxy.

---

## 📚 Metodologias e práticas

- **Desenvolvimento iterativo** — evolução da API com versionamento e migrações.
- **Documentação como parte do produto** — OpenAPI + docs internos para onboarding e manutenção.
- **Refatoração guiada** — análises SOLID e guias de refatoração para melhorar estrutura sem alterar comportamento visível.
- **Deploy reproduzível** — Docker e scripts para ambientes consistentes (local, produção, IIS quando aplicável).
- **Observabilidade** — health checks, logging e, em dev, ferramentas de debugging (Telescope, Pail).

---

## 🎯 Resumo para recrutadores e entrevistas

O programador demonstra capacidade para:

- Desenhar e manter uma **API REST** de dimensão média-grande em **Laravel** e **PHP 8**.
- Aplicar **SOLID** e padrões Laravel (Services, Form Requests, Resources, Jobs).
- Trabalhar com **SQL Server**, **Redis**, **Docker** e **filas** em ambiente multi-serviço.
- **Integrar com sistemas ERP legados** (PHC) — sincronização de dados, stored procedures, compatibilidade com autenticação existente.
- Integrar **autenticação avançada** (tokens, 2FA, SSO) e **autorização** (roles/permissões).
- Documentar decisões técnicas e processos (OpenAPI, Markdown, guias de refatoração).
- Automatizar deploy e operação com **Docker** e **PowerShell**.

Este documento descreve **competências e tecnologias** utilizadas no projeto, sem revelar dados sensíveis do negócio ou da organização.

---

<p align="center">
    <a href="../README.md">
        <img 
            alt="Voltar ao Portfólio" 
            src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=for-the-badge"
        />
    </a>
    <a href="PORTFOLIO_PROJETO_CRM.md">
        <img 
            alt="Ver Aplicação Mobile →" 
            src="https://img.shields.io/badge/Ver%20App%20Mobile%20→-512BD4?style=for-the-badge&logo=dotnet&logoColor=white"
        />
    </a>
</p>
