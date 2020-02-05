import sys
import math 
from PriorityQueue import PriorityQueue2
from Path import Tree

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
    route = uninformed_search(source, dest, cities)

def uninformed_search(source, destination, cities):
    """
    This algorithm takes in the source, destination, and a dictionary of cities and adjacencies basically a smallest cost first algorithm
    """
    #[ {'Bremen' : 14}, {'Frankfurt' : 43} ]
    #Bremen to Frankfurt = 455
    count = 0
    visited = set()

    # for the PriorityQueue
    frontier = PriorityQueue2()
    frontier.put(0, source)

    current_name = frontier.get()[1]
    paths = []

    # initialize paths
    for child in cities[current_name]:
        child_name = str(list(child.keys())[0])
        child_weight = int(list(child.values())[0])
        current_path = ( current_name, [{child_name : child_weight}], child_weight) 

        if current_path not in paths:
            # create a new path
            paths.append(current_path)
        frontier.put(child_weight, child_name)
    visited.add(current_name)
    next_node = frontier.get() 

    # now we know that each node is in a path
    parent_name = current_name
    current_name = next_node[1]
    while current_name != destination:

        for child in cities[current_name]:
            # search for our current path
            child_name = str(list(child.keys())[0])
            child_weight = int(list(child.values())[0])
            temp_tuple = (parent_name, [{current_name : 116}], 116)
            old_path = paths[paths.index(temp_tuple)]
            print('Old:', old_path)
            new_path = old_path
            new_path[1].append({'Test' : 1}) 
            print('New: ', new_path)
            if child_name not in visited:
                print(current_name, '\'s child is: ', child) 
        break

    return '\'route\'' 

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
