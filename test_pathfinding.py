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

assert bfs(grid, (0, 0), (0, 2)) == [
    (0, 0),
    (0, 1),
    (0, 2)
]
assert bfs(grid,(0,0),(0,0)) == [
    (0,0)
]
assert bfs(grid, (0, 0), (0, 4)) == [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (2, 3),
    (2, 4),
    (1, 4),
    (0, 4)
]
assert bfs(blocked_grid, (0, 0), (2, 2)) is None