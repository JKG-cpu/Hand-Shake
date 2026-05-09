# Project Setup

## File Structure

```
src/
    __init__.py
    nodes/
        __init__.py

    logic/
        __init__.py
        start.py
        connections.py

    helpers/
        __init__.py
        imports.py
        config.py
        helpers.py

main.py
```

## Flow

Entry Point: main.py

- A nice TUI with *rich*
    - A "mini" terminal
- Run commands
    - *handshake compile* => creates and starts an empty civilization
    - *handshake settings* => opens another TUI with *rich*
    - *handshake close* => closes all current civilizations and exits
    - *handshake view -civilization [CIVILIZATION]* => view a specific civilization
    - *handshake view* => view all running civilizatoins (brief) with their status

Civilization
- Details
    - Start a civilization with a TUI with *textual*
    - Stats on the left, terminal on the right

Nodes
- Properties
    - `Name: str`
    - `Age: int`
    - `Job: str | dict`
    - `Moral: str | int`
    - `State: str`
    - `Corruption_level: int (1-5)`
    - `Influence: int (1-5)`
    - `Likes: list[str]`
    - `Dislikes: list[str]`
    - `Trusts: dict[str, int]`
    - `Uptime: int`
    - `Reputation: int (1-5)`
    - `Stress: int (1-5)`

## Commands

### Basic
- `handshake compile`
- `handshake settings`
- `handshake close`
- `handshake view -civilization [CIVILIZATION]`
- `handshake view`

### Nodes
- `create node -p [PORT_NUMBER]`
- `create nodes -p [PORT_NUMBER],[PORT_NUMBER]`
- `remove node -id [NODE_ID] -name [NODE_NAME]`
- `remove nodes -id [NODE_ID],[NODE_ID] -name [NODE_NAME],[NODE_NAME]`
- `run election -start-node [NODE_ID]`

### Jobs
- `assign -node [NODE_ID] -job [JOB]`
- `fire -node [NODE_ID] -job [JOB]`
- `create job`
- `view jobs`

### Chaos Commands
- `corrupt -econonmy`
- `corrupt -jobs`
- `corrupt -gov`

## Modules

### TUI
- rich
- textual

### Data handling
- json

### Threading
- Threading
- Asyncio