import math

class PriorityQueue2:
    """
    Takes in Node
    """
    queue = []
    def put(self, node):
        self.queue.append({node.weight : node.name})
    
    def get(self):
        smallest_weight = math.inf
        smallest_name = "Error"
        # find the smallest weight
        for item in self.queue:
            current_weight = int(list(item.keys())[0])
            current_name = str(list(item.values())[0])
            if  current_weight < smallest_weight:
                smallest_weight = current_weight

        # find the name of the element with the smallest weight
        for item in self.queue:
            if ( int(list(item.keys())[0]) == int(smallest_weight)):
                smallest_name = str(list(item.values())[0])
        
        # remove the popped element from the queue
        self.queue.remove({smallest_weight : smallest_name})

        smallest_node = (smallest_weight, smallest_name)
        return smallest_node

    def isEmpty(self):
        return True if self.queue == [] else False

    def __repr__(self):
        return_statement = "Name : Weight...\n"
        for item in self.queue:
            weight = str(int(list(item.keys())[0]))
            name = str(list(item.values())[0])
            return_statement += (name + ' : ' + weight + ', ')
        return_statement += '\n'
        return return_statement

# need to have a path that we can add to
class Node:
    """
    A path contains the source node and all of the children
    """
    # a path has a list of children and the root node
    path = {}
    total_weight = 0

    def __init__(self, name, parent, weight):
        self.name = name 
        self.parent = parent
        self.weight = weight 
    def __repr__(self):
        result = str(self.name) + str(self.parent) 


class Path:
    """
    A path is a list of elements in order that were added
    """
    path = []
    total_dist = 0
    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        self.total_dist += node.weight
        self.path.append((node.name, node.weight, node.parent))
    
    def __repr__(self):
        if self.path == []:
            result = 'none'
        else:
            result = ''
            result += 'distance:' + str(self.total_dist) + '\n'
            result += 'route:\n'
            for item in self.path:
                name, parent, weight = item
                result += str(parent) + ' to ' + str(name) + ', ' + str(weight) + ' km'
        return result