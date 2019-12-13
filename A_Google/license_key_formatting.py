from collections import deque


class Solution:
    def license_key_formatting(self, s, k):
        res, tmp, count = deque([]), deque([]), 0
        for i, x in enumerate(reversed(s)):
            if x != '-':
                tmp.appendleft(x.upper())
                count += 1
                if count == k:
                    res.appendleft(''.join(tmp))
                    tmp.clear()
                    count = 0

        if tmp:
            res.appendleft(''.join(tmp))

        return '-'.join(res)


class Solution2:
    def license_key_formatting(self, s, k):
        s = s.upper().replace('-', '')
        n = len(s)
        i = k if n % k == 0 else n % k
        res = s[:i]

        while i < n:
            res += '-' + s[i:i + k]
            i += k

        return res
