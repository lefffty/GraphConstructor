from .base import GraphTraversal
from src.data.classes.vertex import Vertex
from src.graph.base import Graph

from collections import defaultdict, deque


class BFSAlgorithm(GraphTraversal):
    def execute(self, graph: Graph, start: Vertex) -> list[Vertex]:
        edges = graph.get_edges()

        gr = defaultdict(list)
        for edge in edges:
            gr[edge.start].append(edge)

        visited = []

        queue = deque([start])
        while queue:
            top = queue.pop()
            if top not in visited:
                visited.append(top)
            if gr[top]:
                for node in gr[top]:
                    if node.finish not in visited:
                        queue.append(node.finish)

        return visited
