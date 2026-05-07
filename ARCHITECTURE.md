# Architecture

## Overview

AI Decision Assistant is a lightweight AI application that converts unstructured user input into validated structured decision data.

The architecture evolved from a simple terminal learning project into a deployed AI system with:

- FastAPI backend
- Streamlit frontend
- multi-model orchestration
- validation pipeline
- retry and fallback handling
- persistence layer
- deployment support

The system prioritizes:

- reliability
- simplicity
- modularity
- visibility into failures
- practical AI engineering patterns

---

# High-Level Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
FastAPI Endpoint
  │
  ▼
Core Pipeline
  │
  ├── Prompt Templates
  ├── Model Layer
  ├── Cleaner
  ├── Parser
  ├── Validation
  ├── Retry / Fallback
  ├── Metrics
  └── Persistence
  │
  ▼
Structured JSON Response
```
