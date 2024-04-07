class Token:
    def __init__(self, token_type: str, value: str) -> None:
        self.token_type: str = token_type
        self.value: str = value

    def __repr__(self) -> str:
        return f"{self.value}"


class Integer(Token):
    def __init__(self, value: str) -> None:
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value: str) -> None:
        super().__init__("FLT", value)


class Operation(Token):
    def __init__(self, value: str) -> None:
        super().__init__("OP", value)
