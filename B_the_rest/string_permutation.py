def permute(string):
    return _permute(list(string), 0, len(string) - 1, [])


def _permute(a, l, r, res):
    if l == r:
        res.append(_to_string(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            _permute(a, l + 1, r, res)
            # backtrack
            a[l], a[i] = a[i], a[l]

    return res


def _to_string(list_):
    return ''.join(list_)


print(permute('ABC'))
