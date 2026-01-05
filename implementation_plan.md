# Full-Stack Interview Kit Implementation Plan

## 1. Frontend Bugs (Implicit)
### Bug 1: State Mutation in Sorting
- **Symptom**: Sorting the task list behaves inconsistently or doesn't update the UI correctly.
- **Root Cause**: `tasks.sort()` is used directly on the state array, mutating it in-place.
- **Fix**: Create a copy of the array before sorting: `[...tasks].sort()`.

### Bug 2: Stale Debounced Handler
- **Symptom**: Search results are inconsistent or lag behind the input.
- **Root Cause**: The debounced search function captures stale state or is recreated on every render without `useCallback`.
- **Fix**: Use `useCallback` with correct dependencies or a `useRef` for the debounced function.

## 2. Backend Bugs (Implicit)
### Bug 1: Unstable Pagination Ordering
- **Symptom**: Duplicate tasks appear on different pages, or some tasks are skipped.
- **Root Cause**: SQL query (or mock repo) sorts by a non-unique field (e.g., `created_at`) without a deterministic tie-breaker (e.g., `id`).
- **Fix**: Add `id` as a secondary sort key.

### Bug 2: Off-by-one in Pagination
- **Symptom**: The last item of page N is the first item of page N+1.
- **Root Cause**: Incorrect slicing logic in the repository: `filtered[skip : skip + limit]` vs `filtered[limit : limit + skip]`.
- **Fix**: Correct the slice indices.

## 3. Integration Mismatch (Implicit)
### Bug 1: Response Shape Mismatch
- **Symptom**: UI shows "No tasks" despite the backend returning data.
- **Root Cause**: Backend returns `{ items: [...] }` but Frontend expects `{ data: [...] }`.
- **Fix**: Align the key names in both FE and BE.

### Bug 2: Naming Mismatch (CamelCase vs snake_case)
- **Symptom**: Task details (like `createdAt`) are missing in the UI.
- **Root Cause**: Backend sends `created_at` but Frontend expects `createdAt`.
- **Fix**: Use a consistent naming convention or a mapper.

## 4. Algorithmic Complexity Trap
### Challenge: Task Suggestion Engine
- **Scenario**: A function `suggest_tasks(query, tasks)` that finds similar tasks.
- **Naive Solution**: Nested loops with repeated `.lower()` and string operations inside the inner loop, leading to O(N*M) or worse.
- **Optimized Solution**: Pre-process tasks into a searchable index or use a Set/Dict for lookups.
- **Test**: Use an `ops_counter` to assert that the number of operations is below a specific threshold.

## 5. Refactor Pressure
- **Task**: Add a "Due Today" quick filter or a "Total Count" in the pagination response.
- **Goal**: See if the candidate can integrate these changes into the existing (now fixed) architecture without breaking things.
