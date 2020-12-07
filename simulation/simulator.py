from utils.priority_queue import EventQueue
from .events import PriorityEvent

class Simulator(object):
    def __init__(self, time=0.0, end_time=None):
        self.queue = EventQueue()
        self.time = time
        self.end_time = end_time

        #add end event
        if end_time is not None:
            self.push(PriorityEvent(end_time, 0))

    def push(self, e):
        self.queue.push(e)

    def now(self):
        return self.time

    def do_all_events(self):
        while self.queue.has_more():
            # bug probable
            e = self.queue.pop()
            self.time = e.time
            if self.end_time is not None and self.time >= self.end_time:
                break
            e.execute()
