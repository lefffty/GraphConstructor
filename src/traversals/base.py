from abc import abstractmethod, ABC

from src.graph.base import Graph
from src.data.classes.vertex import Vertex


class GraphTraversal(ABC):
    @abstractmethod
    def execute(self, graph: Graph, start: Vertex) -> list[Vertex]:
        pass
