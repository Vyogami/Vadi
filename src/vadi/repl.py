import sys

from rich.traceback import install
from utils.console import console, prompt

from .interpreter import Interpreter
from .lexer import Lexer
from .memory import Memory
from .parser import Parser  # type: ignore # To disable pylance warnings

install()


def main() -> None:
    memory = Memory()

    while True:
        try:
            text = prompt()
            # if the incoming sting text is empyt then skip the iteration, empty string means <enter> | ""
            if text == "":
                continue

            tokenizer = Lexer(text)
            tokens = tokenizer.tokenize()

            parser = Parser(tokens)
            tree = parser.parse()

            interpreter = Interpreter(tree, memory)
            result = interpreter.interpret()

            if result is not None:
                console.print(result)
        except KeyError:
            console.print("[b][ERROR][/b]: Syntax error", style="error")

        except (KeyboardInterrupt, EOFError):
            sys.exit()


if __name__ == "__main__":
    main()
