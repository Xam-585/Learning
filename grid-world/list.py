


world = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

def is_valid_position (world, x, y):
    position_allowed = False
    if (0 <= x < len(world[0]) and 0 <= y < len(world) and world[y][x] != 1):
        position_allowed = True

    return position_allowed


result = is_valid_position(world, 1, 1)
print(result)