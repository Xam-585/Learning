import sys
from pathlib import Path


main_file = str(Path(__file__).resolve().parent.parent)

if main_file not in sys.path:
    sys.path.append(main_file)

from main import move_agent, best_moving_path, is_valid_position


def test_move_agent_block():
    test_world =[
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    start_position = [1, 2]
    expected_position = [1, 2]
    actual_position = move_agent(test_world, start_position.copy(), [0, -1])

    assert actual_position == expected_position


def test_move_agent():
    test_world =[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    start_position = [1, 1]
    expected_position = [1, 0]
    actual_position = move_agent(test_world, start_position.copy(), [0, -1])

    assert actual_position == expected_position


def test_move_agent_partial():
    test_world =[
        [0,0,0,0],
        [0,0,1,0],
        [0,0,0,0]
    ]
    start_position = [0, 1]
    expected_position = [1, 1]
    actual_position = move_agent(test_world, start_position.copy(), [3, 0])

    assert actual_position == expected_position


def test_unreachable_goal():
    test_world = [
        [0,1,0],
        [1,1,0],
        [0,0,0]      
    ]
    start_position = (0, 0)
    goal_position = (2, 2)

    start_x, start_y = start_position
    goal_x, goal_y = goal_position
    not_possible = best_moving_path(goal_x, goal_y, start_x, start_y, test_world)

    assert not_possible is None


def test_shortest_route():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    start_position = (0, 0)
    goal_position = (0, 2)
    expected_path = [(0, 0), (0, 1), (0, 2)]
    start_x, start_y = start_position
    goal_x, goal_y = goal_position
    result_best_moving_path = best_moving_path(goal_x, goal_y, start_x, start_y, test_world)

    assert expected_path == result_best_moving_path


def test_shortest_route_more_options():
    test_world = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0]
    ]
    start_position = (0, 2)
    goal_position = (4, 2)
    
    start_x, start_y = start_position
    goal_x, goal_y = goal_position
    result_best_moving_path = best_moving_path(goal_x, goal_y, start_x, start_y, test_world)

    assert result_best_moving_path is not None

    steps = len(result_best_moving_path) -1 
    start_result = result_best_moving_path[0]
    goal_result = result_best_moving_path[-1]

    assert 8 == steps 
    assert start_position == start_result
    assert goal_position == goal_result

    for i in range(steps):
            x1, y1 = result_best_moving_path[i]
            x2, y2 = result_best_moving_path[i +1]
            assert abs(x1 - x2) + abs(y1 - y2) == 1

    for x1, y1 in result_best_moving_path:
        assert is_valid_position(test_world, x1, y1) == True

def test_start_equals_goal():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    assert best_moving_path(0, 0, 0, 0, test_world) == [(0, 0)]


def test_blocked_start():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    assert best_moving_path(0, 0, 1, 1, test_world) is None


def test_start_out_of_world():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    assert best_moving_path(0, 0, 10, 10, test_world) is None


def test_blocked_goal():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    assert best_moving_path(1, 1, 0, 0, test_world) is None


def test_goal_out_of_world():
    test_world = [
        [0,0,0],
        [0,1,0],
        [0,0,0]      
    ]
    assert best_moving_path(10, 10, 0, 0, test_world) is None