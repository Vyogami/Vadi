from vadi.typedef import UnaryType


def datatype_casting(value: UnaryType, type: str) -> UnaryType:
    match type:
        case "INT":
            value = int(value)
        case "FLT":
            value = float(value)

    return value
