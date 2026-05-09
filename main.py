from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class HandShake(App):
    BINDINGS = [("q", "quit", "Quit HandShake")]

    def compose(self) -> ComposeResult:
        yield Header("HandShake")
        
        yield Footer()

if __name__ == "__main__":
    HandShake().run()