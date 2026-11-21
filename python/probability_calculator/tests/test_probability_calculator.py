import sys
from pathlib import Path


main_file = str(Path(__file__).resolve().parent.parent)
if main_file not in sys.path:
    sys.path.append(main_file)


from main import action_loop


def test_action_loop():

    action_a = {
        "Probability_of_success" : 100,
        "success_reward" : 10,
        "fail_reward" : 0, 
        "cost_per_action" : 5
    }
    action_b = {
        "Probability_of_success" : 0,
        "success_reward" : 10,
        "fail_reward" : 0, 
        "cost_per_action" : 5
    }
    expected_result_test_a = ((10),[],[10])
    assert action_loop(action_a,0,10) == expected_result_test_a

    expected_result_test_b = ((25),[5,5,5,5,5],[0,5,10,15,20,25])
    assert action_loop(action_a,5,0) == expected_result_test_b

    expected_result_test_c = ((-25),[-5,-5,-5,-5,-5],[0,-5,-10,-15,-20,-25])
    assert action_loop(action_b,5,0) == expected_result_test_c