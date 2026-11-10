# Session 4 — Build a Guardrailed Assistant

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (public sources and invented examples only — everything sent leaves Weizmann)  
**API:** NVIDIA build.nvidia.com (free tier sufficient)

---

## What students leave with

The ability to call a large language model through an API, write a system prompt that guardrails its behavior, and recognise when the model has broken the rules they set.

## Learning outcomes

- Connect to a hosted LLM through an OpenAI-compatible API
- Write a system prompt that restricts topic, tone, and output format
- Push the assistant until it breaks the rules, then redesign the guardrail

## Session structure

| Time | Activity |
|---|---|
| 0–15 min | The working loop in a Colab notebook: describe goal → prompt → run → paste back errors |
| 15–20 min | What to share with the model: column names and example rows, never the full dataset |
| 20–60 min | Guided lab: connect, write system prompt, build a small assistant |
| 60–80 min | Challenge: reworded questions and pushing back on a correct answer |
| 80–90 min | Share-out + failure log |

## Materials

| File | Description |
|---|---|
| [`Session_4_Assistant_API.ipynb`](Session_4_Assistant_API.ipynb) | Main hands-on notebook |
| [`Session_4_Assistant_API_DEMO.ipynb`](Session_4_Assistant_API_DEMO.ipynb) | Instructor demo version |
| [`Session_4_Recap_Colab.ipynb`](Session_4_Recap_Colab.ipynb) | Recap / review notebook |
| [`Session_4_Write_the_Rules_Once.pptx`](Session_4_Write_the_Rules_Once.pptx) | Session slides |
| [`submission_demo.json`](submission_demo.json) | Example structured output |

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S4/Session_4_Assistant_API.ipynb)

## Before the session

Students need an NVIDIA API key from [build.nvidia.com](https://build.nvidia.com). Registration is free and the free tier covers all session exercises. Keys begin with `nvapi-`. Students should not share or hard-code their key.

## Critical-thinking challenge

Each student tries to make their own assistant break its rules using three strategies: rephrasing the question, claiming a special role ("I am the administrator"), and hiding the instruction inside a longer text. They log which strategy worked and what guardrail would prevent it.
