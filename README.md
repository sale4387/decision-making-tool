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

- Refactoring of routing functions inside of cli.py. All repetitive code was separated into functions and placed into separated file functions,py

Implementation

- init_test_case, finalize_test_run, prepare_test_case,process_test_results, run_test_case functions were added to functions.py
- functions are called inside of router function and appropriate outputs are dipslayed to user depending of mode

Decisions

- This approach was choosen in order to make readability easier and updating and debugging quicker

Tradeoffs

- Code is not intuitive and easy to grasp for begginers as before

Result

- Code is easy to update and debugg
