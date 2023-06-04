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
    edges = [(nodes_weight, start_vertex, neighbor) for neighbor, nodes_weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        # Pop the edge with the minimum nodes_weight
        nodes_weight, Vertex_u, Vertex_v = heapq.heappop(edges)

        if Vertex_v not in visited:
            # Add the edge to the minimum spanning tree
            minimum_spanning_tree.append((Vertex_u, Vertex_v, nodes_weight))
            visited.add(Vertex_v)

            # Add the adjacent edges of Vertex_v to the heap
            for neighbor, nodes_weight in graph[Vertex_v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (nodes_weight, Vertex_v, neighbor))

    return minimum_spanning_tree


# Create a graph
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 8)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 6)
graph.add_edge('D', 'E', 3)
graph.add_edge('D', 'F', 4)
graph.add_edge('E', 'F', 2)

# Compute the MST using Prim's algorithm
minimum_spanning_tree = prim(graph.graph)

# Print the minimum spanning tree
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f"{u} -- {v}: {weight}")