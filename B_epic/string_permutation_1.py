def permute(string):
    return _permute(list(string), 0, len(string) - 1, [])


def _permute(arr, l, r, res):
    if l == r:
        res.append(_to_string(arr))
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            _permute(arr, l + 1, r, res)
            # backtrack
            arr[l], arr[i] = arr[i], arr[l]

    return res


def _to_string(list_):
    return ''.join(list_)


print(permute('123'))
