


world = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

def is_valid_position(world, x, y):
    """
    Check if the position (x, y) is valid in the given world.

    Args:
        world (list of list of int): The grid representing the world.
        x (int): The column index of the position to check.
        y (int): The row index of the position to check.

    Returns:
        bool: True if the position is valid (within bounds and not an obstacle), False otherwise
    """
    position_allowed = False
    if 0 <= x < len(world[0]) and 0 <= y < len(world) and world[y][x] != 1:
        position_allowed = True

    return position_allowed


result = is_valid_position(world, 1, 1)
print(result)