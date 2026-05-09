# HandShake

Hand Shake is a terminal-first autonomous distributed infrastructure simulator written primarily in python.

## Project Details

### How it works
To start the project, run:
```bash
uv run main.py
```

Or if you don't have uv installed:
```bash
# Create & activate venv

# Mac/Linux
python -m venv .venv
source .venv/bin/activate

# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate.bat

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies & run
pip install -r requirements.txt
python main.py
```

You will be able to launch it via a command
```bash
handshake compile
```
This will launch the community and create a TUI for you to monitor everything!

You will be able to create different nodes ("people") that will auto add to your civilization
```bash
create node -port 5000
```

### File Structure
```bash

```

## Links

- [Source Code](https://github.com/JKG-cpu/Hand-Shake)
- [My Github](https://github.com/JKG-cpu)

## License

This is under a MIT License
