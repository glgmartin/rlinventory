from simulation.tasks import Task

class Sequence(object):
    # a Sequence is a directed graph of TasksMessages
    def __init__(self, graph):
        self.graph = graph
        self.finished = False
        self.frontier = []

    def get_reachable(self, message):
        candidates = []
        if task.state == Task.DONE:
            return self.graph.neighbors_for_vertex(task)
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
            if candidate.state != Task.DONE:
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
            [task.state == Task.DONE for task in self.graph.vertices]
        )

    def push_task(self, task):
        task.sim.push(task)

    def update(self):
        self.frontier = self.find_frontier()
        for task in self.frontier:
            if task.state == Task.PENDING and task.is_ready():
                task.state = Task.READY
                self.push_task(task)

    def __repr__(self):
        return f"Sequence from Graph\n{self.graph}"