# Description: Print continuous alphabets from a sequence of arbitrary alphabets
# For example:
# Input: abcdefljdflsjflmnopflsjflasjftuvwxyz
# Output: abcdef lmnop  tuvwxyz
# Input: AbcDefljdflsjflmnopflsjflasjftuvWxYz
# Output: abcdef lmnop tuvwxyz


def continuous_alpha(string):
    res, temp = [], []
    arr = [ord(x) for x in string]

    for i in range(len(arr) - 1):
        if arr[i] + 1 == arr[i + 1]:
            temp.append(arr[i])
        elif arr[i] - 1 == arr[i - 1]:
            temp.append(arr[i])
        else:
            con_string = ''.join([chr(x) for x in temp]).lower()
            if len(con_string):
                res.append(con_string)
            temp = []

    res.append(''.join([chr(x) for x in temp]))

    return res


test = continuous_alpha('abcdefljdflsjflmnopflsjflasjftuvwxyz')
print(test)
