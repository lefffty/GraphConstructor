from decimal import Decimal

from .base import GraphParser

from src.data.classes.edge import Edge
from src.data.classes.vertex import Vertex
from src.graph.base import Graph


class AdjaencyMatrixParser(GraphParser):
    def parseFrom(self):
        edges = []

        with open(self.filepath, 'r') as fp:
            vertices = [Vertex(name.strip())
                        for name in fp.readline().split(' ')]
            for row, values in enumerate(fp.readlines()):
                for col, value in enumerate(values.split(' ')):
                    if self.isNumber(value):
                        if Decimal(value) != Decimal('0.0'):
                            weight = float(value)
                            edges.append(
                                Edge(vertices[row], vertices[col], weight))

        return Graph(edges, vertices)

    def parseTo(self, graph: Graph):
        vertices = graph.get_vertices()
        vertices_names = (vertex.name for vertex in vertices)
        edges = graph.get_edges()
        vertice_to_index = {vertex: index for index,
                            vertex in enumerate(vertices)}
        matrix = [[0 for _ in range(len(vertices))]
                  for _ in range(len(vertices))]

        for edge in edges:
            row = vertice_to_index[edge.start]
            col = vertice_to_index[edge.finish]
            weight = edge.weight
            matrix[row][col] = weight
            matrix[col][row] = weight

        parse_result = ''
        parse_result += ' '.join(vertices_names)
        parse_result += '\n'

        for row in matrix:
            parse_result += ' '.join(str(cell) for cell in row)
            parse_result += '\n'

        with open(self.filepath, 'w') as fp:
            chars = fp.write(parse_result)

        return chars
