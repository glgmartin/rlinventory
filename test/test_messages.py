import unittest
from simulation.messages import Message

class TestStartMessage(unittest.TestCase):
    def setUp(self):
        self.m0 = Message(sim=None, time=0, priority=9)
        self.m1 = Message(sim=None, time=1, priority=9)
        self.m2 = Message(sim=None, time=2, priority=0,
            preqs=[self.m0, self.m1])

    def test_is_pending_start(self):
        self.assertEqual(Message.PENDING, self.m0.state)
        self.assertEqual(Message.PENDING, self.m2.state)

    def test_is_ready_start(self):
        self.assertEqual(self.m0.is_ready(), 1)
        self.assertEqual(self.m1.is_ready(), 1)
        self.assertEqual(self.m2.is_ready(), 0)

class TestUpdatedMessage(unittest.TestCase):
    def setUp(self):
        self.m0 = Message(sim=None, time=0, priority=9)
        self.m1 = Message(sim=None, time=1, priority=9)
        self.m2 = Message(sim=None, time=2, priority=0,
            preqs=[self.m0, self.m1])
        self.m0.state = Message.READY

    def test_is_pending(self):
        self.assertEqual(Message.PENDING, self.m2.state)

    def test_is_ready(self):
        self.assertEqual(self.m2.is_ready(), 0)

class TestFinishedMessage(unittest.TestCase):
    def setUp(self):
        self.m0 = Message(sim=None, time=0, priority=9)
        self.m1 = Message(sim=None, time=1, priority=9)
        self.m2 = Message(sim=None, time=2, priority=0,
            preqs=[self.m0, self.m1])
        self.m0.state = Message.DONE
        self.m1.state = Message.DONE

    def test_is_ready(self):
        self.assertEqual(self.m2.is_ready(), 1)

class TestCloning(unittest.TestCase):
    def setUp(self):
        self.m0 = Message('sim', 1, 'han', 'cmd')
        self.m1 = Message('sim', 1, 'han', 'cmd', preqs=[self.m0])

    def test_clone(self):
        m_clone = self.m1.clone()
        self.assertEqual(m_clone.preqs, [])
        self.assertEqual(m_clone.state, Message.PENDING)

if __name__ == '__main__':
    unittest.main()