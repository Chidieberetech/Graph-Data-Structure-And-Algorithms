# define the Graph class before using it
class Graph:
    def __init__(self):
        self.nodes = {}

    # Function to add the vertices
    def add_node(self, mark):
        if mark not in self.nodes:
            self.nodes[mark] = Vertex(mark)

    # Function to add the edges
    def add_edge(self, source, target, weight):
        if source in self.nodes and target in self.nodes:
            self.nodes[source].add_edge(target, weight)

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def add_edge(self, target, weight):
        self.edges.append((target, weight))

def printGraph(graph, highlighted_edges=None):
    # Start the dot graph representation
    dot_graph = "Graph using the dot format notation {\n"

    # Iterate over the nodes and their edges
    for node in graph.nodes.values():
        # Include the nodes to the dot graph
        dot_graph += f"  {node.id};\n"

        # Iterate over the edges of the node
        for target, weight in node.edges:
            # Check whether the edge is part of the highlighted edges
            if highlighted_edges and (node.id, target) in highlighted_edges:
                # Add the edge with a different color
                dot_graph += f"  {node.id} -- {target} [color=green, label={weight}];\n"
            else:
                # Add the edge with the designated color
                dot_graph += f"  {node.id} -- {target} [label={weight}];\n"

    # Close the dot graph representation
    dot_graph += "}\n"

    # Print the dot graph
    print(dot_graph)


# Example usage:
graph = Graph()

# Add nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

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
