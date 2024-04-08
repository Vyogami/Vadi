from typing import List

from tokens import Float, Integer, Operator, Token


class Lexer:
    digits: str = "0123456789"
    operators: str = "+-*/()"
    stopwords = [" "]

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.idx: int = 0
        self.tokens: List[Token] = []
        self.token: Token | None = None
        self.char: str = self.text[self.idx]

    def tokenize(self) -> List[Token]:
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operators:
                self.token = Operator(self.char)
                self.look_ahead()

            elif self.char in Lexer.stopwords:
                self.look_ahead()
                continue

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
            self.look_ahead()

        if isFloat:
            return Float(numbers)
        else:
            return Integer(numbers)

    def look_ahead(self) -> None:
        self.idx += 1

        if self.idx < len(self.text):
            self.char = self.text[self.idx]
