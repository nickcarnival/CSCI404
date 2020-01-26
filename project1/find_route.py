import sys

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
    This algorithm takes in the source, destination, and a dictionary of cities and adjacencies 
    """
    adj_cities = cities[source]
    done = False
    seen_cities = []
    while not done:
        # go to each adjacent city and look at the weight 
        # then do this for each city until we find the desired city.
        for city in adj_cities:
            if city in seen_cities:
                # not actually break, we need to adjust the weight of going here
                print(city)
                break
            elif city not in seen_cities:
                seen_cities.append(city)
                break
        adj_cities = cities[destination]

    print(seen_cities)
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
