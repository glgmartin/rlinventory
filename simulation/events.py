class Event(object):
    def __init__(self, sim, time):
        self.sim = sim
        self.time = time

    def execute(self):
        print('This method should be over-ridden!')

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f'Event ({self.time})'

class PriorityEvent(Event):
    def __init__(self, sim, time, priority=9):
        Event.__init__(self, sim, time)
        self.priority = priority

    def __lt__(self, other):
        if self.time == other.time:
            return self.priority < other.priority
        else:
            return self.time < other.time

    def __repr__(self):
        return f'Priority event ({self.time}, {self.priority})'

if __name__ == "__main__":
    e1 = Event('e', 1)
    e2 = Event('e', 2)
    print(e1 < e2)
    p1 = PriorityEvent('e', 1.0, priority=1)
    p2 = PriorityEvent('e', 1.0, priority=2)
    print(p1 < p2)
