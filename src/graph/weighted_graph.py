from .base import Graph

from src.data.classes.edge import Edge
from src.data.classes.vertex import Vertex

from typing import SupportsFloat


class WeightedGraph(Graph):
    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def add_vertex(self, vertex: Vertex):
        self._vertices.append(vertex)

    def add_vertices(self, vertices: list[Vertex]):
        return [self.add_vertex(vertex) for vertex in vertices]

    def add_edge(self, start: Vertex, finish: Vertex, weight: SupportsFloat):
        edge = Edge(start, finish, weight)
        if not self.is_vertex_in(start):
            self.add_vertex(start)
        if not self.is_vertex_in(finish):
            self.add_vertex(finish)
        if edge not in self._edges:
            self._edges.append(edge)

    def add_edges(self, edges: list[Edge]):
        return [self.add_edge(edge) for edge in edges]

    def set_names(self, names: list[str]):
        if len(names) != len(self._vertices):
            raise ValueError(
                "Numbers of names doesn`t match numbers of vertices!")
        self._vertices = [vertex.rename(name)
                          for vertex, name in zip(self._vertices, names)]

    def remove_edge(self, start: Vertex, finish: Vertex, weight: SupportsFloat) -> bool:
        edge = Edge(start, finish, weight)
        if self.is_edge_in(edge):
            raise ValueError('Edge is not in graph!')

        for index, _edge in enumerate(self._edges):
            if edge == _edge:
                self._edges.pop(index)
                return True

        return False

    def remove_vertex(self, vertex: Vertex):
        if not self.is_vertex_in(vertex):
            raise ValueError('Vertex is not in graph!')

        for index, edge in enumerate(self._edges):
            if edge.start == vertex or edge.finish == vertex:
                self._edges.pop(index)

        for index, _vertex in enumerate(self._vertices):
            if vertex == _vertex:
                self._vertices.pop(index)
