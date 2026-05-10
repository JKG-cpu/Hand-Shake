from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, Static
from textual.containers import Horizontal, Vertical

__all__ = [
    "HomePage"
]

class HomePage(Screen):
    def compose(self) -> ComposeResult:
        yield Header("HandShake")
        
        with Horizontal():
            with Vertical():
                static = Static("Running Civilization Stats", classes = "section")
                static.styles.height = "1fr"
                yield static
                
                static = Static("Info on X Selected Civilization", classes = "section")
                static.styles.height = "1fr"
                yield static

            with Vertical():
                static = Static("Terminal Logs", classes = "section")
                static.styles.height = "1fr"
                yield static

                horizontal = Horizontal(classes = "section")
                horizontal.styles.height = "auto"
                with horizontal:
                    input = Input(placeholder = "Enter in a command", id="cmd-input")
                    input.styles.width = "50%"
                    yield input

                    button = Button("Run Command", id = "cmd-main")
                    button.styles.width = "50%"
                    yield button

        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cmd-main":
            command_text = self.query_one("#cmd-input", Input).value
            self.query_one("#cmd-input", Input).clear()
            self.app.run_command(command_text)