# Project Board

## Backlog

TASK-002 – Prompt templates and versioning
Create reusable prompt templates and track prompt versions.

TASK-003 – Logging and metrics
Log model calls, latency, and possible token usage.

TASK-004 – Automatic retry and fallback routing
Retry when model output is invalid and optionally switch models.

TASK-005 – Evaluation harness
Create fixed test inputs to evaluate model output quality.

TASK-006 – CLI UX improvements
Improve terminal display and add modes such as `plan`, `summarize`, and `rage`.

TASK-007 – Local memory and weekly summaries
Store previous sessions and generate summaries.

TASK-008 – Retrieval Augmented Generation (RAG)
Retrieve relevant previous notes before sending prompts.

TASK-009 – Speech-to-text input
Allow voice input using a local speech model.

TASK-010 – Packaging the tool
Make the tool installable and runnable easily.

---

## This Sprint

(No tasks currently waiting)

---

## In Progress

---

## Blocked

(No blocked tasks)

---

## Done

Initial LLM integration
Project repository created
Core documentation created (README, PROJECT_SCOPE, ARCHITECTURE, DECISIONS)

---

TASK-001 – Parse and validate LLM JSON output

Goal
Convert model JSON output into a Python dictionary safely.

Subtasks

[x] Detect JSON block in model response (between first `{` and last `}`).
[x]Parse JSON using `json.loads()`.
[x]Add `try/except` handling for malformed JSON.
[x] Confirm parsed structure by inspecting keys.
[x]Add minimal debug output when parsing fails.

Acceptance Criteria

- Model response can be parsed into a Python dictionary.
- Program does not crash on malformed output.
- Keys like `goal`, `constraints`, and `options` can be accessed.

Learning Objective

Understand JSON parsing and reliability patterns for LLM outputs.

Reference

Python JSON documentation
https://docs.python.org/3/library/json.html

---
