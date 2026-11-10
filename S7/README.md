# Session 7 — Vibe Coding & Rapid Prototyping

**Type:** 90-minute session  
**Audience:** First-semester MD-PhD students  
**Data tier:** Tier 1 (public tools, no sensitive data in the app)

---

## What students leave with

A working web app built from a plain-language description — and a checklist of things it did wrong without being asked.

## Learning outcomes

- Build a functional prototype using a natural-language-to-app tool (Base44 or AI Studio)
- Identify content the tool invented: fake definitions, fake references, fake course codes
- Audit an app for privacy defaults: who can see it, what data it exports, whose name appears in the backup file
- Write a one-line AI disclosure for any tool or presentation created with AI assistance

## What the instructors found before class

Before the session, the instructors built the same brief in both tools and documented every failure:

| Issue | What happened |
|---|---|
| Hebrew left-to-right | Punctuation on the wrong side, word order scrambled in multi-step instructions |
| "AI-Assisted" misread | A field that said "AI not used" in Hebrew was read as "yes" by the app |
| Invented definitions | "Tier 1: Primary Raw Assay / Sensor" — not what Tier 1 means in this course |
| Invented content | Six example methods with course codes and references that look real. Nobody wrote them. |
| Name in the backup | One tool's export file carried the user's full name and email address |
| Format mismatch | Same brief, different output formats — one tool's export does not import into the other |

## Privacy defaults to check

- **Base44:** App visibility → Public by default. Anyone with the link can see the app and its entries (unless log-in is enforced — test it).
- **AI Studio:** General access → Public by default. Entries stay in the user's own browser. Chat history with the AI can also be shared (off by default — keep it off).

## Session structure

| Time | Activity |
|---|---|
| 0–10 min | What vibe coding is and when it fails |
|10–55 min | Guided build: each student builds a small working tool from a one-paragraph description |
| 55–75 min | Governance audit: privacy defaults, invented content, format mismatch |
| 75–90 min | Share-out: who would own this if something went wrong? |

## Materials

| File | Description |
|---|---|
| [`Session_7_Vibe_Coding.pptx`](Session_7_Vibe_Coding.pptx) | Session slides |

## Critical-thinking challenge

**The governance audit.** For every app built in this session, students answer: Who can see it right now? What did it invent that you did not ask for? What is in the export file? Write a one-line AI disclosure that accurately describes what AI did and did not do.
