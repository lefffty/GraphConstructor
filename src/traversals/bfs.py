from .base import GraphTraversal

from collections import defaultdict, deque


class BFSAlgorithm(GraphTraversal):
    def execute(self, graph, *args, **kwargs):
        start = kwargs.pop('start', None)
        if start is None:
            raise ValueError

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
