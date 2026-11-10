# Session 6 — Build an Agent

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (published case report CC BY-NC 4.0, public APIs)  
**API:** NVIDIA build.nvidia.com (same key as Sessions 4 and 5)

---

## What students leave with

A working agent they built themselves — a model in a loop with real tools — and a concrete sense of where agents act without checking.

## The setup

> An agent is a model in a loop: **goal → choose a tool → act → read the result → repeat → stop.**

Students build an agent with three real tools — ClinicalTrials.gov, PubMed, and a simulated email writer (writes to a file, does not send) — and deploy it on a published oncology case report.

The patient is from: *Scandurra et al., EMJ Oncology 2023* (CC BY-NC 4.0), so everything sent to the model is public.

## Learning outcomes

- Implement a tool-use loop with function calling
- Understand how the agent decides which tool to call next
- Identify steps the agent took without verifying the result
- Recognise prompt injection: a hidden instruction on a web page

## Session structure

| Time | Activity |
|---|---|
| 0–20 min | What an agent is: model + tools + loop |
| 20–55 min | Notebook: connect → define tools → run the loop → read the step log |
| 55–75 min | Challenge: mark every unchecked step; demo of a hidden instruction |
| 75–90 min | Share-out + failure log |

## Materials

| File | Description |
|---|---|
| [`Session_6_Build_an_Agent.ipynb`](Session_6_Build_an_Agent.ipynb) | Student notebook |
| [`Session_6_Build_an_Agent_INSTRUCTOR.ipynb`](Session_6_Build_an_Agent_INSTRUCTOR.ipynb) | Instructor version with completed agent |
| [`agent_tools_ready.py`](agent_tools_ready.py) | Pre-built tool definitions (ClinicalTrials, PubMed) |
| [`Session_6_Agents.pptx`](Session_6_Agents.pptx) | Session slides |

[![Open Student Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yonatanzor/ai-workshop/blob/main/S6/Session_6_Build_an_Agent.ipynb)

## Critical-thinking challenge

Students read the agent's step log and highlight every action it took without verifying the result. Then they see a demo where a hidden instruction embedded in a web page changes what the agent does. They discuss: what guardrails would prevent this?
