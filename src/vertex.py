import sys


class Vertex:

    def __init__(self, title):
        self._title = title
        self._previous = None
        self._distance = sys.maxsize
        self._visited = False

    @property
    def title(self):
        return self._title

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, val):
        if not isinstance(val, Vertex) and val is not None:
            raise TypeError("value of Previous must be a Vertex")
        self._previous = val

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, val):
        if not isinstance(val, int):
            raise TypeError("value of distance must be an integer")
        self._distance = val

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, val):
        if not isinstance(val, bool):
            raise TypeError("value of visited must be a boolean")
        self._visited = val

    def __str__(self):
        return "Vertex: {}, Distance: {}, Previous: {}, Visited: {}\n".format(self._title, self._distance,
                                                                              self._previous.title, self._visited)

    def __repr__(self):
        return "Vertex('{}')".format(self._title)
