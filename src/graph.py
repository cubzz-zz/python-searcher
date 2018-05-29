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

    def contains_vertex(self, v):
        if not isinstance(v, Vertex):
            raise TypeError("contains_vertex argument must be a Vertex")
        return v in self._vertices

    def contains_edge(self, e):
        if not isinstance(e, Edge):
            raise TypeError("contains_edge argument must be an Edge")
        return e in self._edges

    def contains_edge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError("Inputs must be vertices")
        for e in self._edges:
            if v1 in e.endpoints and v2 in e.endpoints:
                return True
        return False

    def get_neighbors(self, v):
        if not isinstance(v, Vertex):
            raise TypeError("can only get neighbors of a Vertex")
        output = list()
        for e in self._edges:
            if v in e.endpoints:
                for en in e.endpoints:
                    output.append(en)
        output.remove(v)
        return output
