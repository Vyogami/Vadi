from typing import List, TypeAlias, Union

from .tokens import Float, Integer, Token

TokenListType: TypeAlias = List[Token]
NumberType: TypeAlias = Union[Integer, Float]
WordType: TypeAlias = str

VariableType: TypeAlias = Token | None
ParseTreeType: TypeAlias = Union[Token, List[Token], List["ParseTreeType"], None]

UnaryType: TypeAlias = Union[int, float]
BinaryType: TypeAlias = Union[Integer, Float, str]

PrintDataType: TypeAlias = Union[UnaryType, BinaryType, ParseTreeType]
