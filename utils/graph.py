class Edge(object):
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f'{self.u} -> {self.v}'

class DirectedGraph(object):
    def __init__(self):
        self.vertices = []
        self.edges = [[] for vertex in self.vertices]
        self.parents: Dict[int, List[V]] = {self.vertices.index(vertex): [] for vertex in self.vertices}
    
    @property
    def vertex_count(self):
        return len(self.vertices)
    
    @property
    def edge_count(self):
        return sum(map(len, self.edges))

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.edges.append([])
        self.parents[self.index_of(vertex)]: List[V] = []
        return self.vertex_count - 1

    def add_edge(self, edge):
        self.edges[edge.u].append(edge)
        self.parents[edge.v].append(edge.u)

    def add_edge_by_indices(self, u, v):
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second):
        u: int = self.vertices.index(first)
        v: int = self.vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index):
        return self.vertices[index]

    def index_of(self, vertex):
        return self.vertices.index(vertex)

    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self.edges[index]]))

    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index):
        return self.edges[index]

    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    def parents_for_index(self, index):
        return self.parents[index]

    def parents_for_vertex(self, vertex):
        return self.parents[self.index_of(vertex)]

    def find_sources(self):
        sources = []
        for vertex in self.vertices:
            if self.parents_for_vertex(vertex) == []:
                sources.append(vertex)
        return sources

    def from_adjacency_list(self, adj_list):
        for vertex, adj in adj_list.items():
            if vertex not in self.vertices:
                self.add_vertex(vertex)
            for v in adj:
                if v not in self.vertices:
                    self.add_vertex(v)
                self.add_edge_by_vertices(vertex, v)

    def __str__(self):
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc
