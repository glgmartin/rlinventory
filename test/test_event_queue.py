import unittest
from utils.priority_queue import EventQueue

class TestEventQueue(unittest.TestCase):
    def test_simple_push(self):
        e0 = 1
        e1 = 2
        q = EventQueue()
        q.push(e0)
        q.push(e1)
        self.assertEqual(e0, q.pop())

    def test_complex_push(self):
        from simulation.messages import Message
        m0 = Message(sim=None, time=0, priority=9)
        m1 = Message(sim=None, time=1, priority=9)
        m2 = Message(sim=None, time=1, priority=0)
        q = EventQueue()
        q.push(m0)
        q.push(m1)
        q.push(m2)
        self.assertEqual(m0, q.pop())
        self.assertEqual(m2, q.pop())

if __name__ == '__main__':
    unittest.main()