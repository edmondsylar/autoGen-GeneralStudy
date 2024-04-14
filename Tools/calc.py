from typing import Annotated, Literal

operators = Literal['+', '-', '*', '/']

def calculator(a: int, b:int, operator: Annotated[operators, "operator"]) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(a / b)
    else:
        raise ValueError("Invalid operator")