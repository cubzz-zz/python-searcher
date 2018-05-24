import unittest
import sys

from src.edge import Edge
from src.vertex import Vertex


class TestEdge(unittest.TestCase):

    def setUp(self):
        self.v1 = Vertex('a')
        self.v2 = Vertex('b')
        self.e1 = Edge(self.v1, self.v2)

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.e1.endpoints[0], self.v1)
        self.assertEqual(self.e1.endpoints[1], self.v2)
