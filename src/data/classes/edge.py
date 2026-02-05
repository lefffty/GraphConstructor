from dataclasses import dataclass
from typing import SupportsFloat


from src.data.classes.vertex import Vertex


@dataclass(frozen=True)
class Edge:
    start: Vertex
    finish: Vertex
    weight: SupportsFloat = 1.

    def to_serializable(self):
        return {
            'start': self.start.to_serializable(),
            'finish': self.finish.to_serializable(),
            'weight': self.weight,
        }

    def __eq__(self, other):
        return (
            self.start == other.start and
            self.finish == other.finish and
            self.weight == other.weight
        )

    def __gt__(self, other):
        return self.weight > other.weight

    def __iter__(self):
        return iter((self.start, self.finish, self.weight))
