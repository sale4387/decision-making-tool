# Technical Decisions

This document records major architectural and technical decisions made during development of the AI Decision Assistant.

The goal is to capture:

- why decisions were made
- what tradeoffs were accepted
- how the architecture evolved

This document focuses on reasoning, not implementation details.

---

# Decision 001 – Start with Terminal-First Architecture

## Decision

The project initially started as a terminal-based application.

## Reasoning

- Faster iteration
- Lower complexity
- Easier debugging
- Focus on AI engineering instead of frontend work
- Better visibility into raw model behavior

## Tradeoff

- Poor usability for non-technical users
- Limited presentation value

## Final Outcome

The project later evolved into:

- FastAPI backend
- Streamlit UI
- deployed web application

but the terminal-first approach accelerated learning significantly.

---

# Decision 002 – Use Hosted APIs Instead of Local Models

## Decision

Use hosted inference APIs instead of running models locally.

## Reasoning

- No GPU requirements
- Faster experimentation
- Easier deployment
- Ability to test multiple providers quickly
- Lower infrastructure complexity

## Tradeoff

- External dependency
- API limits and costs
- Provider instability
- Less control over infrastructure

## Providers Used

- HuggingFace
- Google Gemini

---

# Decision 003 – Use Structured JSON Outputs

## Decision

Require all model responses to follow strict JSON structure.

## Reasoning

- Enables deterministic parsing
- Enables validation
- Enables API/UI integration
- Makes outputs machine-readable
- Allows downstream automation

## Tradeoff

- Models frequently fail strict formatting
- Requires retries and cleaning
- Prompt engineering becomes more difficult

## Final Outcome

Structured outputs became the foundation of the entire system architecture.

---

# Decision 004 – Separate Prompt Templates from Logic

## Decision

Move prompts into external template files.

## Reasoning

- Faster prompt iteration
- Cleaner codebase
- Easier experimentation
- Separation of concerns

## Tradeoff

- Templates and validators must remain synchronized
- Poor prompt changes can silently reduce output quality

## Final Outcome

Template-based prompting became one of the most useful architectural decisions in the project.

---

# Decision 005 – Build Validation Layer Instead of Trusting Model

## Decision

Never trust raw model output directly.

## Reasoning

LLMs:

- hallucinate
- omit keys
- ignore formatting instructions
- produce inconsistent structure

Validation was necessary for:

- reliability
- API safety
- UI stability

## Tradeoff

- Stricter validation increases failure rate
- More retries and fallback calls required

## Final Outcome

Validation became a core architectural principle.

---

# Decision 006 – Use Manual Validation Instead of Heavy Schema Frameworks

## Decision

Implement custom validation logic manually.

## Reasoning

- Better understanding of reliability problems
- Lower dependency complexity
- Easier debugging during learning phase

## Tradeoff

- More maintenance work
- Less elegant than full schema frameworks

## Final Outcome

Manual validation worked well for MVP scale and learning objectives.

---

# Decision 007 – Add Retry Logic Early

## Decision

Retry invalid outputs automatically.

## Reasoning

Malformed outputs were common even with strict prompts.

Retries:

- improved reliability
- reduced manual reruns
- improved UX

## Tradeoff

- Increased latency
- Increased API usage

## Final Outcome

Retries significantly improved system stability.

---

# Decision 008 – Add Fallback Model Provider

## Decision

Use secondary provider when primary provider fails.

## Reasoning

Different providers:

- fail differently
- follow instructions differently
- vary in reliability

Fallback improved:

- resilience
- uptime
- experimentation

## Tradeoff

- Increased complexity
- Different providers behave inconsistently
- More runtime metadata required

## Final Outcome

Fallback handling became one of the strongest parts of the architecture.

---

# Decision 009 – Use Gemini for Reliability and HuggingFace for Experimentation

## Decision

Use Gemini as stronger structured-output provider and HuggingFace for experimentation/open models.

## Reasoning

Gemini:

- followed JSON instructions more reliably
- reduced validation failures

HuggingFace:

- enabled testing open models
- enabled experimentation with Mistral/Qwen

## Tradeoff

- Mixed provider ecosystem
- Different latency and reliability behavior

## Final Outcome

The combination worked well for balancing experimentation and stability.

---

# Decision 010 – Keep Persistence Lightweight

## Decision

Use JSONL file persistence instead of database.

## Reasoning

- Faster implementation
- Simpler debugging
- Minimal infrastructure
- Good enough for MVP

## Tradeoff

- Poor scalability
- Weak querying
- Ephemeral cloud storage issues

## Final Outcome

JSONL worked well locally but became a limitation after deployment.

---

# Decision 011 – Use Simple RAG Instead of Embeddings

## Decision

Use recent sessions instead of vector databases or embeddings.

## Reasoning

- Faster implementation
- Easier to understand
- No external infrastructure
- Lower complexity

## Tradeoff

- No semantic relevance filtering
- Noisy context possible
- Limited scalability

## Final Outcome

Simple context injection was sufficient for MVP learning goals.

---

# Decision 012 – Prefer Simplicity Over Overengineering

## Decision

Avoid enterprise-scale architecture during MVP phase.

## Reasoning

Focus areas were:

- learning
- shipping
- understanding reliability patterns

not:

- Kubernetes
- distributed systems
- enterprise auth
- advanced observability stacks

## Tradeoff

- Some production limitations remain unresolved

## Final Outcome

This decision accelerated progress significantly.

---

# Decision 013 – Move from Batch Testing to Single-Input Flow

## Decision

Transition from evaluation-focused architecture into real user workflow.

## Reasoning

Batch testing:

- increased cost
- increased complexity
- no longer matched real usage

Single-input flow:

- simplified UX
- simplified architecture
- matched deployment goals

## Tradeoff

- Less automated benchmarking

## Final Outcome

The system became much closer to a real AI product.

---

# Decision 014 – Keep UI Thin

## Decision

Keep Streamlit frontend intentionally simple.

## Reasoning

The project focus remained:

- AI pipeline engineering
- backend reliability
- model orchestration

not frontend development.

## Tradeoff

- Basic visual appearance
- Limited frontend flexibility

## Final Outcome

Thin UI allowed focus to remain on core AI architecture.

---

# Decision 015 – API-First Architecture After MVP

## Decision

Expose pipeline through FastAPI endpoint.

## Reasoning

API layer:

- enables UI integration
- improves reusability
- simulates real production architecture
- supports future integrations

## Tradeoff

- Introduced deployment complexity
- Added dependency/environment issues

## Final Outcome

API architecture made the project portfolio-ready.

---

# Decision 016 – Track Runtime Metadata

## Decision

Return metadata together with model outputs.

## Reasoning

Metadata such as:

- provider
- retries
- duration
- fallback
- quality
- errors

helps:

- debugging
- evaluation
- transparency

## Tradeoff

- Larger responses
- More complexity in persistence and UI

## Final Outcome

Metadata became extremely valuable during debugging and iteration.

---

# Decision 017 – Use Render for Deployment

## Decision

Deploy API and UI using Render.

## Reasoning

- Simple deployment flow
- GitHub integration
- Free tier available
- Good enough for MVP

## Tradeoff

- Ephemeral storage
- Cold starts
- Limited production features

## Final Outcome

Render enabled fast deployment and portfolio visibility.

---

# Decision 018 – Prioritize Reliability over Pure AI Capability

## Decision

Optimize for:

- predictable outputs
- validation success
- stability

instead of:

- most advanced reasoning
- largest model
- most creative responses

## Reasoning

The project goal was AI engineering reliability, not raw model intelligence.

## Tradeoff

- Some responses became more constrained or rigid

## Final Outcome

The system became significantly more dependable.

---

# Decision 019 – Use Simple Heuristic Evaluation

## Decision

Implement lightweight quality scoring instead of advanced evaluation systems.

## Reasoning

- Easier to understand
- Faster to implement
- Lower complexity
- Good enough for MVP visibility

## Tradeoff

- Quality evaluation is subjective and shallow
- No semantic scoring

## Final Outcome

Simple scoring added useful visibility without overengineering.

---

# Decision 020 – Learn Through Shipping

## Decision

Continue evolving the system instead of endlessly redesigning architecture upfront.

## Reasoning

Many architectural lessons only appeared after:

- retries failed
- providers behaved differently
- deployment broke
- validation exposed issues
- persistence stopped working on cloud

## Tradeoff

- Some early architectural choices had to be refactored later

## Final Outcome

The project evolved organically into a much more realistic AI application than originally planned.

---

# Final Architectural Direction

The final architecture became:

- API-first
- validation-focused
- multi-model
- modular
- deployment-ready
- reliability-oriented

while intentionally remaining:

- lightweight
- understandable
- inexpensive
- iterative

The project prioritizes practical AI engineering patterns over theoretical complexity.
