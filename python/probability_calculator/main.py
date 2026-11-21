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
    else:
        new_pocket += action_fail_reward
    return new_pocket


def action_loop(action, attempts, pocket):
    """
    Simulate multiple attempts of an action and track the pocket value after each attempt.
    Args:
        action (dict): action configuration containing:
            Probability_of_success,
            success_reward,
            fail_reward,
            cost_per_action
        attempts (int): number of runs
        pocket (int): The current pocket value.

    Returns:
        tuple: Contains:
            - int: Final pocket value.
            - list: Changes in pocket for each attempt.
            - list: Pocket values, including the initial value.
    """
    action_list = []
    result_list = [pocket]
    if attempts > 0:
        for i in range(attempts):
            new_pocket = get_result(action, pocket)
            action_list.append(new_pocket - pocket)
            result_list.append(new_pocket)
            pocket = new_pocket

    print("Results:", action_list)
    print("Account_value:", result_list)
    return pocket, action_list, result_list


if __name__ == "__main__":

    pocket = 0
    pocket = action_loop(action_a,10, pocket)
    print(pocket)