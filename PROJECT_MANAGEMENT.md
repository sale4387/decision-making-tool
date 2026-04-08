# Project Management

## TASK-00x – TASK TITLE

Problem

User

Metrics

Trade off

## TASK-007 – Local Memory and Weekly Summaries

Problem
Current system produces a solution which exists on its own with no connection with previous interactions.

User
End user

Metrics
95% of successfully saved runs

Trade off
Chose simple local JSON storage over a more powerful database to keep implementation fast and lightweight, at the cost of scalability and querying.

---

## TASK-026 – Refactor Router Functions and Core Logic

Problem
Significant code duplication across route functions increases maintenance complexity and risk of inconsistencies.

User
Developer of the solution

Metric
All route functions use a single shared core function for execution

Tradeoff
Introduces additional abstraction, making code slightly harder to follow for beginners

## TASK-025 – Multi-Model Support & Experimentation

Problem
Currently the system relies on a single model provider, limiting redundancy and experimentation.

User
Developer of solution

Metrics
Ability to switch between at least two model providers and successfully fallback to a secondary provider on failure

Trade off
Only two model providers are used excluding widely accepted openAI and Anthophic still making system limited and dependent on cheap solutions

## TASK-008 – Retrieval Augmented Generation (RAG)

Problem
Current solution relies only on existing promtp not taking previous interactions into consideration

User
Previously defined end user of the solution

Metrics
% of interactions in which at least 3 previous sessions are injected

Trade off
