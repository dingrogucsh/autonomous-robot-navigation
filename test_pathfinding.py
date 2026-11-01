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
assert bfs(blocked_grid, (0, 0), (2, 2))["path"] is None

assert bfs(grid, (0, 0), (0, 2))["path"] == [
    (0, 0),
    (0, 1),
    (0, 2)
]