__all__ = [
    "Terminal"
]

class Terminal:
    def __init__(self):
        self.command_help: dict[str, dict] = {
            "exit": {
                "info": "Exit the application",
                "usage": "exit"
            },
            "handshake": {
                "info": "Handle main operations",
                "usage": "handshake <subcommand> [args...]",
                "sub-commands": {
                    
                }
            }
        }
    
    def invalid_args(self, command: str, sub_command: str | None = None) -> str:
        cmd = f"{command} {sub_command}" if sub_command else command
        key = self.command_help.get(command, {})
        if sub_command:
            key = key.get("sub-commands", {}).get(sub_command, {})
        usage = key.get("usage")
        return f"[red]Invalid arguments for [italic red]'{cmd}'.\n[$panel italic]  Usage: {usage}[/]"

    def invalid_command(self, command: str, sub_command: str | None = None) -> str:
        cmd = f"{command} {sub_command}" if sub_command else command
        return f"[red]Unknown command [red italic]'{cmd}'.\n[$panel italic]  Type 'help' for more options[/]"
