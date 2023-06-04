import math


class GraphTemplate(object):
    _nodes = []  # ! list of NodeTemplate ONLY
    _minPriorityQueue = []  # ! list of NodeTemplate ONLY

    def __init__(self):
        pass

    # Implement additional constructors.
    class Graph:
        def __init__(self):
            self.adjacency_list = {}

        # Implement method for adding a node
        def add_vertex(self, vertex):
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = []

        def add_edge(self, First_vertex, Second_vertex):
            if First_vertex in self.adjacency_list and Second_vertex in self.adjacency_list:
                self.adjacency_list[First_vertex].append(Second_vertex)
                self.adjacency_list[Second_vertex].append(First_vertex)

        # Implement method for removing a node
        def remove_vertex(self, vertex):
            if vertex in self.adjacency_list:
                del self.adjacency_list[vertex]
                for vertices in self.adjacency_list.values():
                    if vertex in vertices:
                        vertices.remove(vertex)

        def remove_edge(self, First_vertex, Second_vertex):
            if First_vertex in self.adjacency_list and Second_vertex in self.adjacency_list:
                if Second_vertex in self.adjacency_list[First_vertex]:
                    self.adjacency_list[First_vertex].remove(Second_vertex)
                if First_vertex in self.adjacency_list[Second_vertex]:
                    self.adjacency_list[Second_vertex].remove(First_vertex)

        def get_vertices(self):
            return list(self.adjacency_list.keys())

        def get_edges(self):
            edges = []
            for vertex, vertices in self.adjacency_list.items():
                for v in vertices:
                    if (vertex, v) not in edges and (v, vertex) not in edges:
                        edges.append((vertex, v))
            return edges

        def is_adjacent(self, First_vertex, Second_vertex):
            if First_vertex in self.adjacency_list and Second_vertex in self.adjacency_list:
                return Second_vertex in self.adjacency_list[First_vertex]
            return False

    # Output

    graph = Graph()
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_vertex("L")
    graph.add_edge("G", "H")
    graph.add_edge("H", "L")
    graph.add_edge("L", "G")

    print("Implementing additional constructors")
    print(graph.get_vertices())
    print(graph.get_edges())
    print(graph.is_adjacent("G", "H"))
    print(graph.is_adjacent("G", "L"))
    print(graph.is_adjacent("H", "L"))

    graph.remove_edge("G", "H")
    print(graph.get_edges())

    graph.remove_vertex("L")
    print(graph.get_vertices())
    print(graph.get_edges())

    # Implement method for sorting the min-priority Queue

    class NodeTemplate:
        def __init__(self, name, priority, properties=None):
            self.name = name
            self.priority = priority
            self.properties = properties or {}

        def set_property(self, key, value):
            self.properties[key] = value

        def get_property(self, key):
            return self.properties.get(key)

        def remove_property(self, key):
            if key in self.properties:
                del self.properties[key]

        @staticmethod
        def sort_priority_queue(queue):
            queue.sort(key=lambda node: node.priority)

        # Implement method for extracting an element from the min-priority Queue
        def extract_min_priority(queue):
            if not queue:
                return None
            min_node = min(queue, key=lambda node: node.priority)
            queue.remove(min_node)
            return min_node

    # Printing the Graph
    print("Implementing sorting the min-priority Queue")
    # Creating node templates
    VertexK20 = NodeTemplate("Vertex K20", 5)
    VertexK30 = NodeTemplate("Vertex K30", 3)
    VertexK40 = NodeTemplate("Vertex K40", 7)

    # Creating a priority queue
    priority_queue = [VertexK20, VertexK30, VertexK40]

    # Sorting the priority queue
    NodeTemplate.sort_priority_queue(priority_queue)

    # Printing the sorted priority queue
    for node in priority_queue:
        print(f"Name: {node.name}, Priority: {node.priority}")

    # Implement method for extracting an element from the min-priority Queue
    print("Extracting an element from the min-priority Queue")
    # Extracting an element from the min-priority Queue
    min_node = NodeTemplate.extract_min_priority(priority_queue)
    if min_node:
        print(f"Name: {min_node.name}, Priority: {min_node.priority}")
    else:
        print("Priority queue is empty")

    # TODO: implement Dijkstra (in another class)


import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1][vertex2] = weight
            self.adjacency_list[vertex2][vertex1] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Example usage:

graph = Graph()
graph.add_vertex("K10")
graph.add_vertex("K20")
graph.add_vertex("K30")
graph.add_vertex("K40")
graph.add_vertex("K50")
graph.add_edge("K10", "K20", 4)
graph.add_edge("K10", "K30", 2)
graph.add_edge("K30", "K40", 2)
graph.add_edge("K30", "K20", 1)
graph.add_edge("K20", "K50", 3)
graph.add_edge("K40", "K50", 3)

start_vertex = "K10"
distances = graph.dijkstra(start_vertex)

print(f"Shortest distances from each vertex {start_vertex}:")
for vertex, distance in distances.items():
    print(f"To vertex {vertex}: {distance}")


class NodeTemplate(object):
    class NodeTemplate:
        def __init__(self, label):
            self.label = label  # ! string
            self.adjacentNodes = {}  # ! dict of pairs (NodeTemplate : integer)
            self.parent = None  # ! reference to NodeTemplate
            self.distance = math.inf  # ! number (float)

        # Implement additional constructors
        def __str__(self):
            return str(self.label)

        # Implement method for adding a connection
        def add_edge(self, node, weight):
            self.adjacentNodes[node] = weight

        # Implement method for removing a connection
        def remove_edge(self, node):

            if node in self.adjacentNodes:
                del self.adjacentNodes[node]
## Return neighbor node
        def get_neighbors(self):

            return list(self.adjacentNodes.keys())

        def get_weight(self, node):

            return self.adjacentNodes[node]

        # Implement methods for manipulating the parent and distance
        def set_parent(self, parent):

            self.parent = parent

        def set_distance(self, distance):

            self.distance = distance

        def get_distance(self):

            return self.distance

        def add_connection(self, node, weight):
            self.add_edge(node, weight)
            node.add_edge(self, weight)

