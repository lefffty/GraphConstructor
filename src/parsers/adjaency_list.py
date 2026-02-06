from .base import GraphParser

from ..graph.base import Graph, Edge, Vertex

from collections import defaultdict


class AdjaencyListParser(GraphParser):
    def serialize(self, graph: Graph) -> int:
        vertices = graph.get_vertices()
        vertex_to_index = {vertex: index for index,
                           vertex in enumerate(vertices)}
        edges = graph.get_edges()

        parsed_result = ''
        parsed_result += ' '.join(vertex.name for vertex in vertices)
        parsed_result += '\n'
        strings = ['' for _ in range(len(vertices))]
        for edge in edges:
            start_to_index = vertex_to_index[edge.start]
            finish_to_index = vertex_to_index[edge.finish]
            weight = edge.weight
            start_to_finish = '[{},{}] '.format(finish_to_index, weight)
            finish_to_start = '[{},{}] '.format(start_to_index, weight)
            strings[start_to_index] += start_to_finish
            strings[finish_to_index] += finish_to_start

        parsed_result += '\n'.join(strings)

        with open(self.filepath, 'w') as fp:
            chars = fp.write(parsed_result)

        return chars

    def deserialize(self) -> tuple[list[Vertex], list[Edge]]:
        edges = []

        with open(self.filepath, 'r') as fp:
            vertices = [Vertex(name.strip())
                        for name in fp.readline().split(' ')]

            for index, values in enumerate(fp.readlines()):
                for edge_str in values.split(' '):
                    left_brace = edge_str.find('[')
                    if left_brace == -1 or left_brace != 0:
                        raise ValueError

                    right_brace = edge_str.find(']')
                    if right_brace == -1 or right_brace != len(values) - 2:
                        raise ValueError

                    edge_str = edge_str[left_brace + 1:right_brace]
                    parts = edge_str.split(',')
                    if not self.isNumber(parts[1]):
                        raise ValueError
                    edge = Edge(vertices[index],
                                vertices[int(parts[0])], float(parts[1]))
                    edges.append(edge)

        return edges, vertices

    def to(self, graph: Graph):
        edges = graph.get_edges()
        gr = defaultdict(list)
        for edge in edges:
            gr[edge.start].append((edge.finish, edge.weight))
            gr[edge.finish].append((edge.start, edge.weight))

        return gr
