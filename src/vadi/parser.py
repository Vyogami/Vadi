from .tokens import Token
from .typedef import ParseTreeType, TokenListType, VariableType


class Parser:
    def __init__(self, tokens: TokenListType) -> None:
        # type: ignore # To disable pylance warnings
        self.tokens: TokenListType = tokens
        self.idx: int = 0

        self.token: Token = self.tokens[self.idx]

    def look_ahead(self) -> None:
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

    def variable(self) -> VariableType:
        if self.token.type.startswith("VAR"):
            temp = self.token
            self.look_ahead()
            return temp

        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

        return None

    def factor(self) -> ParseTreeType:
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
            expression: ParseTreeType = self.expression()

            return expression

        elif self.token.type.startswith("VAR"):
            return self.token

        elif self.token.value in ("+", "-"):
            operator = self.token
            self.look_ahead()
            operand = self.factor()

            return [operator, operand]

        return None

    def term(self) -> ParseTreeType:
        left_node: ParseTreeType = self.factor()
        self.look_ahead()

        while self.token.value in ("*", "/"):
            operator = self.token
            self.look_ahead()

            right_node: ParseTreeType = self.factor()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self) -> ParseTreeType:
        left_node: ParseTreeType = self.term()

        while self.token.value in ("+", "-"):
            operator: Token = self.token
            self.look_ahead()

            right_node: ParseTreeType = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def statement(self) -> ParseTreeType:
        # Variable assignment
        if self.token.type == "DECL":
            self.look_ahead()
            left_node: VariableType = self.variable()
            if self.token.value == "=":
                operator: Token = self.token
                self.look_ahead()
                right_node: ParseTreeType = self.expression()

                return [left_node, operator, right_node]

        # Arithmetic expression
        elif self.token.type in ("INT", "FLT", "OP"):
            return self.expression()

        return None

    def parse(self) -> ParseTreeType:
        return self.statement()
