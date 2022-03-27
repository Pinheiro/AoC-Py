class Graph:
    
    def __init__(self):
        self.nodes = set()
        self.edges = dict()
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, weight):
        self.edges[(fromNode, toNode)] = weight
    
    def getWeight(self, fromNode, toNode):
        if (fromNode, toNode) in self.edges.keys():
            return self.edges[(fromNode, toNode)]
        elif (toNode, fromNode) in self.edges.keys():
            return self.edges[(toNode, fromNode)]
        else:
            return None
    
if __name__ == '__main__':
    g = Graph()
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addEdge("A", "B", 1)
    g.addEdge("A", "C", 2)
    g.addEdge("B", "C", 3)
    print()
    print(sorted(g.nodes))
    print(sorted(g.edges))
    print("('A', 'B'): " + str(g.getWeight('A', 'B')))
    print("('B', 'A'): " + str(g.getWeight('B', 'A')))
    print("('A', 'D'): " + str(g.getWeight('A', 'D')))