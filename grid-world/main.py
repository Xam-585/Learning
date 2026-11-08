
start_position = [1, 2]
current_position = start_position.copy()


world = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]


def move_agent(world, current_position, action):
    """
    move the agent step by step through the grid.

    The x-axis is processed before the y-axis.
    Movment stops when an invalid position is reached.
    Succesful steps are preserved

    Args:
        world (list of list of int): The grid representing the world.
        current_position (list of int): The agent's current [x, y] position.
        action (list of int): Movement vector [dx, dy].

    Returns:
        list of int: The resulting position after movement.
            The input position is modified in place.
    """

    x_operation = "+"
    y_operation = "+"
    moving_position = current_position.copy()

    if action[0] < 0:
        x_operation = "-"

    if action[1] < 0:
        y_operation = "-"
    
    if abs(action[0]) > 0:
        for x in range(abs(action[0])):
            moving_position[0] = current_position[0] + (1 if x_operation == "+" else -1)
            if is_valid_position(world, moving_position[0], moving_position[1]) == True:
                current_position[0] = moving_position[0]
            else:
                return current_position

    if abs(action[1]) > 0:
        for y in range(abs(action[1])):
            moving_position[1] = current_position[1] + (1 if y_operation == "+" else -1)

            if is_valid_position(world, moving_position[0], moving_position[1]) == True:
                current_position[1] = moving_position[1]
            else:
                return current_position

    return current_position


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







if __name__ == "__main__":
    current_position = move_agent(world, current_position, [0, -1])