from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import VerticalScroll

__all__ = [
    "TerminalWidget"
]

class TerminalWidget(Static):
    def __init__(self, id = None, classes = None):
        super().__init__(id = id, classes = classes)
        self.logs: list[tuple[str, str]] = []
        self.styles.padding = (1, 1, 1, 2)

    def _get_log_text(self) -> str:
        return "\n\n".join(self.logs)

    def add_log(self, text: str) -> None: 
        self.logs.append(text)
        self.refresh(recompose = True)

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            text = self._get_log_text()

            if text:
                yield Static(text)

            else:
                yield Static("[bold]No Logs to Display![/]")
