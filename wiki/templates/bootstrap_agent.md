# Bootstrap Agent Prompt

Paste everything between the triple dashes into your CLI agent.
Fill in the two paths before pasting — that's the only thing you need to do.

---

```
WIKI_PATH = [absolute path to this wiki directory]
CODEBASE_PATH = [absolute path to the codebase you want to document]

You are setting up a persistent knowledge wiki for a codebase. Your job is to survey the codebase, understand what it contains, and populate the wiki with what you find. The wiki is plain markdown — no special tooling required.

---

STEP 1 — Understand the wiki structure.

Read the file at WIKI_PATH/schema.md completely before doing anything else. It defines the directories, naming rules, page structure, and what belongs where. Follow it exactly.

---

STEP 2 — Survey the codebase. Do a broad, systematic sweep of CODEBASE_PATH.

Find answers to these questions:
- What kind of project is this? What does it do?
- What are the top-level directories and what does each contain?
- What are the primary "things" (entities) in this codebase — the main components, modules, services, agents, blocks, or other named units?
- What tools, scripts, or automation are present?
- Are there any existing docs, READMEs, specs, or config files that describe the system?
- What languages and frameworks are in use?

Do not read every file. Skim directory structure, README files, top-level configs, and representative files. Breadth first, depth second.

---

STEP 3 — Fill in WIKI_PATH/schema.md.

Find the section marked "What This Wiki Is" and write 2–3 sentences describing:
- What this project is and what it does
- Who this wiki is for
- What it does NOT cover

Leave everything else in schema.md unchanged.

---

STEP 4 — Create entity pages.

For each major entity you identified in Step 2, create a markdown file in WIKI_PATH/entities/ named in lowercase_with_underscores.md.

Use WIKI_PATH/entities/_template.md as the structure for every page.

Rules:
- One file per entity. Do not nest.
- Synthesize — do not paste raw file contents.
- Write only what you can verify from the codebase. Mark anything uncertain with the comment <!-- unverified -->.
- If something is unknown, write "Unknown — needs investigation." Do not guess.
- Aim for one stub page per entity rather than one deep page for a few.

---

STEP 5 — Add domain acronyms.

Open WIKI_PATH/glossary/acronyms.md. Add any project-specific or domain-specific acronyms you encountered, using the existing table format.

---

STEP 6 — Update the index.

Open WIKI_PATH/index.md. Under the "Entities" section, add one line per entity page you created:
[Entity Name](entities/filename.md) — one-sentence description

---

STEP 7 — Append to the log.

Open WIKI_PATH/log.md and append one line at the bottom:
[TODAY'S DATE] INGEST [CODEBASE_PATH] — Bootstrap: initial wiki population from codebase survey. [N] entity pages created.

---

When you are done, print a short summary:
- How many entity pages were created
- What the project is (one sentence)
- Any areas where the wiki is thin and needs follow-up ingestion
```

---
