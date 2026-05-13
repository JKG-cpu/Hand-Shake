# RoadMap of building HandShake

## File Setup
- main.py
    - Entry point
- src/
    - Holds Nodes, Civilization handlers, helpers, and the Server
- data/
    - civilizations/
        - Has files for specific civlizations (name)
    - Holds node_config.json + civilization_config.json

## Start on building a basic Node
1. Each Node will have attributes
    - See attributes [here](./project_setup.md)

2. Each Node will have methods to change attributes
    - Methods to increase age, change job, etc.

3. Be able to create a new node just by using `Node()`

## Start building a basic Civilization Handler
When creating a new civilization, just use `Civilization()` to create one

1. Handling Nodes
    - Creating, Removing, Updating *(All?)*
    - Server Storage

2. Systems
    - Tick system (time), Job system, election system, etc.

    - ****Need to come up with a time system***

3. *Offline + Online mode*
    - Starting / Stopping the civilization

## Start building data saving / loading + file creation
Be able to easily create new files, read .json files, etc.

## Create a Server
Just handles all the Civilizations created

## UI
Create TUI with rich *(or textual???)*
- Console like layout
- Commands to view active / inactive civilizations