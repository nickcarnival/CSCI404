import math
from queue import PriorityQueue
from heapq import heappush, heappop

class queue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0
    def put(self, item):
        return heappush(self.queue, item)
