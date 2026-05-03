# Lint Prompt Template

Copy this prompt periodically to health-check the wiki.

---

```
You are performing a health check on a persistent knowledge wiki. Read `schema.md` first, then audit the wiki for the following issues:

1. **Broken links** — markdown links that point to files that don't exist
2. **Missing cross-references** — pages that mention an entity/concept that has a wiki page but don't link to it
3. **Orphaned pages** — pages that exist but are not listed in `index.md`
4. **Missing sections** — pages that are missing required sections from their `_template.md`
5. **Stale pages** — pages with no updates in 90+ days that cover evolving topics (flag for human review)
6. **Contradictions** — statements on different pages that conflict with each other

Report your findings as a numbered list with: file path, issue type, and a one-line description.
Do NOT auto-fix anything — only report. Human review is required before changes.

Append a one-line record to `log.md`: [DATE] LINT [] — [summary of findings, e.g. "3 broken links, 1 orphan, 0 contradictions"].
```
