import time
from src import *
from src.civilization.events import Event, EventType

civ = Civilization("My First Civilization")

civ.add_node(
    node = Node("First Node")
)

civ.start()

i = 10
while i > 0:
    time.sleep(1)
    i -= 1

civ.stop()

print(civ._total_ticks)