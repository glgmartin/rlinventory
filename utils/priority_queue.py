from queue import PriorityQueue

class EventQueue(object):
    def __init__(self):
        self.queue = PriorityQueue()

    def push(self, element):
        self.queue.put(element)

    def pop(self):
        return self.queue.get()

    def remove(self, element):
        for i in range(self.size()):
            if self.queue.queue[i] == element:
                x = self.queue.queue[i]
                self.queue.queue.remove(x)
                return x
        return None

    def has_more(self):
        return self.size() > 0

    def size(self):
        return self.queue.qsize()