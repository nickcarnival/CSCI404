import sys
import math 
from copy import deepcopy
from PriorityQueue import PriorityQueue2
from PriorityQueue import Node
from PriorityQueue import Path 

def main():
    """
    Takes in three command line arguments in the form:
    'find_route input_filename origin_city destination_city'
    """
    # sys.argv[1] = input_filename
    # sys.argv[2] = origin_city
    # sys.argv[3] = destination_city

    if (len(sys.argv) != 4):
        print("Not enough arguments")
        sys.exit()
    file_name = sys.argv[1]

    # Generate all of the cities
    cities = parse_input(file_name)

    # Find the specified route
    source = sys.argv[2]
    dest = sys.argv[3]
    #graph = create_graph(source, cities)
    route = ucs(source, dest, cities)

def ucs(source, dest, cities):
    """
    This algorithm takes in the source, destination, and a dictionary of cities and adjacencies basically a smallest cost first algorithm
    """

    visited = set()
    done = False
    count = 0
    smallest_weight = math.inf
    paths = []

    # add the source node to the PQ
    frontier = PriorityQueue2()
    root_node = Node(source, 'NO_PARENT', 0)

    frontier.put(root_node)
    parent_weight, parent_name = frontier.get()
    print(parent_name)
    # consider current state, and check if if finishes in a goal state 
    while parent_name != dest:

        print('Current Parent:', parent_name, ' weight: ', parent_weight)
        # lets find out how to print the path that it took to get here
        # consider all places in the graph that we can get to
        # get the weights to those nodes
        for child in cities[parent_name]:
            # get each childs name and weight
            child_name = str(list(child.keys())[0])
            child_weight = int(list(child.values())[0])

            if child_name not in visited:
                node = Node(child_name, parent_name, child_weight + parent_weight)
                path = Path(parent_name)
                path.add_node(node)
                print(path)
                frontier.put(node)

        # add current node to the visited list
        visited.add(parent_name)

        # calculate the total cost of the paths

        # change the current node to the cheapest PATH

        # visit that path next

        # rinse repeat...
        parent_weight, parent_name = frontier.get()
    return '\'route\'' 

def calc_path_weight(parent_struct):
    return 4

def parse_input(file_name):
    """
    Parses the input and creates an array of cities and their adjacencies
    """
    cities = {}
    with open(file_name, 'r') as f:
        line = f.readline()
         
        cities = {}
        while line:
            # Leave the loop at the end of the file
            if line == 'END OF INPUT\n':
                break
            city, adjacency, weight = line.strip().split(' ') 

            adj_weight = {adjacency : weight}
            city_weight = {city : weight}

            # if the city is in cities
            if cities.get(city, 'f') != 'f':
                # add adjacency
                cities[city].append(adj_weight)
                if cities.get(adjacency, 'f') == 'f':
                    # if the adjacent city is not in the dict
                    cities[adjacency] = [city_weight]
                else:
                    # if the adjacent city is in the dict
                    cities[adjacency].append(city_weight)
            # if the city is not in cities
            elif cities.get(city, 'f') == 'f':
                # add new city
                cities[city] = [adj_weight]
                if cities.get(adjacency, 'f') == 'f':
                    # if the adjacent city is not in the dict
                    cities[adjacency] = [city_weight]
                else:
                    # if the adjacent city is in the dict
                    cities[adjacency].append(city_weight)

            line = f.readline()
    return cities

if __name__ == "__main__":
    main()
