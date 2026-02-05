from abc import ABC, abstractmethod
from typing import Optional, SupportsFloat

from src.data.classes.edge import Edge
from src.data.classes.vertex import Vertex


class Graph(ABC):
    def __init__(self, edges: Optional[list[Edge]] = None, vertices: Optional[list[Vertex]] = None):
        if edges is None:
            edges = []
        if vertices is None:
            vertices = []
        self.edges: list[Edge] = edges
        self.vertices: list[Vertex] = vertices

    @abstractmethod
    def add_vertex(self, vertex: str) -> None:
        pass

    @abstractmethod
    def add_vertices(self, vertices: list[Vertex]) -> None:
        pass

    @abstractmethod
    def add_edge(self, start: str, finisg: str, weight: SupportsFloat) -> None:
        pass

    @abstractmethod
    def remove_edge(self, start: str, finish: str, weight: SupportsFloat) -> bool:
        pass

    @abstractmethod
    def remove_vertex(self, name: str):
        pass

    @abstractmethod
    def add_edges(self, edges: list[Edge]) -> None:
        pass

    @abstractmethod
    def get_vertices(self) -> list[Vertex]:
        pass

    @abstractmethod
    def get_edges(self) -> list[Edge]:
        pass

    @abstractmethod
    def set_names(self, names: list[str]):
        pass

    def __str__(self):
        return 'Graph(v={}, e={})'.format(len(self.vertices), len(self.edges))
