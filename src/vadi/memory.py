from typing import Dict

from .tokens import Token


class Memory:
    def __init__(self) -> None:
        self.variables: Dict[str, Token] = {}

    def read(self, id: str) -> Token:
        return self.variables[id]

    def read_all(self) -> Dict[str, Token]:
        return self.variables

    def write(self, variable: Token, expression: Token) -> None:
        variable_name: str = variable.value
        self.variables[variable_name] = expression
