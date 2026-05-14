import asyncio
from collections import defaultdict
from typing import Callable

from .events import *
from .time import *
from ..nodes import Node

__all__ = [
    "Civilization"
]

class Civilization:
    """
    A class for handling + creating new civilizations
    """
    def __init__(self, civilization_name: str) -> None:
        self.name = civilization_name
        self.nodes: dict[str, Node] = {}
        self._listeners: dict[EventType, list[Callable[[Event], None]]] = defaultdict(list)

        self.current_time: Time = Time()
        self._total_ticks: int = 0
        self._scheduled: dict[int, list[Event]] = defaultdict(list)
        self._time_task: asyncio.Task | None = None

    # Time System
    #region
    def schedule(self, tick: int, event: Event) -> None:
        """Schedule an event to happen at a specified tick"""
        self._scheduled[tick].append(event)

    def schedule_at(self, event: Event, *, year: int = 0, month: int = 1, day: int = 0, tick: int = 0) -> None:
        total = (
            year * MONTHS_PER_YEAR * DAYS_PER_MONTH, * TICKS_PER_DAY +
            (month - 1) * DAYS_PER_MONTH * TICKS_PER_DAY +
            day * TICKS_PER_DAY +
            tick
        )
        self._scheduled[total].append(event)

    async def _run_time(self) -> None:
        while True:
            self._total_ticks += 1
            self.current_time = Time.from_ticks(self._total_ticks)

            if self._total_ticks in self._scheduled:
                for event in self._scheduled[self._total_ticks]:
                    self.emit(event)
                
            if self.current_time.tick == 0 and self.current_time.day == 0 and self.current_time.month == 1:
                self.emit(EventType.INCREASE_AGE)

    def start(self) -> None:
        """Start Time System"""
        self._time_task = asyncio.create_task(self._run_time())

    def stop(self) -> None:
        """Stop the Time System"""
        if self._time_task:
            self._time_task.cancel()
            self._time_task = None
    #endregion

    # Event System
    #region
    def on(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        """Register an event"""
        self._listeners[event_type].append(handler)
    
    def off(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        """Unregister an event"""
        self._listeners[event_type].remove(handler)
    
    def emit(self, event: Event) -> None:
        """Fire an event — notifies all registered handlers, then updates nodes."""
        for handler in self._listeners[event.type]:
            handler(event)
        self._update_nodes(event)
    #endregion

    # Handling Nodes
    #region
    def add_node(self, node: Node) -> bool:
        """Add a node to the civilization"""
        if node.name in self.nodes:
            return False

        self.nodes[node.name] = node
        return True

    def remove_node(self, node_name: str) -> bool:
        """Remove a node by name"""
        if node_name not in self.nodes:
            return False

        del self.nodes[node_name]
        return True
    
    def _update_nodes(self, event: Event) -> None:
        """Update all the nodes on an event"""
        for node in self.nodes.values():
            node.on_event(event)
    #endregion
