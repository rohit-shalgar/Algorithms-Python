def isValidSubsequence(array, sequence):
    count = 0
    for i in sequence:
        for j in array:
            if i == j:
                count += 1
                break
    return count == len(sequence)


def isValidSubSequenceOpt(array, sequence):
    seqindx = 0
    for value in array:
        if seqindx == len(sequence):
            break
        if sequence[seqindx] == value:
            seqindx += 1
    return seqindx == len(sequence)
