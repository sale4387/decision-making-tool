# Project Board

## Backlog

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

TASK-005 — Evaluation Harness (basic LLM testing)

Goal:
Verify the tool consistently produces valid JSON and correct structure for different inputs.

Description:
Create a small testing script that runs several predefined prompts through the tool automatically and validates that the output JSON contains required keys. This prevents prompt or model changes from silently breaking the system.

Subtasks:

005-1 Create test prompt dataset
Create a Python list with 5–10 different decision problems (career change, relocation, budgeting, job offers, business idea, etc.).

005-2 Run prompts automatically
Replace user input with a loop that sends each test prompt to the model and collects responses.

005-3 Validate required JSON keys
Check that every response contains:
goal
constraints
options
pros_cons
next_steps

Log an error if any key is missing.

005-4 Track pass / fail results
Log result for each test case.
Example:
Test 1 — PASS
Test 2 — FAIL

At the end print a summary:
Total tests
Passed
Failed

005-5 Save evaluation results
Write evaluation results to a log file (for example: eval_results.log).

Definition of Done:

• Script runs multiple prompts automatically
• JSON parsing still works
• Required keys are validated
• Pass/fail summary printed
• Results logged to file

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

[x] Subtask 1 – Introduce logging module
Replace basic print statements with Python logging.

[x] Subtask 2 – Log model request and response timing
Measure how long the model call takes.

[x] Subtask 3 – Log JSON parsing failures
Record errors when JSON decoding fails.

References

Python logging documentation
https://docs.python.org/3/library/logging.html

---

TASK-004 – Automatic retry for invalid model output

Goal
Make the system automatically retry the model call when the output cannot be parsed as valid JSON.

Problem
LLMs sometimes return malformed JSON or ignore formatting instructions.  
Currently the program fails after one attempt.

Acceptance Criteria

- Program retries the model request when JSON parsing fails
- Retry is limited (e.g., max 2–3 attempts)
- Each retry is logged
- If all retries fail, the program logs a final error and exits cleanly

Learning Objective

- Understand reliability patterns used in AI systems
- Implement retry logic
- Separate model calling from parsing logic

Subtasks

[x] Subtask 1 – Extract model call into a function  
Create a function that performs the model request and returns the raw response.

[x] Subtask 2 – Implement retry loop  
Add a loop that retries the request if parsing fails.

[x] Subtask 3 – Add retry logging  
Log attempt number and failure reason.

[x] Subtask 4 – Add retry limit  
Stop retrying after a fixed number of attempts.

References

Python while loops  
https://docs.python.org/3/tutorial/controlflow.html#while-statements

Python functions  
https://docs.python.org/3/tutorial/controlflow.html#defining-functions

---
