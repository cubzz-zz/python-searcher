import unittest
import sys

from src.vertex import Vertex


class TestVertex(unittest.TestCase):

    def setUp(self):
        self.v1 = Vertex('a')
        self.v2 = Vertex('b')
        self.v3 = Vertex('c')

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.v1.title, 'a')
        self.assertEqual(self.v2.title, 'b')
        self.assertEqual(self.v3.title, 'c')

        self.assertEqual(self.v1.previous, None)
        self.assertEqual(self.v2.previous, None)
        self.assertEqual(self.v3.previous, None)

        self.assertEqual(self.v1.distance, sys.maxsize)
        self.assertEqual(self.v2.distance, sys.maxsize)
        self.assertEqual(self.v3.distance, sys.maxsize)

        self.assertEqual(self.v1.visited, False)
        self.assertEqual(self.v2.visited, False)
        self.assertEqual(self.v3.visited, False)

    def test_setters(self):
        self.v1.distance = 3
        self.v2.distance = 400
        self.v3.distance = 649000

        self.assertEqual(self.v1.distance, 3)
        self.assertEqual(self.v2.distance, 400)
        self.assertEqual(self.v3.distance, 649000)

        self.v1.previous = self.v2
        self.v2.previous = self.v3
        self.v3.previous = self.v1

        self.assertEqual(self.v1.previous, self.v2)
        self.assertEqual(self.v2.previous, self.v3)
        self.assertEqual(self.v3.previous, self.v1)

        self.v1.visited = True
        self.v2.visited = True
        self.v3.visited = True

        self.assertEqual(self.v1.visited, True)
        self.assertEqual(self.v2.visited, True)
        self.assertEqual(self.v3.visited, True)
