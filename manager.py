from src.algorithms.base import GraphAlgorithm
from src.graph.weighted_graph import Graph, Vertex, WeightedGraph
from src.parsers.base import GraphParser
from src.traversals.base import GraphTraversal
from src.parsers.edges_list import EdgesListParser

from pathlib import Path


class GraphManager:
    def __init__(self, graph: Graph, parser: GraphParser):
        self.__graph = graph
        self.__parser = parser

    def setParser(self, parser: GraphParser):
        self.__parser = parser

    def applyAlgorithm(self, algorithm: GraphAlgorithm):
        return algorithm.execute(self.__graph)

    def traverse(self, traversal: GraphTraversal, start: Vertex):
        return traversal.execute(self.__graph, start)

    def serializeGraph(self):
        return self.__parser.serialize(self.__graph)

    def deserializeGraph(self):
        return self.__parser.deserialize(self.__graph)


if __name__ == '__main__':
    filepath = Path('list_of_edges.txt')
    parser = EdgesListParser(filepath)
    edges, vertices = parser.deserialize()
    graph = WeightedGraph(edges, vertices)
