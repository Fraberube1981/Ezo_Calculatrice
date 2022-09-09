
from abc import ABC, abstractmethod
from typing import Union, Optional


class Operator(ABC):

    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def get_char_id(self) -> str:
        pass

    @abstractmethod
    def get_priority(self) -> int:
        pass

    @abstractmethod
    def do_operation(self, first_argument: float, second_argument: Optional[float]) -> Union[float, str]:
        pass
