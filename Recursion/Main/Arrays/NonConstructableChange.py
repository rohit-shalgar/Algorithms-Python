def nonConstructibleChange(input):
    input.sort()
    change = 0
    for value in input:
        if value > change + 1:
            return change + 1
        change = change + value

    return change + 1
