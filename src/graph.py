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

    def contains_edge(self, edge=None, vertex1=None, vertex2=None):
        if edge is None and (vertex1 is None or vertex2 is None):
            raise TypeError("usage of contains edge is either with an edge or 2 vertices")
        if edge is None:
            for e in self._edges:
                if vertex1 in e.endpoints and vertex2 in e.endpoints:
                    return True
            return False
        else:
            return edge in self._edges

        return edge in self._edges

    def contains_edge(self, v1: Vertex, v2: Vertex) -> bool:
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError("Inputs must be vertices")
        for e in self._edges:
            if v1 in e.endpoints and v2 in e.endpoints:
                return True
        return False

    def get_neighbors(self, v):
        if not isinstance(v, Vertex):
            raise TypeError("can only get neighbors of a Vertex")
        output = []
        for e in self._edges:
            if v in e.endpoints:
                for en in e.endpoints:
                    if en is not v:
                        output.append(en)
        return output
