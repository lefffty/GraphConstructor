from abc import abstractmethod, ABC

from src.graph import Graph


class GraphTraversal(ABC):
    @abstractmethod
    def execute(self, graph: Graph, *args, **kwargs):
        pass
