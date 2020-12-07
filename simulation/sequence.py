from simulation.messages import Message

class Sequence(object):
    # a Sequence is a directed graph of Messages
    def __init__(self, graph):
        self.graph = graph
        self.finished = False
        self.frontier = []

    def get_reachable(self, message):
        candidates = []
        if message.state == Message.DONE:
            return self.graph.neighbors_for_vertex(message)
        else:
            return []

    def find_frontier(self):
        frontier = []
        if self.frontier == []:
            candidates = self.graph.find_sources()
        else:
            candidates = self.frontier
        while candidates:
            candidate = candidates.pop()
            if candidate.state != Message.DONE:
                if candidate not in frontier:
                    frontier.append(candidate)
            else:
                candidate_neighbors = self.get_reachable(candidate)
                if candidate_neighbors != []:
                    for cd in candidate_neighbors:
                        if cd not in frontier:
                            candidates.append(cd)
        return frontier

    def is_finished(self):
        return all(
            [message.state == Message.DONE for message in self.graph.vertices]
        )

    def push(self, message):
        message.sim.push(message)

    def update(self):
        self.frontier = self.find_frontier()
        for message in self.frontier:
            if message.state == Message.PENDING and message.is_ready():
                message.state = Message.READY
                self.push(message)

    def __repr__(self):
        return f"Sequence from Graph\n{self.graph}"