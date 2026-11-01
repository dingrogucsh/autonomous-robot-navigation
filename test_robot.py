from robot import move_robot

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0]
]
assert move_robot(grid,(0,0),'RIGHT') == (0,1)
assert move_robot(grid,(0,0),'UP') == (0,0)
assert move_robot(grid,(0,2),'RIGHT') == (0,2)
assert move_robot(grid,(0,0),'FLY') == (0,0)
print("passed")