# Query Prompt Template

Copy this prompt into your LLM when you want to query the wiki.

---

```
You are answering a question using a persistent knowledge wiki. Before answering, read `schema.md` and `index.md` to understand what knowledge is available and where it lives.

My question: [YOUR QUESTION HERE]

Your task:
1. Search `index.md` for relevant sections.
2. Read the relevant wiki pages.
3. Synthesize a clear, direct answer grounded in what the wiki contains.
4. If the wiki does not have enough information to answer, say so explicitly — do not hallucinate.
5. If your answer reveals a gap in the wiki (something that should be documented but isn't), note it at the end as: "Wiki gap: [description]".

Optionally: if this answer is non-trivial and useful to preserve, save it as a new page in `artifacts/` and add it to `index.md`.
```
