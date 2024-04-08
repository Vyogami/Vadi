from parser import Parser  # type: ignore # To disable pylance warnings
from typing import List

from interpreter import Interpreter
from lexer import Lexer
from memory import Memory
from rich.traceback import install
from tokens import Token
from utils.console import console

install()
memory = Memory()

while True:
    console.print("[REPL] Vadi: ", style="info", end="")
    text = input()

    # if the incoming sting text is empyt then skip the iteration, empty string means <enter> | ""
    if text == "":
        continue

    try:
        tokenizer: Lexer = Lexer(text)
        tokens: List[Token] = tokenizer.tokenize()

        parser = Parser(tokens)
        tree = parser.parse()

        interpreter = Interpreter(tree, memory)
        result: Token = interpreter.interpret()

        if result is not None:
            console.print(result)
    except KeyError:
        console.print("[b][ERROR][/b]: Syntax error", style="error")
