from src.vertex import Vertex


class Edge:

    def __init__(self, end1: Vertex, end2: Vertex):
        if not isinstance(end1, Vertex) or not isinstance(end2, Vertex):
            raise TypeError("endpoints must be Vertexes")
        self._endpoints = list()
        self._endpoints.append(end1)
        self._endpoints.append(end2)

    @property
    def endpoints(self):
        return self._endpoints
