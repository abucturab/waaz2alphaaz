# Ingest Prompt Template

Copy this prompt into your LLM, followed by the source file(s) you want to ingest.

---

```
You are maintaining a persistent knowledge wiki. Before doing anything else, read `schema.md` in the wiki root — it tells you the structure, naming rules, and what belongs where.

I am giving you the following source file(s) to ingest:
[PASTE FILE(S) HERE]

Your task:
1. Identify which wiki pages need to be created or updated based on the content of these files.
2. For each affected page, produce the full updated markdown content (use the `_template.md` in the relevant directory as your structure guide).
3. Update `index.md` with any new page entries.
4. Append a one-line record to `log.md` in the format: [DATE] INGEST [files touched] — [summary].

Rules:
- Synthesize, don't dump. Summarize and extract key knowledge — do not copy-paste raw source content.
- Cross-link aggressively. If a page mentions something that has its own page, link to it.
- If you are unsure which directory something belongs in, default to `entities/` and note the uncertainty in the page.
- Do NOT invent information not present in the source files.
```
