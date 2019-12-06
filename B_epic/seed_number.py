# Input: n = 138
# Output: 23
# 23 is a seed of 138 because
# 23*2*3 is equal to 138

# Input: n = 4977
# Output: 79 711
# 79 is a seed of 4977 because
# 79 * 7 * 9 = 4977.
# 711 is also a seed of 4977 because
# 711 * 1 * 1 * 7 = 4977

# Input: n = 9
# Output: No seed exists

# Input: n = 738
# Output: 123


def get_product(n):
    prod = 1
    while n > 1:
        prod *= (n % 10)
        n = n // 10

    return prod


def get_seed(num):
    res = []
    for i in range(num // 2 + 1):
        if i * get_product(i) == num:
            res.append(i)

    return res if len(res) else None


test = get_seed(119)
print(test)
