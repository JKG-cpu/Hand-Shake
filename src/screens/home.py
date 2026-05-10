from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, Static
from textual.containers import Horizontal, Vertical

from ..widgets import TerminalWidget
from ..logic import Terminal

__all__ = [
    "HomePage"
]

class HomePage(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.terminal = Terminal()

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
                self.terminal_widget = TerminalWidget(classes = "section")
                self.terminal_widget.styles.height = "1fr"
                yield self.terminal_widget

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
    
    def update_terminal(self, command_ran: str, error_code: int) -> None:
        if not command_ran:
            return
        
        name, *extra = command_ran
        sub, *_ = extra if extra else (None, [])
        
        match error_code:
            # Command Executed
            case 0:
                pass

            # Invalid Command
            case 1:
                output = self.terminal.invalid_command(name, sub)
                self.terminal_widget.add_log(output)

            # Invalid Args
            case 2:
                output = self.terminal.invalid_args(name, sub)
                self.terminal_widget.add_log(output)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cmd-main":
            command_text = self.query_one("#cmd-input", Input).value
            self.query_one("#cmd-input", Input).clear()
            
            command_ran, error_code = self.app.run_command(command_text)
            self.update_terminal(command_ran, error_code)
