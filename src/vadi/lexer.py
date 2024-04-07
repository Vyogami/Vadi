from typing import List

from tokens import Float, Integer, Operation, Token
from utils.console import console


class Lexer:
    digits: str = "0123456789"
    operations: str = "+-*/()"
    stopwords = [" "]

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.idx: int = 0
        self.tokens: List[Token] = []
        self.token: Token | None = None

        # Sets current character value to text[0] only if the incoming text string is not empty
        if text != "":
            self.char: str = self.text[self.idx]

    def tokenize(self) -> List[Token] | None:
        # Checks if the incoming text string is empty
        if self.text == "":
            return None

        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move_ahead()

            elif self.char in Lexer.stopwords:
                self.move_ahead()
                continue
            else:
                console.print(f"[b][ERROR] [/b]Syntax error: [u grey66]{self.char}[/u grey66]", style="error")
                return None

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self) -> Integer | Float:
        numbers: str = ""
        isFloat = False

        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            # Check if the number is floating point by checking if it contains decimal point(.)
            if self.char == ".":
                isFloat = True

            numbers += self.char
            self.move_ahead()

        if isFloat:
            return Float(numbers)
        else:
            return Integer(numbers)

    def move_ahead(self) -> None:
        self.idx += 1

        if self.idx < len(self.text):
            self.char = self.text[self.idx]
