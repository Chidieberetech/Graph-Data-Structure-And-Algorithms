import self as self


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

    # The minimum spanning tree and marking the visited vertices.
    minimum_spanning_tree = []
    visited = {start_vertex}

    # A min_heap to store the edges and their respective weights
    edges = [(edges_weight, start_vertex, neighbor) for neighbor, edges_weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        # The edge with the minimum weight
        edges_weight, Vertex_u, Vertex_v = heapq.heappop(edges)

        if Vertex_v not in visited:
            # Including the edge to the minimum spanning tree
            minimum_spanning_tree.append((Vertex_u, Vertex_v, edges_weight))
            visited.add(Vertex_v)

            # Including the adjacent edges of Vertex_v to the min_heap
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

# Implement a binary Min Heap that will act as the value queue for Prim.
    class MinHeap:
        def __init__(self):
            self.min_heap = [0]*80
            self.size = 0
# A function that return the parent node index of a given node.
        def parent(self, index):
            return (index - 1) // 2
# A function that return left child index of node.
        def left_child(self, index):
            return (2 * index) + 1

        # A function that return right child index of node.
        def right_child(self, index):
            return (2 * index) + 2
# A function that hold the  heap characteristics
        # Switch the parent and main node
        def swap(self, i, j):
            self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]

# A function that hold the  heap characteristics by pushing up the node
        def heapify_up(self, index):
            while index > 0 and self.min_heap[index][0] < self.min_heap[self.parent(index)][0]:

                parent_index = self.parent(index)
                self.swap(index, parent_index)
                # Update the Parent index
                index = parent_index

# A function that hold the heap characteristics by pushing down the node
        def heapify_down(self, index):
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < self.size and self.min_heap[left][0] < self.min_heap[smallest][0]:
                smallest = left

            if right < self.size and self.min_heap[right][0] < self.min_heap[smallest][0]:
                smallest = right
            # If index not same as smallestIndex
            if smallest != index:
                self.swap(index, smallest)
                self.heapify_down(smallest)

# Function that insert the new factor into the Binary Heap
        def insert(self, key, value):
            self.min_heap.append((key, value))
            self.size += 1
            self.heapify_up(self.size - 1)
# Function to extract the Key with minimum value
        def extract_min(self):
            if self.size == 0:
                return None
# Change the value at the root with the last leaf
            min_value = self.min_heap[0]
            self.min_heap[0] = self.min_heap[self.size - 1]
            self.min_heap.pop()
            self.size -= 1
            self.heapify_down(0)

            return min_value

# Function to change the value of a Key

        def change_priority(self, key, value):
            for i in range(self.size):
                if self.min_heap[i][1] == key:
                    self.min_heap[i] = (value, self.min_heap[i][1])
                    if self.has_parent(i) and self.min_heap[i][0] < self.min_heap[self.parent(i)][0]:
                        self.heapify_up(i)
                    else:
                        self.heapify_down(i)
                    break

# Create an instance of MinHeap
        class MinHeap:
            max_key, max_value = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.heap.pop()
            self.heapify_down(0)

            return max_key, max_value

        # Example usage of MaxHeap
        max_heap = MaxHeap()
        max_heap.insert(5, "A")
        max_heap.insert(2, "B")
        max_heap.insert(8, "C")

        print("MaxHeap:")
        while max_heap.size > 0:
            key, value = max_heap.extract_max()
            print(f"Key: {key}, Value: {value}")
        def is_empty(self):
            return self.size == 0

