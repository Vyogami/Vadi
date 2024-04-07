from rich.console import Console, Theme

console_theme = Theme({"info": "blue", "warning": "yellow", "error": "bold red"})

console = Console(theme=console_theme)
