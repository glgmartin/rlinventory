from .events import Event, PriorityEvent
from .messages import Message
from .sequence import Sequence
from .sequence_memory import SequenceMemory

class MessageAggregator(object):
    def __init__(self):
        self.memory = SequenceMemory()

    def handle(self, item):
        if type(item) == Event or type(item) == PriorityEvent:
            self.push(item)
        if type(item) == Message:
            message_known = self.memory.exists_message(item)
            message_state = item.state
            #                 | Known         | Unknown         |
            # state = PENDING | Update state  | Error           |
            # state = READY   | Error         | Error           |
            # state = DONE    | Error         | Update sequence |
            if not message_known and message_state == Message.PENDING:
                # normal case for Messages not linked to a sequence
                # stamp the Message as READY and push it
                item.state = Message.READY
                self.push(item)
            elif message_known and message_state == Message.DONE:
                # normal case for known messages that have been handled and are
                # returned as they belong to a sequence
                sequence = self.memory.get_sequence_by_message(item)
                sequence.update()
                if sequence.is_finished():
                    self.delete_sequence(sequence)
            else:
                raise RuntimeError(
                    f"{'Known' if message_known else 'Unknown'} Message in State {message_state} passed to MessageAggregator.")
        elif type(item) == Sequence:
            self.store_sequence(item)
            #update the sequence to push doable messages
            item.update()
        else:
            raise TypeError('Unknown type to be handled by MessageAggregator!')

    def push(self, e):
        e.sim.push(e)

    def store_sequence(self, sequence):
        self.memory.add_sequence(sequence)

    def delete_sequence(self, sequence):
        #delete sequence and all corresponding messages
        self.memory.remove_sequence(sequence)

    def __str__(self):
        return 'MessageAggregator object'