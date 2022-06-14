# [1, 2, 3] will result in
# [1,2,3],[1,3,2],[2,3,1],[2,1,3],[3,1,2],[3,2,1]
# n! permutations

def get_permutations_helper(permutations, current_permutation, input_array: list):
    if not len(input_array) and len(current_permutation):
        permutations.append(current_permutation)
    else:
        for i in range(len(input_array)):
            new_array = input_array[:i] + input_array[i + 1:]
            new_permutation = current_permutation + [input_array[i]]
            get_permutations_helper(permutations, new_permutation, new_array)


def get_permutations(input_array):
    permutations = []
    get_permutations_helper(permutations, [], input_array)
    return permutations


def swap(index, j, input_array):
    input_array[index], input_array[j] = input_array[j], input_array[index]


def get_permutations_swap_helper(permutations: list, input_array: list, index: int):
    if index == len(input_array) - 1:
        permutations.append(input_array[:])
    else:
        for j in range(index, len(input_array)):
            swap(index, j, input_array)
            get_permutations_swap_helper(permutations, input_array, index+1)
            swap(index, j, input_array)


def get_permutations_swap(input_array: list):
    permutations = []
    get_permutations_swap_helper(permutations, input_array, 0)
    return permutations
