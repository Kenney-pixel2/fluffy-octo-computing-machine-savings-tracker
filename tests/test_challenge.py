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
