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
        self.m_alone_pending = Message(self.sim, 4, 'han_alone', 'cmd')
        self.m_alone_ready = Message(self.sim, 5, 'han_far_away', 'cmd')
        self.m_alone_ready.state = Message.READY
        self.m_alone_done = Message(self.sim, 5, 'han_far_away', 'cmd')
        self.m_alone_done.state = Message.DONE

    def test_handle_unknown_pending_messages(self):
        self.agg.handle(self.m_alone_pending)
        self.assertEqual(self.sim.queue.queue.queue[0], self.m_alone_pending)

    def test_handle_unknown_ready_messages(self):
        with self.assertRaises(RuntimeError):
            self.agg.handle(self.m_alone_ready)

    def test_handle_unknown_done_messages(self):
        with self.assertRaises(RuntimeError):
            self.agg.handle(self.m_alone_done)

    def test_handle_known_pending_messages(self):
        self.agg.handle(self.seq)
        self.m0.state = Message.PENDING
        with self.assertRaises(RuntimeError):
            self.agg.handle(self.m0)

    def test_handle_known_ready_messages(self):
        self.agg.handle(self.seq)
        self.m0.state = Message.READY
        with self.assertRaises(RuntimeError):
            self.agg.handle(self.m0)

    def test_handle_known_done_messages(self):
        self.agg.handle(self.seq)
        self.m0.state = Message.DONE
        self.agg.handle(self.m0)
        self.m1.state = Message.DONE
        self.agg.handle(self.m1)
        self.assertEqual(self.m2.state, Message.READY)

    def test_know_if_sequence_finished(self):
        self.agg.handle(self.seq)
        self.m0.state = Message.DONE
        self.m1.state = Message.DONE
        self.m2.state = Message.DONE
        self.agg.handle(self.m2)
        self.assertEqual({}, self.agg.memory.message_finder)
        self.assertEqual({}, self.agg.memory.sequence_finder)
        self.assertEqual({}, self.agg.memory.message_to_sequence)

    def test_handle_sequences(self):
        self.agg.handle(self.seq)
        self.assertEqual(self.agg.memory.sequence_finder[0], self.seq)
        self.assertListEqual(
            sorted([self.m0, self.m1]),
            sorted(self.sim.queue.queue.queue)
        )

    def test_error_double_sequence(self):
        with self.assertRaises(KeyError):
            self.agg.handle(self.seq)
            self.agg.handle(self.seq)

class TestComplexSequenceManagement(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()
        self.agg = MessageAggregator()
        self.m0 = Message(self.sim, 1, 'han0', 'cmd')
        self.m1 = Message(self.sim, 2, 'han1', 'cmd')
        self.m2 = Message(self.sim, 3, 'han2', 'cmd', preqs=[self.m0, self.m1])
        adj_list1 = {
            self.m0: [self.m2],
            self.m1: [self.m2],
            self.m2: []
        }
        self.seq1 = Sequence(
            DirectedGraph().from_adjacency_list(adj_list1)
        )
        self.m3 = Message(self.sim, 1, 'han0', 'cmd')
        self.m4 = Message(self.sim, 2, 'han1', 'cmd', preqs=[self.m3])
        adj_list2 = {
            self.m3: [self.m4],
            self.m4: []
        }
        self.seq1 = Sequence(DirectedGraph())
        self.seq1.graph.from_adjacency_list(adj_list1)
        self.seq2 = Sequence(DirectedGraph())
        self.seq2.graph.from_adjacency_list(adj_list2)

    def test_two_sequence_case(self):
        self.agg.handle(self.seq1)
        self.agg.handle(self.seq2)
        self.m0.state = Message.DONE
        self.agg.handle(self.m0)
        self.m3.state = Message.DONE
        self.agg.handle(self.m3)
        self.m1.state = Message.DONE
        self.agg.handle(self.m1)
        self.m2.state = Message.DONE
        self.agg.handle(self.m2)
        self.assertEqual(self.m4.state, Message.READY)
        self.assertEqual(False, self.agg.memory.exists_message(self.m2))

if __name__ == '__main__':
    unittest.main()