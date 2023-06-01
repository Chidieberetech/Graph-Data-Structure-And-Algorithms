#include <vector>
#include <string>
#include <map>

class GraphTemplate {
private:
    std::vector<NodeTemplate> nodes;
    std::vector<NodeTemplate> minPriorityQueue;

public:
    GraphTemplate(/* args */);
    ~GraphTemplate();

    // TODO: implement additional constructors
    // TODO: implement method for adding a node
    // TODO: implement method for removing a node
    // TODO: implement method for sorting the min-priority Queue
    // TODO: implement method for extracting an element from the min-priority Queue
    // TODO: implement Djikstra (in another class)
};


class NodeTemplate {
private:
    /* data */
    std::string label;
    std::map<NodeTemplate, int> adjacentNodes;
    NodeTemplate *parent;
    int distance;

public:
    NodeTemplate(/* args */);
    ~NodeTemplate();
    
    // TODO: implement additional constructors
    // TODO: implement method for adding a connection
    // TODO: implement method for removing a connection
    // TODO: implement methods for manipulating the parent and distance
};