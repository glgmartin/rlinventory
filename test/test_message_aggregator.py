import unittest
from simulation.message_aggregator import MessageAggregator
from simulation.simulator import Simulator
from simulation.messages import Message
from simulation.sequence import Sequence
from utils.graph import DirectedGraph

class TestBasicAggregation(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()
        self.agg = MessageAggregator()
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
        self.m_alone = Message(self.sim, 4, 'han_alone', 'cmd')

    def test_handle_messages(self):
        self.assertEqual(self.sim.queue.queue.queue[0], self.m0)

if __name__ == '__main__':
    unittest.main()