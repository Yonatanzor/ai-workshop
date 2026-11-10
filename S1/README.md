# Session 1 — The AI Landscape

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (public tools, public sources only)

---

## What students leave with

A map of what AI can do today, the difference between open and closed models, a framework for deciding whether AI is the right tool at all, and their first entry in the failure log.

## Learning outcomes

- Name the main families of AI use: chat assistants, evidence tools, coding and data analysis, agents, scientific models, clinical AI, generated media
- Distinguish open from closed models and explain why an open model that runs inside the institution matters for confidential data
- Apply four tests to decide whether a task calls for AI, traditional software, or both

## Session structure

| Time | Activity |
|---|---|
| 0–10 min | Course overview: nine families, two threads, the capstone showcase, the failure log |
| 10–20 min | Recap of the AI day: how a language model produces text (prediction, not lookup); machine learning vs. deep learning |
| 20–40 min | The map: AI families, Hugging Face as the hub for open models |
| 40–60 min | Guided lab — card sort in groups of three (mixing biology and CS backgrounds): 12 research and clinical tasks sorted into AI, traditional, or hybrid |
| 60–80 min | Challenge: the headline audit |
| 80–90 min | The data rule and three tiers; first failure-log entry |

## The four tests before reaching for AI

1. **Is the task fixed or open-ended?** A fixed rule or formula favours traditional software. Open-ended language or pattern tasks favour AI.
2. **Can the answer be checked?** If you cannot verify the output, AI is risky however good it sounds.
3. **What does an error cost?** A wrong email is cheap. A wrong dose or a wrong statistic is not.
4. **How sensitive is the data?** Tier 3 and Tier 4 data rule out public AI tools, whatever the task.

## Materials

| File | Description |
|---|---|
| [`Session_1_final.pptx`](Session_1_final.pptx) | Session slides |
| [`AI workshop curriculum.pdf`](AI%20workshop%20curriculum.pdf) | Full curriculum overview (PDF) |

## Critical-thinking challenge

The **headline audit.** Groups receive four claims about medical AI from news stories or abstracts. For each, they write the evidence they would need before believing it, guided by the red-flag checklist:

- Accuracy reported above 99%
- No external test set
- No comparison with a simple baseline
