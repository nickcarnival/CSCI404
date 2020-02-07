import sys
from queue import PriorityQueue

def main():
    """
    Handles getting the system arguments and calling all of the functions
    """

    if (len(sys.argv) != 4):
        print("Not enough arguments")
        sys.exit()

    file_name = sys.argv[1]

    # Make all cities uppercase
    source = str(sys.argv[2]).upper()
    destination = str(sys.argv[3]).upper()

    # Generate all of the cities
    graph = parse_input(file_name)

    # Find the path from source to destination
    results = find_route(graph, source, destination)

    # Print the path in the expected format
    print_results(graph, results)

def print_results(graph, results):
    """
    print_results takes in a graph and the results
    it then parses those results and prints the weight for each path taken
    """
    if results is not None:
        print("distance: ", results[-1],"km")
        print("route:")
        print_statement = ''

        previous_node = 'EMPTY'

        for current_node in results[:-1]:
            if previous_node != 'EMPTY':
                for connection in graph[current_node]:
                    if connection[0] == previous_node:
                        previous_node = previous_node.lower().capitalize()
                        current_node = current_node.lower().capitalize()
                        print(previous_node, "to ", current_node, ",", connection[1], "km")

            previous_node = current_node.upper()
    else:
        print("distance: infinity")
        print("route:")
        print("none")

def parse_input(file_name):
    """
    Takes in the input file and converts it to the appropriate data structure
    """
    graph = {}

    file = open(file_name, 'r')

    for line in file:
        if 'END OF INPUT' in line:
            return graph
        node1, node2, distance = line.lower().split()

        node1 = node1.upper()
        node2 = node2.upper()

        graph.setdefault(node1, []).append((node2, distance))
        graph.setdefault(node2, []).append((node1, distance))

def find_route(graph, source, destination):
    frontier = set()
    q = PriorityQueue()
    q.put((0, [source]))
    while q.empty() is False:
        cost, route = q.get()
        node = route[len(route) -1]
        if node not in frontier:
            frontier.add(node)
            if node == destination:
                route.append(cost)
                return route
            edges = graph[node]
            for edge in [edge[0] for edge in edges]:
                if edge not in frontier:
                    loc = [n[0] for n in graph[node]].index(edge)
                    path_cost = cost + int(graph[node][loc][1])
                    last_route = route[:]
                    last_route.append(edge)
                    q.put((path_cost, last_route))
                    
                    
if __name__ == "__main__":
    main()
