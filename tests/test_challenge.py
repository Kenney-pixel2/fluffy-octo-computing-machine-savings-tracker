from savings_challenge.challenge import Challenge


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
