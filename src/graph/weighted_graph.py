from .base import Graph

from src.data.classes.edge import Edge
from src.data.classes.vertex import Vertex

from typing import overload, SupportsFloat


class WeightedGraph(Graph):
    @overload
    def add_vertex(self, name: str):
        if not isinstance(name, str):
            raise ValueError
        vertex = Vertex(name)
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    @overload
    def add_vertex(self, vertex: Vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    @overload
    def add_edge(self, edge: Edge):
        if edge not in self.edges:
            self.edges.append(edge)

    @overload
    def add_edge(self, start: Vertex, finish: Vertex, weight: SupportsFloat):
        if not isinstance(start, Vertex):
            raise ValueError
        if not isinstance(finish, Vertex):
            raise ValueError
        if not isinstance(weight, SupportsFloat):
            raise ValueError
        edge = Edge(start, finish, weight)
        if edge not in self.edges:
            self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def get_vertices(self):
        return self.vertices

    def add_edges(self, edges: list[tuple[str, str, SupportsFloat]]):
        return [self.add_edge(*edge) for edge in edges]

    def add_vertices(self, vertices: list[Vertex]):
        return [self.add_vertex(vertex) for vertex in vertices]

    def set_names(self, names: list[str]):
        if len(names) != len(self.vertices):
            raise ValueError
        self.vertices = [vertex.rename(name)
                         for vertex, name in zip(self.vertices, names)]

    def remove_edge(self, start: str, finish: str, weight: SupportsFloat) -> bool:
        start_v = Vertex(start)
        finish_v = Vertex(finish)
        edge = Edge(start_v, finish_v, weight)

        for index, _edge in enumerate(self.edges):
            if edge == _edge:
                self.edges.pop(index)
                return True

        return False

    def remove_vertex(self, name: str):
        vertex = Vertex(name)

        for index, edge in enumerate(self.edges):
            if edge.start == vertex or edge.finish == vertex:
                self.edges.pop(index)

        for index, vertex in enumerate(self.vertices):
            if vertex == Vertex(name):
                self.vertices.pop(index)
