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

### Git

```
    feat: calculate remaining challenge days
```
