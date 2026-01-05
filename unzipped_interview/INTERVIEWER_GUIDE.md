# Interviewer Guide

This kit contains intentional bugs designed to test a candidate's debugging skills, architectural understanding, and algorithmic awareness.

## Bug Categories & Signals

| Category | Bug | Root Cause | Signal |
|----------|-----|------------|--------|
| **Frontend** | Sorting Inconsistency | `tasks.sort()` mutates state in-place. | Understands React state immutability. |
| **Frontend** | Stale Fetch | Missing deps in `useEffect` or missing `useCallback`. | Understands hook lifecycles. |
| **Backend** | Unstable Pagination | Missing deterministic tie-breaker in SQL/Sort. | Attention to detail in data consistency. |
| **Backend** | Pagination Off-by-one | Incorrect slice indices `[limit : limit+skip]`. | Basic logic and testing rigor. |
| **Integration** | Empty UI | Backend returns `items`, FE expects `data`. | Network log inspection vs blind guessing. |
| **Algorithm** | Slow Suggestions | O(N*M) due to repeated normalization in loops. | Identifies redundant operations; uses pre-computation. |

## Refactor Pressure Task
Ask the candidate to:
- "Add a total count to the pagination response" (Tests if they update both schema and UI).
- "Add a 'Due Today' filter" (Tests if they can modify the repository and router safely).

## Expected Solutions
- **FE Sort**: `[...tasks].sort(...)`
- **BE Pagination**: `sorted(tasks, key=lambda x: (x['created_at'], x['id']))` and `tasks[skip : skip+limit]`
- **Integration**: Align keys to `data`.
- **Algorithm**: Move `.lower()` outside the loops or pre-process tasks.
