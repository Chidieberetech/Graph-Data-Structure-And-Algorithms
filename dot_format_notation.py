class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertex(id)

    def add_edge(self, source, target, weight):
        if source in self.vertices and target in self.vertices:
            self.vertices[source].add_edge(target, weight)


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def add_edge(self, target, weight):
        self.edges.append((target, weight))


def printGraph(graph, highlighted_edges=None):
    # Start the dot graph representation
    dot_graph = "graph {\n"

    # Iterate over the vertices and their edges
    for vertex in graph.vertices.values():
        # Add the vertex to the dot graph
        dot_graph += f"  {vertex.id};\n"

        # Iterate over the edges of the vertex
        for target, weight in vertex.edges:
            # Check if the edge is part of the highlighted edges
            if highlighted_edges and (vertex.id, target) in highlighted_edges:
                # Add the edge with a different color
                dot_graph += f"  {vertex.id} -- {target} [color=red, label={weight}];\n"
            else:
                # Add the edge with the default color
                dot_graph += f"  {vertex.id} -- {target} [label={weight}];\n"

    # Close the dot graph representation
    dot_graph += "}\n"

    # Print the dot graph
    print(dot_graph)

# Example usage:
graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Add edges
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)

# Define highlighted edges (e.g., MST or shortest path)
highlighted_edges = {("A", "B"), ("B", "C"), ("C", "D")}

# Print the graph with highlighted edges
printGraph(graph, highlighted_edges)
