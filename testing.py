from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    DataTable,
    RichLog,
    Input,
    Header,
    Footer
)

class HandShake(App):

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():

            with Horizontal():

                # Left panel
                nodes = DataTable()
                nodes.add_columns("Node", "Status")
                nodes.add_row("Node-1", "ACTIVE")
                nodes.add_row("Node-2", "CORRUPTED")

                yield nodes

                # Right panel
                logs = RichLog()
                logs.write("[green]Node-1 joined civilization[/green]")
                logs.write("[red]Corruption spreading...[/red]")

                yield logs

            # Bottom command input
            yield Input(
                placeholder="Enter command..."
            )

        yield Footer()

app = HandShake()
app.run()