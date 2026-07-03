from dataclasses import dataclass


@dataclass(frozen=True)
class Challenge:
    name: str
    target_amount: int
    target_days: int
