from .events import Event, PriorityEvent
from .messages import Message
from.sequence import Sequence
from .sequence_memory import SequenceMemory

class MessageAggregator(object):
    def __init__(self):
        self.memory = SequenceMemory()

    def handle(self, item):
        if type(item) == Message or type(item) == Event or \
            type(item) == PriorityEvent:
            if type(item) == Message:
                if item.state != Message.READY:
                    raise RuntimeError('You are trying to push a message that is not READY')
            self.push(item)
        elif type(item) == Sequence:
            pass
        else:
            raise TypeError('Unknown type to be handled by MessageAggregator!')

    def push(self, e):
        e.sim.push(e)

    def store(self, seq):
        pass

    def delete(self, seq):
        idx = None
        for k, v in self.memory.items():
            if v == seq:
                idx = k
        if idx is not None:
            del self.memory[idx]
        else:
            raise KeyError('No such sequence in memory')

    def __str__(self):
        return 'MessageAggregator object'