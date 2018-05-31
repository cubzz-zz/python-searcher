from src.graph import *


class Dijkstra:

    def __init__(self, source: Vertex, graph: Graph, boot=True):
        if not isinstance(graph, Graph):
            raise TypeError("DSP requires a graph to search")
        self._g = graph
        if not isinstance(source, Vertex) or not self._g.contains_vertex(source):
            raise TypeError("Source must be a vertex and must be in the graph")
        self._source = source
        if boot:
            self.__perform_search()

    @property
    def source(self):
        return self._source

    def __perform_search(self):
        pass

    def find_path(self, v: Vertex):
        if not isinstance(v, Vertex) or not self._g.contains_vertex(v):
            raise TypeError("find_path requires a vertex in the graph")

