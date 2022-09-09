from typing import Union

from calculator.operators.operator import Operator


class Multiplication(Operator):

    def get_symbol(self):
        return "*"

    def get_char_id(self):
        return "*"

    def get_priority(self):
        return 2

    def do_operation(self, first, second) -> Union[float, str]:
        return first * second
