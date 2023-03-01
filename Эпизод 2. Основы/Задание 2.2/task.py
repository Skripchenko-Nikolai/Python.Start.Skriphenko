# Пример 1
def task_1(A):
    list = A
    nums = []
    for x in list:
        if x > 0:
            nums.append(x)
    result = sum(nums)
    return result


# Пример 2
def task_2(A):
    list = A
    nums = []
    for x in list:
        if x > 0:
            nums.append(x)
    result = sum(nums)
    return result / len(nums)


# Пример 3
def task_3(A):
    result = 0
    average = task_2(A)
    for element in A:
        result += (element - average) ** 2
    result *= 1 / len(A)
    return result ** 0.5
