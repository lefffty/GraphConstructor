from .base import GraphAlgorithm, Graph

from src.utils.djs import DisjointSet
from src.data.classes.edge import Edge


def sort_by_weight(edge: Edge):
    _, _, weight = edge
    return weight


class KruskalAlgorithm(GraphAlgorithm):
    def execute(self, graph: Graph, **kwargs):
        edges = graph.get_edges()
        vertices = graph.get_vertices()
        mst_edges = []
        djs = DisjointSet(len(vertices))
        edges.sort(key=sort_by_weight)

        for u, v, weight in edges:
            if djs.union(u, v):
                mst_edges.append(Edge(u, v, weight))
                if len(mst_edges) == len(vertices) - 1:
                    break

        return mst_edges
