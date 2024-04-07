from typing import List

from tokens import Token


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens: List[Token] = tokens  # type: ignore  # noqa: PGH003 # To disable pylint and ruff warnings
        self.idx: int = 0

        self.token: Token = self.tokens[self.idx]

    def factor(self) -> Token:
        if self.token.token_type in ("INT", "FLT"):
            factor_token: Token = self.token
            self.move_ahead()

            return factor_token

        elif self.token.value == "(":
            # To skip '('
            self.move_ahead()
            # To evaluate the expression in between parenthesis '(<expr>)'
            expression: List[Token] = self.expression()
            # To skip ')'
            self.move_ahead()

            return expression

    def term(self) -> List[Token]:
        left_node: Token | List[Token] = self.factor()

        while self.token.value in ("*", "/"):
            operator: Token = self.token
            self.move_ahead()

            right_node: Token = self.factor()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self) -> List[Token]:
        left_node: Token | List[Token] = self.term()

        while self.token.value in ("+", "-"):
            operator: Token = self.token
            self.move_ahead()

            right_node: Token = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def parse(self) -> Token | List[Token]:
        return self.expression()

    def move_ahead(self) -> None:
        self.idx += 1

        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
