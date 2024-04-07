from lexer import Lexer
from rich.traceback import install
from utils.console import console

install()

while True:
    console.print("[REPL] Vadi: ", style="info", end="")
    text = input()
    tokenizer: Lexer = Lexer(text)
    tokens = tokenizer.tokenize()
    if tokens is not None:
        console.print(tokens)
