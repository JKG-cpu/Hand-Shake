from os import system, name

__all__ = [
    "cc"
]

def cc():
    system("cls" if name == "nt" else "clear")