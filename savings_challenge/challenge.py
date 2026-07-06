from dataclasses import dataclass


@dataclass(frozen=True)
class Challenge:
    name: str
    target_amount: int
    target_days: int

    @property
    def daily_target(self) -> float:
        return self.target_amount / self.target_days

    def amount_for_day(self, day: int) -> int:
        base = self.target_amount // self.target_days
        remainder = self.target_amount % self.target_days

        if day <= remainder:
            return base + 1

        return base
