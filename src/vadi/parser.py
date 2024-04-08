from typing import List

from tokens import Token


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        # type: ignore # To disable pylance warnings
        self.tokens: List[Token] = tokens
        self.idx: int = 0

        self.token: Token = self.tokens[self.idx]

    def look_ahead(self) -> None:
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

    def variable(self) -> Token:
        if self.token.type.startswith("VAR"):
            temp: Token = self.token
            self.look_ahead()
            return temp

        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

    def factor(self) -> Token | List[Token] | None:
        """A factor can be an int, float, expression inside parenthesis or a variable.

        Grammar:
            <factor> = INT | FLT | (<expr>) | VAR

        Returns:
            Token | List[Token]
        """

        if self.token.type in ("INT", "FLT"):
            return self.token

        elif self.token.value == "(":
            # To skip '('
            self.look_ahead()
            # To evaluate the expression in between parenthesis '(<expr>)'
            expression: List[Token] = self.expression()

            return expression

        elif self.token.type.startswith("VAR"):
            return self.token

        elif self.token.value in ("+", "-"):
            operator: Token = self.token
            self.look_ahead()
            operand: Token = self.factor()

            return [operator, operand]

        return None

    def term(self) -> List[Token]:
        left_node: Token | List[Token] = self.factor()
        self.look_ahead()

        while self.token.value in ("*", "/"):
            operator: Token = self.token
            self.look_ahead()

            right_node: Token = self.factor()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self) -> List[Token]:
        left_node: Token | List[Token] = self.term()

        while self.token.value in ("+", "-"):
            operator: Token = self.token
            self.look_ahead()

            right_node: Token = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def statement(self) -> List[Token] | None:
        # Variable assignment
        if self.token.type == "DECL":
            self.look_ahead()
            left_node: Token = self.variable()
            if self.token.value == "=":
                operator: Token = self.token
                self.look_ahead()
                right_node: Token = self.expression()

                return [left_node, operator, right_node]

        # Arithmetic expression
        elif self.token.type in ("INT", "FLT", "OP"):
            return self.expression()

        return None

    def parse(self) -> Token | List[Token]:
        return self.statement()
