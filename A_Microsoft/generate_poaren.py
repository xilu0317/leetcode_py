class Solution:
    def generateParenthesis(self, n):
        res = []

        self.backtrack(res, '', 0, 0, n)

        return res

    def backtrack(self, res, _str, _open, close, _max):
        if len(_str) == _max * 2:
            res.append(_str)
            return

        if _open < _max:
            self.backtrack(res, _str + '(', _open + 1, close, _max)

        if close < _open:
            self.backtrack(res, _str + ')', _open, close + 1, _max)
