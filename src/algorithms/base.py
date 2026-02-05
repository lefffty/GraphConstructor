from abc import ABC, abstractmethod

from src.graph.base import Graph


class GraphAlgorithm(ABC):
    @abstractmethod
    def execute(self, graph: Graph, *args, **kwargs):
        pass
