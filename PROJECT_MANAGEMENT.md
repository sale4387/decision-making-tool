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
Current solution relies only on the current prompt and does not use previous interactions, making responses stateless and less context-aware.

User
End user of the decision-making tool.

Metrics
Percentage of interactions where at least 3 previous sessions are injected into the prompt.

Trade off
System relies on simple JSONL file storage without relevance filtering, which may introduce irrelevant context and does not scale compared to vector databases or embedding-based retrieval.

## TASK-024 – Metrics

Problem
System generates structured outputs but lacks aggregated performance metrics, making evaluation, comparison, and improvement difficult.

User
Developer of the solution

Metrics
% of runs where aggregated metrics are computed and stored successfully

Tradeoff
Relies on simple JSONL storage, which limits querying, filtering, and analysis compared to database-based solutions

## TASK-009 – Speech-to-Text Input

Problem
System currently supports only text input and lacks voice interaction capability.

## TASK-027 – Robustness Layer

User
End user of the tool

Metrics
% of runs where voice input is successfully converted to text and processed through the pipeline

Tradeoff
Uses lightweight local model (via HuggingFace), reducing dependency on external services but with lower transcription accuracy compared to cloud-based solutions

Problem
Current system assumes ideal conditions and may fail or break when model calls, parsing, or validation do not behave as expected.

User
Developer of the solution

Metrics
% of runs completed without crashing despite model or processing errors

Tradeoff
Additional logic increases complexity but significantly improves system reliability
