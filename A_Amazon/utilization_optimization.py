# [TWO-POINTER]
def two_sum_cloest(a, b, target):
    i, j, min_ = 0, len(b) - 1, float('inf')

    while i < len(a) and j >= 0:
        diff = abs(target - a[i][1] - b[j][1])
        min_ = min(min_, diff)

        if a[i][1] + b[j][1] > target:
            j -= 1
        elif a[i][1] + b[j][1] < target:
            i += 1
        else:
            break

    # reverse indexing
    dic = {x[1]: x[0] for x in b}

    for x, y in a:
        if target - min_ - y in dic:
            return x, dic[target - min_ - y]

    return -1


# testcase 1 => (3, 1)
# a = [[1, 8], [2, 7], [3, 14]]
# b = [[1, 5], [2, 10], [3, 14]]
# target = 20


# testcase 2 => (2, 4)
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10


s = two_sum_cloest(a, b, target)
print(s)
