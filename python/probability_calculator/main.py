import random

action_a = {
    "Probability_of_success" : 80,
    "success_reward" : 5,
    "fail_reward" : 0, 
    "cost_per_action" : 0
}
    
action_b = {
    "Probability_of_success" : 50,
    "success_reward" : 12,
    "fail_reward" : 0, 
    "cost_per_action" : 2
}

action_c = {
    "Probability_of_success" : 25,
    "success_reward" : 30,
    "fail_reward" : 0, 
    "cost_per_action" : 5
}


def get_result(action, pocket):
    """
    Simulate an action and calculate the updated pocket.
    Args:
        action (dict): action configuration containing:
            Probability_of_success,
            success_reward,
            fail_reward,
            cost_per_action

        pocket (int): The current pocket value.

    Returns:
        int: The updated pocket value after executing the action.
    """

    action_probability_of_success = action["Probability_of_success"]
    action_success_reward = action["success_reward"]
    action_fail_reward = action["fail_reward"]
    action_cost_per_action = action["cost_per_action"]

    new_pocket = pocket - action_cost_per_action

    rand_number = random.randint(1,100)
    if rand_number <= action_probability_of_success:
        new_pocket += action_success_reward
        print("success")
    else:
        new_pocket += action_fail_reward
        print("fail")
    return new_pocket


print(get_result.__doc__)
pocket = 0
pocket = get_result(action_a, pocket)
print(pocket)