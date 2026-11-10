# Session 2 — Reviewing AI-Written Code

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (CPTAC public dataset, published proteomics)

---

## What students leave with

The ability to read AI-generated analysis code critically, predict what it will do before running it, catch mistakes, and confirm a result a second way.

## The question

> What do microsatellite-unstable (MSI-H) endometrial tumors lose — and gain — at the protein level compared with microsatellite-stable (MSS) tumors?

A colleague asked an AI assistant, step by step, to analyse the CPTAC endometrial cancer proteomics dataset: 104 tumors and 49 normal tissue samples measured by TMT mass spectrometry. Students receive that AI-generated code and work through it systematically.

## Learning outcomes

- Apply the inspect → predict → check → fix loop to AI-generated data-analysis code
- Identify planted errors in statistical code (wrong test, wrong column, off-by-one)
- Confirm a biological result using a second, independent method

## Session structure

| Time | Activity |
|---|---|
| 0–10 min | The working loop: inspect, predict, run, check |
| 10–75 min | Notebook: five parts, one planted error each |
| 75–90 min | Challenge: find the error that changes the biological conclusion |

## Materials

| File | Description |
|---|---|
| [`Session_2_Reviewing_AI_Code_STUDENT.ipynb`](Session_2_Reviewing_AI_Code_STUDENT.ipynb) | Student version — answer boxes empty |
| [`Session_2_Reviewing_AI_Code_MASTER.ipynb`](Session_2_Reviewing_AI_Code_MASTER.ipynb) | Instructor version with answers |
| [`Session_2_Reviewing_AI_Code.pptx`](Session_2_Reviewing_AI_Code.pptx) | Session slides |

[![Open Student Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S2/Session_2_Reviewing_AI_Code_STUDENT.ipynb)

## Critical-thinking challenge

After completing the notebook, students are asked: "One of these results would change if you used the correct statistical test. Which one, and why?" They must propose and run the correction themselves.

## Notes for instructors

The student notebook deliberately contains subtle errors that do not raise exceptions — the code runs, produces a figure, and gives a wrong answer. Resist the urge to hint which cells contain errors; the discovery process is the point.

> *For next year:* Consider splitting assignments so each pair works on a different error, then groups compare findings.
