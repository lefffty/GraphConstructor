from .base import GraphTraversal, Graph, Vertex


class HamiltonPath(GraphTraversal):
    def execute(self, graph: Graph, start: Vertex):
        self.gr_matrix, self.start = self.__create_adjaency_matrix(
            graph, start)
        self.n = len(self.gr_matrix)
        self.path = [-1] * (self.n + 1)
        self.visited = [False] * self.n
        return self.__find_cycle(self.start)

    def __create_adjaency_matrix(self, graph: Graph, start: Vertex) -> list[list[int]]:
        vertices = graph.get_vertices()
        self.vertex_to_index = {vertex: index for index,
                                vertex in enumerate(vertices)}
        self.index_to_vertex = {
            index: vertex for index, vertex in enumerate(vertices)}
        edges = graph.get_edges()
        n = len(vertices)
        gr_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            row = self.vertex_to_index[edge.start]
            col = self.vertex_to_index[edge.finish]
            gr_matrix[row][col] = 1
            gr_matrix[col][row] = 1
        return gr_matrix, self.vertex_to_index[start]

    def __is_safe(self, vertex, pos):
        if self.gr_matrix[self.path[pos - 1]][vertex] == 0:
            return False

        if self.visited[vertex]:
            return False

        return True

    def __hamiltonian_util(self, pos):
        if pos == self.n:
            if self.gr_matrix[self.path[pos - 1]][self.path[0]] == 1:
                return True
            return False

        for v in range(1, self.n):
            if self.__is_safe(v, pos):
                self.path[pos] = v
                self.visited[v] = True

                if self.__hamiltonian_util(pos + 1):
                    return True

                self.path[pos] = -1
                self.visited[v] = False

        return False

    def __find_cycle(self, start) -> list | None:
        self.path[0] = start
        self.visited[start] = True

        if not self.__hamiltonian_util(1):
            return None

        self.path[-1] = self.path[0]
        self.path = list(
            map(lambda index: self.index_to_vertex[index], self.path))
        return self.path
