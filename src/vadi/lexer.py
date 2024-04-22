from utils import constants

from .tokens import Declaration, Float, Integer, Operator, Token, Variable
from .typedef import NumberType, TokenListType, WordType


class Lexer:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.idx: int = 0
        self.tokens: TokenListType = []
        self.token: Token
        self.char: str = self.text[self.idx]

    def look_ahead(self) -> None:
        self.idx += 1

        if self.idx < len(self.text):
            self.char = self.text[self.idx]

    def extract_number(self) -> NumberType:
        numbers: str = ""
        isFloat: bool = False

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

    def extract_word(self) -> WordType:
        word: str = ""
        while self.char.lower() in constants.ALPHABETS and self.idx < len(self.text):
            word += self.char
            self.look_ahead()

        return word

    def tokenize(self) -> TokenListType:
        while self.idx < len(self.text):
            if self.char in constants.DIGITS:
                self.token = self.extract_number()

            elif self.char in constants.OPERATORS:
                self.token = Operator(self.char)
                self.look_ahead()

            elif self.char.lower() in constants.ALPHABETS:
                word: str = self.extract_word()

                if word in constants.DECLARATIONS:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)

            elif self.char in constants.STOPWORDS:
                self.look_ahead()
                continue

            self.tokens.append(self.token)

        return self.tokens
