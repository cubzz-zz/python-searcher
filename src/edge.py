from src.vertex import Vertex


class Edge:

    def __init__(self, end1: Vertex, end2: Vertex):
        self._endpoints = list()
        self._endpoints.append(end1)
        self._endpoints.append(end2)

    @property
    def endpoints(self):
        return self._endpoints
