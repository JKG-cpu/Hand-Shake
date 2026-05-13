from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any

__all__ = [
    "EventType",
    "Event"
]

class EventType(Enum):
    INCREASE_AGE = auto()

@dataclass
class Event:
    type: EventType
    function: dict[str, Any] = field(default_factory = dict)
