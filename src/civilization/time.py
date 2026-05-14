from dataclasses import dataclass

__all__ = [
    "Time",
    "TICKS_PER_DAY",
    "DAYS_PER_MONTH",
    "MONTHS_PER_YEAR",
    "TICK_SPEED"
]

TICKS_PER_DAY = 5
DAYS_PER_MONTH = 20
MONTHS_PER_YEAR = 12
TICK_SPEED = 0.5

@dataclass
class Time:
    tick:  int = 0
    day:   int = 0
    month: int = 0
    year:  int = 0

    @classmethod
    def from_ticks(cls, total_ticks: int) -> "Time":
        """Get all units from raw tick count"""
        day_total = total_ticks // TICKS_PER_DAY
        month_total = day_total // DAYS_PER_MONTH
        year = month_total // MONTHS_PER_YEAR

        return cls(
            tick = total_ticks % TICKS_PER_DAY,
            day = day_total % DAYS_PER_MONTH,
            month = month_total % MONTHS_PER_YEAR + 1,
            year = year,
        )

    def __str__(self) -> str:
        return f"Year {self.year}, Month {self.month}, Day {self.day}, Tick {self.tick}"
