def sortedSquaredArray(input):
    sortedSquaredArray = []
    for value in input:
        sortedSquaredArray.append(value * value)
    sortedSquaredArray.sort()
    return sortedSquaredArray


def sortedSquaredArrayOpt(input):
    leftIndx = 0
    rightIndx = len(input) - 1
    sortedArrayIndx = rightIndx
    sortedSquaredArray = [0] * len(input)
    while leftIndx <= rightIndx:
        leftValue = input[leftIndx]
        rightValue = input[rightIndx]
        if abs(leftValue) > abs(rightValue):
            sortedSquaredArray[sortedArrayIndx] = leftValue * leftValue
            leftIndx += 1
        else:
            sortedSquaredArray[sortedArrayIndx] = rightValue * rightValue
            rightIndx -= 1
        sortedArrayIndx -= 1
    return sortedSquaredArray
