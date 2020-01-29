import sys
from queue import PriorityQueue

class Route:
    """
    The route contains the total distance and the cities visited to achieve this route
    """
    def __repr__(self):
        return "distance: " + str(self.distance) + "\n" + "route:\n"
    def __init__(self, distance):
        self.distance = distance

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
    done = False
    current_city = source
    visited = set()
    best_weight = 9999999999999999999999999

    debug = 0
    while debug < 10:
        debug += 1
        visited.add(current_city)
        print(visited)
        adj_cities = cities[current_city]
        # find lowest weight neighbor
        for i, city in enumerate(adj_cities):
            current_weight = int(list(city.values())[0])
            print('City Name: ', str(list(city.keys())[0]))
            #TODO: this needs to not exclusively check if the place has been visited
            if ((current_weight < best_weight) and (str(list(city.keys())[0]) not in visited)): 
                best_weight = current_weight
        # find the next city to go to
        for city in adj_cities:
            current_weight = (list(city.values())[0])
            if (int(current_weight) == int(best_weight)):
                current_city = str(list(city.keys())[0])

    route = Route(69) 
    return route

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

            # if the city is in cities
            if cities.get(city, 'f') != 'f':
                # add adjacency
                cities[city].append({adjacency : weight})
                if cities.get(adjacency, 'f') == 'f':
                    # if the adjacent city is not in the dict
                    cities[adjacency] = [{city :weight}]
                else:
                    # if the adjacent city is in the dict
                    cities[adjacency].append({city :  weight})
            # if the city is not in cities
            elif cities.get(city, 'f') == 'f':
                # add new city
                cities[city] = [adj_weight]
                if cities.get(adjacency, 'f') == 'f':
                    # if the adjacent city is not in the dict
                    cities[adjacency] = [{city :weight}]
                else:
                    # if the adjacent city is in the dict
                    cities[adjacency].append({city :  weight})

            line = f.readline()
    return cities
if __name__ == "__main__":
    main()
