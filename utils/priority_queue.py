import heapq
from itertools import count

class PriorityQueue(object):
    def __init__(self):
        self._heap = []
        self.entry_finder = {}
        self.counter = count()

    def push(self, priority, item):
        count = next(self.counter)
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heapq.heappush(self._heap, entry)

    def pop(self):
        if self._heap:
            priority, count, item = heapq.heappop(self._heap)
            del self.entry_finder[item]
            return item
        raise KeyError('pop from an empty priority queue')

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except IndexError or KeyError:
            raise StopIteration

if __name__ == "__main__":
    l = PriorityQueue()
    l.push(10, 'last')
    l.push(1, 'first')
    l.push(5, 'middol')
    for x in l:
        print(x)
    print(len(l))