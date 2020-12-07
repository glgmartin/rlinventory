import unittest
from simulation.events import PriorityEvent

class TestPriorityEvent(unittest.TestCase):
    def test_ordering(self):
        e0 = PriorityEvent(None, 0, 9)
        e1 = PriorityEvent(None, 1, 9)
        e2 = PriorityEvent(None, 1, 0)
        self.assertLess(e0, e1)
        self.assertLess(e2, e1)

if __name__ == '__main__':
    unittest.main()    
        