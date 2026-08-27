# 📱 Projeto CRM — Aplicação Multiplataforma

<p align="left">
    <a href="../README.md">
        <img 
            alt="Voltar ao Portfólio" 
            src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=flat-square"
        />
    </a>
    <a href="PORTFOLIO_PROJETO_CRM_API.md">
        <img 
            alt="Ver API Backend" 
            src="https://img.shields.io/badge/Ver%20API%20Backend-FF2D20?style=flat-square&logo=laravel&logoColor=white"
        />
    </a>
</p>

Documento de portfólio que descreve o âmbito técnico do projeto, as competências utilizadas e a dimensão do trabalho realizado, sem expor detalhes sensíveis do negócio.

<p align="left">
    <img 
        alt=".NET MAUI" 
        src="https://img.shields.io/badge/.NET%20MAUI-512BD4?style=for-the-badge&logo=dotnet&logoColor=white"
    />
    <img 
        alt="Blazor" 
        src="https://img.shields.io/badge/Blazor-512BD4?style=for-the-badge&logo=blazor&logoColor=white"
    />
    <img 
        alt="C#" 
        src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white"
    />
    <img 
        alt="Multiplataforma" 
        src="https://img.shields.io/badge/Multiplataforma-Android%20%7C%20iOS%20%7C%20Windows%20%7C%20Mac-3DDC84?style=for-the-badge"
    />
</p>

<!-- GITHUB_REPO_STATS_START -->
## 🔗 Dados GitHub (repositórios reais)

_Métricas agregadas por origem (conta pessoal ou organização), sem nomes de repositórios._

<p align="left"><img alt="Repositórios" src="https://img.shields.io/badge/Repositórios-2-blue?style=flat-square&logo=github" /> <img alt="Commits" src="https://img.shields.io/badge/Commits-16-green?style=flat-square" /> <img alt="Tamanho" src="https://img.shields.io/badge/Tamanho-273MB+-informational?style=flat-square" /> </p>

| Origem | Visibilidade | Linguagem | Commits |
|--------|--------------|-----------|---------|
| Conta pessoal | privado | CSS | 14 |
| Conta pessoal | privado | C# | 2 |

**Distribuição de linguagens (média ponderada):** CSS (37%), HTML (35%), C# (27%), JavaScript (1%), PowerShell (0%)
<!-- GITHUB_REPO_STATS_END -->

---

## Visão geral

Aplicação **híbrida** de gestão (CRM) desenvolvida em **.NET MAUI** com **Blazor**, destinada a equipas de campo e escritório. Funciona em **Android**, **iOS**, **Windows** e **Mac Catalyst** a partir de um único código-base, consumindo uma API REST externa e integrando serviços como Microsoft Graph (email) e geolocalização.

---

## 📊 Dimensão do projeto (estatísticas)

<p align="left">
    <img 
        alt="Ficheiros C#" 
        src="https://img.shields.io/badge/Ficheiros%20C%23-111-blue?style=flat-square"
    />
    <img 
        alt="Componentes Blazor" 
        src="https://img.shields.io/badge/Componentes%20Blazor-66-blue?style=flat-square"
    />
    <img 
        alt="Linhas de Código" 
        src="https://img.shields.io/badge/Linhas%20de%20Código-40k%2B-success?style=flat-square"
    />
    <img 
        alt="Páginas" 
        src="https://img.shields.io/badge/Páginas-50%2B-orange?style=flat-square"
    />
</p>

| Métrica | Valor |
|--------|--------|
| **Ficheiros C#** | ~111 |
| **Componentes Blazor (.razor)** | ~66 |
| **Páginas/layouts XAML** | 5 |
| **Ficheiros CSS** (incl. isolados por componente) | ~54 |
| **Scripts JavaScript** (wwwroot) | 5 |
| **Linhas de código** (C#, Razor, XAML) | ~40 000+ |
| **Serviços + interfaces** | 22 pares (44 ficheiros) |
| **DTOs e modelos** | ~45 |
| **Páginas/ecrãs principais** | 50+ |
| **Documentos técnicos (docs/)** | 45+ |

O projeto está organizado em **Components** (Blazor), **Services**, **Models**, **Platforms**, **Utils** e **wwwroot**, com documentação técnica contínua em `docs/`.

---

## 📑 Índice

- [Visão geral](#visão-geral)
- [Dimensão do projeto](#-dimensão-do-projeto-estatísticas)
- [Stack tecnológica](#️-stack-tecnológica)
- [Arquitetura e padrões](#️-arquitetura-e-padrões)
- [Princípios e metodologias](#-princípios-e-metodologias)
- [Competências demonstradas](#-competências-demonstradas)
- [Funcionalidades](#-funcionalidades-resumo-técnico)
- [Conclusão](#conclusão)

---

## 🛠️ Stack tecnológica

### Core

- **.NET 9**
- **.NET MAUI** (Multi-platform App UI) — UI nativa multiplataforma
- **Blazor Hybrid** (Blazor WebView no MAUI) — UI principal com componentes reutilizáveis
- **C#** com `nullable reference types` e `ImplicitUsings`

### UI e componentes

- **Radzen Blazor** (8.x) — DataGrid, formulários, diálogos, notificações, menus
- **Bootstrap** e **Bootstrap Icons** (wwwroot)
- **CSS isolado** por componente (`.razor.css`)
- **XAML** em pontos específicos (ex.: splash, scanner de códigos)

### Comunicação e API

- **HttpClient** e **IHttpClientFactory** — consumo de API REST
- **System.Text.Json** — serialização/deserialização com conversores customizados
- Integração com **API REST** (Laravel) — autenticação (Sanctum), CRUD e endpoints específicos

### Autenticação e integrações

- **Laravel Sanctum** — login, refresh de token, recuperação de senha (código de verificação)
- **Microsoft Identity (MSAL)** e **Microsoft Graph** — integração com contas Microsoft (email/Outlook)
- **SecureStorage** (MAUI) — armazenamento seguro de tokens

### Dispositivo e sensores

- **ZXing.Net.Maui** — leitura de códigos de barras e QR
- **Geolocation** (MAUI Essentials) — GPS
- **Geocodificação reversa** — serviço externo (ex.: Nominatim/OpenStreetMap) via `HttpClient` dedicado
- **Clipboard** — deteção de códigos de verificação

### Configuração e qualidade

- **Microsoft.Extensions.Configuration** — `appsettings` por ambiente (Development/Production)
- **Microsoft.Extensions.Logging** — logging estruturado com `ILogger<T>`
- **CommunityToolkit.Mvvm** — suporte a padrões MVVM onde aplicável

---

## 🏗️ Arquitetura e padrões

### Injeção de dependências

- **MauiProgram.cs** como composição raiz: todos os serviços registados aqui
- **HttpClient** por serviço via `AddHttpClient<TInterface, TImplementation>` (evitar instâncias soltas)
- **Scoped**: serviços Radzen (Dialog, Notification, etc.) e alguns de domínio
- **Singleton**: serviços de dispositivo (geolocalização, scanner, clipboard, Graph auth)
- **Transient**: páginas e PageModels XAML

### Serviços e contratos

- **Interface por serviço** (ex.: `IAuthService` / `AuthService`) — testabilidade e inversão de dependência
- Serviços de API: recebem `HttpClient` injetado, leem configuração (`IConfiguration`) e tokens via `IAuthService`
- **Um HttpClient nomeado** para geocodificação (base URL e headers específicos)

### Modelos e DTOs

- **DTOs** para requests/responses da API (Create/Update quando necessário)
- **JsonPropertyName** para mapear `snake_case` da API para propriedades C#
- **Conversores JSON** customizados (datas Laravel, IDs em string, decimais, booleanos nullable)
- Separação entre modelos de **Auth**, **DTOs** e **Enums**

### UI (Blazor)

- **Layouts**: MainLayout, EmptyLayout, NavMenu
- **Rotas** centralizadas (Router + RouteView), página 404 customizada
- **Componentes partilhados**: Header, ConfirmDialog, modais de edição, formulários reutilizáveis, QrScanner, MapView, etc.
- **Dashboards** por perfil (Admin, Gestor Comercial, Vendedor)
- **CSS isolado** por componente para evitar conflitos

### Segurança e boas práticas

- Tokens em **SecureStorage**; não logar senhas ou tokens completos
- **Headers** HTTP (Accept, X-Requested-With) configurados na composição, não espalhados nos serviços
- **Timeout** e tratamento de erros (ex.: HttpRequestException, TaskCanceledException) em chamadas HTTP
- **Validação** e mensagens de erro claras nos formulários

---

## 📐 Princípios e metodologias

- **SOLID**: interfaces para serviços, responsabilidades bem definidas (auth, clientes, contactos, vendas, tarefas, visitas, stock, etc.)
- **Async/await** em toda a I/O; convenção de sufixo `Async` e evitar `.Result`/`.Wait()`
- **Configuração por ambiente** (URLs de API diferentes por plataforma e emulador vs dispositivo)
- **Documentação contínua**: pasta `docs/` com decisões, correções, configuração de API, autenticação, Outlook, dashboards, etc.
- **Convenções de código** definidas (ex.: `.cursorrules`) — nomenclatura, estrutura de pastas, padrão de serviços, integração com API
- **Multiplataforma** considerada desde o início (Android, iOS, Windows, Mac Catalyst) com configurações específicas por plataforma (ex.: Android emulator vs device)

---

## 💼 Competências demonstradas

### Desenvolvimento

- **C#** avançado: genéricos, async, nullable, atributos, conversores JSON
- **.NET MAUI**: ciclo de vida, recursos, plataformas, Essentials (SecureStorage, Geolocation, etc.)
- **Blazor**: componentes, binding, layouts, rotas, injeção de dependências, CSS isolado
- **REST**: desenho de clientes HTTP, tratamento de erros e códigos de estado, serialização JSON
- **Autenticação**: tokens, refresh, recuperação de senha com código, integração com Azure AD / MSAL e Microsoft Graph

### Integração e APIs

- Consumo de **API REST** (Laravel) com convenções (snake_case, datas, IDs)
- **Microsoft Graph** (email): autenticação OAuth e operações de correio
- **Serviços externos** (geocodificação) com `HttpClient` dedicado e respeito por políticas de uso (ex.: User-Agent)

### UI/UX

- **Radzen Blazor**: grids, formulários, diálogos, notificações
- **Responsividade** e consistência entre plataformas
- **Acessibilidade** básica (ex.: FocusOnNavigate, títulos de página)

### DevOps e qualidade

- **Configuração** multi-ambiente (appsettings, variáveis por plataforma)
- **Logging** estruturado e redação de dados sensíveis
- **Build** multi-target (Android, iOS, Windows, Mac Catalyst) e otimizações de Debug (MAUI)
- **Documentação** técnica e resolução de problemas registada em Markdown

### Soft skills implícitas

- Organização de código em pastas e namespaces
- Manutenção de um projeto de dimensão considerável ao longo do tempo
- Resolução de problemas de integração (API, auth, Outlook, Android) com documentação das soluções

---

## ⚡ Funcionalidades (resumo técnico)

- **Autenticação**: login, refresh, logout, recuperação de senha com código (Forgot → Verify → Reset), splash com verificação de sessão
- **Dashboards** por perfil (Admin, Gestor Comercial, Vendedor)
- **CRUD** e listagens: contactos/leads, clientes, vendas, tarefas, visitas, dossiers, contas, ocorrências
- **Detalhes e formulários** reutilizáveis (modais e páginas dedicadas)
- **Integração de email** (Microsoft Graph): leitura e envio no contexto da aplicação
- **Geolocalização** e mapas (lista e mapa de contactos/clientes)
- **Scanner** de códigos de barras/QR (ZXing) integrado em fluxos da app
- **Stock e artigos**: consulta de ficha e stock (API)
- **Negociações**: fluxo de negócio com fases e ações automáticas (ex.: criação de visita/tarefa)
- **Configurações**: perfil, definições da app, integração Outlook (Azure AD)
- **Documentação**: dezenas de ficheiros em `docs/` sobre API, auth, Outlook, dashboards, correções e configuração

---

## Conclusão

Este projeto ilustra capacidade para desenvolver e manter uma **aplicação multiplataforma de média/grande dimensão** em .NET MAUI e Blazor, com:

- Consumo robusto de **API REST** e integração com **Microsoft Graph**
- Uso consistente de **injeção de dependências**, **interfaces** e **async/await**
- Atenção a **segurança** (tokens, logging), **configuração** e **documentação**
- Cobertura de **Android**, **iOS**, **Windows** e **Mac Catalyst** a partir de um único repositório

As tecnologias e padrões utilizados estão alinhados com o que o mercado espera em projetos .NET modernos, aplicações híbridas e integração com ecossistema Microsoft e APIs REST.

---

<p align="center">
    <a href="../README.md">
        <img 
            alt="Voltar ao Portfólio" 
            src="https://img.shields.io/badge/←%20Voltar%20ao%20Portfólio-0D1117?style=for-the-badge"
        />
    </a>
    <a href="PORTFOLIO_PROJETO_CRM_API.md">
        <img 
            alt="Ver API Backend" 
            src="https://img.shields.io/badge/Ver%20API%20Backend%20→-FF2D20?style=for-the-badge&logo=laravel&logoColor=white"
        />
    </a>
</p>
