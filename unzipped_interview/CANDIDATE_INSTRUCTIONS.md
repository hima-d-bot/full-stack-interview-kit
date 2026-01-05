# Full-Stack Interview Challenge

Welcome! Your goal is to fix a set of bugs in this task management application and implement a small feature.

## The Application
- **Frontend**: React + TypeScript (Vite)
- **Backend**: FastAPI (Python)

## Setup
1. **Backend**:
   ```bash
   cd apps/api
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
2. **Frontend**:
   ```bash
   cd apps/web
   npm install
   npm run dev
   ```

## Your Tasks
1. **Fix Existing Bugs**: There are several bugs across the stack. Some are explicit (failing tests), others are implicit (UI oddness).
   - Run backend tests: `pytest apps/api/tests/test_api.py`
   - Observe the UI for inconsistent sorting or empty states.
2. **Algorithmic Optimization**: The "Task Suggestion" feature is slow. Optimize it to handle larger datasets efficiently.
3. **Feature Request**: Once the bugs are fixed, add a "Due Today" filter to the task list.

## Evaluation Criteria
- **Correctness**: Do the tests pass? Does the UI work?
- **Reasoning**: Can you explain *why* a bug occurred?
- **Code Quality**: Is your fix clean and idiomatic?
- **Efficiency**: Did you identify the O(N²) trap?
