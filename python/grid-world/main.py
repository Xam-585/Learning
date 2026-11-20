import heapq


start_position = [1, 2]
current_position = start_position.copy()


world = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
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


def get_neighbors(world, position):
    """
    Check which of the four neighboring positions are accessible.

    The neighboring positions are checked in the following order:
    right (+x), left (-x), down (+y), up (-y).

    Args:
        world (list of list of int): Grid containing free cells (0)
            and obstacles (1).
        position (tuple or list of int): Current position (x, y).

    Returns:
        list of int: Four movement flags in the order
            [+x, -x, +y, -y].
            0 indicates an allowed movement.
            1 indicates a blocked or out-of-bounds movement.
    """

    movement = [1, -1]
    neighbors = [0,0,0,0]

    for i in range(2):
        if is_valid_position(world, position[0] + movement[i], position[1]) == True:
            neighbors[i] = 0
        else:
            neighbors[i] = 1

        if is_valid_position(world, position[0] ,position[1] + movement[i]) == True:
            neighbors[i + 2] = 0
        else:
            neighbors[i + 2] = 1 
    
    return neighbors


def best_moving_path_helper(decision, g, goal_x, goal_y, x, y):
    """
    Calculate the A* priority of a position and add it to the queue.

    The priority is calculated using f(n) = g(n) + h(n),
    where h(n) is the Manhattan distance to the goal.

    Args:
        decision (list): Priority queue containing (f, -g, position) entries.
            entries.
        g (int): Known movement cost from the start to the position.
        goal_x (int): X-coordinate of the goal.
        goal_y (int): Y-coordinate of the goal.
        x (int): X-coordinate of the position.
        y (int): Y-coordinate of the position.

    Returns:
        None: The function does not return a value.

    Side Effects:
        Adds a new entry to the decision priority queue.
    """

    h = abs(goal_x - x) + abs(goal_y - y)
    f =  g + h
    minus_g = g *(-1)
    heapq.heappush(decision, (f, minus_g,(x, y)))


def process_neighbors(world, next_position, goal_position, came_from, g_score, decision):
    """
    Evaluate the valid neighboring positions of the current node.

    For each valid neighbor, calculate the tentative movement cost.
    If a shorter path to the neighbor is found, update its g-score
    and predecessor, then add it to the priority queue.

    Movement is restricted to four directions, with a cost of 1
    per movement.

    Args:
        world (list of list of int): Grid containing free cells (0)
            and obstacles (1).
        next_position (tuple of int): Current position (x, y).
        goal_position (tuple of int): Goal position (x, y).
        came_from (dict): Maps each discovered position to its
            predecessor position.
        g_score (dict): Maps positions to their lowest known
            movement cost from the start.
        decision (list): Priority queue containing (f, position)
            entries, managed using heapq.

    Returns:
        None: The function does not return a value.

    Side Effects:
        Updates came_from and g_score when a shorter path is found.
        Adds updated neighbor positions to decision.
    """

    moving_field_range = 4
    operation_list = [(1,0), (-1, 0), (0,1), (0,-1)]

    next_x, next_y = next_position
    goal_x, goal_y = goal_position
    current_g = g_score[(next_x, next_y)]
    new_g = current_g +1 
    possible_movements = get_neighbors(world, (next_x,next_y))  

    for i in range(moving_field_range):
        if possible_movements[i] == 0:
            a,b = operation_list[i]
            neighbor = (next_x + a, next_y + b)
            if new_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = (next_x, next_y)
                g_score[neighbor] = new_g
                best_moving_path_helper(decision, new_g, goal_x, goal_y,neighbor[0], neighbor[1])            
                    

def best_moving_path(goal_x,goal_y,current_x,current_y, world):
    """
     Find a shortest path through a grid using the A* algorithm.

    Movement is restricted to four directions.
    Each movement has a cost of 1.
    Manhattan distance is used as the heuristic.
    
    Args:
        goal_x (int): X-coordinate of the goal.
        goal_y (int): Y-coordinate of the goal.
        current_x (int): X-coordinate of the start.
        current_y (int): Y-coordinate of the start.
        world (list of list of int): Grid containing free cells (0)
            and obstacles (1).

    Returns:
        list of tuple or None: Shortest path from start to goal,
            including both endpoints, or None if no path exists.
    """
    expanded_nodes = 0
    if is_valid_position(world,goal_x,goal_y) == True and is_valid_position(world,current_x,current_y) == True:

        decision = []
        g = 0
        g_score = {
            (current_x, current_y): 0
        }
        came_from = {
            (current_x, current_y): None
        }

        best_moving_path_helper(decision,g, goal_x,goal_y, current_x, current_y )
        while decision:
            f, minus_g,(current_x, current_y) = heapq.heappop(decision)
            h = abs(goal_x - current_x) + abs(goal_y - current_y)
            if f> h + g_score[(current_x, current_y)]:
                continue
            if current_x == goal_x and current_y == goal_y:
                path = reconstruct_path(came_from, (goal_x, goal_y))
                return path
            expanded_nodes +=1
            process_neighbors(world,(current_x, current_y),(goal_x, goal_y), came_from, g_score, decision)
            print(expanded_nodes)
    else:
        return None


def reconstruct_path(came_from, goal_position):
    """
    Reconstruct the path from the start to the goal.

    Follow the stored predecessor positions backwards from the goal
    until the start position is reached, then reverse the resulting
    path to obtain the correct movement order.

    Args:
        came_from (dict): Maps each discovered position to its
            predecessor. The start position maps to None.
        goal_position (tuple of int): Goal position (x, y).

    Returns:
        list of tuple: Ordered path from start to goal,
            including both endpoints.
    """

    path = []
    position = goal_position
    while position is not None:
        path.append(position) 
        position =  came_from[position]
    path.reverse()
    return path

if __name__ == "__main__":
    print(best_moving_path(7, 7, 0, 0, world))
    
