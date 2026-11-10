# AI for MD-PhD Students — An Exposure Curriculum in 9 Sessions

> **Nine 90-minute sessions** that show first-semester MD-PhD students the main families of AI use in research and medicine, let them try each one hands-on, and train them to question every tool they meet.

Developed at the **Weizmann Institute of Science, MD-PhD Program** · Last updated October 2026

---

## What this course is

Each session covers one family of AI use and follows the same rhythm:

| Phase | Duration | What happens |
|---|---|---|
| Concepts + live demo | ~20 min | Instructor introduces the tool family |
| Hands-on | ~40 min | Students work on the notebook, ideally on their own research |
| Critical-thinking challenge | ~20 min | A structured exercise around how that session's tool fails |
| Share-out + failure log | ~10 min | Groups report back; each student logs one AI failure |

**Two threads run through every session:** critical thinking and data confidentiality.  
**The course ends** with a capstone showcase: each student presents one AI workflow they have adopted and the failures they found in it.

---

## Sessions

| # | Session | Notebook | Slides |
|---|---|---|---|
| S0 | [Introduction & Simulation Day](S0/) | [Open in Colab](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S0/AI_Workshop.ipynb) | — |
| S1 | [The AI Landscape](S1/) | — | [Slides](S1/Session_1_final.pptx) |
| S2 | [Reviewing AI-Written Code](S2/) | [Student](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S2/Session_2_Reviewing_AI_Code_STUDENT.ipynb) · [Master](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S2/Session_2_Reviewing_AI_Code_MASTER.ipynb) | [Slides](S2/Session_2_Reviewing_AI_Code.pptx) |
| S3 | [One Paper, Many Audiences](S3/) | — | [Slides](S3/Session_3_One_Paper_Many_Audiences.pptx) |
| S4 | [Build a Guardrailed Assistant](S4/) | [Open in Colab](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S4/Session_4_Assistant_API.ipynb) | [Slides](S4/Session_4_Write_the_Rules_Once.pptx) |
| S5 | [Retrieval-Augmented Generation](S5/) | [Open in Colab](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S5/Session_5_RAG_v2.ipynb) | [Slides](S5/Session_5_RAG.pptx) |
| S6 | [Build an Agent](S6/) | [Student](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S6/Session_6_Build_an_Agent.ipynb) · [Instructor](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S6/Session_6_Build_an_Agent_INSTRUCTOR.ipynb) | [Slides](S6/Session_6_Agents.pptx) |
| S7 | [Vibe Coding & Rapid Prototyping](S7/) | — | [Slides](S7/Session_7_Vibe_Coding.pptx) |
| S8 | [From Workshop to Project](S8/) | — | [Slides](S8/Session_8_From_Workshop_to_Project.pptx) |

> **Replace `Yonatanzor/ai-workshop`** in the Colab links above with your actual GitHub username/org and repository name.

---

## Critical thinking in every session

Critical thinking is practised, not lectured. Every session ends with a challenge built around how that day's tool fails, and every student keeps a **failure log** — one AI failure per session: the tool, what they asked, what went wrong, how they caught it.

Students ask these five questions of every tool, in every session, until they are a habit:

1. What was it trained on, or given to read?
2. How would I know if this is wrong?
3. Who or what is missing from its data?
4. What did using it cost — privacy, time, or a skill I did not practise?
5. Would a non-AI method do this better?

---

## Data confidentiality

The course data rule: **no identifiable patient data and no unpublished lab data in any public AI tool.**

| Data | What the AI may see | The human's role |
|---|---|---|
| Published papers, public datasets | Any approved tool | Spot-checks output and sources |
| De-identified research data | Structure only; code runs where data lives | Verifies results a second way |
| Identifiable patient / unpublished lab data | Nothing in public tools | Approves every input and output |
| Anything affecting a patient decision | Drafts only, never actions | A qualified clinician decides |

---

## Prerequisites

- A Google account (for Colab)
- An [NVIDIA build.nvidia.com](https://build.nvidia.com) API key (Sessions 4, 5, 6 — free tier is sufficient)
- No prior programming experience required for Sessions 1–3; basic Python familiarity helps from Session 4 onward

---

## Repository structure

```
/
├── S0/   Introduction & simulation day
├── S1/   The AI landscape
├── S2/   Reviewing AI-written code
├── S3/   One paper, many audiences
├── S4/   Guardrailed assistants (Assistant API)
├── S5/   Retrieval-augmented generation
├── S6/   Agents — tools, loop, supervisor
├── S7/   Vibe coding & rapid prototyping
└── S8/   From workshop to project (capstone)
```

---

## Citation

If you use or adapt this curriculum, please cite:

> *AI for MD-PhD Students: An Exposure Curriculum in 9 Sessions.* Weizmann Institute of Science MD-PhD Program, 2026.

---

## License

Materials in this repository are shared for educational use. The scientific papers in the `S3/`, `S5/` folders remain under their original publishers' copyright — please access them through your institutional library. All original notebooks, slides, and course documents are © Weizmann Institute of Science and are available under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
