# It's getting caught trying to get edges with edges=graph[node], so I'm trying to slice instead for now.
from queue import PriorityQueue
from heapq import heappush, heappop
import sys
import sys
from collections import deque
input_file = 'filepath'

f = open(input_file, "r")
graph = []

for line in f:
    if "END OF INPUT" in line:
        break
    else:
        cities = line.split()
        sources = cities[0]
        destinations = cities[1]
        weight = cities[2]
        orig_path = [sources, destinations, weight]
        rev_path = [destinations, sources, weight]
        graph.append(orig_path)
        graph.append(rev_path)

print(graph)

class queue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0
        
    def put(self, item):
        return heappush(self.queue, item)
    def get(self):
        return heappop(self.queue)

def find_route(graph, source, destination):
    fringe = set()
    q = queue()
    q.put((0, [source]))
    while q.empty() is False:
        weight, route = q.get()
        node = route[len(route) -1]
        if node not in fringe:
            fringe.add(node)
            if node == destination:
                route.append(weight)
                return route
            edges = graph[node]
            for edge in [edges[0] for edge in edges]:
                if edge not in fringe:
                    index = [node[0] for node in graph[node]].index(edge)
                    total_cost = weight + int(graph[node][index][1])
                    visited = route[:]
                    visited.append(edge)
                    q.put((total_cost, visited))

def results(graph, visited):
    weights = visited[-1]
    print('Distance: %s' %(distance))
    print('Path: ')
    for k in visited[:-2]:
        v = visited.index(k)
        index = [n[0] for n in graph[k]].index(visited[v+1])
        weights = graph[k][index][1]
        print('%s to %s, %s miles' %(k, visited[v+1], weights))

path = find_route(graph, graph[graph[0][0] == "Berlin"], # slice that has destination in second column])
                    
