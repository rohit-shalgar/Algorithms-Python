# powerset of [1,2,3] is [],[1],[1,2],[2],[3],[1,3],[1,2,3],[2,3] -2 ^ n * n


def get_power_set(input_array: list):
    power_sets = [[]]
    for number in input_array:
        power_sets_length = len(power_sets)
        for i in range(power_sets_length):
            current_power_set = power_sets[i]
            power_sets.append(current_power_set + [number])

    return power_sets
