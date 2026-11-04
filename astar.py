import heapq
from grid_world import get_neighbor
from pathfinding import reconstruct_path

def manhattan_distance(current, goal):
    r1, c1 = current
    r2, c2 = goal
    return abs(r1 - r2) + abs(c1 - c2)


def astar(grid, start, goal, cost_grid=None):
    pq = []

    start_h = manhattan_distance(start, goal)

    heapq.heappush(pq, (start_h, 0, start))

    distance = {start: 0}
    parent = {start: None}

    nodes_explored = 0
    while pq:
        current_f, current_g, current = heapq.heappop(pq)

        if current_g > distance[current]:
            continue

        nodes_explored += 1
        if current == goal:
            path = reconstruct_path(parent, start, goal)

            return {
                "path": path,
                "total_cost": current_g,
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

            new_g = movement_cost + current_g

            if new_g < distance.get(neighbor, float("inf")):
                distance[neighbor] = new_g
                parent[neighbor] = current

                h = manhattan_distance(neighbor, goal)

                f = h + new_g
                heapq.heappush(pq, (f,new_g, neighbor))

    return {
        "path": None,
        "total_cost": float("inf"),
        "nodes_explored": nodes_explored
    }