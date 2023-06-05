# define the Graph class before using it
class Graph:
    def __init__(self):
        self.nodes = {}

    # Function to add the vertices
    def add_node(self, mark):
        if mark not in self.nodes:
            self.nodes[mark] = Node(mark)

    # Function to add the edges
    def add_edge(self, source, target, weight):
        if source in self.nodes and target in self.nodes:
            self.nodes[source].add_edge(target, weight)

class Node:
    def __init__(self, mark):
        self.id = mark
        self.edges = []

    def add_edge(self, target, weight):
        self.edges.append((target, weight))

def printGraph(graph, highlighted_edges=None):
    # Start the dot graph representation
    dot_graph = "Graph using the dot format notation {\n"

    # Iterate over the nodes and their edges
    for node in graph.nodes.values():
        # Include the nodes to the dot graph
        dot_graph += f" For Vertex {node.id};\n"

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



graph = Graph()

# Add nodes
graph.add_node("K10")
graph.add_node("K20")
graph.add_node("K30")
graph.add_node("K40")

# Add edges
graph.add_edge("K10", "K20", 4)
graph.add_edge("K10", "K30", 2)
graph.add_edge("K20", "K30", 1)
graph.add_edge("K20", "K40", 5)
graph.add_edge("K30", "K40", 8)

# Define highlighted edges (Minimum Spanning Tree or the
# Shortest Path.)
highlighted_edges = {("K10", "K20"), ("K20", "K30"), ("K30", "K40")}

# Print the graph with highlighted edges
printGraph(graph, highlighted_edges)
