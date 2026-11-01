from collections import deque
from grid_world import get_neighbor
def bfs(grid, start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {}
    parent[start] = None
    nodes_explored = 0
    while queue:
        current = queue.popleft()
        nodes_explored += 1
        print(current)
        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return { 
                "path" : path,
                "nodes explored":nodes_explored
            }
    
        row, col = current
        neighbor = get_neighbor(grid, row, col)
        for neigh in neighbor:
            if neigh in visited:
                continue
            visited.add(neigh)
            parent[neigh] = current
            queue.append(neigh)
    return {
        "path" : None,
        "nodes explored": nodes_explored
    }

def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path