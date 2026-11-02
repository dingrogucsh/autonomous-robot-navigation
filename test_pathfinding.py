from pathfinding import bfs

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0]
]

blocked_grid = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

# Test 1: Simple shortest path
result = bfs(grid, (0, 0), (0, 2))

assert result["path"] == [(0, 0), (0, 1), (0, 2)]
assert result["nodes explored"] == 5

# Test 2: Start equals Goal
result = bfs(grid, (0, 0), (0, 0))

assert result["path"] == [(0, 0)]
assert result["nodes explored"] == 1

# Test 3: Unreachable Goal
result = bfs(blocked_grid, (0, 0), (2, 2))

assert result["path"] is None
assert result["nodes explored"] == 1

print("All BFS tests passed!")