import unittest
from utils.graph import DirectedGraph

class TestDirectedGraphBuild(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.adj_list = {
            'a': ['c'],
            'b': ['c'],
            'c': []
        }

    def test_adjacency_building(self):
        self.graph.from_adjacency_list(self.adj_list)
        self.assertEqual(self.graph.neighbors_for_vertex('a'), ['c'])

class TestDirectedGraphNeighbors(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.adj_list = {
            'a': ['c'],
            'b': ['c'],
            'c': []
        }
        self.graph.from_adjacency_list(self.adj_list)

    def test_parents_for_vertex(self):
        self.assertEqual(
            [self.graph.vertex_at(v) for v in self.graph.parents_for_vertex('c')], 
            ['a', 'b'])

    def test_find_sources(self):
        self.assertEqual(
            self.graph.find_sources(), 
            ['a', 'b']
        )

if __name__ == '__main__':
    unittest.main()