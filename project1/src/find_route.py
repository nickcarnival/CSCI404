import sys
import math 
from PriorityQueue import PriorityQueue2

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
    route = uninformed_search(source, dest, cities)
    print(route)

def uninformed_search(source, destination, cities):
    """
    This algorithm takes in the source, destination, and a dictionary of cities and adjacencies basically a smallest cost first algorithm
    """
    #[ {'Bremen' : 14}, {'Frankfurt' : 43} ]
    current_node = source
    print('Original Current Node: ', current_node)

    done = False
    count = 0
    smallest_weight = math.inf  

    visited = set()

    pq = PriorityQueue2()

    pq.put(0, current_node)
    while not done:
        visited.add(current_node)
        count += 1
        if count > 7:
            break
        parent_weight = pq.get()[0]
        print('Parent Weight:', parent_weight)
        # set the parent node for all of the children
        parent_node = {'Parent' : str(current_node)}
        cities[current_node].append(parent_node)
        # at each child node, we want to remove the parent node name and set the weight equal to the child plus the parent weights
        # find the lowest weight
        children_nodes = cities[current_node]
        for item in cities[current_node]:
            print(item)
        #parent_weight = next(item for item in cities[current_node] if item[current_node] == current_node)
        #print(parent_weight)
        for child in children_nodes:
            current_name = str(list(child.keys())[0])
            if current_name != 'Parent':
                current_weight = int(list(child.values())[0])

                # add each of the adj nodes to the PriorityQueue
                pq.put(current_weight, current_name)
            # if it is a parent node, do something...
            elif current_name == 'Parent':
                print('Parent Node')
        cheapest_node = pq.get()
        current_node = cheapest_node[1]
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
