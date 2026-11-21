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
    "Probability_of_success" : 5,
    "success_reward" : 300,
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
        - int: The updated pocket value after executing the action.
        - bool: True if action was successful
    """

    succeed = False
    action_probability_of_success = action["Probability_of_success"]
    action_success_reward = action["success_reward"]
    action_fail_reward = action["fail_reward"]
    action_cost_per_action = action["cost_per_action"]

    new_pocket = pocket - action_cost_per_action

    rand_number = random.randint(1,100)
    if rand_number <= action_probability_of_success:
        new_pocket += action_success_reward
        succeed = True
    else:
        new_pocket += action_fail_reward
    return new_pocket, succeed


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
            - int: Number of successful actions
    """
    succeed_results = 0
    action_list = []
    result_list = [pocket]
    if attempts > 0:
        for i in range(attempts):
            new_pocket, succeed = get_result(action, pocket)
            action_list.append(new_pocket - pocket)
            result_list.append(new_pocket)
            pocket = new_pocket
            if succeed:
                succeed_results += 1

    return pocket, action_list, result_list, succeed_results


def statistical_analysis(action, attempts, pocket):
    """
    Simulate multiple attempts of an action and return statistical results as a dictionary.
    
    Args:
        action (dict): action configuration containing:
            Probability_of_success,
            success_reward,
            fail_reward,
            cost_per_action
        attempts (int): number of runs
        pocket (int): The current pocket value.

    Returns:
        dict or None: Statistical results, or None if attempts <= 0.
            dict:
                - int: "attempts":
                - int: "suceeds":
                - int: "fails":
                - float: "success rate":        
                - float: "average value per action":
                - int: "Overall result":
                - int: "pocket_result":
    """

    statistic_dict = {}

    if attempts <= 0:
        return None
    new_pocket, action_list, pocket_list, succeed_results= action_loop(action, attempts, pocket)
    statistic_dict["attempts"] = attempts
    statistic_dict["suceeds"] = succeed_results
    statistic_dict["fails"] = attempts - succeed_results
    statistic_dict["success rate"] = (succeed_results / attempts) *100
    statistic_dict["average value per action"] = (new_pocket - pocket) / attempts
    statistic_dict["Overall result"] = new_pocket - pocket
    statistic_dict["pocket_result"] = new_pocket
    return statistic_dict


if __name__ == "__main__":

    pocket = 0
    print(statistical_analysis(action_c, 10000, pocket))