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
        self._previous = val

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, val):
        self._distance = val

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, val):
        self._visited = val