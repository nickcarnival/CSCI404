import sys
from queue import PriorityQueue

def main():
    # sys.argv[1] = input_filename
    # sys.argv[2] = origin_city
    # sys.argv[3] = destination_city

    if (len(sys.argv) != 4):
        print("Not enough arguments")
        sys.exit()

    file_name = sys.argv[1]

    # Find the specified route
    source = sys.argv[2]
    dest = sys.argv[3]

    # Generate all of the cities
    graph = parse_input(file_name)

    # TODO: this line causes error right now:
    path = find_route(graph, source, dest)

# handles placing the input file into an appropriate data structure
def parse_input(file_name):
    graph = {}
    file = open(file_name, 'r')
    for line in file:
        if 'END OF INPUT' in line:
            return graph
        node1, node2, distance = line.lower().split()
        graph.setdefault(node1, []).append((node2, distance))
        graph.setdefault(node2, []).append((node1, distance))
        
graph = parse_input(filepath)
path = []

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
                    if q.empty() is True:
                        print("No Path Found")
                    
def results(graph, visited):
    weights = visited[-1]
    print('Distance: %s' %(distance))
    print('Path: ')
    for k in visited[:-2]:
        v = visited.index(k)
        index = [n[0] for n in graph[k]].index(visited[v+1])
        weights = graph[k][index][1]
        print('%s to %s, %s miles' %(k, visited[v+1], weights))

                    
if __name__ == "__main__":
    main()
