from typing import List

from calculator.operators.addition import Addition
from calculator.operators.division import Division
from calculator.operators.exponent import Exponent
from calculator.operators.multiplication import Multiplication
from calculator.operators.operator import Operator
from calculator.operators.square_root import SquareRoot
from calculator.operators.substraction import Substraction


def get_all_operators() -> List[Operator]:
    return [
        Exponent(),
        SquareRoot(),
        Division(),
        Multiplication(),
        Division(),
        Addition(),
        Substraction()
    ]


def get_all_operator_ids() -> List[str]:
    return [operator.get_char_id() for operator in get_all_operators()]


def get_operator_from_id(id: str) -> Operator:
    for operator in get_all_operators():
        if operator.get_char_id() == id:
            return operator

    raise ValueError("Unsupported id.")


def is_substraction(id: str) -> bool:
    return id == Substraction().get_char_id()


def is_operator(id: str) -> bool:
    return id in get_all_operator_ids()


def convert_symbols_to_char_ids(formula: str) -> str:
    for operator in get_all_operators():
        formula = formula.replace(operator.get_symbol(), operator.get_char_id())

    return formula
