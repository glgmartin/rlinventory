import unittest
from simulation.sequence import Sequence
from simulation.messages import Message
from simulation.simulator import Simulator
from utils.graph import DirectedGraph

class TestSequenceStart(unittest.TestCase):
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

    def test_get_reachable(self):
        self.assertListEqual(self.seq.get_reachable(self.m0), [])

    def test_frontier_at_start(self):
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m0, self.m1]))

    def test_is_finished(self):
        a = self.seq.is_finished()
        self.assertEqual(False, a)

    def test_update(self):
        self.seq.update()
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m0, self.m1]))
        self.assertEqual(self.m2.state, Message.PENDING)
        self.assertListEqual(
            sorted(self.sim.queue.queue.queue),
            sorted([self.m0, self.m1]))

class TestSequenceMiddle(unittest.TestCase):
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
        #a message has been updated
        self.m0.state = Message.DONE

    def test_get_reachable(self):
        self.assertListEqual(self.seq.get_reachable(self.m0), [self.m2])

    def test_frontier_at_middle(self):
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m2, self.m1]))

    def test_is_finished(self):
        a = self.seq.is_finished()
        self.assertEqual(False, a)

    def test_update(self):
        self.seq.update()
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m2, self.m1]))
        self.assertEqual(self.sim.queue.queue.queue, [self.m1])
        self.assertEqual(self.m2.state, Message.PENDING)

class TestSequenceEnding(unittest.TestCase):
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
        self.m0.state = Message.DONE
        self.m1.state = Message.DONE

    def test_get_reachable(self):
        self.assertListEqual(self.seq.get_reachable(self.m0), [self.m2])

    def test_frontier_at_ending(self):
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m2]))

    def test_is_finished(self):
        a = self.seq.is_finished()
        self.assertEqual(False, a)

    def test_update(self):
        self.seq.update()
        self.assertEqual(
            sorted(self.seq.find_frontier()), 
            sorted([self.m2]))
        self.assertEqual(self.sim.queue.queue.queue, [self.m2])
        self.assertEqual(self.m2.state, Message.READY)

class TestSequenceFinished(unittest.TestCase):
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
        self.m0.state = Message.DONE
        self.m1.state = Message.DONE
        self.m2.state = Message.DONE

    def test_frontier_at_finish(self):
        self.assertEqual(
            sorted(self.seq.find_frontier()), [])

    def test_is_finished(self):
        a = self.seq.is_finished()
        self.assertEqual(True, a)

    def test_update(self):
        self.seq.update()
        self.assertEqual(self.seq.find_frontier(), [])

class TestCloneSequence(unittest.TestCase):
    def setUp(self):
        

if __name__ == '__main__':
    unittest.main()

