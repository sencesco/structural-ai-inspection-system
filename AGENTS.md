# AGENTS.md

## Communication style

When user asks for compressed answers, brief mode, caveman mode, or token-saving mode, use the `caveman` skill if available.

Do not use caveman style for dangerous commands, irreversible operations, or instructions where compression may cause ambiguity.

## Agent Working Rules

This is the main project brain.

All coding agents must read:
- AGENTS.md
- SKILL.md

Tool-specific files such as CLAUDE.md, Cursor rules, Codex config, and Antigravity skills should be thin pointers only.

MCP servers are allowed only when they provide real external tool access.

1. Read this file first.
2. Do not scan the whole repository by default.
3. For any task, inspect only:
   - this file
   - the relevant `docs/agent/*.md`
   - Use `skills/` only for repeated task workflows.
   - directly affected source files
   - related tests
4. Prefer small, reviewable changes.
5. Do not introduce paid cloud dependencies.
6. Keep the project portfolio-friendly and explainable to recruiters.
7. Preserve separation between:
   - ML logic
   - RAG logic
   - LLM agent orchestration
   - API layer
   - frontend layer
   - contracts/schemas
   - ops/deployment

## Purpose

This repository is a portfolio-grade Structural AI Inspection System.

It combines:
- FastAPI backend
- Next.js frontend
- ML/CV damage detection
- sensor analytics
- RAG guideline retrieval
- agentic repair-priority reasoning
- inspection report generation
- testing, logging, and deployment foundations

Agents should treat this file as the canonical project brain.

## Repository Map

- `apps/api/` — FastAPI backend
- `apps/web/` — Next.js frontend
- `ml/` — ML pipelines, inference, evaluation, model registry placeholders
- `rag/` — document ingestion, embeddings, retriever, guideline knowledge
- `agents/` — LLM agents, tools, prompts
- `contracts/` — shared schemas and DTOs
- `tests/` — unit, integration, and e2e tests
- `ops/` — Docker, Makefile, CI/CD, monitoring config
- `logs/` — local runtime logs, gitignored
- `docs/` — architecture notes, ADRs, diagrams, agent context


## Current Architecture Intent

The system should demonstrate both AI Engineering and Software Engineering.

Core pipeline:

1. Upload inspection data/image/sensor input
2. Detect or analyze structural damage
3. Retrieve relevant guideline/context through RAG
4. Calculate severity and repair priority
5. Generate inspection report
6. Expose result through API and frontend
7. Log inference, agent steps, errors, and app events

## Build and Run Commands

Use these only when relevant.

```bash
make dev
make test
make lint
docker compose up
```

<!-- code-review-graph MCP tools -->
## MCP Tools: code-review-graph

**IMPORTANT: This project has a knowledge graph. ALWAYS use the
code-review-graph MCP tools BEFORE using Grep/Glob/Read to explore
the codebase.** The graph is faster, cheaper (fewer tokens), and gives
you structural context (callers, dependents, test coverage) that file
scanning cannot.

### When to use graph tools FIRST

- **Exploring code**: `semantic_search_nodes` or `query_graph` instead of Grep
- **Understanding impact**: `get_impact_radius` instead of manually tracing imports
- **Code review**: `detect_changes` + `get_review_context` instead of reading entire files
- **Finding relationships**: `query_graph` with callers_of/callees_of/imports_of/tests_for
- **Architecture questions**: `get_architecture_overview` + `list_communities`

Fall back to Grep/Glob/Read **only** when the graph doesn't cover what you need.

### Key Tools

| Tool | Use when |
| ------ | ---------- |
| `detect_changes` | Reviewing code changes — gives risk-scored analysis |
| `get_review_context` | Need source snippets for review — token-efficient |
| `get_impact_radius` | Understanding blast radius of a change |
| `get_affected_flows` | Finding which execution paths are impacted |
| `query_graph` | Tracing callers, callees, imports, tests, dependencies |
| `semantic_search_nodes` | Finding functions/classes by name or keyword |
| `get_architecture_overview` | Understanding high-level codebase structure |
| `refactor_tool` | Planning renames, finding dead code |

### Workflow

1. The graph auto-updates on file changes (via hooks).
2. Use `detect_changes` for code review.
3. Use `get_affected_flows` to understand impact.
4. Use `query_graph` pattern="tests_for" to check coverage.

## External Documentation Rule

When working with library/API/framework code, setup, configuration, or version-sensitive implementation details, use Context7 before coding or modifying files.

Use Context7 especially for:
- Next.js / React / TypeScript
- FastAPI / Pydantic / Python packaging
- LangChain / LangGraph / RAG frameworks
- Vector databases and embedding libraries
- Docker / Kubernetes / CI tooling
- Testing frameworks
- ML/DL libraries when API behavior may have changed

Prefer exact library IDs when known, for example:
- /vercel/next.js
- /fastapi/fastapi
- /pydantic/pydantic

## Frontend Design Skill

For frontend UI, layout, visual design, dashboards, pages, components, styling, animation, or design polish:

1. Read `SKILL.md` first.
2. Apply it as frontend design guidance.
3. Keep architecture, folder structure, and engineering rules controlled by this `AGENTS.md`.
4. Do not duplicate `SKILL.md` content into `CLAUDE.md`, Cursor rules, or other agent files.
