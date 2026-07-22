import pytest

from challenge.challenge import Challenge
from challenge.challenge_manager import ChallengeManager


def test_new_manager_starts_empty() -> None:
    manager = ChallengeManager()

    assert manager.challenge_count == 0


def test_manager_can_add_challenge() -> None:
    manager = ChallengeManager()

    challenge = Challenge(
        name="Emergency Fund",
        target_amount=10000,
        target_days=60,
    )

    manager.add_challenge(challenge)

    assert manager.challenge_count == 1


def test_new_manager_returns_empty_challenges() -> None:
    manager = ChallengeManager()

    assert manager.challenges == ()


def test_manager_returns_challenges_in_added_order() -> None:
    manager = ChallengeManager()

    emergency = Challenge(
        name="Emergency Fund",
        target_amount=10000,
        target_days=60,
    )

    vacatio = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    manager.add_challenge(emergency)
    manager.add_challenge(vacatio)

    assert manager.challenges == (
        emergency,
        vacatio,
    )


def test_remove_existing_challenge() -> None:
    manager = ChallengeManager()

    emergency = Challenge(
        name="Emergency Fund",
        target_amount=10000,
        target_days=60,
    )

    vacation = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    manager.add_challenge(emergency)
    manager.add_challenge(vacation)

    manager.remove_challenge(emergency)

    assert manager.challenges == (vacation,)


def test_removing_unknown_challenge_raises_value_error() -> None:
    manager = ChallengeManager()

    challenge = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    with pytest.raises(ValueError):
        manager.remove_challenge(challenge)


def test_find_existing_challenge_by_name() -> None:
    manager = ChallengeManager()

    vacation = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    manager.add_challenge(vacation)

    assert manager.find_challenge("Vacation") is vacation


def test_find_unknown_challenge_returns_none() -> None:
    manager = ChallengeManager()

    assert manager.find_challenge("Vacation") is None


def test_rename_challenge() -> None:
    challenge = Challenge(
        name="Vacation",
        target_amount=30000,
        target_days=180,
    )

    challenge.rename("Japan Vacation")

    assert challenge.name == "Japan Vacation"
