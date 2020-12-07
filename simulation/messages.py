from .events import PriorityEvent

class Message(PriorityEvent):

    PENDING = 0
    READY = 1
    DONE = 2

    def __init__(self, sim, time, handler=None, cmd=None, priority=9, 
        state=PENDING, preqs=[]):
        PriorityEvent.__init__(self, sim, time, priority)
        self.handler = handler
        self.cmd = cmd
        self.state = state
        self.preqs = preqs

    def execute(self):
        if self.handler is not None and self.cmd is not None:
            self.handler.handle(self)

    def is_ready(self):
        if self.preqs == []:
            return True
        else:
            return all([message.state == Message.DONE for message in \
                self.preqs])

if __name__ == '__main__':
    msg = Message('e', 5, 'h', 'do')
    print(msg.state, msg.is_ready())
