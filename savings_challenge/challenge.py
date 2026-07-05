from dataclasses import dataclass


@dataclass(frozen=True)
class Challenge:
    name: str
    target_amount: int
    target_days: int

    @property
    def daily_target(self) -> float:
        return self.target_amount / self.target_days
