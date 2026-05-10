from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, Button
from textual.containers import Horizontal, Vertical
from os.path import join
from shlex import split

from src import *

class HandShake(App):
    BINDINGS = [("q", "quit", "Quit HandShake Application")]
    CSS_PATH = [join("styles", "base.tcss")]
    SCREENS = {
        "Home": HomePage
    }
    theme = "tokyo-night"

    def __init__(self) -> None:
        super().__init__()
        self.commands: dict[str, function | dict] = {
            "exit": lambda: self.call_later(self.action_quit),
            "handshake": {
                "exit": lambda: self.call_later(self.action_quit)
            }
        }

    def on_mount(self) -> None:
        self.push_screen("Home")

    def run_command(self, input_str: str) -> tuple[list[str], int]:
        command = split(input_str)

        if not command:
            return (command, 3)

        name, *extra = command
        
        # Unknown Command
        if name not in self.commands:
            return (command, 2)
    
        entry = self.commands[name]

        if callable(entry):
            entry(*extra)
            return (command, 0)
    
        # Needs Sub Command
        if not extra:
            return (command, 1)

        sub, *args = extra

        # Unknown Command
        if sub not in entry:
            return (command, 2)

        entry[sub](*args)
        return (command, 0)

    async def action_quit(self):
        self._clear_on_exit = True
        await super().action_quit()

if __name__ == "__main__":
    app = HandShake()
    app.run()
    if getattr(app, "_clear_on_exit", False):
        cc()
