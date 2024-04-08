from parser import Parser  # type: ignore  # noqa: PGH003 # To disable pylint and ruff warnings
from typing import List

from interpreter import Interpreter
from lexer import Lexer
from rich.traceback import install
from tokens import Token
from utils.console import console

install()

while True:
    console.print("[REPL] Vadi: ", style="info", end="")
    text = input()

    # if the incoming sting text is empyt then skip the iteration, empty string means <enter> | ""
    if text == "":
        continue

    tokenizer: Lexer = Lexer(text)
    tokens: List[Token] = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree)
    result: Token = interpreter.interpret()

    console.print(result)
