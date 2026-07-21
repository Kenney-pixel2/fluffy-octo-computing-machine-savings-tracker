from challenge.challenge import Challenge


class ChallengeManager:
    def __init__(self) -> None:
        self._challenges: list[Challenge] = []

    @property
    def challenge_count(self) -> int:
        return len(self._challenges)

    def add_challenge(self, challenge: Challenge) -> None:
        self._challenges.append(challenge)

    @property
    def challenges(self) -> tuple[Challenge, ...]:
        return tuple(self._challenges)

    def remove_challenge(self, challenge: Challenge) -> None:
        self._challenges.remove(challenge)
