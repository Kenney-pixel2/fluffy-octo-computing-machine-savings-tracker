# Savings Challenge Development Journal

> Building **Savings Challenge** one Challenge Day at a time using
> Test-Driven Development.

---

# Challenge Day No. 1 — Foundation

**Date:** YYYY-MM-DD

## Goal

Set up the project foundation.

## Accomplished

- Initialized Git repository.
- Created Poetry project.
- Configured Ruff.
- Configured mypy.
- Configured pytest.
- Installed pre-commit hooks.

## Lessons Learned

A solid development environment reduces friction for every future feature.

## Next Challenge Day

Create the `Challenge` domain model.

---

# Challenge Day No. 2 — First Domain Object

**Date:** YYYY-MM-DD

## Goal

Create the core `Challenge` model.

## Tests

- `test_create_challenge`

## Accomplished

- Added immutable `Challenge` dataclass.
- Introduced the first domain model.

## Lessons Learned

Start with the simplest model that satisfies the test. Avoid adding behavior prematurely.

## Next Challenge Day

Calculate the daily target.

---

# Challenge Day No. 3 — Daily Target

**Date:** YYYY-MM-DD

## Goal

Calculate the daily savings amount.

## Tests

- `test_calculate_daily_target`

## Accomplished

- Added the `daily_target` property.

## Lessons Learned

Derived values are often best expressed as read-only properties.

## Next Challenge Day

Distribute the remainder across challenge days.

---

# Challenge Day No. 4 — Distribute the Remainder

**Date:** YYYY-MM-DD

## User Story

> As a saver,
>
> I want every day's savings target to be a whole peso,
>
> so that I can save practical amounts while still reaching my goal exactly.

## Goal

Ensure that a challenge always reaches its target amount using whole-peso daily savings by distributing any remainder fairly across the challenge period.

## Tests

- `test_first_day_gets_extra_peso`
- `test_last_day_has_normal_amount`
- `test_total_of_all_days_equals_target_amount`

## Accomplished

- Added `Challenge.amount_for_day(day)`.
- Calculated the base daily amount using integer division.
- Distributed the remainder by adding one peso to the earliest days of the challenge.
- Verified that the sum of all daily amounts exactly equals the target amount.

Example:

```text
Target Amount : ₱5,000
Target Days   : 30

Base Amount   : ₱166
Remainder     : ₱20

Days 1–20  : ₱167
Days 21–30 : ₱166

Total Saved : ₱5,000
```

## Design Decisions

- Daily savings should always be whole pesos.
- The remainder is distributed across the first `remainder` days.
- The algorithm guarantees that the total savings exactly matches the target amount.
- Kept the implementation inside the `Challenge` class. No separate calculator class was introduced, following the YAGNI principle.

## Lessons Learned

A simple algorithm can provide a much better user experience than rounding up or down. By distributing the remainder across the earliest days, users receive a predictable savings schedule that always reaches the intended goal without requiring a large adjustment on the final day.

This was also a good reminder to focus tests on observable behavior rather than implementation details.

## Quality Checks

- ✅ Ruff
- ✅ mypy
- ✅ pytest
- ✅ pre-commit hooks

## Git

```text
feat: distribute remainder across challenge days
```

## Next Challenge Day

Track challenge progress by answering questions such as:

- How many days have been completed?
- How much has been saved?
- How many days remain?
- Is the challenge complete?

---

# Challenge Day No. 5 — Complete a Day

**Date:** 2026-07-07

## User Story

> As a saver,
>
> I want to mark today's savings as completed,
>
> so that I can keep track of my progress.

## Goal

A challenge should remember that a day has been completed.

## Tests

- `test_complete_day_increments_completed_days`

## Design Decisions

- A `Challenge` is now a mutable object because its progress changes over time.
- Progress is tracked using the `completed_days` attribute.
- Completing a day is represented by the `complete_day()` method instead of modifying `completed_days` directly.
- Kept progress tracking inside the `Challenge` class. No separate progress or state management class was introduced, following the YAGNI principle.

## Accomplished

- Added the `completed_days` attribute to the `Challenge` model.
- Introduced the `complete_day()` method to represent completing a day's savings.
- Initialized every new challenge with zero completed days.
- Verified that calling `complete_day()` increments the completed day count.

Example:

```text
New Challenge

Completed Days : 0

↓

challenge.complete_day()

↓

Completed Days : 1
```

## Quality Checks

- ✅ Ruff
- ✅ mypy
- ✅ pytest
- ✅ pre-commit hooks

## Git

```text
feat: track completed challenge days
```

## Next Challenge Day

Calculate the number of days remaining in a challenge.

Questions to answer:

- How many days are left to complete the challenge?
- Does completing a day reduce the remaining days?
- Can a challenge ever have a negative number of remaining days?

---

# Challenge Day No. 6  — Tracking Remaining Days
**Date:** 2026/07/08

## Feature: Track Remaining Days

> As a saver,
>
> I want to know how many days remain in my challenge,
>
> so that I can track my progress toward completion.

### Background:

Given the target days are set to \<target>

#### Scenario Outline: Calculate remaining days for different completion levels

- **Given** the target days are \<target>
- **And** the completed days are \<completed>
- **When** I calculate the remaining days
- **Then** the remaining days should be \<remaining>

    **Examples:**

    | target | completed | remaining |
    |--------|-----------|-----------|
    | 30     | 0         | 30        |
    | 30     | 1         | 29        |

### Tests

- `def test_new_challenge_has_all_days_remaining() -> None`
- `def test_completed_day_reduces_remaining_days() -> None`

## Design Decisions

- Exposed `remaining_days` as a read-only property because it is derived state.
- Calculated the value directly from `target_days` and `completed_days` instead of storing redundant data.
- Deferred validation against negative values until a future requirement demands it, 
following the TDD principle of implementing only the behavior required by the current tests.

### Git

```
    feat: calculate remaining challenge days
```

### Lessons Learned

Derived values should not be stored when they can be calculated from existing state. 
Keeping `remaining_days` as a computed property avoids duplication 
and ensures the value is always consistent with the challenge's progress.

### Next Day Challenge

Refactor the project to use the standard Python src/ layout while keeping all tests passing.

---

# Challenge Day No. 7 — Adopt the `src/` Layout

**Date:** 2026-07-10

## User Story

> As a developer,
>
> I want to organize the project using the standard `src/` layout,
>
> so that imports are explicit and tests execute against the installed package instead of the source tree.

## Objective

Refactor the project to use the standard Python `src/` layout while keeping all tests passing.

## Tasks

Before ending Challenge Day No. 7, verify that all of the following are complete:

- [x] Refactored the project to use the `src/` layout.
- [x] Updated `pyproject.toml` to recognize the package in `src/`.
- [x] Ran `poetry install` successfully.
- [x] Verified that all imports continue to work correctly.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

## Lessons Learned

Software engineering isn't just adding features—it also involves improving the structure that supports those features.

Adopting the standard `src/` layout early in the project makes the package structure more explicit and ensures that tests run against the installed package rather than relying on the current working directory.

## Git Commits

```text
refactor: adopt src project layout
```

## Next Challenge Day

Determine when a challenge is complete.

Questions to answer:

- When should a challenge be considered complete?
- Does completing the final day mark the challenge as complete?
- Can a challenge still be completed more than once?

---

# Challenge Day No. 8 — Complete a Challenge
**Date:** 2026-07-13

## User Story

> As a saver,
>
> I want to know when my savings challenge is complete,
>
> so that I can celebrate reaching my goal and stop tracking that challenge.

## Objective

A `Challenge` should report whether it has been completed.

## Acceptance Criteria

A challenge is **not complete** when:
```
Target Days    : 30
Completed Days : 29
```
A challenge **is complete** when:
```
Target Days    : 30
Completed Days : 30
```

## Design Decisions

- Exposed `is_complete` as a read-only property because completion is derived from the challenge's progress.
- Considered a challenge complete when `completed_days` is greater than or equal to `target_days`.
- Deferred deciding how to handle attempts to complete an already finished challenge until a future requirement introduces that behavior.

## Tasks

Before ending Challenge Day No. 8, verify that all of the following are complete:

- [x] Added the `is_complete` property.
- [x] Verified that a new challenge is not complete.
- [x] Verified that completing all days marks the challenge as complete.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

## Git Commits

```text

feat: determine when a challenge is complete

```

## Lessons Learned

Not every piece of state needs to be stored. Like `remaining_days`, 
whether a challenge is complete can be derived from existing data. 
Keeping derived state out of the model reduces duplication and helps ensure consistency.


## Next Challenge Day

Prevent a completed challenge from being completed again.

*Questions to answer:*

- What should happen if `complete_day()` is called after the challenge is already complete?
- Should the method raise an exception or simply ignore the request?
- How can we ensure that `completed_days` never exceeds `target_days`?

---
# Challenge Day No. 9 -- Prevent Completing a Challenge Twice

**Date:** 2026-07-14

## User Story

> As a saver,
>
> I want a completed challenge to reject additional completed days,
>
> so that my progress always reflects reality.
>

## Objective

Prevent `completed_days` from ever exceeding `target_days`.

## Acceptance Criteria

**Given**

```

Target Days     : 30
Completed Days  : 30

```

**When** I issue this command

```

challenge.complete_day()

```

**Then** the app should reject the command.

## Design Discussion

**Handling Invalid Operations**

*Objective:* Establish a consistent strategy for rejecting invalid operations 
before implementation begins.

*Candidate Approaches*

    Ignore the call – Silently discard the operation.

    Return False – Indicate failure via a boolean response.

    Raise an exception – Halt execution with an explicit error.

**Recommendation: Raise an Exception**

*Rationale*

    🔍 Immediate failure detection – Invalid operations (e.g., advancing to Day 31 in a 
    30‑day challenge) indicate a programming error, not a routine runtime condition.

    🛡️ Fail‑fast principle – Exceptions expose bugs at the source, 
    preventing silent data corruption or inconsistent state.

    📐 Semantic clarity – The caller is forced to handle or acknowledge the error, 
    making code self‑documenting.

*Implementation Plan*

    Initial choice: Use Python’s built‑in ValueError – simple, standard, and sufficient 
    for current needs.

    Future extension: If the project evolves to require richer domain signaling 
    (e.g., ChallengeAlreadyCompletedError), we can introduce custom exception subclasses 
    without changing the overall handling strategy.

*Key Takeaway*

    Exceptions are the preferred mechanism for invalid‑operation scenarios, 
    aligning with defensive programming and maintainability goals.

## Tasks

Before ending Challenge Day No. 9, verify that all of the following are complete:

- [x] Prevented a completed challenge from being completed again.
- [x] Verified that attempting to exceed the target days raises a ValueError.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

## Git

```

feat: prevent completing challenge beyond target days

```

## Lessons Learned

A domain model should enforce its own business rules. 
By preventing invalid state transitions inside the `Challenge` class, 
we ensure that every part of the application can rely on the model to remain consistent, 
regardless of how it is used.

## Next Challenge Day

Calculate the total amount saved based on completed challenge days.

Questions to answer:

- How much has been saved so far?
- Does the calculation account for the distributed remainder?
- Does the saved amount always match the sum of the completed daily targets?

---
# Challenge Day No. 10 — Calculate Amount Saved
**Date:** 07-15-2026

## User Story

> As a saver,
>
> I want to know how much money I have saved,
>
> so that I can measure my progress toward my savings goal.

## Objective

Calculate the total amount saved based on the completed challenge days.

## Acceptance Criteria

**Given**

```
Target Amount : ₱5,000
Target Days   : 30
```

**When** the schedule is

```
Days 1–20 : ₱167
Days 21–30: ₱166
```

**And** 

```
Completed Days : 5
```

**Then**
```
Amount Saved : ₱835
```

## Design Decision

Following the DRY principle, Calculate it whenever needed.

```python

@property
def amount_saved(self) -> int:
    ...

```

## Tasks

Before ending Challenge Day No. 10, verify that all of the following are complete:

- [x] Added the amount_saved property.
- [x] Verified that a new challenge starts with zero pesos saved.
- [x] Verified the saved amount after completing several days.
- [x] Verified that a completed challenge has saved the target amount.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

## Git

```

feat: calculate saved amount from completed days

```

## Lessons Learned

Derived state should be computed from existing behavior whenever possible. 
By building `amount_saved` on top of `amount_for_day()`, 
the model has a single source of truth for the daily savings schedule, 
reducing duplication and making future changes easier to maintain.

## Next Challenge Day

Calculate challenge progress as a percentage.

Questions to answer:

- What percentage of the challenge has been completed?
- Should a new challenge report 0% progress?
- Should a completed challenge report exactly 100% progress?

---

## Challenge Day No. 11 - Calculate Challenge Progress

**Date:** July 17, 2026

## User Story

> As a saver,
>
> I want to see my overall progress,
>
> so that I can quickly understand how far I am from completing my savings challenge.

## Objective

Calculate the challenge's progress as a percentage.

## Acceptance Criteria

A new challenge should report:

```
Completed Days : 0
Progress       : 0%
```

Halfway through the challenge:

```
Completed Days : 15
Target Days    : 30

Progress       : 50%
```

A completed challenge should report:

```
Completed Days : 30
Progress       : 100%
```

## Design Dicussion

There are several ways to represent progress:

- integer percentage

- decimal

- double percentage

**Recommendation:** integer percentage

**Rationale:** 

- Simple to display in the GUI.
- No floating-point rounding surprises.
- Easy to use with a progress bar.

## Tasks

Before ending Challenge Day No. 11, verify that all of the following are complete:

- [x] Added the progress_percentage property.
- [x] Verified that a new challenge starts at 0% progress.
- [x] Verified that a halfway-completed challenge reports 50% progress.
- [x] Verified that a completed challenge reports 100% progress.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

## Git

```

feat: calculate challenge progress percentage

```

## Lessons Learned

Progress is another example of derived state. Computing it from existing data keeps 
the model simple and ensures that the reported progress is always consistent with 
the challenge's current state.

## Next Day Challenge

Introduce a `ChallengeManager` to manage multiple challenges.

Questions to answer:

- How are challenges added and removed?
- How can all active challenges be retrieved?
- How does the application ensure each challenge has a unique identity?

---

## Challenge Day No. 12 — Introduce ChallengeManager

**Date:** July 18, 2026

### User Story

> As a saver,
>
> I want the application to manage multiple savings challenges,
>
> so that I can work toward several financial goals at the same time.
>

### Objective

Introduce a ChallengeManager that maintains a collection of Challenge objects.

### Design Discussion

Today we need to answer an important question.

Where should multiple challenges live?

Not here:

```python

Challenge

```

A Challenge should never know about other challenges.

Instead:

```

ChallengeManager
    ├── Challenge
    ├── Challenge
    ├── Challenge

```

This follows the Single Responsibility Principle.

Challenge manages one challenge.
ChallengeManager manages many challenges.

## Acceptance Criteria

A new manager

```

ChallengeManager()

```

contains

```

0 challenges

```

After adding one challenge

```

1 challenge

```

### Tasks

Before ending Challenge Day No. 12, verify that all of the following are complete:

- [x] Added the ChallengeManager class.
- [x] Verified that a new manager starts with zero challenges.
- [x] Added the ability to add a Challenge.
- [x] Verified that the manager tracks the correct number of challenges.
- [x] Ruff passes.
- [x] mypy passes.
- [x] pytest passes.
- [x] Code committed.
- [x] Journal updated.
- [x] Changes pushed to GitHub.

### Git

```
feat: introduce ChallengeManager

```

### Lessons Learned

Managing a collection of objects is a different responsibility from modeling a single object. 
Introducing `ChallengeManager` keeps the domain model cohesive and prepares the application 
for managing multiple savings challenges without increasing the complexity of the `Challenge` 
class.

### Next Day Challenge
Retrieve managed challenges.

Questions to answer:

- How can all managed challenges be retrieved?
- Should the internal collection remain protected from modification?
- Should challenges be returned in the order they were added?
