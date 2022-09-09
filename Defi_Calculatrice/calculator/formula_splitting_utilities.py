from typing import Union, List, Tuple

from calculator.operators.operator import Operator
from calculator.operators.multiplication import Multiplication
from calculator.operators.operator_utilities import get_operator_from_id, get_all_operator_ids, \
    convert_symbols_to_char_ids, is_substraction, is_operator


def split_formula(formula: str) -> list:

    prepared_formula = _prepare_formula(formula)
    _validate_formula(prepared_formula)

    return _split_formula_recursively(prepared_formula)


def _prepare_formula(raw_formula: str) -> str:

    no_space_formula = _remove_empty_spaces(raw_formula)
    prepared_formula = convert_symbols_to_char_ids(no_space_formula)

    return prepared_formula


def _remove_empty_spaces(formula: str) -> str:
    return formula.replace(" ", "")


def _validate_formula(formula: str):

    for position in range(len(formula)):

        if is_operator(formula[position]) \
                and is_operator(formula[position+1]) \
                and not is_substraction(formula[position+1]):
            raise ValueError("When 2 operators are next to each other, the second must be -.")


def _split_formula_recursively(formula: str) -> List[Union[float, Operator]]:

    if _is_formula_contains_brackets(formula):
        return _parse_formula_and_reorganize_with_operator_priority(formula)

    first_opening_bracket_position, last_closing_bracket_position = \
        _find_first_opening_and_last_closing_bracket_positions(formula)

    between_bracket_formula = formula[first_opening_bracket_position + 1:last_closing_bracket_position]
    between_bracket_splitted_formula = _split_formula_recursively(between_bracket_formula)
    between_bracket_prefix_last_position = first_opening_bracket_position - 1

    if _is_opening_bracket_preceded_with_minus(formula, first_opening_bracket_position):
        between_bracket_prefix_last_position -= 1
        between_bracket_splitted_formula = [-1.0, Multiplication(), between_bracket_splitted_formula]

    splitted_formula = _split_bracket_prefix(formula, between_bracket_prefix_last_position)
    _append_between_bracket_to_prefix_splitted_formula(between_bracket_splitted_formula, splitted_formula)
    
    _split_and_append_bracket_suffix(formula, last_closing_bracket_position, splitted_formula)

    return splitted_formula


def _is_formula_contains_brackets(formula: str) -> bool:
    return "(" not in formula and ")" not in formula


def _find_first_opening_and_last_closing_bracket_positions(formula: str) -> Tuple[int, int]:

    open_bracket_positions: List[int] = [position for position, char in enumerate(formula) if char == "("]
    first_opening_bracket_position = open_bracket_positions[0]

    close_bracket_positions: List[int] = [position for position, char in enumerate(formula) if char == ")"]
    last_closing_bracket_position = close_bracket_positions[-1]

    if len(open_bracket_positions) != len(close_bracket_positions):
        raise ValueError("The brackets () are not correctly balanced.")

    return first_opening_bracket_position, last_closing_bracket_position


def _is_opening_bracket_preceded_with_minus(formula: str, opening_bracket_position: int) -> bool:
    return (opening_bracket_position == 1 and is_substraction(formula[opening_bracket_position - 1])) \
           or (opening_bracket_position > 1 and is_operator(formula[opening_bracket_position - 2]))


def _split_bracket_prefix(formula: str, prefix_last_position: int):
    brackets_prefix_formula = formula[:prefix_last_position + 1]
    return _parse_formula_and_reorganize_with_operator_priority(brackets_prefix_formula)


def _append_between_bracket_to_prefix_splitted_formula(between_bracket_splitted_formula: list,
                                                       prefix_splitted_formula: list):

    if len(prefix_splitted_formula) > 0 and isinstance(prefix_splitted_formula[-1], list):
        prefix_splitted_formula[-1].append(between_bracket_splitted_formula)
    else:
        prefix_splitted_formula.append(between_bracket_splitted_formula)


def _split_and_append_bracket_suffix(formula: str, last_closing_bracket_position: int, splitted_formula: list):

    if last_closing_bracket_position < len(formula) - 1:
        brackets_suffix_formula = formula[last_closing_bracket_position + 1:]
        splitted_formula.extend(_parse_formula_and_reorganize_with_operator_priority(brackets_suffix_formula))


def _parse_formula_and_reorganize_with_operator_priority(formula: str) -> List[Union[float, Operator]]:

    operator_positions = _find_operator_positions(formula)

    splitted_formula = _cast_numbers_and_operators(formula, operator_positions)

    return reorganize_with_operator_priority(splitted_formula)


def _find_operator_positions(formula: str) -> List[int]:

    operator_and_minus_positions: List[int] = \
        [position for position, char in enumerate(formula) if char in get_all_operator_ids()]
    operator_positions = _remove_minus_sign(formula, operator_and_minus_positions)

    return operator_positions


def _remove_minus_sign(formula: str, operator_and_minus_positions: List[int]) -> List[int]:

    operator_positions = []

    for operator_position in operator_and_minus_positions:

        if is_substraction(formula[operator_position]):
            if operator_position == 0 and operator_position + 1 not in operator_and_minus_positions:
                continue

            if operator_position - 1 in operator_and_minus_positions:
                continue

        operator_positions.append(operator_position)
        
    return operator_positions


def _cast_numbers_and_operators(formula: str, operator_positions: List[int]) -> List[Union[float, Operator, list]]:

    current_position = 0
    splitted_formula = []

    for real_operator_position in operator_positions:

        if real_operator_position > current_position:
            splitted_formula.append(float(formula[current_position:real_operator_position]))

        splitted_formula.append(get_operator_from_id(formula[real_operator_position]))

        current_position = real_operator_position + 1

    if current_position < len(formula):
        splitted_formula.append(float(formula[current_position:]))

    return splitted_formula


def reorganize_with_operator_priority(splitted_formula: List[Union[float, Operator, list]]) \
        -> List[Union[float, Operator, list]]:

    if _is_formula_contain_single_operation(splitted_formula):
        return splitted_formula

    formula_operators = [(element, element.get_priority(), position)
                         for position, element in enumerate(splitted_formula) if isinstance(element, Operator)]
    formula_operators_ordered_with_priority = sorted(formula_operators, key=lambda x: (x[1], x[2]))

    previous_operator = formula_operators_ordered_with_priority[0]
    previous_operator_operation = splitted_formula[previous_operator[2]-1:previous_operator[2]+2]
    reordered_formula = [previous_operator_operation]

    for operator_position in range(1, len(formula_operators_ordered_with_priority)):

        current_operator = formula_operators_ordered_with_priority[operator_position]

        if _is_current_operator_located_before_previous(current_operator, previous_operator):
            reordered_formula.insert(0, splitted_formula[current_operator[2]])
            reordered_formula.insert(0, splitted_formula[current_operator[2]-1])
        else:
            reordered_formula.extend(splitted_formula[current_operator[2]:current_operator[2] + 2])

    return reordered_formula


def _is_formula_contain_single_operation(splitted_formula: List[Union[float, Operator, list]]) -> bool:
    return len(splitted_formula) <= 3


def _is_current_operator_located_before_previous(current_operator, previous_operator):
    return current_operator[2] < previous_operator[2]
