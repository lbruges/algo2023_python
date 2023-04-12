# Problem 1 - Depth-first Search
class Node_DFS:
    #complexity: O(V+E) - V: each node, E: vertices connecting a pair of nodes
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array