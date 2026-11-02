from dijkstra import dijkstra

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Test 1: Normal shortest path
result = dijkstra(grid, (0, 0), (2, 2))

assert result["path"] is not None
assert result["path"][0] == (0, 0)
assert result["path"][-1] == (2, 2)
assert len(result["path"]) - 1 == 4
assert result["total_cost"] == 4
assert result["nodes_explored"] == 9

# Test 2: Start equals Goal
result = dijkstra(grid, (0, 0), (0, 0))

assert result["path"] == [(0, 0)]
assert result["total_cost"] == 0
assert result["nodes_explored"] == 1

# Test 3: Unreachable Goal
blocked_grid = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

result = dijkstra(blocked_grid, (0, 0), (2, 2))

assert result["path"] is None
assert result["total_cost"] == float("inf")
assert result["nodes_explored"] == 1

print("All Dijkstra tests passed!")