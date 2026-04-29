# Project Board

## Backlog

## TASK-010 – Packaging the Tool

Goal
Make the tool easy to install and run as a reusable application.

Problem
Currently the tool runs only via direct script execution.
Real tools are packaged for reuse and distribution.

Acceptance Criteria

- Project can be installed locally (e.g., pip install -e .)
- Entry point defined (e.g., CLI command)
- Dependencies managed via requirements or pyproject
- Clear run command (no manual path issues)
- Project structure clean and reusable

Learning Objective

- Understand Python packaging basics
- Learn how to structure projects properly
- Prepare tool for real-world usage

Subtasks

[ ] Subtask 1 – Define structure
Ensure proper folders and modules.

[ ] Subtask 2 – Add requirements
List dependencies.

[ ] Subtask 3 – Create entry point
Define CLI command.

[ ] Subtask 4 – Test install
Install locally and run.

[ ] Subtask 5 – Verify usability
Ensure tool runs without manual setup.

References

Python packaging
https://packaging.python.org/en/latest/tutorials/packaging-projects/

---

## This Sprint

---

## In Progress

---

## Project structure best practices

---

## Blocked

## TASK-023 – Basic UI (Streamlit)

Goal
Provide a minimal user interface to interact with the system and demonstrate its capabilities.

Problem
Currently the system is CLI-only, which makes it harder to demo, explain, and use interactively.
A simple UI improves usability and presentation without adding unnecessary complexity.

Acceptance Criteria

- UI allows user to input text
- UI triggers model pipeline (same as CLI)
- UI displays structured output clearly
- UI integrates with existing system (no duplicated logic)
- Runs locally with a single command
- No complex frontend (use simple framework)

Learning Objective

- Understand how to expose backend systems via UI
- Learn basic integration between UI and logic layer
- Practice keeping UI thin (no business logic inside UI)
- Improve project presentation for demos/interviews

Subtasks

[x] Subtask 1 – Choose framework
Use Streamlit (simple, fast, Python-based).

[x] Subtask 2 – Create UI file
Create `ui.py` (or similar entry point).

[ ] Subtask 3 – Add input field
Allow user to enter text (textarea or input box).

[ ] Subtask 4 – Trigger pipeline
Call existing logic (do NOT duplicate code).

[ ] Subtask 5 – Display output
Show model response in readable format.

[ ] Subtask 6 – Run and test
Ensure UI runs with single command and works end-to-end.

References

Streamlit docs
https://docs.streamlit.io/

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

[x] Subtask 1 – Configure FileHandler  
Add logging handler that writes logs to a file.

[x] Subtask 2 – Define log format  
Include timestamp, level, module name, message.

[x] Subtask 3 – Keep console logging  
Keep using print() for terminal.

[x] Subtask 4 – Test persistence  
Run program twice and confirm logs append to file.

References

Python logging tutorial  
https://docs.python.org/3/howto/logging.html

Logging handlers  
https://docs.python.org/3/library/logging.handlers.html

---

TASK-022 – Code modularization and project structure refactor

Goal
Restructure the project into clear modules so responsibilities are separated and the codebase becomes easier to maintain, extend, and test.

Problem
Currently most logic lives inside main.py.
As features grow (validation, retries, modes, logging), the file becomes harder to read and reuse.
Real applications organize code into modules by responsibility.

Acceptance Criteria

Project is split into logical modules (e.g., model.py, validation.py, config.py, cli.py)

main.py becomes a thin entry point that orchestrates execution

No business logic remains duplicated across files

Shared constants are moved to a dedicated config module

Functions receive dependencies via arguments (no reliance on globals from main)

Program runs exactly the same after refactor

Learning Objective

Understand modular architecture in Python projects

Learn separation of concerns

Practice importing between modules

Prepare system for packaging and scaling features

Subtasks

[x] Subtask 1 – Create config module
Move model name, validation limits, required keys, retry limits into config.py.

[x] Subtask 2 – Extract model interaction
Move call_model() and related logic into model.py.

[x] Subtask 3 – Extract validation logic
Move validate_response() and validation helpers into validation.py.
x[x] Subtask 4 – Extract CLI / mode logic
Move argument parsing and mode routing into cli.py or modes.py.

[x] Subtask 5 – Simplify main entry point
Refactor main.py so it only initializes client, reads args, and calls workflow functions also keeps default route code block

[x] Subtask 6 – Test refactored flow
Run full test suite / manual tests and confirm identical behavior.

References

Python modules tutorial
https://docs.python.org/3/tutorial/modules.html

---

TASK-006 – CLI UX improvements

Goal  
Improve terminal user experience and introduce simple execution modes such as `plan`, `summarize`, and `rage`.

Problem  
Current program runs tests in a fixed flow and prints raw technical output.  
There is no structured interaction layer or user-friendly command interface.  
Real tools provide modes that change behavior without modifying code.

Acceptance Criteria

- Program accepts CLI argument (e.g., --mode)
- Supported modes: plan, summarize, rage
- Each mode changes how results are displayed or processed
- Default mode still runs current test flow
- Invalid mode is handled with clear error message
- Mode selection is logged

Learning Objective

- Learn basic CLI argument parsing in Python
- Separate execution logic from presentation logic
- Understand how real tools provide multiple workflows
- Prepare architecture for future UX features

Subtasks

[x] Subtask 1 – Add argument parsing  
Use argparse (or sys.argv) to read --mode parameter.

[x] Subtask 2 – Define mode router  
Create function that routes execution based on selected mode.

[x] Subtask 3 – Implement `plan` mode  
Show structured goals / options summary without running full validation loop.

[x] Subtask 4 – Implement `summarize` mode  
Display final pass/fail summary only.

[x] Subtask 5 – Implement `rage` mode  
Show verbose logs, retries, raw responses preview.

[x] Subtask 6 – Handle invalid mode  
Print help message and exit cleanly.

References

argparse documentation  
https://docs.python.org/3/library/argparse.html

sys.argv basics  
https://docs.python.org/3/library/sys.html#sys.argv

Python CLI design guide  
https://realpython.com/command-line-interfaces-python-argparse/

---

TASK-017 – Output formatting

Goal  
Improve readability of CLI output so results are easier to scan and understand.

Problem  
Current terminal output is raw and inconsistent.  
When multiple tests run, it is difficult to quickly identify sections, results, and summaries.

Acceptance Criteria

- CLI output contains clear section headers (e.g., ===== TEST START =====)
- Each test result is visually separated
- Pass/fail status is clearly labeled
- Final summary block is easy to read
- No impact on validation or model logic
- Partial implementation based on CLI route is acceptable, as well as flexibility on formats

Learning Objective

- Practice improving developer experience (DX)
- Learn how presentation layer differs from business logic
- Understand importance of structured output in CLI tools

Subtasks

[x] Subtask 1 – Add section separators  
Print visual separators before and after each test case.

[x] Subtask 2 – Standardize labels  
Use consistent labels such as GOAL, CONSTRAINTS, OPTIONS, RESULT.

[x] Subtask 3 – Improve pass/fail display  
Highlight test result clearly (e.g., PASSED / FAILED).

[x] Subtask 4 – Add final summary block  
Display total tests, passed tests, failed tests in structured format.

References

Python print formatting  
https://docs.python.org/3/tutorial/inputoutput.html

String formatting  
https://realpython.com/python-f-strings/

---

TASK-014 – Response cleaning module

Goal  
Create a reusable function that cleans raw model responses before JSON parsing.

Problem  
LLM responses often contain markdown blocks (```json), explanations, duplicated text, or trailing characters.  
This causes JSON parsing errors and makes retry logic less reliable.  
Currently response cleaning logic is scattered inside main execution flow.

Acceptance Criteria

- Raw model response is passed through a dedicated cleaning function
- Function removes markdown code fences (`/`json)
- Function extracts first valid JSON object using { … } boundaries
- Function trims whitespace and stray characters before/after JSON
- Function returns cleaned JSON string ready for json.loads()
- Cleaning module is reusable across all CLI modes
- Cleaning failures are logged clearly
- Partial cleaning success is acceptable (system may still retry)

Learning Objective

- Understand preprocessing pipelines in AI systems
- Learn separation of concerns (model call vs response processing)
- Improve robustness of JSON-driven workflows
- Prepare system for multi-model support

Subtasks

[x] Subtask 1 – Create cleaning module  
Create new file (e.g., `cleaner.py`) and define `clean_response(raw_text)` function.

[x] Subtask 2 – Remove markdown wrappers  
Strip `json and ` blocks safely.

[x] Subtask 3 – Extract JSON boundaries  
Find first `{` and last `}` and slice response.

[x] Subtask 4 – Handle edge cases  
Return `None` or raise controlled error if JSON cannot be extracted.

[x] Subtask 5 – Integrate into main flow  
Replace inline cleaning logic with module function.

[x] Subtask 6 – Add logging  
Log when cleaning modifies response or fails.

References

Python string methods  
https://docs.python.org/3/library/stdtypes.html#string-methods

Exception handling  
https://docs.python.org/3/tutorial/errors.html

Regular expressions (optional improvement)  
https://docs.python.org/3/library/re.html

---

TASK-013 – Model configuration layer

Goal
Centralize all model-related settings into a dedicated configuration structure so the system becomes easier to tune, debug, and extend.

Problem
Currently model name, retry limits, validation limits, and other runtime parameters are scattered across modules.
This makes experimentation harder and increases risk of inconsistent behavior.

Acceptance Criteria

Model name is defined in one configuration location
Retry limits are configurable without modifying logic files
Validation limits (e.g., constraints count, options count) are stored in config
API-related parameters (e.g., temperature, max tokens if used) are configurable
All modules read settings from config instead of hardcoding values
Program behavior remains identical after refactor

Learning Objective

Learn configuration patterns used in production systems
Understand separation between code logic and runtime parameters
Prepare architecture for multi-model and environment switching
Practice passing config into functions instead of relying on globals

Subtasks

[x] Subtask 1 – Define configuration structure
Create dictionary or constants in config.py for model settings and limits.

[x] Subtask 2 – Move model parameters
Move model name and retry count from code into config.

[x] Subtask 3 – Move validation limits
Store min/max lengths for constraints, options, pros, cons, next_steps in config.

[x] Subtask 4 – Refactor imports
Update modules to read values from config instead of local variables.

[x] Subtask 5 – Verify behavior
Run evaluation harness and confirm results are unchanged.

References

Python configuration patterns
https://realpython.com/python-application-configuration/

Python modules
https://docs.python.org/3/tutorial/modules.html

---

TASK-019 – Result persistence

Goal  
Persist evaluation results and model responses to files so runs can be reviewed, compared, and analyzed later.

Problem  
Currently test results are only visible in terminal and partially in logs.  
There is no structured storage of outcomes (PASS/FAIL), cleaned JSON, or raw model responses.  
Real AI systems persist outputs for debugging, regression testing, and performance tracking.

Acceptance Criteria

- Program saves evaluation results to a structured file (e.g., results.json or results.csv)
- Each test case record includes:
  - test name
  - pass / fail status
  - number of retries
  - response time
  - validation errors (if any)
- Optionally store cleaned JSON response
- Optionally store raw model response preview
- File appends or creates new run section (no silent overwrite)
- Saving results does not break CLI modes
- Persistence logic is separated into a dedicated module

Learning Objective

- Understand result tracking in AI pipelines
- Learn structured file writing (JSON / CSV)
- Practice designing simple data schemas
- Prepare system for later analytics and dashboards

Subtasks

[x] Subtask 1 – Design result schema  
Define Python dictionary structure for one test result.

[x] Subtask 2 – Collect results during evaluation  
Accumulate results in a list during test loop.

[x] Subtask 3 – Create persistence module  
Create file such as `persistence.py` with function `save_results(results)`.

[x] Subtask 4 – Write results to JSON file  
Serialize results list using `json.dump()`.

[x] Subtask 5 – Prevent overwrite  
Append timestamped run section or create new file per run.

[x] Subtask 6 – Integrate into evaluation flow  
Call save function after summary block.

References

Python JSON writing  
https://docs.python.org/3/library/json.html#json.dump

Working with files  
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

TASK-015 – Improve logging system

Goal  
Introduce structured logging across the AI pipeline so each run can be traced end-to-end.  
Logs should help understand failures, retries, model behavior, and validation issues.

Problem  
Currently logging is partial and inconsistent across modules.  
Some important events (cleaning step, model retries, validation errors, scoring decisions) are not clearly visible.  
In real AI systems, structured logs are essential for debugging, monitoring, and reproducibility.

Acceptance Criteria

- Each pipeline run logs:
  - raw user input
  - cleaned input
  - model request start
  - retry attempts (if any)
  - raw model response preview
  - cleaned JSON response
  - validation result
  - scoring result
- Errors include meaningful context (which test, which step, which exception)
- Logging level can be configured (INFO vs DEBUG)
- Logging format is consistent across modules
- Logs do not break CLI modes
- Logger initialization is centralized (no duplicate setup)

Learning Objective

- Understand observability in AI pipelines
- Practice structured logging design
- Learn logging levels and debugging strategies
- Improve system reliability mindset
- Prepare system for future scaling and monitoring

Subtasks

[x] Subtask 1 – Define logging strategy  
Decide what events must be logged and at which level (INFO / DEBUG / ERROR).

[x] Subtask 2 – Centralize logger setup  
Ensure single logger configuration reused across modules.

[x] Subtask 3 – Add pipeline step logs  
Log transitions: input → cleaning → model call → validation → scoring.

[x] Subtask 4 – Add retry attempt logging  
Log retry count, reason for retry, and delay if implemented.

[x] Subtask 5 – Improve error logging  
Wrap model / validation / parsing blocks with contextual error logs.

[x] Subtask 6 – Add logging level configuration  
Allow switching verbosity via config or CLI flag.

[x] Subtask 7 – Validate logs during evaluation run  
Run evaluation mode and confirm logs are readable and complete.

References

Python logging HOWTO  
https://docs.python.org/3/howto/logging.html

Logging library reference  
https://docs.python.org/3/library/logging.html

---

TASK-018 – Error classification

Goal  
Classify and track different types of failures in the AI pipeline to better understand where and why the system breaks.

Problem  
Currently all failures are treated similarly (fail / retry), without distinguishing the root cause.  
This makes it difficult to analyze model reliability, debug issues, and understand whether failures come from the model, parsing, validation, or preprocessing.

Acceptance Criteria

- System distinguishes at least the following error types:
  - cleaner failure (no JSON extracted)
  - parsing error (invalid JSON)
  - validation error (schema/structure issues)
  - model error (API / runtime failure)
- Each failure type is:
  - logged clearly
  - tracked per test case
- Final summary includes count of each error type
- Classification does not break existing retry logic
- Error classification integrates with existing logging system

Learning Objective

- Understand failure modes in AI pipelines
- Learn how to categorize errors for debugging and analysis
- Improve observability beyond pass/fail metrics
- Prepare system for evaluation insights and monitoring

Subtasks

[x] Subtask 1 – Define error categories  
Create a fixed set of error types (e.g., CLEANER_ERROR, PARSE_ERROR, VALIDATION_ERROR, MODEL_ERROR).

[x] Subtask 2 – Map errors in pipeline  
Identify where each error occurs (cleaner, json.loads, validation, model call).

[x] Subtask 3 – Track error per test  
Store error type during retries and final result.

[x] Subtask 4 – Aggregate error statistics  
Count occurrences of each error type across all tests.

[x] Subtask 5 – Log error summary  
Log total counts per error type at the end of run.

[x] Subtask 6 – Verify behavior  
Run evaluation and confirm classification is correct and consistent.

References

Error handling patterns in Python  
https://docs.python.org/3/tutorial/errors.html

Observability concepts  
https://martinfowler.com/articles/observability.html

---

TASK-020 – Model abstraction layer

Goal  
Introduce a model abstraction layer so the system can switch between different model providers (e.g., HuggingFace, OpenAI) without changing application logic.

Problem  
Currently the model call is tightly coupled to a specific provider (HuggingFace) inside the code.  
This makes it difficult to switch models, compare providers, or extend the system.  
Real AI systems use abstraction layers to decouple application logic from model providers.

Acceptance Criteria

- Model interaction is accessed through a single interface (e.g., ModelClient)
- CLI and application logic do not directly depend on HuggingFace or any provider
- At least one provider implementation exists (HuggingFace)
- System behavior remains unchanged after refactor
- Model provider and model name are configurable via config
- Code structure allows easy addition of new providers later

Learning Objective

- Understand abstraction and interface design
- Learn how to decouple external dependencies from core logic
- Practice designing extensible architecture
- Prepare system for multi-model experimentation and comparison

Subtasks

[x] Subtask 1 – Create ModelClient interface  
Define a class in `model.py` that exposes a single method (e.g., `generate(prompt)`).

[x] Subtask 2 – Move HuggingFace logic into implementation  
Wrap existing HuggingFace call inside ModelClient (or a dedicated class).

[x] Subtask 3 – Replace direct model calls  
Update `cli.py` to use ModelClient instead of `call_model()`.

[x] Subtask 4 – Add provider configuration  
Use config to define provider and model name.

[x] Subtask 5 – Verify behavior  
Run system and confirm output and logging remain unchanged.

[x] Subtask 6 – Prepare for extension  
Ensure structure allows adding new providers without modifying CLI logic.

References

Python classes and OOP  
https://docs.python.org/3/tutorial/classes.html

Designing abstractions  
https://refactoring.guru/design-patterns/adapter/python/example

---

TASK-016 – Evaluation dataset expansion

Goal  
Create a larger and more structured evaluation dataset to systematically test model behavior, prompt quality, and system reliability.

Problem  
Current evaluation dataset is small and limited.  
It does not cover enough variation in real-world scenarios, making it difficult to assess model consistency, edge cases, and failure patterns.  
Without a richer dataset, evaluation results are not reliable or representative.

Acceptance Criteria

- Dataset contains at least 15–25 test cases
- Test cases cover different categories (e.g., career, finance, personal decisions, ambiguity, edge cases)
- Each test case has:
  - name
  - input text
- Dataset remains easy to extend (simple structure, no hardcoding in logic)
- Evaluation runs without modification to existing pipeline
- New dataset improves visibility of failures and inconsistencies

Learning Objective

- Learn how to design evaluation datasets for AI systems
- Understand importance of coverage and edge cases
- Practice thinking in terms of test scenarios instead of single inputs
- Improve ability to benchmark and compare model behavior

Subtasks

[x] Subtask 1 – Analyze current dataset  
Review existing test cases and identify missing categories or weaknesses.

[x] Subtask 2 – Define dataset categories  
Define 4–6 categories (e.g., simple, complex, ambiguous, edge cases, emotional, practical).

[x] Subtask 3 – Create additional test cases  
Add new test cases to reach at least 15–25 total.

[x] Subtask 4 – Ensure consistent structure  
Verify all test cases follow same schema (name + input + category).

[x] Subtask 5 – Run evaluation with expanded dataset  
Execute tests and observe differences in pass/fail rates.

[x] Subtask 6 – Document findings  
Summarize what types of inputs fail or degrade model performance.

References

Prompt evaluation best practices  
https://platform.openai.com/docs/guides/evals

Dataset design basics  
https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting

---

TASK-012 – Prompt Template System

Goal
Introduce a prompt template system so prompts are reusable, structured, and easily adjustable without changing code.

Problem
Currently prompts are hardcoded inside the application logic.
This makes iteration slow, testing difficult, and mixing logic with prompt design.
Real AI systems separate prompt design from code to allow fast experimentation.

Acceptance Criteria

- Prompts are stored as external template files (e.g., in `templates/` folder)
- Application loads templates dynamically based on mode
- User input is injected into templates via placeholders (e.g., `{user_input}`)
- CLI and core logic do not contain hardcoded prompts
- Switching templates changes model behavior without code changes
- System behavior remains unchanged after refactor

Learning Objective

- Understand separation of concerns (logic vs prompt design)
- Learn how to externalize dynamic content using templates
- Practice building flexible input pipelines for AI systems
- Enable fast iteration and testing of prompts

Subtasks

[x] Subtask 1 – Create templates folder
Create `templates/` directory and add basic templates (e.g., `plan.txt`, `summarize.txt`, `rage.txt`).

[x] Subtask 2 – Define template structure
Add placeholders (e.g., `{user_input}`) inside templates for dynamic content.

[x] Subtask 3 – Load template in code
Implement logic to read template file based on selected mode.

[x] Subtask 4 – Inject user input
Replace placeholders with actual input before sending to model.

[x] Subtask 5 – Replace hardcoded prompts
Remove existing inline prompt strings and use templates instead.

[x] Subtask 6 – Verify behavior
Run system and confirm outputs remain consistent and templates control behavior.

References

Python file handling
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

String formatting
https://docs.python.org/3/library/string.html#formatstrings

---

TASK-007 – Local Memory and Weekly Summaries

Goal
Introduce local memory so the system can store previous sessions and generate summaries over time.

Problem
Currently the system is stateless. Each run starts fresh with no awareness of previous interactions.
Real AI systems persist data to enable continuity, tracking, and improvement.

Acceptance Criteria

- System stores results of each run locally (e.g., JSON file)
- Each entry includes at least: input, output, timestamp, and mode
- System can load past sessions
- Ability to generate a simple summary of recent sessions (e.g., last N entries)
- No external database (local file only)
- Existing functionality remains unchanged

Learning Objective

- Understand persistence and state management
- Learn how to store and retrieve structured data
- Practice building simple memory systems
- Prepare foundation for retrieval (RAG)

Subtasks

[x] Subtask 1 – Design memory structure
Define JSON structure for storing sessions.

[x] Subtask 2 – Save results
After each run, append results to memory file.

[x] Subtask 3 – Load memory
Implement function to read stored sessions.

[x] Subtask 4 – Implement summary
Create simple summary (e.g., last 5 entries).

[x] Subtask 5 – Integrate into CLI
Allow triggering summary mode or use in pipeline.

[x] Subtask 6 – Verify behavior
Ensure memory persists across runs and summaries work.

References

Python JSON handling
https://docs.python.org/3/library/json.html

---

TASK-026 – Refactor Router Functions and Core Logic

Goal
Refactor duplicated logic across router functions by extracting shared behavior into reusable components while keeping mode-specific behavior separate.

Problem
Current implementation contains significant duplication across route functions (test, plan, summarize, rage, default).
Core logic such as retry handling, model calls, validation, and timing is repeated multiple times, making the code harder to maintain and extend.

Acceptance Criteria

- Core logic (retry, model call, cleaning, parsing, validation) is extracted into a single reusable function
- Route functions no longer duplicate core logic
- Mode-specific behavior (printing, logging, formatting output) remains separate
- No `if mode == ...` branching inside core logic
- System behavior remains unchanged after refactor
- Code becomes shorter, cleaner, and easier to extend

Learning Objective

- Understand separation of concerns
- Learn how to refactor duplicated code safely
- Practice designing reusable functions
- Improve code maintainability and readability

Subtasks

[x] Subtask 1 – Identify duplicated logic
Locate repeated blocks across all route functions.

[x] Subtask 2 – Extract core function
Create a function (e.g., `run_test_case`) handling:

- retry logic
- model call
- cleaning
- parsing
- validation
- timing

[x] Subtask 3 – Define return structure
Ensure core function returns structured data:

- status
- parsed output
- errors
- duration
- attempts

[x] Subtask 4 – Update route functions
Replace duplicated logic with calls to the core function.

[x] Subtask 5 – Keep presentation separate
Ensure each mode handles its own printing/logging without modifying core logic.

[x] Subtask 6 – Verify behavior
Run all modes and confirm outputs and logs remain unchanged.

References

Refactoring principles
https://refactoring.guru/refactoring

---

TASK-025 – Multi-Model Support & Experimentation

Goal
Enable the system to run with multiple model providers and compare their outputs.

Problem
Currently the system supports only one active model at a time.
Real AI systems often compare models, switch providers, and implement fallback strategies.

Acceptance Criteria

- System supports multiple providers (e.g., HuggingFace + another provider)
- Models can be switched via config or CLI
- Ability to run same input across multiple models
- Outputs from different models can be compared
- Optional fallback if primary model fails
- CLI logic remains unchanged when adding new providers

Learning Objective

- Understand multi-model architecture
- Learn how to compare model behavior
- Practice building flexible and extensible systems
- Prepare for real-world AI experimentation

Subtasks

[x] Subtask 1 – Add new provider
Implement second client (e.g., OpenAI or alternative).

[x] Subtask 2 – Extend provider mapping
Add new provider to existing mapping structure.

[x] Subtask 3 – Enable switching
Allow selecting provider via config or CLI.

[x] Subtask 4 – Add experiment mode
Run same input through multiple models.

[x] Subtask 5 – Compare outputs
Display or log differences between models.

[x] Subtask 6 – Implement fallback
If primary model fails, call secondary model.

References

Multi-model systems concept
https://platform.openai.com/docs/guides/production-best-practices

---

TASK-008 – Retrieval Augmented Generation (RAG)

Goal
Enhance model responses by retrieving relevant past data and injecting it into prompts.

Problem
Currently the model only sees the current input.
Real AI systems improve responses by using relevant past context.

Acceptance Criteria

- System retrieves relevant past entries from memory
- Retrieved context is injected into prompt before model call
- Retrieval logic is simple (e.g., keyword match or recent items)
- Works with existing template system
- No external vector DB or embeddings (keep simple)
- Behavior improves or changes based on past context

Learning Objective

- Understand RAG concept (retrieve + augment + generate)
- Learn how to enrich prompts with context
- Practice simple retrieval strategies
- Build foundation for advanced AI systems

Subtasks

[x] Subtask 1 – Load memory
Reuse memory loader from TASK-007.

[x] Subtask 2 – Select relevant entries
Implement simple retrieval (keyword or recent N).

[x] Subtask 3 – Format context
Convert retrieved entries into prompt-friendly text.

[x] Subtask 4 – Inject into prompt
Add context before user input in template.

[x] Subtask 5 – Test behavior
Verify responses change based on past data.

[x] Subtask 6 – Keep system simple
Avoid overengineering (no embeddings, no DB).

References

RAG concept
https://huggingface.co/docs/transformers/main/en/tasks/rag

---

TASK-024 – Metrics

Goal
Introduce structured metrics and basic decision scoring to evaluate system performance and improve output usefulness.

Problem
Currently the system generates structured outputs but lacks measurement and decision quality signals.
Without metrics, it is difficult to assess performance, compare runs, or improve the system.

Acceptance Criteria

- System tracks key metrics:
  - success rate per category
  - average attempts per test
  - error distribution (MODEL, CLEANER, PARSE, VALIDATION)
  - latency per test

- Metrics are aggregated and logged at end of run
- Output includes a version field (e.g., `"version": "v1"`)
- No external tools (keep within current structure)

Learning Objective

- Understand evaluation and measurement in AI systems
- Learn how to quantify system performance
- Practice adding lightweight scoring logic
- Improve system credibility for real-world use

Subtasks

[x] Subtask 1 – Extend result structure
Add fields for latency, attempts, errors, and version.

[x] Subtask 2 – Aggregate metrics
Compute summary statistics across all tests.

[x] Subtask 3 – Log metrics
Display aggregated results clearly at end of run.

[x] Subtask 5 – Validate integration
Ensure metrics do not break existing pipeline.

References

Python statistics
https://docs.python.org/3/library/statistics.html

---

## TASK-009 – Speech-to-Text Input

Goal
Allow user to provide input via voice using a local speech-to-text model.

Problem
Currently input is text-only.
Adding speech improves usability but is not core system logic.

Acceptance Criteria

- User can record or input audio
- Audio is converted to text locally
- Converted text is used as standard input
- Works with existing pipeline (no changes to core logic)
- Uses lightweight/local model (no heavy infra)

Learning Objective

- Understand speech-to-text basics
- Learn how to integrate external tools into pipeline
- Practice handling different input types

Subtasks

[x] Subtask 1 – Choose library
Select simple STT tool (e.g., Whisper local).

[x] Subtask 2 – Capture audio
Allow recording or file input.

[x] Subtask 3 – Convert to text
Run speech model and get transcript.

[x] Subtask 4 – Integrate
Feed transcript into existing flow.

[x] Subtask 5 – Test
Verify accuracy and usability.

References

OpenAI Whisper
https://github.com/openai/whisper

---

## TASK-027 – Robustness Layer

Goal
Improve system stability by handling failures, timeouts, and fallback scenarios.

Problem
Current system assumes ideal conditions and may fail or break when model calls, parsing, or validation do not behave as expected.

Acceptance Criteria

- Retry logic implemented (at least 1 retry on failure)
- Timeout handling added to model calls
- Fallback model is triggered on primary failure
- Errors are properly logged and categorized
- System does not crash on failure and continues execution

Learning Objective

- Understand failure handling in AI pipelines
- Learn how to build resilient systems
- Practice defensive programming

Subtasks
[x] Subtask 1 – Retry logic Add retry mechanism for model calls
[x] Subtask 2 – Timeout handling Ensure model calls do not hang indefinitely
[x] Subtask 3 – Fallback model Use secondary model when primary fails
[x] Subtask 4 – Error handling Improve logging and prevent crashes
[x] Subtask 5 – Integration Ensure robustness layer does not break existing pipeline

References
Python exception handling https://docs.python.org/3/tutorial/errors.html

---
