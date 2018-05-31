from src.vertex import Vertex


class Edge:

    def __init__(self, end1: Vertex, end2: Vertex, weight=0):
        if not isinstance(end1, Vertex) or not isinstance(end2, Vertex):
            raise TypeError("endpoints must be Vertexes")
        self._endpoints = list()
        self._endpoints.append(end1)
        self._endpoints.append(end2)
        self._weight = weight

    @property
    def endpoints(self):
        return self._endpoints

    @property
    def weight(self):
        return self._weight
