# Project Management

This document tracks major project-management-level decisions, tradeoffs, risks, and delivery goals during development of the AI Decision Assistant.

The focus of this document is not implementation details, but rather:

- why work was prioritized
- what problem each task solved
- who benefited
- what tradeoffs were accepted

---

# TASK-001 – Parse and Validate LLM JSON Output

## Problem

Model responses were unstructured and unreliable for programmatic use.

## User

Developer of the solution

## Metrics

% of model responses successfully parsed into Python dictionaries

## Tradeoff

Manual parsing logic was implemented instead of advanced schema tooling to better understand raw LLM behavior.

---

# TASK-002 – Prompt Templates and Versioning

## Problem

Prompts were hardcoded inside application logic, making iteration difficult.

## User

Developer of the solution

## Metrics

Ability to update prompts without changing application code

## Tradeoff

External templates improve maintainability but require synchronization with validation rules.

---

# TASK-003 – Logging and Basic Metrics

## Problem

Failures and runtime behavior were difficult to debug without persistent logs.

## User

Developer of the solution

## Metrics

Visibility into request timing, retries, and failures

## Tradeoff

Additional logging increases output noise and operational complexity.

---

# TASK-004 – Automatic Retry for Invalid Model Output

## Problem

LLMs frequently returned malformed JSON or incomplete responses.

## User

End user and developer

## Metrics

% of failed outputs recovered automatically through retries

## Tradeoff

Retries improve reliability but increase latency and API usage.

---

# TASK-005 – Evaluation Harness

## Problem

Prompt and model quality could not be measured consistently across scenarios.

## User

Developer of the solution

## Metrics

Pass/fail rate across predefined evaluation dataset

## Tradeoff

Batch evaluation increases token usage and was later reduced in importance for real-world flow.

---

# TASK-006 – CLI UX Improvements

## Problem

Terminal interaction lacked flexibility and structured execution modes.

## User

Developer of the solution

## Metrics

Ability to run different workflows via CLI modes

## Tradeoff

CLI complexity increased even though later API/UI layers reduced CLI importance.

---

# TASK-007 – Local Memory and Session Persistence

## Problem

System responses were completely stateless and lacked continuity.

## User

End user

## Metrics

% of sessions successfully stored and retrieved

## Tradeoff

Simple JSONL storage was chosen over databases for simplicity and speed, limiting scalability and querying.

---

# TASK-008 – Retrieval Augmented Generation (RAG)

## Problem

The system could not leverage previous interactions as context.

## User

End user

## Metrics

% of runs enriched with previous session context

## Tradeoff

Simple recency-based retrieval was implemented instead of semantic retrieval, causing possible noisy context.

---

# TASK-009 – Speech-to-Text Input

## Problem

System supported only text-based interaction.

## User

End user

## Metrics

Successful transcription rate of voice input

## Tradeoff

Local lightweight speech-to-text models reduce cost but provide lower accuracy than cloud providers.

---

# TASK-010 – Packaging the Tool

## Problem

Project setup and execution were inconsistent across environments.

## User

Developer of the solution

## Metrics

Ability to run the project using documented setup commands

## Tradeoff

Full packaging was postponed to prioritize API/UI delivery and reliability features.

---

# TASK-011 – Response Structure Validation

## Problem

Responses could contain correct keys but invalid structure.

## User

Developer and end user

## Metrics

% of responses matching expected schema rules

## Tradeoff

Strict validation increases rejected outputs but improves reliability.

---

# TASK-012 – Prompt Template System

## Problem

Prompt logic and application logic were tightly coupled.

## User

Developer of the solution

## Metrics

Ability to iterate prompts independently from Python logic

## Tradeoff

Template management adds another layer that must stay aligned with validators.

---

# TASK-013 – Model Configuration Layer

## Problem

Runtime settings and model parameters were scattered across modules.

## User

Developer of the solution

## Metrics

Ability to change providers and runtime behavior via configuration only

## Tradeoff

Centralized configuration increases abstraction and setup complexity.

---

# TASK-014 – Response Cleaning Module

## Problem

LLMs often wrapped JSON inside markdown or extra text.

## User

Developer of the solution

## Metrics

% of malformed responses successfully cleaned before parsing

## Tradeoff

Simple cleaning logic improves robustness but cannot repair deeply invalid JSON.

---

# TASK-015 – Improved Logging System

## Problem

Basic logging lacked enough context to diagnose failures and retries.

## User

Developer of the solution

## Metrics

Ability to trace a full pipeline execution through logs

## Tradeoff

More detailed logging increases operational noise and storage usage.

---

# TASK-016 – Evaluation Dataset Expansion

## Problem

Small dataset coverage did not expose enough edge cases or inconsistent behavior.

## User

Developer of the solution

## Metrics

Coverage of simple, complex, ambiguous, constrained, and edge-case scenarios

## Tradeoff

Larger evaluation datasets increase API usage and execution time.

---

# TASK-017 – Output Formatting

## Problem

CLI output became difficult to scan during development and debugging.

## User

Developer of the solution

## Metrics

Readability of terminal output during multi-step execution

## Tradeoff

Formatting work became less important after UI integration.

---

# TASK-018 – Error Classification

## Problem

Failures were grouped together without visibility into root causes.

## User

Developer of the solution

## Metrics

Ability to categorize failures by source

## Tradeoff

Additional metadata and branching increased complexity.

---

# TASK-019 – Result Persistence

## Problem

Execution results disappeared after runtime and could not be reviewed later.

## User

Developer of the solution

## Metrics

% of runs successfully persisted with metadata

## Tradeoff

JSONL persistence is simple but not production-grade for cloud environments.

---

# TASK-020 – Model Abstraction Layer

## Problem

The system depended directly on provider-specific logic.

## User

Developer of the solution

## Metrics

Ability to switch model providers without changing pipeline logic

## Tradeoff

Provider abstraction increases architecture complexity and hides provider-specific behavior differences.

---

# TASK-021 – Persistent Logging to File

## Problem

Logs were visible only during active terminal execution.

## User

Developer of the solution

## Metrics

Availability of historical logs after application shutdown

## Tradeoff

File logging is unreliable on ephemeral cloud environments such as Render.

---

# TASK-022 – Code Modularization and Project Structure Refactor

## Problem

Single-file architecture became difficult to maintain as features increased.

## User

Developer of the solution

## Metrics

Separation of concerns across dedicated modules

## Tradeoff

More files and abstraction reduce beginner readability.

---

# TASK-023 – Basic UI (Streamlit)

## Problem

CLI-only interaction limited demos and usability for non-technical users.

## User

End user and recruiter/demo audience

## Metrics

Ability to interact with the system through browser UI

## Tradeoff

Streamlit prioritizes speed over frontend flexibility and customization.

---

# TASK-024 – Metrics and Decision Scoring

## Problem

The system lacked visibility into output quality and runtime behavior.

## User

Developer of the solution

## Metrics

Availability of runtime metadata and quality scoring

## Tradeoff

Simple heuristic scoring is easier to explain but less accurate than semantic evaluation.

---

# TASK-025 – Multi-Model Support and Experimentation

## Problem

The system relied on a single provider with no redundancy or experimentation capability.

## User

Developer of the solution

## Metrics

Ability to switch providers and recover from provider failures

## Tradeoff

Different providers behave inconsistently and increase operational complexity.

---

# TASK-026 – Refactor Router Functions and Core Logic

## Problem

Large amounts of duplicated pipeline logic increased maintenance risk.

## User

Developer of the solution

## Metrics

Shared reusable execution flow across CLI, API, and UI

## Tradeoff

Abstraction reduced linear readability for beginners.

---

# TASK-027 – Robustness Layer

## Problem

The system assumed ideal provider behavior and could fail unexpectedly.

## User

End user and developer

## Metrics

% of runs completed without crash despite model/provider failures

## Tradeoff

Retries and fallback improve reliability but increase runtime and API usage.

---

# TASK-028 – Evaluation Layer v2

## Problem

Validation alone could not measure actual output usefulness.

## User

Developer of the solution

## Metrics

Ability to classify output quality beyond pass/fail

## Tradeoff

Simple scoring systems introduce subjective heuristics.

---

# TASK-029 – Data Contracts and Validation

## Problem

Inconsistent output structures could break downstream logic and UI rendering.

## User

Developer and end user

## Metrics

% of outputs conforming to required schema rules

## Tradeoff

Strict validation increases failure frequency but improves downstream reliability.

---

# TASK-030 – Performance Basics

## Problem

The system lacked visibility into execution speed and bottlenecks.

## User

Developer of the solution

## Metrics

Average request duration and retry impact visibility

## Tradeoff

Performance instrumentation adds slight execution overhead.

---

# TASK-031 – API Layer

## Problem

CLI-only architecture limited reuse and integration.

## User

Developer and external consumers

## Metrics

Ability to access decision pipeline through HTTP endpoint

## Tradeoff

API deployment introduced infrastructure and dependency management complexity.

---

# TASK-032 – Cost Control and Usage Limits

## Problem

Retries and multi-model behavior increased risk of excessive API usage.

## User

Developer of the solution

## Metrics

Maximum model calls per run remain bounded

## Tradeoff

Strict limits may stop execution early and reduce fallback opportunities.

---

# TASK-033 – Transition to Single-Input Execution Flow

## Problem

Batch testing architecture no longer matched real user interaction patterns.

## User

End user

## Metrics

Successful execution of one full decision flow per request

## Tradeoff

Reduced emphasis on large-scale automated evaluation.

---

# TASK-034 – Context Handling (Session Relevance)

## Problem

Recent-session retrieval may inject irrelevant or noisy context.

## User

End user

## Metrics

Improved relevance of context-aware outputs

## Tradeoff

Advanced filtering and semantic retrieval were postponed to avoid overengineering the MVP.

---
