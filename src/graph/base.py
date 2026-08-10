from abc import ABC, abstractmethod
from typing import Optional, SupportsFloat

from src.data.classes.edge import Edge, Vertex


class Graph(ABC):
    def __init__(
        self,
        edges: Optional[list[Edge]],
        vertices: Optional[list[Vertex]]
    ):
        if edges is None:
            edges = []
        if vertices is None:
            vertices = []
        self._edges: list[Edge] = edges
        self._vertices: list[Vertex] = vertices

    @abstractmethod
    def add_vertex(self, vertex: Vertex) -> None:
        pass

    @abstractmethod
    def add_vertices(self, vertices: list[Vertex]) -> None:
        pass

    @abstractmethod
    def add_edge(self, start: Vertex, finish: Vertex, weight: SupportsFloat) -> None:
        pass

    @abstractmethod
    def remove_edge(self, start: Vertex, finish: Vertex, weight: SupportsFloat) -> bool:
        pass

    @abstractmethod
    def remove_vertex(self, name: Vertex):
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

    def is_vertex_in(self, vertex: Vertex):
        return vertex in self._vertices

    def is_edge_in(self, edge: Edge):
        return edge in self._edges

    def __str__(self):
        return 'Graph(v={}, e={})'.format(len(self._vertices), len(self._edges))
