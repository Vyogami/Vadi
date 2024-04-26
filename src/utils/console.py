from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.javascript import JavascriptLexer
from rich.console import Console, Theme

rich_console_theme = Theme({"info": "blue", "warning": "yellow", "error": "bold red"})

console = Console(theme=rich_console_theme)


prompt_toolkit_style = Style.from_dict(
    {
        "info": "skyblue bold",
    }
)

session = PromptSession(lexer=PygmentsLexer(JavascriptLexer), style=prompt_toolkit_style)


def prompt():
    """
    Note: this is dirty fix for issue: https://github.com/Textualize/rich/issues/2293 in rich.console.input -> readline
    """

    message = [("class:info", "[REPL] Vadi: ")]

    return session.prompt(message, style=prompt_toolkit_style)
