---
description: Executing a Feature Development Cycle (Plan -> TDD -> Dev -> Ship)
---

# Feature Development Cycle

// turbo-all

Standard workflow for implementing a new feature or fix.

## 1. Plan & TDD

1. **Create/Update Task**:
   - Add new item to `task.md`.
   - Mark as in-progress `[/]`.

2. **Create Reproduction/Test Case**:
   - Create a new test file or add a case to existing test.
   - Run test to confirm failure (RED):
   ```
   .venv\Scripts\pytest.exe tests/new_test_case.py
   ```

## 2. Develop

3. **Implement Feature**:
   - Modify `src/` code.
   - Run test again to confirm pass (GREEN):
   ```
   .venv\Scripts\pytest.exe tests/new_test_case.py
   ```

4. **Verify Global Integrity**:
   - Run all tests:
   ```
   .venv\Scripts\pytest.exe tests/ -q
   ```
   - Run linting:
   ```
   .venv\Scripts\ruff.exe check src/ tests/
   ```

## 3. Verify & Ship

5. **Smoke Test (Optional but recommended)**:
   - Run `/smoke-test` if relevant to parser/generator changes.

6. **Commit & Push**:
   - Use the `/push-pr` workflow or manual git commands.
