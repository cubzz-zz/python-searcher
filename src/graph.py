from src.edge import Edge
from src.vertex import Vertex


class Graph:

    def __init__(self):
        self._vertices = list()
        self._edges = list()

    @property
    def edges(self) -> list:
        return self._edges

    @property
    def vertices(self) -> list:
        return self._vertices

    def add_vertex(self, v: Vertex):
        if isinstance(v, Vertex):
            self._vertices.append(v)
        else:
            raise TypeError("Must be a Vertex")

    def add_edge(self, e: Edge):
        if isinstance(e, Edge):
            self._edges.append(e)
        else:
            raise TypeError("Must be an Edge")

    def add_edge(self, v1: Vertex, v2: Vertex):
        pass

    def contains_vertex(self, v):
        for ve in self._vertices:
            if v == ve:
                return True
        return False

    def contains_edge(self, e):
        pass

    def contains_edge(self, v1, v2):
        pass

    def get_neighbors(self):
        pass
