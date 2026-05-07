# AI Decision Assistant

## Overview

AI Decision Assistant is an applied AI engineering project that transforms unstructured user input into a structured decision framework.

The system accepts natural language input and returns structured output containing:

- goal
- constraints
- options
- pros and cons
- next steps
- category
- quality signal
- runtime metadata

The project started as a terminal-based learning tool and evolved into a deployed AI application with:

- FastAPI backend
- Streamlit UI
- multi-model support
- validation layer
- retry and fallback logic
- prompt templates
- persistence
- deployment

---

## Project Purpose

This project was built to go beyond basic AI prompting.

Many people use AI by writing prompts in ChatGPT or Gemini. This project explores how to build an actual AI-powered system around model calls:

- structured outputs
- prompt templates
- response validation
- retries and fallback
- model abstraction
- evaluation
- API integration
- UI integration
- deployment

The goal was not to build a commercial product, but to demonstrate practical applied AI engineering skills.

---

## Example Input

My phone contract ended. I can pay 200 EUR to keep my Pixel 8 or return it and buy another phone.

{
"goal": "Decide whether to keep the Pixel 8 or buy another phone",
"constraints": [
"Need for a working phone",
"Budget considerations"
],
"options": [
"Keep Pixel 8",
"Return Pixel 8 and buy another phone"
],
"pros_cons": {
"Keep Pixel 8": {
"pros": [
"Lower immediate cost",
"No setup needed"
],
"cons": [
"Older battery",
"No new warranty"
]
},
"Return Pixel 8 and buy another phone": {
"pros": [
"New battery",
"New warranty"
],
"cons": [
"Higher cost",
"Setup required"
]
}
},
"next_steps": [
"Check battery health",
"Compare replacement phone prices"
],
"category": "constrained",
"cheer": "You have enough information to make a practical decision."
}

---

## Current Features

Natural language decision input
Structured JSON output
Prompt templates
JSON response cleaning
JSON parsing
Validation layer
Retry logic
Timeout handling
Multi-model support
Fallback provider
Basic quality scoring
Cost / call tracking
Session persistence
FastAPI endpoint
Streamlit UI
Cloud deployment

---

## Technology Stack

Python
FastAPI
Streamlit
HuggingFace Inference API
Google Gemini API
Pydantic
JSON / JSONL
Git / GitHub
Render

## Main project structure

decision-making-tool/
│
├── api.py
├── ui.py
├── model.py
├── functions.py
├── validation.py
├── cleaner.py
├── persistence.py
├── config.py
├── logger.py
├── templates/
├── README.md
├── PROJECT_SCOPE.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── PROJECT_MANAGEMENT.md
└── PROJECT_BOARD.md

## Example response includes:

data
status
provider
duration
retries
error
validation errors
model calls
quality
fallback flag
primary model failure details

## Project Status

MVP shipped. The project demonstrates:

applied AI system design
structured LLM output handling
validation and reliability logic
multi-model orchestration
API and UI integration
cloud deployment
practical AI engineering workflow

## Implementation Details

TASK-001 – Parse and Validate LLM JSON Output

Overview

Implemented JSON parsing so model responses can be converted into Python dictionaries.

Implementation
Extracted JSON from model response
Parsed response using json.loads()
Added basic error handling for malformed JSON
Confirmed access to keys like goal, constraints, and options

Decisions
JSON was chosen because it allows structured downstream processing.
Parsing was implemented manually to understand LLM output reliability issues.

Tradeoffs
Manual parsing is simple but can fail on malformed model output.
More advanced schema tools were not used initially.

Result
Model output can be programmatically accessed.
The system moved from free-form text to structured data.

TASK-002 – Prompt Templates and Versioning

Overview
Moved prompt logic away from inline code into reusable templates.

Implementation
Created prompt template structure
Added {user_input} placeholder
Loaded prompt content dynamically
Made prompt iteration easier

Decisions
External templates were chosen to separate prompt design from code logic.

Tradeoffs
Requires keeping templates aligned with validation rules.
Bad prompt changes can break output structure.

Result
Prompt changes can be made without changing core Python logic.

TASK-003 – Logging and Basic Metrics

Overview
Added logging to track what happens during execution.

Implementation
Introduced Python logging
Logged model call start and finish
Logged response timing
Logged parsing errors

Decisions
Logging was added early to support debugging and learning.

Tradeoffs
More log output can create noise if not controlled by log levels.

Result
Failures became easier to inspect.
Runtime behavior became more visible.

TASK-004 – Automatic Retry for Invalid Model Output

Overview
Implemented retry logic when model output cannot be processed correctly.

Implementation
Added retry loop
Limited retries to avoid infinite calls
Logged retry attempts
Continued execution after recoverable failures

Decisions
Simple retry logic was chosen over advanced retry libraries.

Tradeoffs
Retries increase latency and model usage.
Failed prompts may still fail after retry.

Result
System became more reliable when models returned invalid output.

TASK-005 – Evaluation Harness

Overview
Created batch testing with multiple predefined decision inputs.

Implementation
Added test dataset
Ran multiple prompts through the pipeline
Validated required keys
Tracked pass/fail results

Decisions
Batch testing was useful during early development to compare prompt/model behavior.

Tradeoffs
Batch tests increased model usage and cost.
Later replaced by single-input execution for real usage.

Result
Prompt and model failures became easier to detect during development.

TASK-006 – CLI UX Improvements

Overview
Added CLI modes and basic command-line routing.

Implementation
Added argument parsing
Added mode routing
Added modes such as summary, compare, and voice
Improved invalid mode handling

Decisions
CLI modes helped test different workflows before API/UI existed.

Tradeoffs
CLI routing became less important after API and UI were introduced.

Result
The tool became easier to run in different development modes.

TASK-007 – Local Memory and Session Persistence

Overview
Added local session persistence.

Implementation
Created session records
Saved input/output data to JSONL
Loaded recent sessions
Used previous sessions as context

Decisions
JSONL was chosen for speed and simplicity.
No database was used for MVP.

Tradeoffs
File storage is not reliable on cloud hosting.
No advanced querying or filtering.

Result
System became stateful locally.
Previous sessions could be reused as context.

TASK-008 – Retrieval Augmented Generation

Overview
Added simple context injection from previous sessions.

Implementation
Retrieved recent session history
Injected previous inputs and outputs into prompts
Used simple recency-based retrieval

Decisions
Simple recent-session retrieval was chosen instead of embeddings or vector DB.

Tradeoffs
Context may be noisy or irrelevant.
No semantic relevance filtering.

Result
Responses can use previous context.
Foundation for future RAG improvements was created.

TASK-009 – Speech-to-Text Input

Overview
Tested voice input support using speech-to-text.

Implementation
Added local speech-to-text function
Used audio file as input source
Converted audio into text
Passed transcript into existing pipeline

Decisions
Whisper-style speech-to-text was selected because it is widely used and practical.

Tradeoffs
Voice support was local only.
Not included in deployed MVP due to deployment complexity.

Result
System proved it can support non-text input types.

TASK-010 – Packaging the Tool

Overview
Packaging was planned to make the tool easier to install and run.

Implementation
Requirements file introduced
Deployment dependencies cleaned
Runtime commands documented

Decisions
Full package distribution was postponed until after API/UI deployment.

Tradeoffs
Project is runnable but not packaged as a polished installable CLI package.

Result
Dependencies and run commands are documented.
Full packaging remains a future improvement.

TASK-011 – Response Structure Validation

Overview
Added validation beyond checking whether keys exist.

Implementation
Checked required keys
Checked list sizes
Checked options match pros_cons keys
Checked pros/cons structure

Decisions
Manual validation was chosen to keep dependencies low and learning clear.

Tradeoffs
Manual validation requires maintaining rules carefully.
Pydantic or JSON Schema could be added later.

Result
Output reliability improved.
Broken model responses are caught before UI/API usage.

TASK-012 – Prompt Template System

Overview
Moved prompts into external template files.

Implementation
Created templates/
Added mode-based templates
Injected user input and previous context
Removed hardcoded prompt strings from logic

Decisions
External templates make prompt iteration faster.

Tradeoffs
Template and validation schema must stay aligned.

Result
Prompt updates became faster and safer.

TASK-013 – Model Configuration Layer

Overview
Centralized runtime and model configuration.

Implementation
Added config values for:
providers
model names
retries
timeout
max tokens
temperature
validation limits

Decisions
Config-driven design makes experimentation easier.

Tradeoffs
More settings increase complexity.

Result
Models and runtime behavior can be changed without changing core logic.

TASK-014 – Response Cleaning Module

Overview
Created reusable response cleaning before JSON parsing.

Implementation
Removed markdown wrappers
Extracted content between first { and last }
Returned cleaned JSON string
Logged cleaning failures

Decisions
Cleaning was separated from parsing and model calls.

Tradeoffs
Cleaner is intentionally simple.
It does not repair invalid JSON.

Result
Model responses became easier to parse consistently.

TASK-015 – Improve Logging System

Overview
Improved logging across the pipeline.

Implementation
Added logs for:
model calls
retries
response previews
validation failures
scoring
runtime metrics

Decisions
Logging was treated as part of reliability, not decoration.

Tradeoffs
File logging is not reliable on cloud hosting.
Console logging is preferred for deployed environments.

Result
Debugging became much faster.

TASK-016 – Evaluation Dataset Expansion

Overview
Expanded test coverage with more varied decision examples.

Implementation
Added multiple decision scenarios
Covered simple, complex, constrained, ambiguous, messy, and edge cases
Used categories for early evaluation

Decisions
More varied inputs helped expose weak prompts and model behavior.

Tradeoffs
Batch evaluation increased API usage.
Categories were later reduced in importance for single-input flow.

Result
Better understanding of model failure patterns.

TASK-017 – Output Formatting

Overview
Improved readability of terminal output.

Implementation
Added section headers
Separated goal, constraints, options, pros/cons, and next steps
Improved CLI output clarity

Decisions
Formatting was added before UI existed to improve development experience.

Tradeoffs
Terminal formatting became less important after Streamlit UI.

Result
CLI output became easier to read and debug.

TASK-018 – Error Classification

Overview
Added categorized error tracking.

Implementation
Tracked errors such as:

MODEL_ERROR
CLEANER_ERROR
PARSE_ERROR
VALIDATION_ERROR

Decisions
Error classification was added to understand where failures happen.

Tradeoffs
Adds more metadata and branching.

Result
Failures became easier to diagnose.
Retry/fallback behavior became more explainable.

TASK-019 – Result Persistence

Overview
Persisted structured run results.

Implementation
Created persistence module
Saved test/run results to JSONL
Stored metadata such as:
status
retries
provider
duration
errors
quality

Decisions
JSONL was chosen for simple append-only storage.

Tradeoffs
Cloud file persistence is temporary on Render.
Firebase or database storage is better for future projects.

Result
Local runs can be reviewed later.
Result history became available for debugging.

TASK-020 – Model Abstraction Layer

Overview
Introduced model client abstraction.

Implementation
Created base ModelClient
Implemented HuggingFace client
Implemented Gemini client
Used shared api_call() pattern

Decisions
Abstraction allows switching providers without rewriting pipeline logic.

Tradeoffs
Providers behave differently even behind a shared interface.

Result
Model switching became fast and config-driven.

TASK-021 – Persistent Logging to File

Overview
Added file-based logging for local development.

Implementation
Configured log file output
Added timestamps, module names, and levels
Kept logs across local runs

Decisions
File logs were useful during local debugging.

Tradeoffs
File logs are not reliable on cloud hosting.
Render requires console logs for visibility.

Result
Local debugging improved.

TASK-022 – Code Modularization and Project Structure Refactor

Overview
Refactored the project into separate modules.

Implementation
Created modules for:
model calls
validation
configuration
cleaning
persistence
CLI/API flow
UI

Decisions
Separation of concerns was needed as the project grew.

Tradeoffs
More files make navigation harder for beginners.

Result
Code became easier to extend and maintain.

TASK-023 – Basic UI

Overview
Added Streamlit UI.

Implementation
Created ui.py
Added text input area
Connected UI to deployed API
Rendered structured output sections

Decisions
Streamlit was chosen for speed and simplicity.

Tradeoffs
UI is simple and not highly customized.
Frontend logic is intentionally thin.

Result
Project became demoable for non-technical users.

TASK-024 – Metrics and Decision Scoring

Overview
Added lightweight metrics and scoring.

Implementation
Tracked duration
Tracked retries
Tracked provider
Tracked model calls
Added basic quality scoring using simple heuristics

Decisions
Chose simple scoring over advanced semantic evaluation.

Tradeoffs
Scoring is heuristic and not deeply semantic.
Good enough for MVP visibility.

Result
Outputs now include a quality signal and runtime metadata.

TASK-025 – Multi-Model Support and Experimentation

Overview
Added multiple model provider support.

Implementation
Added Gemini provider
Added HuggingFace provider
Added primary/secondary provider config
Added comparison/fallback behavior

Decisions
Multi-model support was important for reliability and experimentation.

Tradeoffs
Different providers require different handling.
Some models follow JSON instructions better than others.

Result
System is no longer dependent on one provider.

TASK-026 – Refactor Router Functions and Core Logic

Overview
Reduced duplicate execution logic.

Implementation
Extracted shared pipeline into reusable functions
Centralized model call / clean / parse / validate flow
Simplified route functions

Decisions
Refactor was needed before adding more features.

Tradeoffs
More abstraction, less linear flow.

Result
Core pipeline became reusable by CLI, API, and UI.

TASK-027 – Robustness Layer

Overview
Improved reliability with retries, timeouts, and controlled failures.

Implementation
Added timeout handling
Added model-level retry logic
Added controlled exception handling
Added fallback path

Decisions
Reliability was prioritized before UI polish.

Tradeoffs
More logic and more metadata.
Retries increase latency and usage.

Result
System handles model/provider failures more safely.

TASK-028 – Evaluation Layer v2

Overview
Added basic output quality evaluation.

Implementation
Used lightweight similarity scoring
Compared goal relevance and pros/cons balance
Added quality labels such as bad, good, great

Decisions
Chose simple explainable scoring instead of AI grading AI.

Tradeoffs
Scoring is not semantic enough for production-grade evaluation.

Result
System can separate valid output from output quality.

TASK-029 – Data Contracts and Validation

Overview
Improved schema consistency and validation behavior.

Implementation
Required keys enforced
Min/max limits applied
Pros/cons structure validated
Validation errors tracked and returned

Decisions
The system should fail safely when model output is structurally wrong.

Tradeoffs
Strict validation can reject useful but incorrectly shaped answers.

Result
API/UI can rely on predictable output structure.

TASK-030 – Performance Basics

Overview
Added basic runtime visibility.

Implementation
Measured model call duration
Measured total request duration
Tracked retry impact
Returned duration metadata

Decisions
Lightweight metrics were enough for MVP.

Tradeoffs
No external monitoring or dashboard.

Result
Performance became visible in API responses.

TASK-031 – API Layer

Overview
Added FastAPI backend.

Implementation
Created POST /decision
Added request body model
Connected API to existing pipeline
Returned structured JSON response
Deployed backend to Render

Decisions
API layer makes the system reusable by UI and future services.

Tradeoffs
Added deployment complexity.
Introduced environment/dependency management issues.

Result
Project became an actual callable service.

TASK-032 – Cost Control and Usage Limits

Overview
Added basic model usage awareness.

Implementation
Tracked model calls per run
Enforced max model calls
Included calls in result metadata
Discussed abuse protection/rate limiting

Decisions
Usage control was added after encountering provider limits/cost concerns.

Tradeoffs
Full rate limiting was not finalized.
Provider billing protection still needs stronger production safeguards.

Result
Model usage became visible and bounded per run.

TASK-033 – Transition to Single-Input Execution Flow

Overview
Refactored project from batch-test flow into real user flow.

Implementation
Removed test-case loop from main user flow
Simplified result handling
Single user input now drives one execution
Batch summary logic reduced

Decisions
Real product flow became more important than batch testing.

Tradeoffs
Less built-in batch evaluation.

Result
System became closer to a usable product.

TASK-034 – Context Handling / Session Relevance

Overview
Identified current session context limitations.

Implementation
Current system uses recent sessions as simple context
Relevance filtering was discussed but not fully implemented

Decisions
Advanced context filtering was postponed.

Tradeoffs
Previous context can be noisy.
Cloud persistence needs external storage.

Result
Context handling exists but remains an area for improvement.

---

## Final Notes

This project represents a full learning cycle:

Start with simple LLM call
Add structured output
Add validation and retries
Add model abstraction and fallback
Add persistence and context
Add scoring and performance metadata
Expose system through API
Add UI
Deploy it

The final product is intentionally simple, but it demonstrates applied AI engineering patterns that are useful for larger real-world projects.
