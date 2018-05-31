import unittest

from src.edge import Edge
from src.vertex import Vertex
from src.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.v1 = Vertex('a')
        self.v2 = Vertex('b')
        self.v3 = Vertex('c')
        self.v4 = Vertex('d')
        self.e1 = Edge(self.v1, self.v2)
        self.e2 = Edge(self.v1, self.v3)
        self.e3 = Edge(self.v3, self.v4)
        self.e4 = Edge(self.v2, self.v4)
        self.g.add_vertex(self.v1)
        self.g.add_vertex(self.v2)
        self.g.add_vertex(self.v3)
        self.g.add_vertex(self.v4)
        self.g.add_edge(self.e1)
        self.g.add_edge(self.e2)
        self.g.add_edge(self.e3)
        self.g.add_edge(self.e4)

        self.e5 = Edge(self.v1, self.v4)
        self.v5 = Vertex('e')

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.g.vertices, [self.v1, self.v2, self.v3, self.v4])
        self.assertEqual(self.g.edges, [self.e1, self.e2, self.e3, self.e4])

    def test_contains_vertex(self):
        self.assertTrue(self.g.contains_vertex(self.v1))
        self.assertTrue(self.g.contains_vertex(self.v2))
        self.assertTrue(self.g.contains_vertex(self.v3))
        self.assertTrue(self.g.contains_vertex(self.v4))

        self.assertFalse(self.g.contains_vertex(self.v5))

    def test_contains_edge(self):
        self.assertTrue(self.g.contains_edge(edge=self.e1))
        self.assertTrue(self.g.contains_edge(edge=self.e2))
        self.assertTrue(self.g.contains_edge(edge=self.e3))
        self.assertTrue(self.g.contains_edge(edge=self.e4))

        self.assertFalse(self.g.contains_edge(edge=self.e5))

    def test_get_neighbors(self):
        self.assertEqual(self.g.get_neighbors(self.v1), [self.v2, self.v3])
        self.assertEqual(self.g.get_neighbors(self.v2), [self.v1, self.v4])
        self.assertEqual(self.g.get_neighbors(self.v3), [self.v1, self.v4])
        self.assertEqual(self.g.get_neighbors(self.v4), [self.v3, self.v2])

    def test_from_file(self):
        self.g2 = Graph()
        self.g2.read_from_file('graph.txt')
        print(self.g2.vertices)
        print(self.g2.edges)
