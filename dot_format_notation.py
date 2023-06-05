import pygraphviz as pgv

def printGraph(graph, highlight_edges=None):
    # Create a new PyGraphviz graph
    dot_graph = pgv.AGraph(directed=graph.is_directed())

    # Add vertices to the graph
    for vertex in graph.vertices:
        dot_graph.add_node(vertex)

    # Add edges to the graph
    for source, edges in graph.edges.items():
        for target, weight in edges:
            edge_attrs = {}
            if highlight_edges is not None and (source, target) in highlight_edges:
                edge_attrs['color'] = 'red'  # Highlight the edge in red
            dot_graph.add_edge(source, target, label=str(weight), **edge_attrs)

    # Render the graph to a file or display it
    dot_graph.draw('graph.png', prog='dot')  # Save the graph as an image file
    # dot_graph.draw(prog='dot')  # Display the graph

# Example usage:
class Graph:
    def __init__(self, is_directed=False):
        self.vertices = set()
        self.edges = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, source, target, weight):
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append((target, weight))

graph = Graph(is_directed=False)
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B', 3)
graph.add_edge('B', 'C', 2)
graph.add_edge('C', 'A', 5)
graph.add_edge('A', 'D', 4)

highlight_edges = [('A', 'B'), ('B', 'C')]  # Example highlighting MST or Shortest Path edges
printGraph(graph, highlight_edges)
