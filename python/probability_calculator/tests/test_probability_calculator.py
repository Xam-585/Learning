import sys
from pathlib import Path


main_file = str(Path(__file__).resolve().parent.parent)
if main_file not in sys.path:
    sys.path.append(main_file)


from main import action_loop, statistical_analysis


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
    expected_result_test_a = (10,[],[10],0)
    assert action_loop(action_a,0,10) == expected_result_test_a

    expected_result_test_b = (25,[5,5,5,5,5],[0,5,10,15,20,25],5)
    assert action_loop(action_a,5,0) == expected_result_test_b

    expected_result_test_c = (-25,[-5,-5,-5,-5,-5],[0,-5,-10,-15,-20,-25],0)
    assert action_loop(action_b,5,0) == expected_result_test_c


def test_statistical_analysis_success():
    action_a = {
        "Probability_of_success" : 100,
        "success_reward" : 10,
        "fail_reward" : 0, 
        "cost_per_action" : 0
    }

    test_a_dict = statistical_analysis(action_a,5,-10)
    assert test_a_dict["attempts"] == 5
    assert test_a_dict["suceeds"] == 5
    assert test_a_dict["fails"] == 0
    assert test_a_dict["success rate"] == 100
    assert test_a_dict["average value per action"] == 10
    assert test_a_dict["Overall result"] == 10*5
    assert test_a_dict["pocket_result"] == 10*5-10


def test_statistical_analysis_fail():
    action_b = {
        "Probability_of_success" : 0,
        "success_reward" : 10,
        "fail_reward" : 0, 
        "cost_per_action" : 5
    }

    test_b_dict = statistical_analysis(action_b,5,10)
    assert test_b_dict["attempts"] == 5
    assert test_b_dict["suceeds"] == 0
    assert test_b_dict["fails"] == 5
    assert test_b_dict["success rate"] == 0
    assert test_b_dict["average value per action"] == -5
    assert test_b_dict["Overall result"] == -5*5
    assert test_b_dict["pocket_result"] == -5*5+10


def test_statistical_analysis_none_attempts():
    action_a = {
        "Probability_of_success" : 100,
        "success_reward" : 10,
        "fail_reward" : 0, 
        "cost_per_action" : 0
    }

    assert statistical_analysis(action_a,0,-10) is None
    

def test_success_rate_statistical_experimental():
    action_c = {
    "Probability_of_success" : 50,
    "success_reward" : 10,
    "fail_reward" : 0, 
    "cost_per_action" : 5
    }

    test_c_dict = statistical_analysis(action_c,1000,10)
    assert test_c_dict["success rate"] <= 55 and test_c_dict["success rate"] >= 45