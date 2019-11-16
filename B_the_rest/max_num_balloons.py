class Solution:
    def max_number_of_balloons(self, text):
        if not text:
            return 0

        dic = {'b': 0,
               'a': 0,
               'l': 0,
               'o': 0,
               'n': 0}

        for c in text:
            if c in dic:
                dic[c] += 1

        dic['l'] //= 2
        dic['o'] //= 2

        _min = float('inf')
        for c in dic:
            _min = min(_min, dic[c])

        return _min
