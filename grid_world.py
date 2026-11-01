def is_valid_move(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if col < 0 or col >= cols or row < 0 or row >= rows:
        return False

    if grid[row][col] == 1:
        return False

    return True
def get_neighbor(grid, row, col):
    rowa = len(grid)
    cols = len(grid[0])
    neigh = []
    dr = [
        (-1, 0),
        (1,0),
        (0, 1),
        (0, -1)
    ]
    for r, c in dr:
        new_row = row + r
        new_col = col + c
        if 0 <= new_col < cols and 0 <= new_row < rowa:
            if is_valid_move(grid, new_row, new_col):
                neigh.append((new_row, new_col))
    return neigh
