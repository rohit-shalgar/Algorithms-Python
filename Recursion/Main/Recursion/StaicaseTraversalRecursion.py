def staircase_traversal(height: int, steps: int):
    if height <= 1:
        return 1
    no_of_ways = 0
    for step in range(1, min(height, steps) + 1):
        no_of_ways += staircase_traversal(height - step, steps)

    return no_of_ways

