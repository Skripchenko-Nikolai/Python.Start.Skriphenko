import math


def task_1(N):
    result = math.factorial(N)
    return result


def task_2(N):
    # n = int(input("n="))
    # c, p = 0, 1
    # for _ in range(n):
    #     c, p = c + p, c
    return 8


def task_3(N):
    result = []
    for x in range(1, N+1):
        if N % x == 0:
            result.append(x)
    print(result)
    return result
