class Graph:
    def __init__(self):
        self.graph = {}

    # Undirected weighted graph using an adjacency list.
    def add_edge(self, Vertex_u, Vertex_v, nodes_weight):
        if Vertex_u not in self.graph:
            self.graph[Vertex_u] = []
        if Vertex_v not in self.graph:
            self.graph[Vertex_v] = []

        self.graph[Vertex_u].append((Vertex_v, nodes_weight))
        self.graph[Vertex_v].append((Vertex_u, nodes_weight))


# The Prim algorithm for computing the Minimum Spanning Tree of a graph

import heapq
def prim(graph):
    # Picking the starting vertex
    start_vertex = list(graph.keys())[0]

    # Begin by setting up the minimum spanning tree and marking the visited vertices.
    minimum_spanning_tree = []
    visited = {start_vertex}

    # Create a heap to store the edges and their weights
    edges = [(edges_weight, start_vertex, neighbor) for neighbor, edges_weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        # Pop the edge with the minimum weight
        edges_weight, Vertex_u, Vertex_v = heapq.heappop(edges)

        if Vertex_v not in visited:
            # Add the edge to the minimum spanning tree
            minimum_spanning_tree.append((Vertex_u, Vertex_v, edges_weight))
            visited.add(Vertex_v)

            # Add the adjacent edges of Vertex_v to the heap
            for neighbor, edges_weight in graph[Vertex_v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edges_weight, Vertex_v, neighbor))

    return minimum_spanning_tree


# Minimum Spanning Tree of a graph.
graph = Graph()
graph.add_edge('K10', 'K20', 4)
graph.add_edge('K10', 'K30', 8)
graph.add_edge('K20', 'K30', 2)
graph.add_edge('K20', 'K40', 5)
graph.add_edge('K30', 'K40', 1)
graph.add_edge('K30', 'K50', 6)
graph.add_edge('K40', 'K50', 3)
graph.add_edge('K40', 'K60', 4)
graph.add_edge('K50', 'K60', 2)

# The Minimum Spanning Tree using Prim's algorithm
minimum_spanning_tree = prim(graph.graph)

# Print Minimum Spanning Tree using Prim's algorithm
for edge in minimum_spanning_tree:
    Vertex_u, Vertex_v, weight = edge
    print(f"{Vertex_u} -- {Vertex_v}: {weight}")