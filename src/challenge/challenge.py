from dataclasses import dataclass, field


@dataclass
class Challenge:
    name: str
    target_amount: int
    target_days: int
    completed_days: int = field(default=0)

    @property
    def daily_target(self) -> float:
        return self.target_amount / self.target_days

    def amount_for_day(self, day: int) -> int:
        base = self.target_amount // self.target_days
        remainder = self.target_amount % self.target_days

        if day <= remainder:
            return base + 1

        return base

    def complete_day(self) -> None:
        self.completed_days += 1

    @property
    def remaining_days(self) -> int:
        return self.target_days - self.completed_days

    @property
    def is_complete(self) -> bool:
        return self.completed_days >= self.target_days
