# AI Decision Assistant (Terminal Tool)

## Overview

AI Decision Assistant is a small terminal-based tool designed to help structure messy thoughts into clear decisions and actionable next steps.

The tool takes unstructured input (for example a long description of a problem or situation) and uses a large language model to transform it into a structured format including:

- a clear goal
- constraints
- possible options
- pros and cons for each option
- suggested next steps

The project is intentionally simple and built in the terminal to focus on learning **AI engineering practices**. Later it will evolve into something more serious.

---

## Project Purpose

This project has two goals:

1. Build a useful personal tool for organizing complex decisions.
2. Develop practical AI engineering skills such as:
   - structured LLM outputs
   - prompt design
   - JSON parsing
   - schema validation
   - model reliability patterns
   - evaluation and testing of LLM systems

The repository documents the development process step-by-step.

---

## Example Workflow

User input:

```
My friend is thinking about moving to Amsterdam but is unsure because of
higher living costs and job uncertainty. He likes visiting family in Serbia
often and doesn't know how to evaluate the decision.
```

Structured output produced by the tool:

```
Goal
Help evaluate whether moving to Amsterdam is a good decision.

Constraints
- Higher living costs in NL
- Need for stable employment
- Desire to visit family frequently

Options
- Move to Amsterdam
- Stay in Serbia

Pros / Cons
Move to Amsterdam
+ Career opportunities
+ International environment
- Higher expenses
- Distance from family

Stay in Serbia
+ Lower cost of living
+ Existing support network
- Potentially fewer career opportunities

Next Steps
- Compare salary vs cost of living
- Research job market in Amsterdam
- Estimate travel frequency and cost
```

---

## Current Features

- terminal interface
- LLM integration via HuggingFace inference API
- structured JSON outputs
- JSON parsing in Python
- version controlled development with Git

---

## Planned Improvements

Planned development focuses on making the tool more robust and engineering-grade:

- JSON schema validation
- prompt versioning
- logging and metrics
- retry and fallback mechanisms
- evaluation harness
- local memory and summaries
- optional speech-to-text input

---

## Technology Stack

- Python
- HuggingFace Inference API
- Large Language Models (LLMs)
- JSON structured outputs
- Git / GitHub for project management

---

## Running the Project

Clone the repository:

```
git clone https://github.com/sale4387/decision-making-tool
```

Create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install huggingface_hub
```

Run the tool:

```
python main.py
```

You will be prompted to enter a text description of a situation you want help structuring.

---

## Project Structure

```
decision-making-tool/
│
├── main.py
├── PROJECT_BOARD.md
├── PROJECT_SCOPE.md
├── ARCHITECTURE.md
├── DECISIONS.md
└── README.md
```

---

## Status

Active development.

The repository documents the process of building a small but well-structured AI system while learning modern AI engineering practices.

## Implementation details

## TASK-XXX – Title

Overview

- What was implemented (1–2 lines)

Implementation

- Key components added
- Where it lives (files/functions)
- How it works (short bullets)

Decisions

- Why this approach was chosen
- Key design choices

Tradeoffs

- What was NOT implemented
- Limitations of current solution

Result

- What the system can do now
- What changed vs before

## TASK-007 – Local Memory and Weekly Summaries

Overview

Each run stores session data (mode, test name, input, output) in a local JSONL file and displays a summary of the last 5 sessions.

Implementation

- session list is created and updated during each run
- save_session() (in persistence.py) appends a record to sessions.jsonl
- Each record contains id, timestamp, and session results
- retrieve_session() loads and returns the last 5 sessions for display

Decisions

- This approach was choosen as it was fast , simple and it did not produced any additional costs

Tradeoffs

- Did not implement a database-based solution, limiting scalability and advanced querying.
- No support for large-scale memory or search functionality.

Result

- System can now store and retrieve previous sessions.
- System is no longer stateless.

## TASK-026 – Refactor Router Functions and Core Logic

Overview

- Refactored routing logic by extracting repeated code from cli.py into reusable functions in functions.py

Implementation

- Extracted shared logic into functions.py:
  - init_test_case
  - run_test_case
  - prepare_test_case
  - process_test_results
  - finalize_test_run
- Route functions now call shared logic and handle mode-specific output

Decisions

- Chose to centralize repeated logic into reusable functions to improve maintainability, reduce duplication, and simplify debugging.

Tradeoffs

- Increased abstraction makes the code less intuitive for beginners compared to the previous linear approach.

Result

- Reduced code duplication and improved maintainability, making future changes and extensions easier.

## TASK-025 – Multi-Model Support & Experimentation

Overview

- Added Google Gemini (`gemini-3.1-flash-lite-preview`) as a second model provider.
- Enabled model comparison and failover capability.

Implementation

- Implemented `GEMINIClient` in `model.py`.
- Introduced `PRIMARY_MODEL_PROVIDER` and `SECONDARY_MODEL_PROVIDER` in `config.py`.
- Updated `init_test_case()` to initialize both primary and secondary clients.
- Added `compare` mode for benchmarking models.
- Added `failover` mode to retry with secondary model on failure.

Decisions

- Selected Gemini due to free tier and strong performance for experimentation.
- Kept provider abstraction consistent across models.

Tradeoffs

- Increased complexity due to multi-provider support.
- Did not integrate OpenAI/Anthropic to avoid costs, at the expense of using less industry-standard APIs.

Result

- System supports multiple model providers.
- Can compare latency and output quality between models.
- Failover ensures system resilience when primary model fails.
- System no longer depends on a single model.

## TASK-008 – Retrieval Augmented Generation (RAG)

Overview

- Simple RAG was implemented

Implementation

- Last 3 sessions were retrieved and injected into new input
- Session retrival in persistence.py inside of retrive_session(), actuall injection is done inside of functions.py function get_input_based_on_mode()
- Template file contains placeholder previous_inputs and previous_outputs,
- get_input_based_on_mode() function is called inside of test_init()
- User input gets injected with 3 last sessions
- Model gets more context

Decisions

- This was the simpliest and quickest solution to be implemented
- Key design choices

Tradeoffs

- More complicated RAG based on keywords or embbedings were not implemented
- Although context is provided it is not as precise as keyword based and it is noisy

Result

- Provide more focused response
- No more generic responses

## TASK-024 – Metrics & Decision Scoring Layer

Overview

- Introduced aggregated metrics for evaluating system performance

Implementation

- Calculated global success rate and per-category success rate
- Computed average attempts and average duration per test run
- Tracked error distribution across all tests
- Aggregation handled in finalize_test_run()
- Metrics stored in test_summary dictionary
- Persisted alongside results in JSONL file
- Added version field to track system changes

Decisions

- Kept implementation lightweight using existing JSONL storage
- Avoided external tools or complex analytics layers

Tradeoffs

- Limited querying and filtering capabilities due to flat file storage
- No advanced analytics or visualization

Result

- System outputs are now measurable and comparable
- Improved visibility into performance and stability

# TASK-009 – Speech-to-Text Input

Overview

- Added support for voice input by allowing the user to provide an audio file as a prompt

Implementation

- Integrated Whisper model via HuggingFace transformers for speech-to-text
- Defined convert_voice_to_text() in functions.py to transcribe audio file into text
- Implemented dedicated function_voice() route to handle voice input flow
- Transcribed text replaces user_input and is processed through existing pipeline
- No changes required to core logic (prompting, validation, persistence)

Decisions

- Whisper was selected due to strong adoption, reliability, and availability in HuggingFace ecosystem
- Used lightweight model (tiny/small) to prioritize speed for local usage

Tradeoffs

- No real-time recording; relies on pre-recorded audio file
- Single-file workflow (record → save → process) instead of dynamic input handling
- Lower accuracy compared to larger or cloud-based models

Result

- System supports voice-based input alongside text
- Maintains compatibility with existing architecture
- Enables future UI-based recording and real-time interaction
