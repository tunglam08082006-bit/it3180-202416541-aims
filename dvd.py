"""A DVD is one configuration item in the small AIMS domain."""
from dataclasses import dataclass


@dataclass(frozen=True)
class DigitalVideoDisc:
    title: str
    category: str = ""
    director: str = ""
    length: int = 0
    cost: float = 0.0

    def __str__(self):
        return f"{self.title} | {self.category} | {self.cost:.2f} $"
