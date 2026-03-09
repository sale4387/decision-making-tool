# Project Board

## Backlog

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

TASK-003 – Logging and basic metrics

Goal
Track what happens when the program runs so we can debug and understand model behavior.

Problem
Right now if something fails (model error, parsing error, slow response) we only see prints in the terminal.
Real systems record events so they can be analyzed later.

Acceptance Criteria

- Program logs when a model request starts
- Program logs when a response is received
- Program logs parsing errors
- Logs include timestamps
- Logs are written to a file

Learning Objective
Understand basic observability patterns used in AI systems.

Subtasks

[ ] Subtask 1 – Introduce logging module
Replace basic print statements with Python logging.

[ ] Subtask 2 – Log model request and response timing
Measure how long the model call takes.

[ ] Subtask 3 – Log JSON parsing failures
Record errors when JSON decoding fails.

References

Python logging documentation
https://docs.python.org/3/library/logging.html

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

TASK-002 – Prompt templates and versioning

Goal
Separate prompt logic from application code so prompts can be reused and modified independently.

Problem
The prompt is currently hard-coded inside `main.py`, making it difficult to maintain, compare versions, or reuse prompts.

Acceptance Criteria

- Prompt text is not written inline in the API call.
- Prompt is stored in a reusable variable or template.
- `main.py` loads the prompt from a single location.
- Updating the prompt requires editing only one place.

Learning Objective

- Understand prompt templating
- Understand prompt reuse patterns in LLM systems
- Learn maintainable prompt design

Subtasks

[x] Subtask 1 – Move prompt to variable
Move the long prompt text into a single variable instead of embedding it inside the API call.

[x] Subtask 2 – Create prompt template
Convert the prompt into a reusable template that accepts dynamic user input.

References

Python multiline strings
https://docs.python.org/3/tutorial/introduction.html#strings

Python string formatting
https://docs.python.org/3/library/string.html#formatstrings

---
