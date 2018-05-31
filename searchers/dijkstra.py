from src.graph import *
import sys


class Dijkstra:

    def __init__(self, source: Vertex, graph: Graph, auto_search=True):
        if not isinstance(graph, Graph):
            raise TypeError("DSP requires a graph to search")
        self._g = graph
        if not isinstance(source, Vertex) or not self._g.contains_vertex(source):
            raise TypeError("Source must be a vertex and must be in the graph")
        self._source = source
        self._q = self._g.vertices.copy()
        for v in self._g.vertices:
            v.distance = sys.maxsize
            v.previous = None
            v.visited = False
        source.distance = 0
        source.previous = self._source
        if auto_search:
            self.perform_search()

    @property
    def source(self):
        return self._source

    def perform_search(self):
        while len(self._q) != 0:
            u = self.__get_smallest()
            self._q.remove(u)
            u.visited = True

            for n in self._g.get_neighbors(u):
                if not n.visited:
                    alt = u.distance + self._g.get_edge(u, n).weight
                    if alt < n.distance:
                        n.distance = alt
                        n.previous = u

    def find_path(self, v: Vertex):
        if not isinstance(v, Vertex) or not self._g.contains_vertex(v):
            raise TypeError("find_path requires a vertex in the graph")
        output = list()
        cv = v
        while cv.previous.title != cv.title:
            output.append(cv.title)
            cv = cv.previous
        output.append(cv.previous.title)
        output.reverse()
        return output

    def __get_smallest(self) -> Vertex:
        p = sys.maxsize
        vo = None
        for v in self._q:
            if v.distance < p:
                p = v.visited
                vo = v
        return vo

    def get_v(self):
        return self._g.vertices
