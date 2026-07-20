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
