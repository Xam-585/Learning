import sys
from pathlib import Path


main_file = str(Path(__file__).resolve().parent.parent)

if main_file not in sys.path:
    sys.path.append(main_file)

from main import move_agent as mg 


def test_move_agent_block():
    test_world =[
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    start_position = [1, 2]
    expected_position = [1, 2]
    actual_position = mg(test_world, start_position.copy(), [0, -1])

    assert actual_position == expected_position


def test_move_agent():
    test_world =[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    start_position = [1, 1]
    expected_position = [1, 0]
    actual_position = mg(test_world, start_position.copy(), [0, -1])

    assert actual_position == expected_position


def test_move_agent_partial():
    test_world =[
        [0,0,0,0],
        [0,0,1,0],
        [0,0,0,0]
    ]
    start_position = [0, 1]
    expected_position = [1, 1]
    actual_position = mg(test_world, start_position.copy(), [3, 0])

    assert actual_position == expected_position