from typing import List

from memory import Memory
from tokens import Float, Integer, Token
from utils.console import console


class Interpreter:
    def __init__(self, tree: List[Token] | Token | None, memory: Memory) -> None:
        if tree is None:
            self.syntax_error = True
        else:
            self.syntax_error = False

        self.tree: List[Token] | Token = tree
        self.memory: Memory = memory

    @staticmethod
    def INT(value: str) -> int:
        return int(value)

    @staticmethod
    def FLT(value: str) -> float:
        return float(value)

    def VAR(self, id: str) -> Token:
        variable: Token = self.memory.read(id)
        variable_type: str = variable.type

        return getattr(self, f"{variable_type}")(variable.value)

    def compute_unary(self, operator: Token, operand: Token) -> Token:
        operand_type: str = "VAR" if operand.type.startswith("VAR") else operand.type

        operand = getattr(self, f"{operand_type}")(operand.value)

        match operator.value:
            case "+":
                return +operand
            case "-":
                return -operand

    def compute_binary(self, left_operand: Token, operator: Token, right_operand: Token) -> Integer | Float:
        left_type: str = "VAR" if left_operand.type.startswith("VAR") else left_operand.type
        right_type: str = "VAR" if left_operand.type.startswith("VAR") else right_operand.type

        if operator.value == "=":
            left_operand.type = f"VAR{right_type}"
            self.memory.write(left_operand, right_operand)
            return right_operand.value

        left_operand = getattr(self, f"{left_type}")(left_operand.value)
        right_operand = getattr(self, f"{right_type}")(right_operand.value)

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

    def interpret(self, tree: List[Token] | Token | None = None) -> Token | None:
        if self.syntax_error:
            console.print("[b][ERROR]:[/b] Syntax error", style="error")
            return None

        if tree is None:
            tree = self.tree

        # Arithmetic literal
        if not isinstance(tree, list):
            return tree

        # Unary opeartion
        elif isinstance(tree, list) and len(tree) == 2:
            # compute_unary(operator, operand)
            return self.compute_unary(tree[0], tree[1])

        # Binary operations
        else:
            left_operand: List[Token] | Token = tree[0]
            if isinstance(left_operand, list):
                left_operand = self.interpret(left_operand)

            right_operand: List[Token] | Token = tree[2]
            if isinstance(right_operand, list):
                right_operand = self.interpret(right_operand)

            operator: Token = tree[1]

            return self.compute_binary(left_operand, operator, right_operand)
