import math

class PriorityQueue2:
    queue = []
    def put(self, weight, name):
        self.queue.append({weight : name})
    
    def get(self):
        smallest_weight = math.inf
        # find the smallest weight
        for item in self.queue:
            current_weight = int(list(item.keys())[0])
            current_name = str(list(item.values())[0])
            if  current_weight < smallest_weight:
                smallest_weight = current_weight

        # find the name of the element with the smallest weight
        for item in self.queue:
            if ( int(list(item.keys())[0]) == smallest_weight):
                smallest_name = str(list(item.values())[0])
        
        # remove the popped element from the queue
        self.queue.remove({smallest_weight : smallest_name})

        smallest_node = (smallest_weight, smallest_name)
        return smallest_node
    def __repr__(self):
        return_statement = "Name : Weight...\n"
        for item in self.queue:
            weight = str(int(list(item.keys())[0]))
            name = str(list(item.values())[0])
            return_statement += (name + ' : ' + weight + ', ')
        return_statement += '\n'
        return return_statement
