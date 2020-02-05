import math

class Tree:
    """
    A tree is an arangement of nodes and edges 
    """
    # a tree must be initialized with a parent node
    nodes = []
    def __init__(self, root, directed=False):
        self._directed = directed
        self.root = root 
    
    def add(self, node):
        self.nodes.append(node)

    def get_node(self, node):
        result = Node('temp')
        for item in self.nodes:
            if item.name == node.name:
                result = item
        if result.name == 'temp':
            result = 'Tree does not contain: ' + node.name
        return result

    # just prints self information
    def __repr__(self):
        result = "Tree:\n"
        for item in self.nodes:
            result += str(item.name) + ''
        return result

# each node needs to know it's parent
class Node:
    """
    Represents a node with a name,. adjacencies, and a parent
    -Adjacencies is a list of Edges
    -Name is a String
    -Parent is a String
    """
    smallest_weight = math.inf

    def __init__(self, name, adjacencies=[], parent=None):
        self.name = name
        self.adjacencies = adjacencies
        self.parent = parent

    def add_children(self, children):
        for child in children:
            self.adjacencies.append(child) 
    def __repr__(self):
        result = '\n' + str(self.name).upper() + '\n' + 'Children: \n'
        if self.adjacencies != []:
            for edge in self.adjacencies:
                result += '-' + str(edge.child) + ' : ' + str(edge.weight) + '\n'
                if self.parent != None:
                    result += self.parent.name
        else:
            result += '-None'
        result += '\n'
        return result
    
    def print_adj(self):
        result = ''
        for adj in self.adjacencies:
            print(adj)
        return result

class Edge:
    """
    An edge is a weighted path from a parent node to a child node
    self is the child
    """
    def __init__(self, child, parent, weight):
        self.parent = parent
        self.child = child 
        self.weight = weight

    # parent is of type Node
    def __repr__(self):
        result = str(self.parent.name) + ' => ' + str(self.child) + ' : ' + str(self.weight) + '\n'
        return result
        