class Solution:
    def is_isomorphic(self, s, t):
        dic1, dic2 = {}, {}

        for i, x in enumerate(s):
            if x not in dic1:
                dic1[x] = t[i]
            elif dic1[x] != t[i]:
                return False

        for i, x in enumerate(t):
            if x not in dic2:
                dic2[x] = s[i]
            elif dic2[x] != s[i]:
                return False

        return True
