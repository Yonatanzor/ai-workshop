# Session 5 — Retrieval-Augmented Generation (RAG)

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (seven published immunotherapy papers — all public)  
**API:** NVIDIA build.nvidia.com (free tier sufficient)

---

## What students leave with

A working RAG pipeline they built step by step, and a clear mental model of why RAG fails — and when a long context window is a better answer.

## The question

> Seven published trials of immunotherapy for mismatch-repair-deficient (dMMR) endometrial cancer. Which patients benefit most, and what do the trials disagree on?

Students build a small retrieval pipeline over the seven papers, then interrogate it with clinical questions and examine where it goes wrong.

## Learning outcomes

- Implement a TF-IDF retrieval step over a small corpus of PDFs
- Understand how the retrieved chunks affect the model's answer
- Identify retrieval failures: wrong chunk retrieved, answer not in corpus, model confabulates

## Session structure

| Time | Activity |
|---|---|
| 0–15 min | Recap: how retrieval-augmented generation works |
| 15–45 min | Notebook Part 1–3: connect → chunk → embed → retrieve |
| 45–75 min | Notebook Part 4–5: query the pipeline, compare answers with and without retrieval |
| 75–90 min | Challenge: citation audit — does the retrieved chunk actually say that? |

## Materials

| File | Description |
|---|---|
| [`Session_5_RAG_v2.ipynb`](Session_5_RAG_v2.ipynb) | Main hands-on notebook (place papers in a `papers/` subfolder) |
| [`Session_5_RAG.pptx`](Session_5_RAG.pptx) | Session slides |

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S5/Session_5_RAG_v2.ipynb)

## Papers used in this session

Access these through your institutional library — do not upload them to public AI tools:

| Paper | DOI |
|---|---|
| Le et al. (2017). *Science* | [10.1126/science.aan6733](https://doi.org/10.1126/science.aan6733) |
| GARNET trial. *JITC* 2022 | [10.1136/jitc-2021-004042](https://doi.org/10.1136/jitc-2021-004042) |
| KEYNOTE-158 endometrial. *JCO* 2022 | [10.1200/JCO.21.02167](https://doi.org/10.1200/JCO.21.02167) |
| RUBY trial. *NEJM* 2023 | [10.1056/NEJMoa2301583](https://doi.org/10.1056/NEJMoa2301583) |
| NRG-GY018. *NEJM* 2023 | [10.1056/NEJMoa2302312](https://doi.org/10.1056/NEJMoa2302312) |
| Chow et al. *Cancer Discovery* 2023 | [10.1158/2159-8290.CD-23-0146](https://doi.org/10.1158/2159-8290.CD-23-0146) |
| NRG-GY018 OS update. *Nature Medicine* 2025 | [10.1038/s41591-025-03484-6](https://doi.org/10.1038/s41591-025-03484-6) |
## Critical-thinking challenge

After running the pipeline, students pick one answer it gave and manually check the retrieved chunk it used. They ask: does the chunk actually support the answer, or did the model add something that isn't there?
