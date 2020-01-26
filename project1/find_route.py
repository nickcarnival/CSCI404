import sys

class City:
    """
    A city class that contains the city, its adjacencies, and their weights
    """
    def distance_to(self, city):
        return 6
    def __repr__(self):
        return (str(self.name) + "is adjacent to " + str(self.adjacent) + "with weight: " + self.weight)  
    def __init__(self, name, adjacent, weight):
        self.name = name
        self.adjacent = adjacent
        self.weight = weight

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
    This algorithm takes in the source, destination, and array of cities and returns the best route
    """
    current_city = source
    route = Route(69)
    return route

def parse_input(file_name):
    """
    Parses the input and creates an array of cities and their adjacencies
    """
    cities = []
    with open(file_name, 'r') as f:
        line = f.readline()
         
        while line:
            # Leave the loop at the end of the file
            if line == 'END OF INPUT\n':
                break
            city1, city2, weight = line.strip().split(' ') 

            temp_city2 = City(city1, city2, weight)
            temp_city1 = City(city2, city1, weight)

            cities.append(temp_city1)
            cities.append(temp_city2)
            line = f.readline()

if __name__ == "__main__":
    main()
