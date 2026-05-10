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
        self.commands = {
            "handshake": {
                "exit": lambda: self.call_later(self.action_quit)
            }
        }

    def on_mount(self) -> None:
        self.push_screen("Home")

    def run_command(self, input_str: str) -> None:
        command = split(input_str)

        if not command:
            return

        name, sub, *args = command

        try:
            self.commands[name][sub](*args)
        
        except TypeError:
            self.notify("Invalid Command!")

        except KeyError:
            self.notify("Invalid Command!")

    async def action_quit(self):
        self._clear_on_exit = True
        await super().action_quit()

if __name__ == "__main__":
    app = HandShake()
    app.run()
    if getattr(app, "_clear_on_exit", False):
        cc()
