import heapq

from collections import defaultdict

from .base import GraphAlgorithm

from src.graph.base import Graph
from src.data.classes.edge import Edge
from src.data.classes.vertex import Vertex


class PrimAlgorithm(GraphAlgorithm):
    def execute(self, graph: Graph, *args, **kwargs):
        start: Vertex = kwargs.pop('start', None)
        if start is None:
            raise ValueError
        min_heap: list[Edge] = []
        visited = set()
        mst_edges = []

        visited.add(start)

        edges = graph.get_edges()
        gr = defaultdict(list)

        for edge in edges:
            gr[edge.start].append(edge)
            gr[edge.finish].append(Edge(edge.finish, edge.start, edge.weight))
            if edge.start == start:
                heapq.heappush(min_heap, edge)
            elif edge.finish == start:
                edge = Edge(edge.finish, edge.start, edge.weight)
                heapq.heappush(min_heap, edge)

        while min_heap:
            u, v, weight = heapq.heappop(min_heap)
            if v in visited:
                continue
            visited.add(v)
            mst_edges.append(Edge(u, v, weight))
            for edge in gr[v]:
                if edge.finish not in visited:
                    heapq.heappush(min_heap, edge)

        return mst_edges
