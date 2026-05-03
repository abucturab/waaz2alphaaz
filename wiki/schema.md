# Wiki Schema

This file is the master configuration for this wiki. Any LLM reading this wiki MUST read this file first before performing any operation (ingest, query, lint, update).

## What This Wiki Is

> **Fill in:** One paragraph describing what project/domain this wiki covers, who owns it, and what it is NOT meant to capture.

<!-- To be filled in once the project scope is defined. -->

## Directory Structure

| Directory | What lives here |
|---|---|
| `entities/` | The primary "things" in this domain (blocks, modules, services, components, agents…). One page per entity. |
| `concepts/` | Ideas, patterns, methodologies, and principles relevant to this domain. |
| `processes/` | Workflows, procedures, and how-to guides. Step-by-step operational knowledge. |
| `artifacts/` | Key deliverables and outputs: plans, reports, specs, checklists. |
| `references/` | Pointers to external specs, standards, tools, datasheets. Not summaries — just annotated links and location pointers. |
| `glossary/` | Acronyms and term definitions. Always update here when a new term appears. |
| `templates/` | Prompt templates for LLM operations on this wiki. |
| `scripts/` | Shell helpers for batch operations. |

## Naming Conventions

- File names: `lowercase_with_underscores.md`
- Entity pages: named after the entity (e.g. `usb_controller.md`, `auth_service.md`)
- Template stubs: prefixed with `_` (e.g. `_template.md`)
- Index files: `_index.md` for directory-level overviews

## Page Structure Rules

Every non-template page MUST have:
1. A `# Title` as the first line
2. A one-line `> Summary:` blockquote immediately after the title
3. A `## Cross-references` section at the bottom linking to related pages

## Cross-linking Rules

- Use relative markdown links: `[Entity Name](../entities/entity_name.md)`
- When you create or update a page, check if any existing page should link back to it
- Update `index.md` whenever a new page is created

## Operations

### Ingest
When ingesting a new source file:
1. Read `schema.md` (this file) first
2. Determine which directories are affected (usually `entities/` and one other)
3. Create or update the relevant pages
4. Update `index.md` with new entries
5. Append a one-line record to `log.md`

### Query
When answering a question:
1. Search `index.md` for relevant sections
2. Read the relevant pages
3. Synthesize an answer
4. Optionally: save the answer as a new page in `artifacts/` if it is non-trivial

### Lint
When health-checking the wiki:
1. Find pages missing `## Cross-references`
2. Find links that point to non-existent files
3. Find `index.md` entries with no corresponding file
4. Find pages older than 90 days with no updates (flag for review)
5. Report findings — do NOT auto-fix without human review

## What NOT to Put in This Wiki

- Raw source files or file dumps
- Information already captured verbatim in a spec or formal document (just link to it)
- Opinions, speculation, or unverified claims (mark clearly if included)
- Secrets, credentials, or access tokens
