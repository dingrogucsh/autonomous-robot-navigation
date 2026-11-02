from dijkstra import dijkstra
from pathfinding import bfs

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

cost_grid = [
    [1, 9, 1],
    [1, 9, 1],
    [1, 1, 1]
]

result = dijkstra(grid, (0, 0), (0, 2), cost_grid)

assert result["total_cost"] == 6
assert len(result["path"]) - 1 == 6


start = (0, 0)


goal = (0, 2)

bfs_result = bfs(grid, start, goal)
dijkstra_result = dijkstra(grid, start, goal, cost_grid)

print("BFS path:", bfs_result["path"])
print("Dijkstra path:", dijkstra_result["path"])

def calculate_path_cost(path, cost_grid):
    total = 0
    for row, col in path[1:]:
        total += cost_grid[row][col]
    return total

bfs_cost = calculate_path_cost(bfs_result["path"], cost_grid)
dijkstra_cost = calculate_path_cost(dijkstra_result["path"], cost_grid)

assert bfs_cost == 10
assert dijkstra_cost == 6
assert dijkstra_cost < bfs_cost

print("BFS total cost:", bfs_cost)
print("Dijkstra total cost:", dijkstra_cost)