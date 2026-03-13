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

TASK-012 – Prompt template system
Create reusable prompt templates for different modes such as plan, summarize, and rage.

TASK-013 – Model configuration layer
Move model name, temperature, retries, and other settings into a configuration section.

TASK-014 – Response cleaning module
Create a function that cleans model responses (remove markdown blocks, stray text, and ensure JSON extraction).

TASK-015 – Logging improvements
Introduce structured logging levels and optional debug mode for inspecting raw model responses.

TASK-016 – Evaluation dataset expansion
Create a larger structured test dataset to systematically test prompts and model behavior.

TASK-017 – Output formatting
Improve CLI output readability (sections, separators, clearer labeling).

TASK-018 – Error classification
Differentiate between parsing errors, validation errors, and model format failures.

TASK-019 – Result persistence
Save test results and responses to files for later inspection.

TASK-020 – Model abstraction layer
Create a wrapper allowing easy switching between HuggingFace, OpenAI, and other providers.

---

## This Sprint

TASK-021 – Persistent logging to file

Goal  
Store all runtime logs into files so test runs and model behavior can be analyzed later.

Problem  
Currently logs are printed only to terminal and are lost after program ends.  
Real systems persist logs for debugging, monitoring, and evaluation.

Acceptance Criteria

- Program writes logs to a file (e.g., app.log)
- Log format includes timestamp, level, and message
- Console logging still works
- Errors are clearly visible in log file
- Log file grows across runs (no overwrite)

Learning Objective

- Understand how real applications handle logging
- Learn Python logging handlers and formatters
- Separate logging configuration from business logic
- Prepare system for later evaluation and monitoring tasks

Subtasks

[ ] Subtask 1 – Configure FileHandler  
Add logging handler that writes logs to a file.

[ ] Subtask 2 – Define log format  
Include timestamp, level, module name, message.

[ ] Subtask 3 – Keep console logging  
Ensure StreamHandler still prints logs to terminal.

[ ] Subtask 4 – Test persistence  
Run program twice and confirm logs append to file.

References

Python logging tutorial  
https://docs.python.org/3/howto/logging.html

Logging handlers  
https://docs.python.org/3/library/logging.handlers.html

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

TASK-005 — Evaluation Harness (basic LLM testing)

Goal:
Verify the tool consistently produces valid JSON and correct structure for different inputs.

Description:
Create a small testing script that runs several predefined prompts through the tool automatically and validates that the output JSON contains required keys. This prevents prompt or model changes from silently breaking the system.

Subtasks:

[x] 005-1 Create test prompt dataset
Create a Python list with 5–10 different decision problems (career change, relocation, budgeting, job offers, business idea, etc.).

[x] 005-2 Run prompts automatically
Replace user input with a loop that sends each test prompt to the model and collects responses.

[x] 005-3 Validate required JSON keys
Check that every response contains:
goal
constraints
options
pros_cons
next_steps
cheer

Log an error if any key is missing.

[x] 005-4 Track pass / fail results
Log result for each test case.
Example:
Test 1 — PASS
Test 2 — FAIL

At the end print a summary:
Total tests
Passed
Failed

[x] 005-5 Save evaluation results
Write evaluation results to a log file (for example: eval_results.log).

Definition of Done:

• Script runs multiple prompts automatically
• JSON parsing still works
• Required keys are validated
• Pass/fail summary printed
• Results logged to file

---

TASK-011 – Response structure validation

Goal  
Ensure the model response not only contains required keys but also follows expected structure and size rules.

Problem  
LLMs may return JSON with correct keys but wrong content structure (too few options, missing pros/cons, mismatched keys).  
This can silently break downstream logic and reduce reliability.

Acceptance Criteria

- Program validates number of constraints (3–6)
- Program validates number of options (2–4)
- Program validates each option has matching entry inside pros_cons
- Program validates each pros and cons list has 3–5 items
- If validation fails → test is marked as failed and logged clearly
- Validation logic is separated into a dedicated function

Learning Objective

- Learn defensive programming for AI outputs
- Understand schema-like validation without external libraries
- Practice iterating nested dictionaries and lists
- Build production-style reliability checks

Subtasks

[x] Subtask 1 – Define validation rules  
Create constants for min/max lengths (constraints, options, pros, cons).

[x] Subtask 2 – Extend validation function  
Update existing validate_response() to also check list lengths.

[x] Subtask 3 – Validate pros_cons structure  
Check that each option name exists as key inside pros_cons.

[x] Subtask 4 – Validate pros/cons lengths  
Loop through pros_cons entries and verify item counts.

[x] Subtask 5 – Add validation logging  
Log exactly which rule failed and for which test case.

References

Python len()  
https://docs.python.org/3/library/functions.html#len

Python dict iteration  
https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

Python nested data structures  
https://realpython.com/python-dicts/

---
