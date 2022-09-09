from typing import Union

from calculator.operators.operator import Operator


class SquareRoot(Operator):

    def get_symbol(self):
        return "sqrt"

    def get_char_id(self):
        return "s"

    def get_priority(self):
        return 1

    def do_operation(self, first) -> Union[float, str]:
        return first ** 0.5
