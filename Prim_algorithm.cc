#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Structure to represent an edge in the graph
struct Edge {
    int src, dest, weight;
};

// Structure to represent a node in the adjacency list
struct Node {
    int vertex, weight;
};

class Graph {
private:
    vector<vector<Node>> adjacencyList; // Adjacency list to store the graph
    int numVertices;

public:
    Graph(int numVertices) {
        this->numVertices = numVertices;
        adjacencyList.resize(numVertices);
    }

    void addEdge(int src, int dest, int weight) {
        Node node;
        node.vertex = dest;
        node.weight = weight;
        adjacencyList[src].push_back(node);

        node.vertex = src; // For undirected graph
        adjacencyList[dest].push_back(node);
    }

    void primMST() {
        priority_queue<Node, vector<Node>, greater<Node>> pq; // Priority queue to store nodes
        vector<bool> visited(numVertices, false); // Keep track of visited nodes
        int src = 0; // Start with the first vertex as the source

        // Create a vector to store the MST
        vector<Edge> MST;

        // Mark the source node as visited and push it into the priority queue
        visited[src] = true;
        for (const auto& node : adjacencyList[src]) {
            pq.push(node);
        }

        while (!pq.empty()) {
            Node current = pq.top();
            pq.pop();

            int currentVertex = current.vertex;
            if (visited[currentVertex])
                continue;

            visited[currentVertex] = true;

            Edge edge;
            edge.src = currentVertex;
            edge.dest = current.weight;
            edge.weight = current.weight;
            MST.push_back(edge);

            // Add the adjacent nodes of the current node to the priority queue
            for (const auto& node : adjacencyList[currentVertex]) {
                pq.push(node);
            }
        }

        // Print the Minimum Spanning Tree
        cout << "Minimum Spanning Tree:" << endl;
        for (const auto& edge : MST) {
            cout << edge.src << " -- " << edge.dest << " with weight " << edge.weight << endl;
        }
    }
};

int main() {
    // Create a graph with 6 vertices
    Graph graph(6);

    // Add edges to the graph
    graph.addEdge(0, 1, 4);
    graph.addEdge(0, 2, 3);
    graph.addEdge(1, 2, 1);
    graph.addEdge(1, 3, 2);
    graph.addEdge(2, 3, 4);
    graph.addEdge(3, 4, 2);
    graph.addEdge(4, 5, 6);

    // Find and print the Minimum Spanning Tree.
    graph.primMST();

    return 0;
}
