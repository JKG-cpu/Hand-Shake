# Project Setup

## File Structure

```
src/
    __init__.py
    nodes/
        __init__.py # Only allows node.py
        node.py
        logic.py

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

## Commands

### Basic
- `handshake compile`
- `handshake settings` 

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
