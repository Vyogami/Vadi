from typing import List

from tokens import Float, Integer, Token


class Interpreter:
    def __init__(self, tree: List[Token] | Token) -> None:
        self.tree: List[Token] | Token = tree

    @staticmethod
    def INT(value: str) -> int:
        return int(value)

    @staticmethod
    def FLT(value: str) -> float:
        return float(value)

    def compute_binary(self, left_operand: Token, operator: Token, right_operand: Token) -> Integer | Float:
        left_type: str = left_operand.token_type
        right_type: str = right_operand.token_type

        left_operand = getattr(Interpreter, f"{left_type}")(left_operand.value)
        right_operand = getattr(Interpreter, f"{right_type}")(right_operand.value)

        match operator.value:
            case "+":
                result = left_operand + right_operand
            case "-":
                result = left_operand - right_operand
            case "*":
                result = left_operand * right_operand
            case "/":
                result = left_operand / right_operand

        if "FLT" in (left_type, right_type):
            return Float(result)
        else:
            return Integer(result)

    def interpret(self, tree: List[Token] | Token | None = None) -> Token:
        if tree is None:
            tree = self.tree

        left_operand: str | List[Token] = tree[0]
        if isinstance(left_operand, list):
            left_operand = self.interpret(left_operand)

        right_operand: str | List[Token] = tree[2]
        if isinstance(right_operand, list):
            right_operand = self.interpret(right_operand)

        operator: Token = tree[1]

        return self.compute_binary(left_operand, operator, right_operand)
