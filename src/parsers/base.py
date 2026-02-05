from abc import ABC, abstractmethod
from pathlib import Path

from src.data.classes.vertex import Vertex
from src.data.classes.edge import Edge


class GraphParser(ABC):
    def __init__(self, filepath: Path):
        self.filepath = filepath

    @abstractmethod
    def parseFrom(self) -> tuple[list[Vertex], list[Edge]]:
        pass

    @abstractmethod
    def parseTo(self, graph: Graph) -> str:
        pass

    def isNumber(self, value: str):
        seen_digit = seen_dot = seen_exp = False
        for index, ch in enumerate(value):
            if ch.isdigit():
                seen_digit = True
            elif ch in ['e', 'E']:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            elif ch in ['+', '-']:
                if index > 0 and value[index - 1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit
