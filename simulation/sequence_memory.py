from itertools import count

class SequenceMemory(object):
    def __init__(self):
        self.sequence_finder = {}
        self.message_finder = {}
        self.message_to_sequence = {}
        self.sequence_count = count()
        self.message_count = count()

    def add_sequence(self, seq):
        if not seq in self.sequence_finder.values():
            sequence_counter = next(self.sequence_count)
            self.sequence_finder[sequence_counter] = seq
            for message in seq.graph.vertices:
                self.add_message(message, sequence_counter)
        else:
            raise KeyError('Sequence already registered')

    def remove_sequence(self, seq):
        try:
            sequence_key = self.get_sequence_key(seq)
            for message in self.sequence_finder[sequence_key].graph.vertices:
                self.remove_message(message)
            del self.sequence_finder[sequence_key]
        except:
            raise KeyError('Sequence not found')

    def get_sequence_key(self, seq):
        for key, value in self.sequence_finder.items(): 
            if seq == value:
                return key
        raise KeyError('Sequence not found')

    def get_message_key(self, message):
        for key, value in self.message_finder.items(): 
            if message == value:
                return key
        raise KeyError('Message not found')

    def get_sequence(self, seq):
        return self.sequence_finder[self.get_sequence_key(seq)]

    def get_sequence_by_message(self, message):
        message_key = self.get_message_key(message)
        sequence_key = self.message_to_sequence[message_key]
        return self.sequence_finder[sequence_key]

    def exists_message(self, message):
        return message in self.message_finder.values()

    def add_message(self, message, sequence_counter):
        if not message in self.message_finder.values():
            message_counter = next(self.message_count)
            self.message_finder[message_counter] = message
            self.message_to_sequence[message_counter] = sequence_counter
        else:
            raise KeyError('Message already registered')

    def remove_message(self, message):
        try:
            message_key = self.get_message_key(message)
            del self.message_to_sequence[message_key]
            del self.message_finder[message_key]
        except:
            raise KeyError('Message not found')


