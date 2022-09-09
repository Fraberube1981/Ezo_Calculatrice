from typing import List, Union

from calculator.operators.operator import Operator


class Operation:

    def __init__(self):
        self.operation_members: List[Union[Operator, float, str, list]] = []

    @property
    def is_empty(self):
        return len(self.operation_members) == 0

    @property
    def is_ready_to_be_solved(self):
        return self.is_2_members_operation or self.is_3_members_operation

    @property
    def is_operation_contain_error(self):
        return any(isinstance(element, str) for element in self.operation_members)

    @property
    def is_2_members_operation(self):
        return len(self.operation_members) == 2 \
               and isinstance(self.operation_members[0], Operator) \
               and isinstance(self.operation_members[1], float)

    @property
    def is_3_members_operation(self):
        return len(self.operation_members) == 3 \
                and isinstance(self.operation_members[0], float) \
                and isinstance(self.operation_members[1], Operator) \
                and isinstance(self.operation_members[2], float)

    def add_operation_members(self, member: Union[Operator, float, str, list]):

        if len(self.operation_members) == 3:
            raise ValueError("An operation cannot contain more than 3 members.")

        self.operation_members.append(member)

    def solve_operation(self) -> float:
        if self.is_2_members_operation:
            return self.operation_members[0].do_operation(self.operation_members[1])
        if self.is_3_members_operation:
            return self.operation_members[1].do_operation(self.operation_members[0], self.operation_members[2])

        raise ValueError("Operation cannot be solved.")

    def get_operation_error(self) -> str:

        if not self.is_operation_contain_error:
            raise ValueError("Operation does contain any error.")

        return [element for element in self.operation_members if isinstance(element, str)][0]

    def reset_operation(self):
        self.operation_members = []
