def getFibonacci(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return getFibonacci(n - 1) + getFibonacci(n - 2)


def getFibonacciOptimal(n):
    fibonacci_series = {1: 0, 2: 1}
    if n in fibonacci_series:
        return fibonacci_series[n]
    else:
        fibonacci_series[n] = getFibonacciOptimal(n - 1) + getFibonacciOptimal(n - 2)
        return fibonacci_series[n]


def getFibonacciIterative(n):
    counter = [0, 1]
    count = 3
    while count <= n:
        temp = counter[1]
        counter[1] = counter[0] + counter[1]
        counter[0] = temp
        count = count + 1
    if n > 0:
        return counter[1]
    return counter[0]


if __name__ == '__main__':
    fibOfSix = getFibonacci(6)
    fibOfSixOptimal = getFibonacciOptimal(6)
    fibOfSixIterative = getFibonacciIterative(6)
    print(fibOfSix == 5)
    print("=============")
    print(fibOfSixOptimal == 5)
    print("==============")
    print(fibOfSixIterative == 5)
