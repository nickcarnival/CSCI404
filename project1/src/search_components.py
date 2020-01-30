
class Node:
    """
    Node contains the name of the current node, the nullable parent node, and all of the edges
    """
    def __init__(self, name, edges, parent):
        self.name = name
        self.edges = edges
        self.parent = parent
    # adds an edge to the node
    def add_adj(self, adj):
        self.edges.append(adj)

class Edge:
    """ 
    Edge contains the weight of the edge and the child node
    """
    def __init__(self, weight, node):
        self.weight = weight
        self.node = node