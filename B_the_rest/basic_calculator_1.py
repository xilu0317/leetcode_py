class Solution:
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []

        for c in s:
            if (c == ' '):
                continue

            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                # The 'res' will ensure calculation happen inside the paren locally
                res = 0
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        res += sign * num

        return res
