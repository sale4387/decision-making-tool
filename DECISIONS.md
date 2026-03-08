# Technical Decisions

This document records important technical decisions made during the development of the AI Decision Assistant.
The goal is to capture **why decisions were made**, not just what was implemented.

---

## Decision 001 – Terminal-First Interface

**Decision**
The tool will initially be built as a terminal-based application rather than a web or mobile interface.

**Reasoning**

- Focus on learning AI engineering patterns instead of UI development.
- Faster iteration cycle.
- Simpler debugging and testing.
- Keeps project scope manageable.

**Tradeoff**

- Less user-friendly for non-technical users.

**Future Option**

A simple UI could be added later once the core logic is reliable.

---

## Decision 002 – Use Hosted LLM APIs Instead of Local Models

**Decision**
Use hosted models through the HuggingFace inference API.

**Reasoning**

- No need for local GPU or heavy model downloads.
- Faster experimentation with different models.
- Lower infrastructure complexity.

**Tradeoff**

- Dependence on external services.
- Potential cost if usage increases.

**Future Option**

Evaluate running small models locally if the system grows.

---

## Decision 003 – Structured JSON Outputs

**Decision**
Model responses must be returned in structured JSON format.

**Reasoning**

- Enables deterministic parsing in Python.
- Allows building programmatic features on top of model outputs.
- Improves reliability compared to free-form text responses.

**Tradeoff**

- Models occasionally return malformed JSON.
- Requires additional validation logic.

**Mitigation**

Implement JSON cleaning, parsing safeguards, and schema validation.

---

## Decision 004 – Clean and Extract JSON Before Parsing

**Decision**

Before parsing the response with `json.loads()`, the system extracts the JSON object from the model output.

**Reasoning**

LLMs often return responses wrapped in markdown blocks such as:

```json
{
  ...
}
```

This causes parsing errors.

Extracting the JSON between the first `{` and last `}` ensures the parser receives valid content.

---

## Decision 005 – Version Controlled Development

**Decision**

The project will use Git and GitHub from the beginning.

**Reasoning**

- Track changes and progress.
- Maintain a development history.
- Organize project documentation.
- Simulate professional development workflow.

---

## Decision Philosophy

When making technical choices, the project prioritizes:

- learning AI engineering concepts
- minimizing unnecessary complexity
- incremental improvements
- reliability over sophistication
