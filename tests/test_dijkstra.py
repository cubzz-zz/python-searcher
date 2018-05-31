import unittest
from searchers.dijkstra import *
from src.graph import *


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.vs = []
        self.es = []
        self.v0 = Vertex('0')
        self.vs.append(self.v0)
        self.v1 = Vertex('1')
        self.vs.append(self.v1)
        self.v2 = Vertex('2')
        self.vs.append(self.v2)
        self.v3 = Vertex('3')
        self.vs.append(self.v3)
        self.v5 = Vertex('5')
        self.vs.append(self.v5)
        self.v6 = Vertex('6')
        self.vs.append(self.v6)
        self.v7 = Vertex('7')
        self.vs.append(self.v7)
        # print(self.vs)
        for v in self.vs:
            self.g.add_vertex(v)

        # print('Vertices ' + str(self.g.vertices))
        self.e03 = Edge(self.v0, self.v3, 1)
        self.es.append(self.e03)
        self.e31 = Edge(self.v3, self.v1, 4)
        self.es.append(self.e31)
        self.e37 = Edge(self.v3, self.v7, 2)
        self.es.append(self.e37)
        self.e12 = Edge(self.v1, self.v2, 5)
        self.es.append(self.e12)
        self.e15 = Edge(self.v1, self.v5, 3)
        self.es.append(self.e15)
        self.e16 = Edge(self.v1, self.v6, 3)
        self.es.append(self.e16)
        self.e52 = Edge(self.v5, self.v2, 3)
        self.es.append(self.e52)
        self.e56 = Edge(self.v5, self.v6, 5)
        self.es.append(self.e56)
        self.e67 = Edge(self.v6, self.v7, 6)
        self.es.append(self.e67)
        for e in self.es:
            self.g.add_edge(e)

        self.v868 = Vertex('868')

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            self.d = Dijkstra(self.v868, self.g)
        with self.assertRaises(TypeError):
            self.d = Dijkstra(self.v868, 'the graph')
        with self.assertRaises(TypeError):
            self.d = Dijkstra(self.v1, 'the graph')

    def test_paths(self):
        self.d = Dijkstra(self.v0, self.g)
        self.assertEqual(self.d.find_path(self.v7), ['0', '3', '7'])
        self.assertEqual(self.d.find_path(self.v6), ['0', '3', '1', '6'])
        self.assertEqual(self.d.find_path(self.v5), ['0', '3', '1', '5'])
        self.assertEqual(self.d.find_path(self.v3), ['0', '3'])
        self.assertEqual(self.d.find_path(self.v2), ['0', '3', '1', '2'])
        self.assertEqual(self.d.find_path(self.v1), ['0', '3', '1'])
        self.assertEqual(self.d.find_path(self.v0), ['0'])
