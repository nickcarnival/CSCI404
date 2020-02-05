class Graph(object):
    def __init__(self, graph):
        self.edges = {}
        self.weights = {}
        self.__graph = graph
        
    def nodes(self):
        return list(self.__graph.keys())
    
    def neighbors(self):
        return self.__find_neighbors()
    
    def add_node(self,node):
        if node not in self.__graph:
            self.__graph_dict[node] = []
    
    def add_neighbor(self, neighbor):
        neighbor = set(neighbor)
        (node1, node2) = tuple(neighbor)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]
            
    def __find_neighbors(self):
        neighbors = []
        for node in self.__graph:
            for neighbor in self.__graph[node]:
                if {neighbor, node} not in neighbors:
                    neighbors.append({node, neighbor})
        return neighbors
    
    def __str__(self):
        response = "Nodes: "
        for n in self.__graph:
            response += str(n) + " "
            response += "\nneighbors: "
            for neighbor in self.__find_neighbors():
                reponse += str(neighbor) + " "
            return response
        
# g = Graph(FileName)
# print(g.nodes())
