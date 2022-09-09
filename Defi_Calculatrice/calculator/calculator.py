from typing import Union

from calculator.formula_splitting_utilities import split_formula
from calculator.operation.solving_utilities import solve_formula


class Calculator:

    @staticmethod
    def calculate(formula: str) -> Union[float, int, str]:

        splitted_formula = split_formula(formula)

        output = solve_formula(splitted_formula)

        return output
