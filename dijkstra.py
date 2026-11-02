import heapq
from grid_world import get_neighbor
from pathfinding import reconstruct_path
def dijkstra(grid, start, goal, cost_grid = None):
    pq = []
    heapq.heappush(pq,(0,start))

    distance = {start : 0}
    parent = {start : None}

    nodes_explored = 0

    while pq:
        current_cost, current = heapq.heappop(pq)
        if current_cost > distance[current]:
            continue
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return {
        "path": path,
        "total_cost": current_cost,
        "nodes_explored": nodes_explored
    }
        row, col = current
        neighbors = get_neighbor(grid, row, col)

        for neighbor in neighbors:
            nr, nc = neighbor
            if cost_grid is None:
                movement_cost = 1
            else:
                movement_cost = cost_grid[nr][nc]
                
            new_cost = current_cost + movement_cost

            if new_cost < distance.get(neighbor, float("inf")):
                distance[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))

    return {
            "path": None,
            "total_cost": float("inf"),
            "nodes_explored": nodes_explored
        }