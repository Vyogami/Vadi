import readline  # noqa: F401

from rich.console import Console, Theme

console_theme = Theme({"info": "blue", "warning": "yellow", "error": "bold red"})

console = Console(theme=console_theme)


def prompt():
    """
    Note: this is dirty fix for issue: https://github.com/Textualize/rich/issues/2293 in rich.console.input -> readline
    """

    console.print("[REPL] Vadi:", style="info", end="")
    return input("\u00A0")
