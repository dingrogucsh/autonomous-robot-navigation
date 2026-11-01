from collections import deque
from grid_world import get_neighbor
def bfs(grid, start, goal):
    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)
    parent = {}
    parent[start] = None
    while queue:
        current = queue.popleft()
        print(current)
        if current == goal:
            return reconstruct_path(parent, start,goal)
    
        row, col = current
        neighbor = get_neighbor(grid, row, col)
        for neigh in neighbor:
            if neigh in visited:
                continue
            visited.add(neigh)
            parent[neigh] = current
            queue.append(neigh)
    return None

def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path