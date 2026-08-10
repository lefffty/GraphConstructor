class Coder:
    def __init__(self, vertices):
        self.__vertices = vertices

    def code(self, edges: list, coder: dict):
        for index, _ in enumerate(edges):
            start, finish, weight = edges[index]
            edges[index] = (coder[start], coder[finish], weight)

    def get_encoder_decoder(self):
        encoder = {vertex: index for index,
                   vertex in enumerate(self.__vertices)}
        decoder = {index: vertex for index,
                   vertex in enumerate(self.__vertices)}
        return encoder, decoder
