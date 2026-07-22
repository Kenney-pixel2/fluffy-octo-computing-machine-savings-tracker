import pytest

from challenge.challenge import Challenge


def test_create_challenge() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )
    assert challenge.name == "Groceries"
    assert challenge.target_amount == 5_000
    assert challenge.target_days == 30


def test_calculate_daily_target() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert challenge.daily_target == 5_000 / 30


def test_first_day_gets_extra_peso() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert challenge.amount_for_day(1) == 167


def test_last_day_has_normal_amount() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert challenge.amount_for_day(30) == 166


def test_total_of_all_days_equals_target_amount() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    total = sum(challenge.amount_for_day(day) for day in range(1, 31))

    assert total == 5000


def test_complete_day_increments_completed_days() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    challenge.complete_day()

    assert challenge.completed_days == 1


def test_new_challenge_has_all_days_remaining() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert challenge.remaining_days == 30


def test_completed_day_reduces_remaining_days() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    challenge.complete_day()

    assert challenge.remaining_days == 29


def test_new_challenge_is_not_complete() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert not challenge.is_complete


def test_challenge_is_complete_after_final_day() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    for _ in range(30):
        challenge.complete_day()

    assert challenge.is_complete


def test_cannot_complete_more_days_than_target() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    for _ in range(30):
        challenge.complete_day()

    with pytest.raises(ValueError):
        challenge.complete_day()


def test_new_challenge_has_saved_nothing() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    assert challenge.amount_saved == 0


def test_amount_saved_after_five_days() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5_000,
        target_days=30,
    )

    for _ in range(5):
        challenge.complete_day()

    assert challenge.amount_saved == 835


def test_completed_challenge_has_saved_target_amount() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5000,
        target_days=30,
    )

    for _ in range(30):
        challenge.complete_day()

    assert challenge.amount_saved == 5000


def test_new_challenge_has_zero_percent_progress() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5000,
        target_days=30,
    )

    assert challenge.progress_percentage == 0


def test_half_completed_challenge_has_fifty_percent_progress() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5000,
        target_days=30,
    )

    for _ in range(15):
        challenge.complete_day()

    assert challenge.progress_percentage == 50


def test_completed_challenge_has_one_hundred_percent_progress() -> None:
    challenge = Challenge(
        name="Groceries",
        target_amount=5000,
        target_days=30,
    )

    for _ in range(30):
        challenge.complete_day()

    assert challenge.progress_percentage == 100


def test_cannot_rename_to_empty_string() -> None:
    challenge = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    with pytest.raises(ValueError):
        challenge.rename("")
