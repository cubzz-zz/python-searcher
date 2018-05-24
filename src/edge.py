from src.vertex import Vertex

class Edge:

    def __init__(self, end1:Vertex, end2:Vertex):
        self.endpoints = list()
        self.endpoints.append(end1)
        self.endpoints.append(end2)