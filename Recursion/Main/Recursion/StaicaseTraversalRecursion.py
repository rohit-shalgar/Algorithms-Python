def staircase_traversal(height: int, steps: int):
    if height <= 1:
        return 1
    no_of_ways = 0
    for step in range(1, min(height, steps) + 1):
        no_of_ways += staircase_traversal(height - step, steps)

    return no_of_ways


def staircase_traversal_dp(height, max_steps):
    no_of_ways_to_each_height = [0] * (height + 1)
    no_of_ways_to_each_height[0] = 1
    no_of_ways_to_each_height[1] = 1
    for current_height in range(2, height + 1):
        for step in range(1, max_steps + 1):
            no_of_ways_to_each_height[current_height] = no_of_ways_to_each_height[current_height] + \
                                                no_of_ways_to_each_height[current_height - step]

    return no_of_ways_to_each_height[height]


def staircase_traversal_optimized(height: int, steps: int):
    no_of_ways_for_each_step = {0: 1, 1: 1}
    staircase_traversal_optimized_helper(no_of_ways_for_each_step, height, steps)
    return no_of_ways_for_each_step[height]


def staircase_traversal_optimized_helper(no_of_ways_for_each_step, height, steps):
    if height in no_of_ways_for_each_step:
        return no_of_ways_for_each_step[height]
    no_of_ways = 0
    for step in range(1, min(height, steps) + 1):
        current_height = height - step
        no_of_ways += staircase_traversal_optimized_helper(no_of_ways_for_each_step, current_height, steps)
    no_of_ways_for_each_step[height] = no_of_ways
    return no_of_ways_for_each_step[height]
