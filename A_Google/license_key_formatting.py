from collections import deque


class Solution:
    def licenseKeyFormatting(self, s, k):
        res, tmp, count = deque([]), deque([]), 0
        for i, x in enumerate(reversed(s)):
            if i == len(s) - 1:
                res.appendleft(''.join(tmp))
                break

            if x != '-':
                if count == k:
                    res.appendleft(''.join(tmp))
                    tmp.clear()
                    count = 0
                else:
                    tmp.appendleft(x.upper())
                    count += 1

        return '-'.join(res)
