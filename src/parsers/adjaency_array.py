from src.data.classes.vertex import Vertex
from src.data.classes.edge import Edge
from src.graph.base import Graph
from .base import GraphParser


class AdjaencyArrayParser(GraphParser):
    def parseFrom(self):
        edges = []

        with open(self.filepath, 'r') as fp:
            vertices = [Vertex(name.strip())
                        for name in fp.readline().split(' ')]
            for line in fp.readlines():
                left_brace = line.find('[')
                if left_brace == -1:
                    raise ValueError

                right_brace = line.find(']')
                if right_brace == -1:
                    raise ValueError

                values = line[left_brace + 1: right_brace]

                parts = values.split(',')
                print(parts)
                if len(parts) != 3:
                    raise ValueError

                start_index = parts[0]
                if not start_index.isnumeric():
                    raise ValueError

                finish_index = parts[1]
                if not finish_index.isnumeric():
                    raise ValueError

                if not self.isNumber(parts[2]):
                    raise ValueError
                weight = float(parts[2])

                edges.append(
                    Edge(vertices[int(start_index)], vertices[int(finish_index)], weight))

        return Graph(edges, vertices)

    def parseTo(self, graph: Graph):
        vertices = graph.get_vertices()
        edges = graph.get_edges()
        vertices_names = (vertex.name for vertex in vertices)
        vertex_to_index = {vertex: index for index,
                           vertex in enumerate(vertices)}
        arrays = [[0 for _ in range(len(vertices))]
                  for _ in range(len(vertices))]

        for edge in edges:
            row = vertex_to_index[edge.start]
            col = vertex_to_index[edge.finish]
            weight = edge.weight
            arrays[row][col] = weight
            arrays[col][row] = weight

        parsed_result = ''
        parsed_result += ' '.join(vertices_names)
        for array in arrays:
            array_to_str = '[{}]'.format(','.join(str(cell) for cell in array))
            parsed_result += array_to_str

        with open(self.filepath, 'w') as fp:
            chars = fp.write(parsed_result)

        return chars
