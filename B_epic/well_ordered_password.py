def print_well_ordered(num, x, k):
    if (k == 0):
        print(num)
        return

    for i in range(x + 1, 10):
        print_well_ordered(num * 10 + i, i, k - 1)


def generate_well_ordered(k):
    print_well_ordered(0, 0, k)


generate_well_ordered(7)
