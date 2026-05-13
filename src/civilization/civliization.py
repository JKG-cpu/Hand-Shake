from collections import defaultdict
from typing import Callable

from .events import *
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
