from challenge.challenge_manager import ChallengeManager
from challenge.challenge_service import ChallengeService


def test_create_challenge_adds_it_to_manager() -> None:
    manager = ChallengeManager()
    service = ChallengeService(manager)

    service.create_challenge(
        name="Emergency Fund",
        target_amount=10000,
        target_days=60,
    )

    assert manager.challenge_count == 1
