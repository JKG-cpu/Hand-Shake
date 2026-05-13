from src import *
from src.civilization.events import Event, EventType

civ = Civilization("My First Civilization")

civ.add_node(
    node = Node("First Node")
)

civ.emit(Event(EventType.INCREASE_AGE))
civ.emit(Event(EventType.INCREASE_AGE))

print(civ.nodes["First Node"].age)