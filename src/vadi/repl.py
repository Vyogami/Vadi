from parser import Parser  # type: ignore  # noqa: PGH003 # To disable pylint and ruff warnings

from lexer import Lexer
from rich.traceback import install
from utils.console import console

install()

while True:
    console.print("[REPL] Vadi: ", style="info", end="")
    text = input()
    tokenizer: Lexer = Lexer(text)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()

    if tokens is not None:
        console.print(tree)
