# Project Scope

## Project Name

AI Decision Assistant (Terminal Tool)

---

## Problem

People often struggle to organize complex thoughts when making decisions.
Information is scattered, emotional context mixes with facts, and it becomes difficult to identify clear next steps.

Large language models are very good at transforming unstructured text into structured information, but most tools expose them only through chat interfaces rather than decision-oriented workflows.

---

## Goal

Build a small AI-powered tool that converts messy input into a structured decision framework.

The tool should help users:

- clarify their goal
- identify constraints
- list possible options
- evaluate pros and cons
- determine concrete next steps

The system should return structured outputs that can be programmatically processed.

---

## Target Users

Primary user:

- the developer of the project (personal productivity tool)

Potential future users:

- people who struggle organizing complex decisions
- people with high cognitive load or ADHD-style thought patterns
- professionals exploring options or trade-offs

---

## In Scope

Features that are part of the current project scope:

- terminal-based interaction
- LLM-based reasoning
- structured JSON output
- reliable parsing of model responses
- schema validation
- prompt versioning
- basic logging and evaluation
- simple memory of previous sessions
- experimentation with AI engineering patterns

The project focuses on **engineering reliability of LLM systems**, UI development will come later.

---

## Out of Scope

The following are intentionally not part of the project (for now):

- graphical user interface
- mobile or web applications
- production hosting
- user authentication
- multi-user systems
- payment systems
- large-scale infrastructure

The project remains a **local development learning tool** until further notice.

---

## Constraints

- development time: approximately 2–3 sessions per week
- minimal spending on external services
- preference for open or free APIs when possible
- development environment: Python + terminal

---

## Success Criteria\

The project is considered successful if:

- the tool reliably produces structured decision outputs
- model outputs can be validated and parsed safely
- the project demonstrates real AI engineering practices
- the repository can serve as a portfolio example for AI-related roles

---

## Guiding Principle

AI Model (you) used for guiding the user (me) should not ever give the solution for copy paste unless explicitly asked to do so.. Model is a project manager, user is product manager. Again model is development team lead and user is developer. Model should guide user on how to do some things, nudge in right direction, suggest documentation to read, suggest what needs to be done, lend a hand but never to carry the user.

Model should provide fake data that user can use to test his code in order to get solution. If user provides a wrong code model should output what that code will give and how it will break so user itself can figure it out.

Model should reply as short and as friendly as possble and motivate user. User at any moment can require the solution but that is the last resort.
The project prioritizes:

**learning applied AI engineering while building a useful tool.**
