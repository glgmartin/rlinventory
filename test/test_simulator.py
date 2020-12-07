import unittest
from simulation.simulator import Simulator
from simulation.messages import Message

class TestSimulator(unittest.TestCase):
    def test_basic_simulation(self):
        sim = Simulator(end_time=2)
        m0 = Message(sim=sim, time=0, priority=9)
        m1 = Message(sim=sim, time=1, priority=9)
        m2 = Message(sim=sim, time=1, priority=0)
        m3 = Message(sim=sim, time=4, priority=9)
        msgs = [m0, m1, m2, m3]
        for m in msgs:
            sim.push(m)
        sim.do_all_events()
        self.assertGreaterEqual(sim.time, sim.end_time)

if __name__ == '__main__':
    unittest.main()