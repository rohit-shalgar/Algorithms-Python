# powerset of [1,2,3] is [],[1],[1,2],[2],[3],[1,3],[1,2,3],[2,3] -2 ^ n * n


def get_power_set(input_array: list):
    power_sets = [[]]
    for number in input_array:
        power_sets_length = len(power_sets)
        for i in range(power_sets_length):
            current_power_set = power_sets[i]
            power_sets.append(current_power_set + [number])

    return power_sets


def get_power_sets_optimized_helper(input_array, indx:int):
    if indx == len(input_array):
        return [[]]
    else:
        element = input_array[indx]
        power_sets = get_power_sets_optimized_helper(input_array, indx+1)
        power_sets_size = len(power_sets)
        for i in range(power_sets_size):
            power_set = power_sets[i]
            power_sets.append(power_set + [element])
        return power_sets


def get_power_sets_optimized(input_array: list):
    return get_power_sets_optimized_helper(input_array, 0)
