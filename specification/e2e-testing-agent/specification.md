# Specification: e2e-testing-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read `product-requirements-document.md` and `intent.md`
- [x] Bootstrap agent code in `assets/e2e-testing-agent/` using the `sap-agent-bootstrap` skill (invoke from inside `assets/e2e-testing-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills needed — the hello world scope has no complex multi-step workflow or domain-specific branching logic.

---

## Project-Specific Tasks

### Agent Identity & System Prompt

- [x] Set agent name: `E2E Testing Agent`
- [x] Set agent description: `A hello world E2E testing agent that accepts a test task and returns a structured result`
- [x] Write a system prompt in `app/agent.py` (via `@prompt_section`) that instructs the agent to:
  - Accept a test task input
  - Execute the hello world test scenario (return a greeting + task echo)
  - Return a structured JSON result with fields: `status`, `task`, `result`
  - Never fabricate data — only return what was received as input

### Hello World Task Handling

- [x] Implement tool `run_hello_world_test(task: str) -> dict` in `app/` that:
  - Accepts a task name string
  - Returns `{"status": "passed", "task": task, "result": "Hello, World! Test executed successfully."}`
- [x] Wire the tool into the agent graph so the agent calls it when processing a test task

### Health Check

- [x] Confirm `/.well-known/agent.json` is served correctly and contains `name`, `description`, and `version`

---

## Business Instrumentation

- [x] Implement structured logging and OpenTelemetry spans for all 4 milestones from the PRD:
  - `M1.achieved: agent initialised and health-check passed` / `M1.missed: agent failed to start or health-check timed out`
  - `M2.achieved: hello world task executed and result returned` / `M2.missed: test task did not produce a result`
  - `M3.achieved: end-to-end flow verified successfully` / `M3.missed: end-to-end flow did not complete`
  - `M4.achieved: all pre-built tests passed` / `M4.missed: one or more pre-built tests failed`
- [x] Extract business logic from `stream()` into a plain async helper (e.g. `_run_agent()`) and instrument that method — do NOT use span context managers inside async generators
- [x] Verify `auto_instrument()` is called at top of `main.py` before any AI framework imports

---

## MCP Tool Integration

No SAP API integrations required for hello world scope. Skip MCP translation, setup-solution for MCP assets, and mock generation.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write unit test for `run_hello_world_test` tool in `assets/e2e-testing-agent/tests/test_hello_world_tool.py` — run immediately after writing
- [x] Write one integration test in `assets/e2e-testing-agent/tests/test_e2e_flow.py` that calls the agent's `invoke` function with mocked LLM responses — verifies a structured result is returned
- [x] Run `pytest` from `assets/e2e-testing-agent/` (no args) — fix any failures before proceeding
- [x] Verify `app/agent.py` has exactly 5 decorated functions — confirmed: 5
- [x] Run `pytest` again (no args) from `assets/e2e-testing-agent/` to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/e2e-testing-agent/`
