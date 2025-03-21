import heapq
import math

def velocity(y0, y1):
    """Calculate the velocity based on y0 and y1."""
    if y0 == y1:
        return y0
    return (y1 - y0) / (math.log(y1) - math.log(y0))

def time(x0, y0, x1, y1):
    """Calculate the time required to travel between two points."""
    distance = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    return distance / velocity(y0, y1)

def F(d):
    """Find the shortest travel time from (0,1) to (d,1) using Dijkstra's algorithm."""
    pq = [(0, 0, 1)]  # Min-heap with (time, x, y)
    visited = {}

    while pq:
        t, x, y = heapq.heappop(pq)

        if (x, y) in visited and visited[(x, y)] <= t:
            continue
        visited[(x, y)] = t

        if x == d and y == 1:
            return round(t, 9)

        for y1 in range(1, max(y * 2, 2) + 1):  # Generate valid next steps
            x1 = x + 1
            if x1 <= d:
                heapq.heappush(pq, (t + time(x, y, x1, y1), x1, y1))

print(F(4))
