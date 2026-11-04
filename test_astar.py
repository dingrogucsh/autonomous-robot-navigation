from astar import astar, manhattan_distance

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Test 1: Manhattan Distance
assert manhattan_distance((0, 0), (2, 2)) == 4

# Test 2: A* Shortest Path
result = astar(grid, (0, 0), (2, 2))

assert result["path"] is not None
assert result["path"][0] == (0, 0)
assert result["path"][-1] == (2, 2)
assert len(result["path"]) - 1 == 4
assert result["total_cost"] == 4

# Test 3: Start equals Goal
result = astar(grid, (0, 0), (0, 0))

assert result["path"] == [(0, 0)]
assert result["total_cost"] == 0
assert result["nodes_explored"] == 1

print("Basic A* tests passed!")