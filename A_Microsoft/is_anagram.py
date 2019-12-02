class Solution:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        for x, y in zip(sorted(s), sorted(t)):
            if x != y:
                return False

        return True


class Solution2:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        dic = {}
        for x in s:
            if dic.get(x):
                dic[x] += 1
            else:
                dic[x] = 1

        for x in t:
            if dic.get(x):
                dic[x] -= 1

        return all(value == 0 for value in dic.values())
