from typing import cast

from utils.console import console
from utils.helpers import datatype_casting

from .memory import Memory
from .tokens import Float, Integer, Token
from .typedef import BinaryType, ParseTreeType, PrintDataType, UnaryType


class Interpreter:
    def __init__(self, tree: ParseTreeType, memory: Memory) -> None:
        if tree is None:
            self.syntax_error = True
        else:
            self.syntax_error = False

        self.tree: ParseTreeType = tree
        self.memory: Memory = memory

    @staticmethod
    def INT(value: str) -> int:
        return int(value)

    @staticmethod
    def FLT(value: str) -> float:
        return float(value)

    def VAR(self, id: str) -> UnaryType:
        variable: Token = self.memory.read(id)
        variable_type: str = variable.type

        value = getattr(self, f"{variable_type}")(variable.value)

        return datatype_casting(value, variable_type)

    def compute_unary(self, operator: Token, operand: Token) -> UnaryType:
        operand_type: str = "VAR" if operand.type.startswith("VAR") else operand.type

        operand_value = datatype_casting(getattr(self, f"{operand_type}")(operand.value), operand_type)

        match operator.value:
            case "+":
                operand_value = +operand_value
            case "-":
                operand_value = -operand_value

        return operand_value

    def compute_binary(self, left_operand: Token, operator: Token, right_operand: Token) -> BinaryType:
        left_type: str = "VAR" if left_operand.type.startswith("VAR") else left_operand.type
        right_type: str = "VAR" if left_operand.type.startswith("VAR") else right_operand.type

        if operator.value == "=":
            left_operand.type = f"VAR{right_type}"
            self.memory.write(left_operand, right_operand)
            return right_operand.value

        left_operand_value = getattr(self, f"{left_type}")(left_operand.value)
        right_operand_value = getattr(self, f"{right_type}")(right_operand.value)

        match operator.value:
            case "+":
                result = left_operand_value + right_operand_value
            case "-":
                result = left_operand_value - right_operand_value
            case "*":
                result = left_operand_value * right_operand_value
            case "/":
                result = left_operand_value / right_operand_value

        if "FLT" in (left_type, right_type):
            return Float(result)
        else:
            return Integer(result)

    def interpret(self, tree: ParseTreeType = None) -> PrintDataType:
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
            unary_operator = cast(Token, tree[0])
            unary_operand = cast(Token, tree[1])
            return self.compute_unary(unary_operator, unary_operand)

        # Binary operations
        else:
            left_operand = tree[0]
            if isinstance(left_operand, list):
                left_operand = cast(Token, self.interpret(left_operand))

            right_operand = tree[2]
            if isinstance(right_operand, list):
                right_operand = cast(Token, self.interpret(right_operand))

            left_operand = cast(Token, left_operand)
            right_operand = cast(Token, right_operand)
            operator = cast(Token, tree[1])

            return self.compute_binary(left_operand, operator, right_operand)
