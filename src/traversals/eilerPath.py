from collections import defaultdict, deque

from .base import GraphTraversal
from ..graph.base import Graph, Vertex


class EilerPath(GraphTraversal):
    def execute(self, graph: Graph, start: Vertex):
        edges = graph.get_edges()
        gr = defaultdict(list)

        for edge in edges:
            gr[edge.start].append(edge.finish)
            gr[edge.finish].append(edge.start)

        if start not in gr.keys():
            raise KeyError

        if not self.__hasPath(gr):
            raise ValueError

        cycle = self.__hasCycle(gr)

        path: list[Vertex] = []
        stack = deque([start])
        while stack:
            v = stack[0]
            if len(gr[v]) == 0:
                path.append(v)
                stack.popleft()
            else:
                u = gr[v][0]
                stack.appendleft(u)
                gr[v].remove(u)
                gr[u].remove(v)

        path = path[::-1]
        if cycle:
            return path
        else:
            return path[:-1]

    def __hasPath(self, gr: defaultdict[list]):
        counter = 0
        for _, values in gr.items():
            if len(values) % 2:
                counter += 1

        return True if counter <= 2 else False

    def __hasCycle(self, gr: defaultdict[list]):
        for _, values in gr.items():
            if len(values) % 2 == 1:
                return False
        return True


if __name__ == '__main__':
    pass
