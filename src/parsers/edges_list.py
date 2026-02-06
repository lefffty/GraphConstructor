from .base import GraphParser, Graph, Edge, Vertex


class EdgesListParser(GraphParser):
    def serialize(self, graph: Graph) -> int:
        edges = graph.get_edges()

        def string_func(edge: Edge): return '[{},{},{}]'.format(
            edge.start, edge.finish, edge.weight)

        output = list(map(string_func, edges))

        with open(self.filepath, 'w') as fp:
            chars = fp.write(output)

        return chars

    def deserialize(self) -> tuple[list[Edge], list[Vertex]]:
        vertices = set()
        edges = []
        with open(self.filepath, 'r') as fp:
            for index, line in enumerate(fp.readlines()):
                line = line.strip()[1:-1]
                parts = line.split(',')
                s_name, f_name, w = parts
                start = Vertex(s_name)
                finish = Vertex(f_name)
                try:
                    weight = float(w)
                except ValueError:
                    raise ValueError(f'Can`t convert "{w}"({index}) to float!')
                edge = Edge(start, finish, weight)
                vertices.update([start, finish])
                edges.append(edge)

        return edges, vertices

    def to(self, graph: Graph):
        return NotImplemented
