from grid_world import is_valid_move, get_neighbor

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0]
]
print("Actual:", get_neighbor(grid, 2, 2))
print("Expected:", [(1, 2), (2, 3)])
assert get_neighbor(grid, 2, 2) == [(1, 2), (2, 3)]
assert get_neighbor(grid, 0, 0) == [(1,0),(0,1)]
assert get_neighbor(grid, 3, 4) == [(2,4)]