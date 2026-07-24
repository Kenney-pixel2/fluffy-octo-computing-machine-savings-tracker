from challenge.challenge import Challenge
from challenge.challenge_manager import ChallengeManager


class ChallengeService:
    def __init__(self, manager: ChallengeManager) -> None:
        self._manager = manager

    def create_challenge(
        self,
        name: str,
        target_amount: int,
        target_days: int,
    ) -> None:
        challenge = Challenge(
            name=name,
            target_amount=target_amount,
            target_days=target_days,
        )

        self._manager.add_challenge(challenge)
