# SKILL.md

## Agent Skill Memory

This file stores reusable workflows and learned operating behavior for agents.

## Token Discipline

When the task is simple, debugging-focused, or review-focused:
- Prefer concise answers.
- Avoid long explanations unless requested.
- Keep commands, paths, filenames, APIs, schemas, and code exact.
- Do not compress technical identifiers.
- Use Caveman or similar concise mode when available.

## RTK Usage

Prefer RTK wrappers for shell/file/test/git commands to reduce terminal output tokens.

Use:
- `rtk git status` instead of `git status`
- `rtk git diff` instead of `git diff`
- `rtk read <file>` instead of `cat <file>`
- `rtk grep <pattern> <path>` instead of raw recursive grep
- `rtk find <pattern>` instead of broad file listing
- `rtk pytest` instead of raw pytest when checking tests
- `rtk log <file>` instead of reading full logs

## MCP Boundary

Use MCP only for external tools and data access:
- GitHub
- filesystem
- browser / Playwright
- database
- documentation search
- issue tracker
- vector database

Do not use MCP for general project memory.
Do not use MCP only to store instructions.

## Context7 Usage

Context7 is used as the external live-documentation tool.

Use it when:
- implementing library/API-specific code
- checking current setup/configuration
- fixing errors caused by outdated API assumptions
- comparing framework patterns

Do not store Context7 results as permanent truth unless verified and summarized as project-specific learned knowledge.

## Frontend Design

For frontend design work, use this local reference:

`.claude/skills/frontend-design/skill.md`

This file is copied from Anthropic's frontend-design skill, but it is intentionally saved as lowercase `skill.md`.

Reason:
- This project uses multiple agent providers such as Codex, Claude Code, and Cursor.
- `SKILL.md` at the project root is the shared project skill memory.
- Provider-specific folders such as `.claude/` are references only.
- Do not symlink this file to root `SKILL.md`.

## RAG Ingestion Skill

Use this when adding or modifying document ingestion.

Steps:
1. Add parser logic in `rag/ingestion/`
2. Add chunking logic
3. Add embedding integration
4. Add retriever test
5. Update sample knowledge document
6. Run RAG retrieval test



