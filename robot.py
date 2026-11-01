from grid_world import is_valid_move
def move_robot(grid, position, direction):
    row, col = position
    if direction == 'RIGHT':
        col += 1
    elif direction == 'LEFT':
        col -= 1
    elif direction == 'UP':
        row -= 1
    elif direction == 'DOWN':
        row += 1
    else:
        return position
    if is_valid_move(grid, row, col):
        return (row, col)
    return position