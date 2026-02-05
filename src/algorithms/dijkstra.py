import heapq
from collections import defaultdict
from typing import MutableMapping

from .base import GraphAlgorithm

from src.graph.base import Graph
from src.data.classes.vertex import Vertex


class DijkstraAlgorithm(GraphAlgorithm):
    def execute(self, graph: Graph, *args, **kwargs):
        source = kwargs.pop('source', None)
        if source is None:
            raise ValueError

        vertices = graph.get_vertices()
        edges = graph.get_edges()

        dist = {vertex: float('inf') for vertex in vertices}
        dist[source] = 0.0
        min_heap = [(0.0, source)]

        gr: MutableMapping[Vertex,
                           list[tuple[float, Vertex]]] = defaultdict(list)

        for edge in edges:
            gr[edge.start].append((edge.weight, edge.finish))

        while min_heap:
            curr, u = heapq.heappop(min_heap)

            if curr > dist[u]:
                continue

            for weight, v in gr[u]:
                alt = curr + weight
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(min_heap, (alt, v))

        return dist
