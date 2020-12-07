import unittest
from simulation.sequence_memory import SequenceMemory
from simulation.sequence import Sequence
from simulation.messages import Message
from simulation.simulator import Simulator
from utils.graph import DirectedGraph

class TestSequenceMemory(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()
        self.m0 = Message(self.sim, 1, 'han0', 'cmd')
        self.m1 = Message(self.sim, 2, 'han1', 'cmd')
        self.m2 = Message(self.sim, 3, 'han2', 'cmd', preqs=[self.m0, self.m1])
        self.adj_list = {
            self.m0: [self.m2],
            self.m1: [self.m2],
            self.m2: []
        }
        self.graph = DirectedGraph()
        self.graph.from_adjacency_list(self.adj_list)
        self.seq = Sequence(self.graph)
        self.sequence_memory = SequenceMemory()

    def test_add_sequence(self):
        self.sequence_memory.add_sequence(self.seq)
        self.assertEqual(True, self.seq in self.sequence_memory.sequence_finder.values())
        with self.assertRaises(KeyError):
            self.sequence_memory.add_sequence(self.seq)

    def test_find_sequence_key(self):
        self.sequence_memory.add_sequence(self.seq)
        self.assertEqual(self.sequence_memory.get_sequence_key(self.seq), 0)
    
    def test_get_sequence(self):
        self.sequence_memory.add_sequence(self.seq)
        self.assertEqual(self.seq, self.sequence_memory.get_sequence(self.seq))

    def test_remove_sequence(self):
        self.sequence_memory.add_sequence(self.seq)
        self.sequence_memory.remove_sequence(self.seq)
        self.assertEqual(self.sequence_memory.sequence_finder, {})
        self.assertEqual(False, self.sequence_memory.exists_message(self.m0))
        with self.assertRaises(KeyError):
            self.sequence_memory.remove_sequence(self.seq)

    def test_exists_message(self):
        self.sequence_memory.add_sequence(self.seq)
        self.assertEqual(True, self.sequence_memory.exists_message(self.m0))

if __name__ == '__main__':
    unittest.main()