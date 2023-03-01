# Пример 1
import math


def task_1(n):
    x = 0
    count = 1
    while count <= 10:
        x += 1/count
        count += 1
    return x


# Пример 2
def task_2(x, n):
    y = x
    count = 3
    while count <= n:
        y += x/count
        count += 2
    return y


# Пример 3
def task_3(n):
    result = math.factorial(n)
    return result


# Пример 4
def task_4(x, n):
    z = 0
    count = 1
    while count <= n:
        z += (x + 2) / 2
    return z


# Пример 5
def task_5(x, n):
    y = 0
    count = 1
    while count <= n:
        y += (x*count)/(2*count)
        count += 1
    return y


# Пример 6
def task_6(n):
    result = 1
    count = 2
    while count <= 20:
        result *= count
        count += 2
    return result
