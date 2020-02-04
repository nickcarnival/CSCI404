import math

class Tree:
    """
    A tree is an arangement of nodes and edges 
    """
    # a tree must be initialized with a parent node
    def __init__(self, source):
        self.source = source
    
    # adding a node will 
    def add_node(self, node):


# each node needs to know it's parent
class Node:
    # every node has a list of adjacencies
    # adjacencies are other nodes
    # leaf nodes may have no adjacencies
    adjacencies = []
    smallest_weight = math.inf

    def __init__(self, parent, adjacencies):
        self.adjacencies.append(adjacencies)
        self.parent = parent
    def add_edge(self, adj):
        self.adj.append(adj)
    def cheapest_child(self):
        for item in self.adjacencies:
            if item.weight

class Edge:
    """
    An edge is a weighted path from a parent node to a child node
    self is the child
    """
    def __init__(self,child, parent, weight):
        self.parent = parent
        self.child = child 
        self.weight = weight