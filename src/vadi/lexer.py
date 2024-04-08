from typing import List

from tokens import Float, Integer, Operator, Token
from utils import constants


class Lexer:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.idx: int = 0
        self.tokens: List[Token] = []
        self.token: Token | None = None
        self.char: str = self.text[self.idx]

    def tokenize(self) -> List[Token]:
        while self.idx < len(self.text):
            if self.char in constants.DIGITS:
                self.token = self.extract_number()

            elif self.char in constants.OPERATORS:
                self.token = Operator(self.char)
                self.look_ahead()

            elif self.char in constants.STOPWORDS:
                self.look_ahead()
                continue

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self) -> Integer | Float:
        numbers: str = ""
        isFloat = False

        while (self.char in constants.DIGITS or self.char == ".") and (self.idx < len(self.text)):
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
