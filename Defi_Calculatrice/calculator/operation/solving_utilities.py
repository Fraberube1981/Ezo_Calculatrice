from typing import Union, List

from calculator.operation.operation import Operation
from calculator.operators.operator import Operator


def solve_formula(splitted_formula: List[Union[float, Operator, list]]) -> float:

    if len(splitted_formula) == 1:
        return _solve_formula_recursively(splitted_formula[0])

    return _solve_formula_recursively(splitted_formula)


def _solve_formula_recursively(splitted_formula: List[Union[float, Operator, list]]) \
        -> Union[float, str]:

    current_operation = Operation()
    current_operation_output = None

    for element_iterator, element in enumerate(splitted_formula):

        if isinstance(element, list):
            element = _solve_formula_recursively(element)

        current_operation.add_operation_members(element)

        if current_operation.is_operation_contain_error:
            return current_operation.get_operation_error()

        if current_operation.is_ready_to_be_solved:

            current_operation_output = current_operation.solve_operation()
            current_operation.reset_operation()

            if element_iterator < len(splitted_formula) - 1:
                current_operation.add_operation_members(current_operation_output)

    if not current_operation.is_empty:
        raise ValueError("Something is wrong with the formula splitting.")

    return current_operation_output
