# Architecture

## Overview

The AI Decision Assistant is a simple terminal-based system that converts unstructured user input into structured decision data using a large language model.

The system is intentionally minimal to focus on reliability patterns for LLM applications.

---

## System Flow

1. User enters a description of a situation in the terminal.

2. The application sends the input to a large language model with a prompt instructing the model to return structured JSON.

3. The model generates a response.

4. The application cleans the response and extracts the JSON object.

5. The JSON is parsed into a Python dictionary.

6. The structured information is displayed to the user.

---

## High-Level Components

### 1. Input Layer

Responsible for collecting user input from the terminal.

Responsibilities:

- accept unstructured text
- pass input to the prompt builder

---

### 2. Prompt Layer

Constructs the prompt sent to the model.

Responsibilities:

- instruct model to return JSON
- define the expected schema
- include user input

---

### 3. LLM Inference Layer

Sends the prompt to a model via HuggingFace inference API.

Responsibilities:

- authenticate with API token
- send request to model
- receive completion response

---

### 4. Output Processing Layer

Handles the model response.

Responsibilities:

- remove markdown wrappers
- extract JSON content
- parse JSON using Python

Future improvements:

- schema validation
- automatic retry on invalid output

---

### 5. Presentation Layer

Displays structured decision information in the terminal.

Responsibilities:

- show goal
- list constraints
- list options
- display pros/cons
- display next steps

---

## Current Architecture Characteristics

- single Python script
- synchronous model calls
- terminal-only interface
- minimal dependencies

---

## Planned Architectural Improvements

Future development will introduce:

- schema validation layer
- retry logic for invalid outputs
- prompt version management
- logging and metrics
- evaluation framework
- optional speech-to-text input

---

## Design Philosophy

The architecture prioritizes:

- simplicity
- transparency
- reliability of LLM outputs
- incremental improvement
- learning AI engineering patterns
